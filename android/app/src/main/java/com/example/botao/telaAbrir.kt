package com.example.botao

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

class telaAbrir : AppCompatActivity() {
    private lateinit var btn_switch: Button
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_abrir)
        btn_switch = findViewById(R.id.btn_voltar)
    }

    fun voltarTela(view: View){
        if (view == btn_switch){
            startActivity(Intent(this@telaAbrir, MainActivity::class.java))
        }
    }
}