package com.exemplo.models;

public class SavingsAccount extends Account{

    private Double annualRate = 0.001;

    public SavingsAccount(String owner, Double balance, String annualRate){
        super(owner, balance);
    }

    public SavingsAccount(String owner, Double balance, Double annualRate){
        super(owner, balance);
        if (annualRate > 0.0){
            this.annualRate = annualRate;
        }
    }

}
