import { createContext, useContext, useEffect, useState } from "react";
import { api } from "../services/api";

type TransactionType = {
  id: number;
  title: string;
  amount: number;
  type: string;
  category: string;
  createdAt: string;
};

type TransactionInputType = Omit<TransactionType, "id" | "createdAt">;

type TransactionsProviderProps = {
  children: React.ReactNode;
};

type TransactionsContextType = {
  transactions: TransactionType[];
  createTransaction: (transaction: TransactionInputType) => Promise<void>;
};

const TransactionsContext = createContext<TransactionsContextType>(
  {} as TransactionsContextType
);

export function TransactionsProvider({ children }: TransactionsProviderProps) {
  const [transactions, setTransactions] = useState<TransactionType[]>([]);

  useEffect(() => {
    api
      .get("/transactions")
      .then((response) => setTransactions(response.data.transactions));
  }, []);

  async function createTransaction(transactionInput: TransactionInputType) {
    const response = await api.post("/transactions", {
      ...transactionInput,
      createdAt: new Date(),
    });

    const { transaction } = response.data;

    setTransactions([...transactions, transaction]);
  }

  return (
    <TransactionsContext.Provider value={{ transactions, createTransaction }}>
      {children}
    </TransactionsContext.Provider>
  );
}

export function useTransactions() {
  const context = useContext(TransactionsContext);

  return context;
}