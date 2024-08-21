package com.store.store.model;

import jakarta.persistence.Column;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

import java.util.Date;

public class Employee {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer EmployeeID;

    @Column
    private String Name;

    @Column
    private Date BirthDate;

    @Column
    private Date HireDate;

    @Column
    private String address;

    @Column
    private String City;

    @Column
    private  String State;

    @Column
    private String PostalCode;

    @Column
    private String Phone;

    public Employee(String name, Date birthDate, Date hireDate, String address, String city, String state, String postalCode, String phone) {
        Name = name;
        BirthDate = birthDate;
        HireDate = hireDate;
        this.address = address;
        City = city;
        State = state;
        PostalCode = postalCode;
        Phone = phone;
    }

    public Integer getEmployeeID() {
        return EmployeeID;
    }

    public String getName() {
        return Name;
    }

    public Date getBirthDate() {
        return BirthDate;
    }

    public Date getHireDate() {
        return HireDate;
    }

    public String getAddress() {
        return address;
    }

    public String getCity() {
        return City;
    }

    public String getState() {
        return State;
    }

    public String getPostalCode() {
        return PostalCode;
    }

    public String getPhone() {
        return Phone;
    }

    public void setName(String name) {
        Name = name;
    }

    public void setBirthDate(Date birthDate) {
        BirthDate = birthDate;
    }

    public void setHireDate(Date hireDate) {
        HireDate = hireDate;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setCity(String city) {
        City = city;
    }

    public void setState(String state) {
        State = state;
    }

    public void setPostalCode(String postalCode) {
        PostalCode = postalCode;
    }

    public void setPhone(String phone) {
        Phone = phone;
    }
}
