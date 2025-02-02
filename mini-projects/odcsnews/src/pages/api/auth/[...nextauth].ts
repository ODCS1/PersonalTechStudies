import NextAuth from "next-auth";
import GitHubProvider from "next-auth/providers/github";
import { query as q } from "faunadb";
import { fauna } from "../../../services/fauna";

export default NextAuth({
  providers: [
    GitHubProvider({
      clientId: process.env.GITHUB_ID!,
      clientSecret: process.env.GITHUB_SECRET!,
      authorization: {
        params: { scope: "read:user" },
      },
    }),
  ],
  secret: process.env.NEXTAUTH_SECRET,
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async signIn({user, account, profile}) {
      try {
        const email = user.email;

        if (!email) {
          console.error("No email found in user profile");
          return false;
        }

        await fauna.query(
          q.Create(q.Collection("users"), { data: { email } })
          // q.If(
          //   q.Not(
          //     q.Exists(
          //       q.Match(q.Index("user_by_email"), email)
          //     )
          //   ),
          //   q.Create(q.Collection("users"), { data: { email } }),
          //   q.Get(q.Match(q.Index("user_by_email"), email))
          // )
        )

        return true;
      } catch (error) {
        console.error("Could not sign in: ", error);
        return false;
      }
    }
  }
});
