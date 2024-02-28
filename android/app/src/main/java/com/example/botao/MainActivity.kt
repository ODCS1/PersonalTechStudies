package com.example.botao

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

class MainActivity : AppCompatActivity() {
    private lateinit var btn_switch: Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btn_switch = findViewById(R.id.btn_mostrar)
    }

    fun trocarTela(view: View) {
        if (view == btn_switch) {
            startActivity(Intent(this@MainActivity, telaAbrir::class.java))
            finish()
        }
    }
}