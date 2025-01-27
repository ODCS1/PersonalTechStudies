import { useContext } from "react";
import { Container } from "./style";
import { TransactionsContext } from "../../TransactionsContext";


type TransactionType = {
  id: number;
  title: string;
  amount: number;
  type: string;
  category: string;
  createdAt: string;
}


export function TransactionsTable() {
  const transactions = useContext(TransactionsContext);
  // const [transactions, setTransactions] = useState<TransactionType[]>([]);
  
  //   useEffect(() => {
  //       api.get('/transactions')
  //       .then(response => setTransactions(response.data.transactions));
  //   }, []);

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
        </tbody>
      </table>
    </Container>
  );
}
