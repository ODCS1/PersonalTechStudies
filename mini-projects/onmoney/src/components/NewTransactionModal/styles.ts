import styled from "styled-components";
import { darken, transparentize } from "polished";

export const Container = styled.form`
    h2 {
        color: var(--text-title);
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }

    input {
        width: 100%;
        padding: 0 1.5rem;
        height: 4rem;
        border-radius: 0.25rem;

        border: 1px solid #d7d7d7;
        background: #e7e9ee;

        font-weight: 400;
        font-size: 1rem;

        &::placeholder {
            color: var(--text-body);
        }

        & + input {
            margin-top: 1rem;
        }
    }

    button[type="submit"] {
        width: 100%;
        padding: 0 1.5rem;
        height: 4rem;
        background: var(--green);
        color: #FFF;
        border-radius: 0.25rem;
        border: 0;
        font-size: 1rem;
        margin-top: 1.5rem;
        transition: filter 0.2s;
        font-weight: 600;

        &:hover {
            filter: brightness(0.9);
        }
    }
`;


export const TransactionTypeContainer = styled.div`
    width: 100%;
    margin: 1rem 0;
    display: flex;
    justify-content: center;
    gap: 1rem;
`;


type RadioBox = {
    $isActive: boolean;
    $activeColor: 'red' | 'green';
}

const colors = {
    red: '#E52E4D',
    green: '#33CC95'
}

export const RadioBox = styled.button<RadioBox>`
    width: 100%;
    height: 4rem;
    border: 1px solid #d7d7d7;
    border-radius: 0.25rem;

    background: ${(props) => props.$isActive 
        ? transparentize(0.9, colors[props.$activeColor])
        : 'transparent'};

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;

    transition: border-color 0.2s;

    &:hover {
        border-color: ${darken(0.1, '#d7d7d7')};
    }

    img {
        width: 20px;
        height: 20px;
    }

    span {
        color: var(--text-title);
        font-size: 1rem;
    }


`;