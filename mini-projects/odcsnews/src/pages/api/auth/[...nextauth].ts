import NextAuth from "next-auth";
import GitHubProvider from "next-auth/providers/github";
import { queryFauna } from "../../../services/fauna";

export default NextAuth({
  providers: [
    GitHubProvider({
      clientId: process.env.GITHUB_ID!,
      clientSecret: process.env.GITHUB_SECRET!,
      authorization: { params: { scope: "read:user" } },
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
  session: { strategy: "jwt" },

  callbacks: {
    async signIn({ user }) {
      try {
        const email = user.email;

        if (!email) {
          console.error("No email found in user profile");
          return false;
        }

        const query = `
          let userMatch = Match(Index("user_by_email"), "${email}")
          let userExists = Exists(userMatch)

          if (userExists) {
            Get(userMatch)
          } else {
            Create(Collection("users"), { email: "${email}" })
          }
        `;

        const userDoc = await queryFauna<{ email: string }>(query);
        console.log("User document from Fauna:", userDoc);

        return true;
      } catch (error) {
        console.error("Could not sign in:", error);
        return false;
      }
    }
  }
});
