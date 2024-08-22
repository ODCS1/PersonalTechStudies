package com.store.store.model;

import jakarta.persistence.*;

@Entity
@Table
public class Product{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer ProductID;


}
