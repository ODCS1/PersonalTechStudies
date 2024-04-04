package praticando.p016;

import java.util.Arrays;

public class Ex13 {
    public class Product {
        private int id;
        private String name;
        private double price;
    
        public Product(int id, String name, double price) {
            this.id = id;
            this.name = name;
            this.price = price;
        }
    
        public int getId() {
            return this.id;
        }
    
        public String getName() {
            return this.name;
        }
    
        public double getPrice() {
            return this.price;
        }
    
        public void setPrice(double price) {
            this.price = price;
        }
    
        public boolean equals(Product other) {
            return (this.id == other.getId() && this.name == other.getName());
        }
    
        @Override
        public String toString() {
            return "Product{" +
                    "id=" + id +
                    ", name='" + name + '\'' +
                    ", price=" + price +
                    '}';
        }
    }

    public class Customer {
        private int id;
        private String name;
        private int discount;
    
        public Customer(int id, String name, int discount) {
            this.id = id;
            this.name = name;
            this.discount = discount;
        }
    
        public int getId() {
            return id;
        }
    
        public String getName() {
            return name;
        }
    
        public int getDiscount() {
            return discount;
        }
    
        public void setDiscount(int discount) {
            this.discount = discount;
        }
    
        @Override
        public String toString() {
            return "Customer[" +
                    "id = " + id +
                    ", name = '" + name + '\'' +
                    ", discount = " + discount +
                    ']';
        }
    }

    public class Invoice {
        private int id;
        private Customer customer;
        private int nProducts = 0;
        private Product[] products;
        private int[] quantities;

        public Invoice(int id, Customer customer) {
            this.id = id;
            this.customer = customer;
            this.products = new Product[30];
            this.quantities = new int[30];
        }

        public double getTotal() {
            double total = 0.0;
            for (int i = 0; i < this.nProducts; i++) {
                total += this.products[i].getPrice() * this.quantities[i];
            }
            return total;
        }

        public double getTotalAfterDiscount() {
            return (1 - (double) this.customer.getDiscount() / 100) * this.getTotal();
        }

        public boolean addProduct(Product product, int amount) {
            for (int i = 0; i < this.nProducts; i++) {
                if (products[i].equals(product)) {
                    return false;
                }
            }
            this.products[this.nProducts] = product;
            this.quantities[this.nProducts] = amount;
            this.nProducts++;
            return true;
        }

        public boolean removeProduct(Product product) {
            boolean found = false;
            int index = -1;
            for (int i = 0; i < this.nProducts; i++) {
                if (products[i].equals(product)) {
                    found = true;
                    index = i;
                    break;
                }
            }
            if (found) {
                for (int i = index; i < this.nProducts - 1; i++) {
                    this.products[i] = this.products[i + 1];
                    this.quantities[i] = this.quantities[i + 1];
                }
                this.nProducts--;
                return true;
            }
            return false;
        }

        @Override
        public String toString() {
            return "Invoice[" +
                    "id = " + id +
                    ", customer = " + customer +
                    ", nProducts = " + nProducts +
                    ", products = " + Arrays.toString(products) +
                    ", quantitie = " + Arrays.toString(quantities) +
                    ']';
        }
    }
}
