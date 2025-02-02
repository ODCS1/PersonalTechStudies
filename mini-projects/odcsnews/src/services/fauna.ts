import { fql, Client, type QuerySuccess, type QueryValue } from "fauna";

const client = new Client({
  secret: process.env.FAUNADB_KEY
});

export async function queryFauna<T extends QueryValue>(query: string):Promise<T> {
  try {
    const response: QuerySuccess<T> = await client.query<T>(fql`${query}`);
    return response.data;
  } catch (error) {
    console.error("FaunaDB Error:", error);
    throw error;
  }
}
