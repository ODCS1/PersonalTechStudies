import React from 'react';
import ReactDOM from 'react-dom/client';
import { createServer } from 'miragejs';
import { App } from './App';

createServer({
  routes() {
    this.namespace = 'api';
    this.get('/transactions', () => {
      return [
        {
          id: 1,
          title: 'Website development',
          type: 'deposit',
          category: 'Sale',
          amount: 12000,
          createdAt: new Date()
        },
        {
          id: 2,
          title: 'Apartment rental',
          type: 'withdraw',
          category: 'Home',
          amount: 12000,
          createdAt: new Date()
        }
      ];
    });
  }
});


const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);