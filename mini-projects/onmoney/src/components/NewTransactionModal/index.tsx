import Modal from "react-modal";
import { Container, TransactionTypeContainer, RadioBox } from "./styles";
import closeSvg from "../../assets/close.svg";
import incomeSvg from "../../assets/income.svg";
import outcomeSvg from "../../assets/outcome.svg";
import { useState } from "react";

Modal.setAppElement("#root");


type newTransactionModalProps = {
    isOpen: boolean;
    onRequestClose: () => void;
}

export function NewTransactionModal ({ isOpen, onRequestClose }: newTransactionModalProps) {
  const [type, setType] = useState('deposit');

  return (
    <Modal
        isOpen={isOpen}
        onRequestClose={onRequestClose}
        overlayClassName={"react-modal-overlay"}
        className={"react-modal-content"}
    >
        <button type="button" className="react-modal-close">
            <img src={closeSvg} alt="Close modal" onClick={onRequestClose} />
        </button>
        <Container>
          <h2>Register Transaction</h2>
          <input placeholder="Title"/>
          <input type="number" placeholder="Value" />

          <TransactionTypeContainer>
            <RadioBox
              isActive={type === 'deposit'}
              type="button"
              onClick={() => { setType('deposit'); }}
            >
              <img src={incomeSvg} alt="Income" />
              <span>Income</span>
            </RadioBox>

            <RadioBox
              isActive={type === 'withdraw'}
              type="button"
              onClick={() => { setType('withdraw'); }}
            >
              <img src={outcomeSvg} alt="Outcome" />
              <span>Outcome</span>
            </RadioBox>
          </TransactionTypeContainer>

          <input placeholder="Category" />
          <button type="submit">Register</button>
        </Container>
    </Modal>
  );
};
