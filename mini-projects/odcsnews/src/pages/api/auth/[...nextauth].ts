import { supabase } from "../../../services/supabase";
import NextAuth from "next-auth";
import GitHubProvider from "next-auth/providers/github";

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
      const email = user.email;

      if (!email) {
        console.error("No email found in user profile");
        return false;
      }

      const { data: existingUser, error: selectError } = await supabase
        .from('users')
        .select('email')
        .eq('email', email)
        .single();

      if (selectError && selectError.code !== 'PGRST116') {
        // PGRST116 INDICATES THAT NO USER WAS FOUND, WHICH IS EXPECTED IF IT'S A NEW USER
        console.error("Error checking existing user:", selectError);
        return false;
      }

      if (!existingUser) {
        // IF THE USER DOES NOT EXIST, INSERT INTO THE DATABASE 
        const { error: insertError } = await supabase
          .from('users')
          .insert([{ email }]);

        if (insertError) {
          console.error("Error inserting user into Supabase:", insertError);
          return false;
        }
      }

      return true; // ALLOWS LOGIN IN NEXTAUTH 
    },
  },
});
