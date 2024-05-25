package com.daroca.ecommerce.controller;

import com.daroca.ecommerce.model.Customer;
import com.daroca.ecommerce.repositories.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/customers")
public class CustomerController {

    @Autowired
    private CustomerRepository repository;

    @GetMapping
    public List<Customer> all() {
        return repository.findAll();
    }

    @GetMapping("/customers/{id}")
    public Optional<Customer> one(@PathVariable Integer id) {
        return repository.findById(id);
    }

    @DeleteMapping("/customers/{id}")
    public void delete(@PathVariable Integer id) {
        repository.deleteById(id);
    }

    @PostMapping("/customers/save")
    public Customer save(@RequestBody Customer customer) {
        return repository.save(customer);
    }

    @PutMapping
    public Customer replace(@RequestBody Customer newCustomer, @PathVariable Integer id) {
        return repository.findById(id)
                .map(customer -> {
                    customer.setName(newCustomer.getName());
                    customer.setEmail(newCustomer.getEmail());
                    customer.setLatitude(newCustomer.getLatitude());
                    customer.setLongitude(newCustomer.getLongitude());
                    return repository.save(customer);
                })
                .orElseGet(() -> {
                    return repository.save(newCustomer);
                });
    }
}
