package com.spring.praticas.repositories;

import com.spring.praticas.models.ProductReview;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProductReviewRepository extends JpaRepository<ProductReview, Integer> {
    List<ProductReview> findProductReviewById (Integer productId);
}
