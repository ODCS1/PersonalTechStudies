import { NextApiRequest, NextApiResponse } from "next";

// JWT (STORAGE)
// Next Auth (SOCIAL)
// Cognito, Auth0


export default (req: NextApiRequest, res: NextApiResponse) => {
    const users = [
        { id: 1, name: 'John Doe' },
        { id: 2, name: 'Jane Doe' },
        { id: 3, name: 'Alice Doe' },
    ]

    return res.json(users);
}