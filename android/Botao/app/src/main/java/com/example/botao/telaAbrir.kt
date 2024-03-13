package com.example.botao

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import com.example.botao.databinding.ActivityMainBinding

class telaAbrir : AppCompatActivity() {
    private lateinit var btn_switch: Button
    private lateinit var txt: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_abrir)

        btn_switch = findViewById(R.id.btn_voltar)
        txt = findViewById(R.id.textView2)

        val bundle = intent.extras // todos os parâmetros passados

        if (bundle != null) {
            val filme = bundle.getString("filme")
            val classificacao = bundle.getInt("classificacao")
            val avaliacoes = bundle.getDouble("avaliacoes")

            val result = "Filme: $filme - Classificação: $classificacao - Avaliações: $avaliacoes"

            txt.text = result
        }

    }

    fun voltarTela(view: View){
        if (view == btn_switch){
            startActivity(Intent(this@telaAbrir, MainActivity::class.java))
        }
    }
}