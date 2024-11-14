package com.spring.praticas.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class PingController {
    @GetMapping("ping")
    public String ping() {
        System.out.println("LIVE RELOAD FUNCIONANDO! ");
        return "Pong";
    }

    @GetMapping("PING")
    public String pingM() {
        System.out.println("LIVE RELOAD FUNCIONANDO! ");
        return "PONG";
    }
}
