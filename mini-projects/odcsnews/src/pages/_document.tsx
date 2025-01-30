import Document, { Html, Head, Main, NextScript } from 'next/document';
// import favicon from '../../public/favicon.png';

export default class MyDocument extends Document {
    render() {
        return (
            <Html>
                <Head>
                    {/* <title>Odcs news</title> */}
                    <link rel="preconnect" href="https://fonts.googleapis.com" />
                    <link rel="shortcut icon" href="/favicon.png" type="image/png" />
                    <link 
                        href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Roboto:wght@400;700;900&display=swap" rel="stylesheet">
                    </link>
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}