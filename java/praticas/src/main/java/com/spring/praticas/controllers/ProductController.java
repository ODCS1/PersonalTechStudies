package com.spring.praticas.controllers;

import com.spring.praticas.models.Product;
import com.spring.praticas.models.ProductReview;
import com.spring.praticas.repositories.ProductRepository;
import com.spring.praticas.repositories.ProductReviewRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/products")
public class ProductController {


    @Autowired
    private ProductRepository productRepository;

    @Autowired
    private ProductReviewRepository productReviewRepository;

    @GetMapping("/")
    public ResponseEntity<List<Product>> getAll () {
        List<Product> products = productRepository.findAll();
        return products.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(products);
    }

    @GetMapping("/{idProduct}")
    public ResponseEntity<Product> getProductById (@PathVariable Integer idProduct) {
        return productRepository.findById(idProduct)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.noContent().build());
    }

    @PostMapping("/")
    public ResponseEntity<Product> createProduct (@RequestBody Product product) {
        Product savedProduct = productRepository.save(product);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedProduct);
    }

    @PutMapping("/{idProduct}")
    public ResponseEntity<Product> updateProduct (@PathVariable Integer idProduct, @RequestBody Product product) {
        return  productRepository.findById(idProduct)
                .map(_product -> {
                    _product.setDiscounted(product.getDiscounted());
                    _product.setName(product.getName());
                    _product.setUnitPrice(product.getUnitPrice());
                    _product.setUnitsInStock(product.getUnitsInStock());
                    return ResponseEntity.ok(productRepository.save(_product));
                })
                .orElseGet( () -> {
                    // return ResponseEntity.notFound().build();
                    return ResponseEntity.status(HttpStatus.CREATED).body(productRepository.save(product));
                });
    }



    @GetMapping("/{idProduct}/reviews")
    public ResponseEntity<List<ProductReview>> getReviewByProductId (@PathVariable Integer idProduct) {
        List<ProductReview> reviews = productReviewRepository.findProductReviewById(idProduct);
        return reviews.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(reviews);
    }

}
