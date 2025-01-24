import logoImg from '../../assets/logo.png';
import { Container, Content } from './styles';

export function Header() {
  return (
    <Container>
        <Content>
            <img src={logoImg} alt="on money" />
            <button type="button">
                New Transaction
            </button>
        </Content>
    </Container>
  )
}
