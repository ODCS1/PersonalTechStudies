package com.tucapay.account.model;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "transaction")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@EqualsAndHashCode
@ToString
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer transactionId;

    @Column(name = "account_id", nullable = false)
    private Integer accountId;

    @Column(name = "data", nullable = false)
    private LocalDateTime data;

    @Column(name = "amount", nullable = false)
    private Double amount;

    @Column(name = "notes", nullable = false, length = 255)
    private  String notes;
}
