import { Container } from "./style";

export function TransactionsTable() {

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
          <tr>
            <td>Website development</td>
            <td className="deposit">$2000.00</td>
            <td>Sale</td>
            <td>01/01/2025</td>
          </tr>
          {/* <tr>
                    <td>Hamburger</td>
                    <td>- $59.00</td>
                    <td>Food</td>
                    <td>01/01/2025</td>
                </tr> */}
          <tr>
            <td>Apartment rental</td>
            <td className="withdraw">- $1200.00</td>
            <td>Home</td>
            <td>03/01/2022</td>
          </tr>
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
