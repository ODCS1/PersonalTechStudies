package com.daroca.ecommerce.controller;

import com.daroca.ecommerce.model.ProductCategory;
import com.daroca.ecommerce.repositories.ProductCategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/ProductCategory")
public class ProductCategoryController {
    @Autowired
    private ProductCategoryRepository repository;

    @GetMapping("/ProductCategory")
    public List<ProductCategory> all(){
        return repository.findAll();
    }

    @GetMapping("/ProductCategory/{id}")
    public Optional<ProductCategory> one(@PathVariable Integer id){
        return repository.findById(id);
    }

}
