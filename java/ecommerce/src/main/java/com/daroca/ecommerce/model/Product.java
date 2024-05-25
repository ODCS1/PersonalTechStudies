package com.daroca.ecommerce.model;

import jakarta.persistence.*;

public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer productId;

    @Column(length = 50, nullable = false)
    private String name;

    @Column(nullable = false)
    private Double unitPrice;

    @OneToMany
    @JoinColumn(name = "product_category_id", foreignKey = @ForeignKey(name = "FK_ProductCategory"))
    @Column
    private ProductCategory productCategory;

    public Product(int productId, String name, Double unitPrice){
        this.productId = productId;
        this.name = name;
        this.unitPrice = unitPrice;
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getUnitPrice() {
        return unitPrice;
    }

    public void setUnitPrice(Double unitPrice) {
        this.unitPrice = unitPrice;
    }
}
