package praticando.p016;

public class Ex015 {
    public abstract class Employee {
        private int id;
        private String firstName;
        private String lastName;
        private char gender;

        public Employee(int id, String firstName, String lastName, char gender){
            this.id = id;
            this.firstName = firstName;
            this.lastName = lastName;
            this.gender = gender;
        }

        public int getId(){
            return id;
        }

        public String getFirstName(){
            return this.firstName;
        }

        public String getLastName(){
            return this.lastName;
        }

        public String getName(){
            return this.firstName + " " + this.lastName;
        }

        public char getGender(){
            return this.gender;
        }

        public abstract double calculateWeeklyPay();

        public String toString(){
            return "Employee[id = " + getId() + ", name = " + getName() + ", gender = " + getGender() + "]";
        }
    }


    public class HourlyEmployee extends Employee {
        private double hourlySalary;
        private int hoursWorked = 0;

        public HourlyEmployee(int id, String firstName, String lastName, char gender, double hourlySalary){
            super(id, firstName, lastName, gender);
            this.hourlySalary = hourlySalary;
        }

        public HourlyEmployee(int id, String firstName, String lastName, char gender, double hourlySalary, int hoursWorked){
            super(id, firstName, lastName, gender);
            this.hourlySalary = hourlySalary;
            this.hoursWorked = hoursWorked;
        }

        @Override
        public int getId(){
            return super.getId();
        }

        @Override
        public String getFirstName(){
            return super.getFirstName();
        }

        @Override
        public String getLastName(){
            return super.getLastName();
        }

        @Override
        public String getName(){
            return super.getName();
        }

        @Override
        public char getGender(){
            return super.getGender();
        }

        public double getHourlySalary(){
            return this.hourlySalary;
        }

        public void setHourlySalary(double hourlySalary){
            this.hourlySalary = hourlySalary;
        }

        public int getHoursWorked(){
            return this.hoursWorked;
        }

        public void setHoursWorked(int hoursWorked){
            this.hoursWorked = hoursWorked;
        }

        @Override
        public double calculateWeeklyPay(){
            if (this.hoursWorked <= 168){
                return this.hoursWorked*this.hourlySalary;
            }

            return 168 * this.hourlySalary;
        }


        @Override
        public String toString(){
            return "HourlyEmployee[Employee[id = " + getId() + ", name = " + getName() + ", gender = " + getGender() + "], hourlySalary = " + getHourlySalary() + ", hoursWorked = " + getHoursWorked() + "]";
        }
    }

    public class SalaryEmployee extends Employee {
        private double weeklySalary;

        public SalaryEmployee(int id, String firstName, String lastName, char gender, double weeklySalary){
            super(id, firstName, lastName, gender);
            this.weeklySalary = weeklySalary;
        }

        @Override
        public int getId(){
            return super.getId();
        }

        @Override
        public String getFirstName(){
            return super.getFirstName();
        }

        @Override
        public String getLastName(){
            return super.getLastName();
        }

        @Override
        public String getName(){
            return super.getName();
        }

        @Override
        public char getGender(){
            return super.getGender();
        }

        public double getWeeklySalary(){
            return this.weeklySalary;
        }

        public void setWeeklySalary(double weeklySalary){
            this.weeklySalary = weeklySalary;
        }

        @Override
        public double calculateWeeklyPay(){
            return this.weeklySalary;
        }

        @Override
        public String toString(){
            return "SalaryEmployee[Employee[id = " + getId() + ", name = " + getName() + ", gender = " + getGender() + "], weeklySalary = " + getWeeklySalary() + "]";
        }

        
    }

}
