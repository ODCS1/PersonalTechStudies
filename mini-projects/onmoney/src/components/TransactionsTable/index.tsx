import { useEffect, useState } from "react";
import { Container } from "./style";
import { api } from "../../services/api";


type TransactionType = {
  id: number;
  title: string;
  amount: number;
  type: string;
  category: string;
  createdAt: string;
}


export function TransactionsTable() {
  const [transactions, setTransactions] = useState<TransactionType[]>([]);
  
    useEffect(() => {
        api.get('/transactions')
        .then(response => setTransactions(response.data.transactions));
    }, []);

    return (
    <Container>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Price</th>
            <th>Category</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map(transaction => (
            <tr key={transaction.id}>
              <td>{transaction.title}</td>

              <td className={transaction.type}>

                {new Intl.NumberFormat('english', { 
                  style: 'currency', 
                  currency: 'USD' 
                }).format(transaction.amount)}

              </td>

              <td>{transaction.category}</td>
              <td>
                {/* {transaction.createdAt} */}
                {new Intl.DateTimeFormat('en-US').format(new Date(transaction.createdAt))}
              </td>
            </tr>
          ))}
          {/* <tr>
            <td>Website development</td>
            <td className="deposit">$2000.00</td>
            <td>Sale</td>
            <td>01/01/2025</td>
          </tr> */}
          {/* <tr>
                    <td>Hamburger</td>
                    <td>- $59.00</td>
                    <td>Food</td>
                    <td>01/01/2025</td>
                </tr> */}
          {/* <tr>
            <td>Apartment rental</td>
            <td className="withdraw">- $1200.00</td>
            <td>Home</td>
            <td>03/01/2022</td>
          </tr> */}
          {/* <tr>
                    <td>Computer</td>
                    <td>R$12000.00</td>
                    <td>Sale</td>
                    <td>03/01/2022</td>
                </tr> */}
        </tbody>
      </table>
    </Container>
  );
}
