package com.daroca.ecommerce.model;


import jakarta.persistence.*;

@Entity
@Table
public class SalesOrderItem {
    @EmbeddedId
    private SalesOrderItemKey salesOrderItemId;

    @ManyToOne
    @MapsId("salesOrderId")
    @JoinColumn(name = "sales_order_id", foreignKey = @ForeignKey(name = "FK_SalesOrderItem_Sales"))
    private SalesOrder salesOrder;

    @ManyToOne // cardinalidade
    @MapsId("productId")
    @JoinColumn(name = "product_id", foreignKey = @ForeignKey(name = "FK_SalesOrderItem_Product"))
    private Product product;

    @Column(nullable = false)
    private  Integer quantity;

    public SalesOrderItem(){}

    public SalesOrderItem(SalesOrderItemKey salesOrderItemId, SalesOrder salesOrder, Product product, Integer quantity) {
        this.salesOrderItemId = salesOrderItemId;
        this.salesOrder = salesOrder;
        this.product = product;
        this.quantity = quantity;
    }

    public SalesOrderItemKey getSalesOrderItemId() {
        return salesOrderItemId;
    }

    public void setSalesOrderItemId(SalesOrderItemKey salesOrderItemId) {
        this.salesOrderItemId = salesOrderItemId;
    }

    public SalesOrder getSalesOrder() {
        return salesOrder;
    }

    public void setSalesOrder(SalesOrder salesOrder) {
        this.salesOrder = salesOrder;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }
}
