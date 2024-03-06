package com.example.teste

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var btn_irTela2: Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btn_irTela2 = findViewById(R.id.btn_irTela2)
    }

    fun irTela2(view: View){
        if (view == btn_irTela2) {
            startActivity(Intent(this@MainActivity, MainActivity2::class.java))
        }
    }
}