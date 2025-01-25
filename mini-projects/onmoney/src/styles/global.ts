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

    .react-modal-overlay {
        background: rgba(0, 0, 0, 0.5);

        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;

        display: flex;
        align-items: center;
        justify-content: center;
    }

    .react-modal-content {
        width: 100%;
        max-width: 576px;
        background: var(--background);
        padding: 3rem;
        position: relative;
        border-radius: 0.24rem;

        button.react-modal-close {
            position: absolute;
            right: 1.5rem;
            top: 1.5rem;
            background: transparent;
            border: 0;
            font-size: 0;

            transition: filter 0.2s;

            &:hover {
                filter: brightness(0.8);
            }
        }
    }
`;