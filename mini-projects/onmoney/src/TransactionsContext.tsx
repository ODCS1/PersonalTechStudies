import {createContext, useEffect, useState } from 'react';
import { api } from './services/api';

type TransactionType = {
    id: number;
    title: string;
    amount: number;
    type: string;
    category: string;
    createdAt: string;
}

type TransactionsProviderProps = {
    children: React.ReactNode;
}

export const TransactionsContext = createContext<TransactionType[]>([]);


 export function TransactionsProvider({ children }: TransactionsProviderProps) {
    const [transactions, setTransactions] = useState<TransactionType[]>([]);
  
    useEffect(() => {
        api.get('/transactions')
        .then(response => setTransactions(response.data.transactions));
    }, []);

    return (
        <TransactionsContext.Provider value={transactions}>
            {children}
        </TransactionsContext.Provider>
    );
 }