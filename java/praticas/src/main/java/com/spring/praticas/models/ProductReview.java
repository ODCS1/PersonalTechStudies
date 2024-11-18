package com.spring.praticas.models;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "product_review")
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@Getter
@Setter
@ToString
public class ProductReview {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "product_review_id")
    private Integer productReviewId;

    @Column(name = "review_name", length = 100, nullable = false)
    String reviewName;

    @Column(name = "review_date", nullable = false)
    private LocalDateTime reviewDate;

    @Column(name = "rating", nullable = false)
    private Integer rating;

    @Column(name = "comments", length = 255, nullable = false)
    String comments;
}
