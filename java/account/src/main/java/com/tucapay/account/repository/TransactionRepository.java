package com.tucapay.account.repository;

import com.tucapay.account.model.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TransactionRepository extends JpaRepository<Transaction, Integer> {
    List<Transaction> findTransactionsByAccountId (Integer id);
}
