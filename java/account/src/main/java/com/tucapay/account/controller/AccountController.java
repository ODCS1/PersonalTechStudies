package com.tucapay.account.controller;

import com.tucapay.account.model.Account;
import com.tucapay.account.model.Transaction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.tucapay.account.repository.AccountRepository;
import com.tucapay.account.repository.TransactionRepository;

import java.time.LocalTime;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/account")
public class AccountController {
    @GetMapping("/teste")
    public String teste () {
        return "foi";
    }



    @Autowired
    private AccountRepository accountRepository;

    @Autowired
    private TransactionRepository transactionRepository;

    @GetMapping("/")
    public ResponseEntity<List<Account>> getAll() {
        List<Account> accounts = accountRepository.findAll();
        return accounts.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(accounts);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Account> getAccountById(@PathVariable Integer id) {
        return accountRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.noContent().build());
    }

    @GetMapping("/{id}/balance")
    public ResponseEntity<Double> getBalanceByAccountId (@PathVariable Integer id) {
        Optional<Account> account = accountRepository.findById(id);
        return account.map(a -> ResponseEntity.ok(a.getBalance()))
                .orElse(ResponseEntity.noContent().build());
    }

    @PostMapping("/")
    public ResponseEntity<Account> createAccount (@RequestBody Account account) {
        Account savedAccount = accountRepository.save(account);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedAccount);
    }

    @PostMapping("/{id}/deposit")
    public ResponseEntity<Account> createDeposit(@PathVariable Integer id, @RequestBody Double value) {
        return accountRepository.findById(id)
                .map(account -> {
                    account.setBalance(account.getBalance() + value);
                    return ResponseEntity.ok(accountRepository.save(account));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/{id}/withdrawal")
    public ResponseEntity<?> createWithdrawal(@PathVariable Integer id, @RequestBody Double value) {
        return accountRepository.findById(id)
                .map(account -> {
                    LocalTime now = LocalTime.now();
                    LocalTime start = LocalTime.of(22, 0);
                    LocalTime end = LocalTime.of(6, 0);

                    if (value > account.getBalance()) return ResponseEntity.badRequest().build();
                    if (now.isAfter(start) || now.isBefore(end)) {
                        if (value > 1000) return ResponseEntity.badRequest().build();
                    }
                    account.setBalance(account.getBalance() - value);
                    return ResponseEntity.ok(accountRepository.save(account));
                })
                .orElse(ResponseEntity.notFound().build());
    }



    @PostMapping("/{id}/transfer")
    public ResponseEntity<?> createTransfer(@PathVariable Integer id, @RequestBody Map<String, Object> requestBody) {
        // EXTRAIR OS VALORES DO CORPO DA REQUISIÇÃO
        Integer targetAccountId = (Integer) requestBody.get("targetAccountId");
        Double value = Double.valueOf(requestBody.get("value").toString());

        // VERIFICAR SE OS IDS E VALORES SÃO VÁLIDOS
        if (targetAccountId == null || value == null || value <= 0) {
            return ResponseEntity.badRequest().body("Invalid targetAccountId or value");
        }

        // BUSCAR CONTAS
        Optional<Account> account1Opt = accountRepository.findById(id);
        Optional<Account> account2Opt = accountRepository.findById(targetAccountId);

        if (account1Opt.isEmpty() || account2Opt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Account not found");
        }

        Account account1 = account1Opt.get();
        Account account2 = account2Opt.get();

        // VALIDAR SALDO
        if (value > account1.getBalance()) {
            return ResponseEntity.badRequest().body("Insufficient balance in the source account");
        }

        // VALIDAR HORÁRIOS E TIPO DE CONTA
        LocalTime now = LocalTime.now();
        LocalTime start = LocalTime.of(22, 0);
        LocalTime end = LocalTime.of(6, 0);

        if (account2.getType().equals("PJ") && (now.isAfter(start) || now.isBefore(end)) && value > 1000) {
            return ResponseEntity.badRequest().body("Transfers above 1000 are not allowed for PJ accounts during restricted hours");
        }


        account1.setBalance(account1.getBalance() - value);
        account2.setBalance(account2.getBalance() + value);

        accountRepository.save(account1);
        accountRepository.save(account2);

        return ResponseEntity.ok("Transfer successful");
    }


    @GetMapping("/{id}/transactions")
    public ResponseEntity<List<Transaction>> getAllTransactions (@PathVariable Integer id) {
        List<Transaction> transactions = transactionRepository.findTransactionsByAccountId(id);
        return transactions.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(transactions);
    }

}
