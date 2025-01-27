import { Container } from "./style";
import incomeImg from "../../assets/income.svg";
import outcomeImg from "../../assets/outcome.svg";
import totalImg from "../../assets/total.svg";
import { TransactionsContext } from "../../TransactionsContext";
import { useContext } from "react";

export function Summary() {
    const data = useContext(TransactionsContext);

    return (
        <Container>
            // OLD API USAGE FOR CONTEXT DATA
            {/* <TransactionsContext.Consumer>
                {(data) => {
                    console.log(data)

                    return <p>Ok</p>
                }}
            </TransactionsContext.Consumer> */}

            <div>
                <header>
                    <p>Incomes</p>
                    <img src={incomeImg} alt="Incomes" />
                </header>
                <strong>R$1000,00</strong>
            </div>
            <div>
                <header>
                    <p>Outcomes</p>
                    <img src={outcomeImg} alt="Outcomes" />
                </header>
                <strong>- R$500,00</strong>
            </div>
            <div className="highlight-background">
                <header>
                    <p>Total</p>
                    <img src={totalImg} alt="Total" />
                </header>
                <strong>R$500,00</strong>
            </div>
        </Container>
    );
}