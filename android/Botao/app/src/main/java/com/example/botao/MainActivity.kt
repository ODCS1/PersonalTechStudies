package com.example.botao

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import org.w3c.dom.Text

class MainActivity : AppCompatActivity() {
    private lateinit var btn_switch: Button
    private lateinit var texto: TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btn_switch = findViewById(R.id.btn_mostrar)
        texto = findViewById(R.id.textoPrincipal)
    }

    fun trocarTela(view: View){
        if (view == btn_switch){
            texto.text = "VOCÊ CLICOU"
            startActivity(Intent(this@MainActivity, telaAbrir::class.java))
        }
    }

}