import Modal from "react-modal";

Modal.setAppElement("#root");


type newTransactionModalProps = {
    isOpen: boolean;
    onRequestClose: () => void;
}

export function NewTransactionModal ({ isOpen, onRequestClose }: newTransactionModalProps) {

  return (
    <Modal
        isOpen={isOpen}
        onRequestClose={onRequestClose}
    >
        <h2>Register Transaction</h2>
    </Modal>
  );
};
