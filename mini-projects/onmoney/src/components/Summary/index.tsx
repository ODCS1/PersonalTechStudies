import { useTransactions } from "../../hooks/useTransactions";

import { Container } from "./style";

import incomeImg from "../../assets/income.svg";
import outcomeImg from "../../assets/outcome.svg";
import totalImg from "../../assets/total.svg";


export function Summary() {
  const { transactions } = useTransactions();

  // CALCULATE TOTAL TRANSACTION VALUES
  const summary = transactions.reduce(
    (acc, transaction) => {
      if (transaction.type === "deposit") {
        acc.totalIncome += transaction.amount;
        acc.totalBalance += transaction.amount;
      } else {
        acc.totalOutcome += transaction.amount;
        acc.totalBalance -= transaction.amount;
      }
      return acc;
    },
    {
      totalIncome: 0,
      totalOutcome: 0,
      totalBalance: 0,
    }
  );

  return (
    <Container>
      {/* OLD API USAGE FOR CONTEXT DATA */}
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
        <strong>
          {new Intl.NumberFormat("english", {
            style: "currency",
            currency: "USD",
          }).format(summary.totalIncome)}
        </strong>
      </div>
      <div>
        <header>
          <p>Outcomes</p>
          <img src={outcomeImg} alt="Outcomes" />
        </header>
        <strong>
          -
          {new Intl.NumberFormat("english", {
            style: "currency",
            currency: "USD",
          }).format(summary.totalOutcome)}
        </strong>
      </div>
      <div className="highlight-background">
        <header>
          <p>Total</p>
          <img src={totalImg} alt="Total" />
        </header>
        <strong>
          {new Intl.NumberFormat("english", {
            style: "currency",
            currency: "USD",
          }).format(summary.totalBalance)}
        </strong>
      </div>
    </Container>
  );
}
