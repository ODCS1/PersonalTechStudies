package com.store.store.model;

import jakarta.persistence.*;

@Entity
@Table
public class ProductCategory {

        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Integer ProductCategoryID;

        @Column
        private String name;

        @Column
        private String Description;

    public ProductCategory(String name, String description) {
        this.name = name;
        Description = description;
    }

    public ProductCategory() {

    }

    public Integer getProductCategoryID() {
        return ProductCategoryID;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return Description;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDescription(String description) {
        Description = description;
    }
}
