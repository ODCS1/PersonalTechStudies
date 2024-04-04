package praticando.p016;

public class Ex11 {

    public class Author {
        private String name;
        private String email;
        private char gender;

        public Author(String name, String email, char gender){
            this.name = name;
            setEmail(email);
            this.gender = gender;
        }

        public String getName(){
            return this.name;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email){
            this.email = email;
        }

        public char getGender() {
            return gender;
        }

        public boolean equals(Author another){
            if ((this.email == another.email) && (this.name == another.name)){
                return true;
            }

            return false;
        }

        public String toString(){
            return "Author[name = " + this.name + ", email = " + this.email + ", gender = "+ this.gender + "]";
        }
    }



    public class Book {
        private String name;
        private Author author;
        private Double price;
        private int quantity = 0;

        public Book(String name, Author author, Double price){
            this.name = name;
            this.author = author;
            setPrice(price);
        }

        public Book(String name, Author author, Double price, int quantity){
            this.name = name;
            this.author = author;
            setPrice(price);
            setQuantity(quantity);
        }

        public String getName() {
            return name;
        }

        public Author getAuthor(){
            return this.author;
        }

        public Double getPrice(){
            return this.price;
        }

        public void setPrice(Double price) {
            this.price = price;
        }

        public int getQuantity(){
            return this.quantity;
        }

        public void setQuantity(int quantity){
            this.quantity = quantity;
        }

        public boolean equals(Book another){
            if ((this.name == another.name) && (this.author == another.author)){
                return true;
            }

            return false;
        }

        public String toString(){
            return "Book[name = " + this.name + ", Author[name = " + this.author.getName() + ", email = " + this.author.getEmail() + ", gender = " + this.author.getGender() + "], price = " + this.price + ", quantity = " + this.quantity + "]";
        }

    }


}