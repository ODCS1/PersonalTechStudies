import { NextApiRequest, NextApiResponse } from "next";
import { stripe } from '../../services/stripe';
import { getSession } from 'next-auth/react';

export default async(req: NextApiRequest, res: NextApiResponse) => {

    if (req.method === 'POST'){
        const session = await getSession({ req })
        
        if (!session || !session.user) {
            res.status(401).end({ message: 'Unauthorized' });
            return;
        }

        const stripeCustomer = await stripe.customers.create({
            email: session.user.email as string,
        })

        const stripeCheckoutSession = await stripe.checkout.sessions.create({
            customer: stripeCustomer.id,
            payment_method_types: ['card'],
            line_items: [
                {
                    price: req.body.priceId,
                    quantity: 1,
                },
            ],
            mode: 'subscription',
            allow_promotion_codes: true,
            success_url: `${req.headers.origin}/posts`,
            cancel_url: `${req.headers.origin}`,
        })

        return res.status(200).json({ sessionId: stripeCheckoutSession.id })
    } else {
        res.setHeader('Allow', 'POST');
        res.status(405).end({ message: 'Method not allowed' });
    }
}