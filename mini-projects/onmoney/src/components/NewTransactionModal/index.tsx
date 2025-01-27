import Modal from "react-modal";
import { Container, TransactionTypeContainer, RadioBox } from "./styles";
import closeSvg from "../../assets/close.svg";
import incomeSvg from "../../assets/income.svg";
import outcomeSvg from "../../assets/outcome.svg";
import { FormEvent, useState } from "react";
import { api } from "../../services/api";

Modal.setAppElement("#root");


type newTransactionModalProps = {
    isOpen: boolean;
    onRequestClose: () => void;
}

export function NewTransactionModal ({ isOpen, onRequestClose }: newTransactionModalProps) {
  const [title, setTitle] = useState('');
  const [value, setValue] = useState(0);
  const [category, setCategory] = useState('');
  const [type, setType] = useState('deposit');

  function handleCreateNewTransaction(event: FormEvent) {
    event.preventDefault();

    const data = {
      title,
      value,
      category,
      type
    };

    api.post('/transactions', data);
  }

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
        <Container onSubmit={handleCreateNewTransaction}>
          <h2>Register Transaction</h2>
          <input 
            placeholder="Title"
            value={title}
            onChange={event => setTitle(event.target.value)}
          />
          <input 
            type="number" 
            placeholder="Value"
            value={value}
            onChange={event => setValue(Number(event.target.value))}
          />

          <TransactionTypeContainer>
            <RadioBox
              $isActive={type === 'deposit'}
              $activeColor={"green"}
              type="button"
              onClick={() => { setType('deposit'); }}
            >
              <img src={incomeSvg} alt="Income" />
              <span>Income</span>
            </RadioBox>

            <RadioBox
              $isActive={type === 'withdraw'}
              $activeColor={"red"}
              accessKey=""
              type="button"
              onClick={() => { setType('withdraw'); }}
            >
              <img src={outcomeSvg} alt="Outcome" />
              <span>Outcome</span>
            </RadioBox>
          </TransactionTypeContainer>

          <input 
            placeholder="Category" 
            value={category}
            onChange={event => setCategory(event.target.value)}
          />
          <button type="submit">Register</button>
        </Container>
    </Modal>
  );
};
