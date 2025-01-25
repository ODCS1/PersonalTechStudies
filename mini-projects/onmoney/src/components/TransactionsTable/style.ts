import styled from "styled-components";

export const Container = styled.div`
    max-width: 1120px;
    margin: 0 auto;

    table {
        width: 80%;
        margin: 0 auto;
        border-collapse: separate;
        border-spacing: 0 0.5rem;

        thead {
            row-gap: 1rem;
            tr {
            background: transparent !important;

                th {
                    padding: 1rem 2rem;
                    color: var(--text-body);
                    font-weight: 400;
                    text-align: left;
                }
            }
        }

        tbody {
            tr {
                background: var(--shape);
                border-radius: 8px;
            
                td {
                    padding: 1rem 2rem;
                    color: var(--text-body);
                    font-weight: 400;
                    text-align: left;
                    vertical-align: middle;
                }

                .deposit {
                    color: var(--green);
                }
                
                .withdraw {
                    color: var(--red);
                }
            }
        }
    }
`;