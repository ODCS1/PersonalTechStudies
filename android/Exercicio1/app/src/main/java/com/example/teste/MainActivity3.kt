package com.example.teste

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

class MainActivity3 : AppCompatActivity() {
    private lateinit var btn_voltarTela2: Button

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main3)
        btn_voltarTela2 = findViewById(R.id.btn_voltarTela2)
    }

    fun voltarTela2(view: View){
        if (btn_voltarTela2 == view) {
            startActivity(Intent(this@MainActivity3, MainActivity2::class.java))
        }
    }
}