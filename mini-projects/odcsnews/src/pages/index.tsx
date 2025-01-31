import Head from 'next/head';
import { GetStaticProps } from 'next';
import styles  from './home.module.scss';
import { SubscribeButton } from '@/components/SubscribeButton';
import { stripe } from '../services/stripe';


// CLIENT SIDE
// SERVER SIDE RENDERING (SSR)
// STATIC SITE GENERATION (SSG)

type HomeProps = {
  product: {
    priceId: string;
    amount: number;
  }
}

export default function Home({ product }: HomeProps) {
  return (
    <>
      <Head>
        <title>Home | odcs.news</title>
      </Head>
      <main className={styles.contentContainer}>
        <section className={styles.hero}>
          <span>👏 Hey, welcome</span>
          <h1>
            News about the <span>React</span> world.
          </h1>
          <p>
            Get acess to all the publications <br/>
            <span>for {product.amount}/month</span>
          </p>
          <SubscribeButton priceId={product.priceId} />
        </section>
        <img src="/images/avatar.svg" alt="Girl Coding" />
      </main>
    </>
  );
}

export const getStaticProps: GetStaticProps = async () => {
  const price = await stripe.prices.retrieve('price_1Qn6GOEXsfTMCeUSVXokw9tW');

  const product = {
    priceId: price.id,
    amount2: price.unit_amount as number / 100,
    amount: new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(price.unit_amount as number / 100)
  }

  return {
    props: {
      product,
    },
    revalidate: 60 * 60 * 24, //24 hours
  }
}
