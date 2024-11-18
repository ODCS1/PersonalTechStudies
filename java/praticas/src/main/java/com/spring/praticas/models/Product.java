package com.spring.praticas.models;


import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "product")
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@Getter
@Setter
@ToString
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "product_id")
    private Integer productId;

    @Column(name = "supplier_id")
    private Integer supplierId;

    @Column(name = "product_category_id")
    private Integer productCategoryId;

    @Column(name = "name", length = 100, nullable = false)
    private String name;

    @Column(name = "unit_price", nullable = false)
    private Double unitPrice;

    @Column(name = "units_in_stock", nullable = false)
    private Integer unitsInStock;

    @Column(name = "discounted", nullable = false)
    private Boolean discounted;

}