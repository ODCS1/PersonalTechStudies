package com.spring.praticas.models;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "supplier")
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@Getter
@Setter
@ToString
public class Supplier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "supplier_id")
    private Integer supplierId;

    @Column(name = "name",length = 100, nullable = false)
    String name;

    @Column(name = "adress", length = 200, nullable = false)
    String address;

    @Column(name = "city", length = 100, nullable = false)
    String city;

    @Column(name = "state", length = 100, nullable = false)
    String state;

    @Column(name = "postal_code", length = 50, nullable = false)
    String postalCode;

}
