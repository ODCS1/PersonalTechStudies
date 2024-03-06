package com.example.teste

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

class MainActivity2 : AppCompatActivity() {
    private lateinit var btn_irTela3: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        btn_irTela3 = findViewById(R.id.btn_irTela3)
    }

    fun irTela3(view: View){
        if (view == btn_irTela3){
            startActivity(Intent(this@MainActivity2, MainActivity3::class.java))
        }
    }

    fun voltarTela1(view: View){
        startActivity(Intent(this@MainActivity2, MainActivity::class.java))
    }
}