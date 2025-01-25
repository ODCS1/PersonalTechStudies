import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`

    :root {
        --background: #f0f2ff;
        --red: #e52e4d;
        --blue: #5429CC;
        --green: #33CC95;

        --blue-light: #6933FF;

        --text-title: #363F5F;
        --text-body: #969cb3;

        --backgorund: #F0F2F5;
        --shape: #FFFFFF;
    }

    * {
        box-sizing: border-box;
        padding: 0;
        margin: 0;
    }

    // font-size: 16px (desktop)
    html {
        @media (max-width: 1080){
            font-size: 93.75%; // 15px
        }

        @media (max-width: 720px){
            font-size: 87.5%; // 14px
        }
    }

    // REM = 1rem = 16px

    body {
        background: var(--background);

        // SHARPER FONTS
        -webkit-font-smoothing: antialiased;
    }

    button {
        cursor: pointer;
    }

    [disabled] {
        opacity: 0.6;
        cursor: not-allowed;
    }
`;