import logoImg from '../../assets/logo.png';
import { Container, Content } from './styles';


type HeaderProps = {
    onOpenNewTransactionModal: () => void;
};


export function Header({onOpenNewTransactionModal}: HeaderProps) {


  return (
    <Container>
        <Content>
            <img src={logoImg} alt="on money" />
            <button onClick={onOpenNewTransactionModal} type="button">
                New Transaction
            </button>
        </Content>
    </Container>
  )
}
