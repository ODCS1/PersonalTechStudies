package com.tucapay.account.model;


import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "account")
@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@EqualsAndHashCode
@ToString
public class Account {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer accountId;

    @Column(name = "number", length = 100, nullable = false)
    private Integer number;

    @Column(name = "type", length = 100, nullable = false)
    private String type;

    @Column(name = "owner", length = 150, nullable = false)
    private String owner;

    @Column(name = "balance", length = 100, nullable = false)
    private Double balance;

}
