package com.daroca.ecommerce.controller;


import java.util.List;
import java.util.Optional;

import javax.swing.text.html.Option;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.daroca.ecommerce.model.Product;
import com.daroca.ecommerce.repositories.ProductRepository;

@RestController
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductRepository productRepository;

    @GetMapping("/product")
    public List<Product> all(){
        return productRepository.findAll();
    }

    @GetMapping("/product/{codigo}")
    public Optional<Product> one(@PathVariable Integer id){
        return productRepository.findById(id);
    }
}
