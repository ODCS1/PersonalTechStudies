import { NextApiRequest, NextApiResponse } from "next";
import { stripe } from '../../services/stripe';
import { getSession } from 'next-auth/react';
import { supabase } from '../../services/supabase';

export default async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method === 'POST') {
    const session = await getSession({ req });

    if (!session || !session.user) {
      res.status(401).end({ message: 'Unauthorized' });
      return;
    }

    const email = session.user.email as string;

    // QUERY TO FETCH THE USER FROM SUPABASE AND CHECK THE stripe_customer_id
    const { data: userData, error: userError } = await supabase
      .from('users')
      .select('stripe_customer_id')
      .eq('email', email)
      .single();

    if (userError) {
      res.status(500).json({ message: 'Error fetching user data from Supabase', error: userError.message });
      return;
    }

    let stripeCustomerId = userData?.stripe_customer_id || null;
    let stripeCustomer;

    if (stripeCustomerId) {
      stripeCustomer = await stripe.customers.retrieve(stripeCustomerId);

    } else {
      stripeCustomer = await stripe.customers.create({
        email: email,
      });


      // UPDATE stripe_customer_id IN SUPABASE
      const { error: updateError } = await supabase
        .from('users')
        .update({ stripe_customer_id: stripeCustomer.id })
        .eq('email', email);

      if (updateError) {
        res.status(500).json({ message: 'Error updating stripe customer ID in Supabase', error: updateError.message });
        return;
      }

      stripeCustomerId = stripeCustomer.id;
    }

    // CREATE CHECKOUT SESSION
    const stripeCheckoutSession = await stripe.checkout.sessions.create({
      customer: stripeCustomerId,
      payment_method_types: ['card'],
      line_items: [
        {
          price: 'price_1Qn6GOEXsfTMCeUSVXokw9tW',
          quantity: 1,
        },
      ],
      mode: 'subscription',
      allow_promotion_codes: true,
      success_url: `${req.headers.origin}/posts`,
      cancel_url: `${req.headers.origin}`,
    });

    return res.status(200).json({ sessionId: stripeCheckoutSession.id });
  } else {
    res.setHeader('Allow', 'POST');
    res.status(405).end({ message: 'Method not allowed' });
  }
};
