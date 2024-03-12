package com.example.botao

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import com.example.botao.databinding.ActivityMainBinding
import org.w3c.dom.Text

// EXISTE ALGUNS MÉTÓDOS QUE CONTROLAM O CICLO DE VIDA DE UMA ACTIVITY
// onCreate, onStart, onResume, onPause, onStop, onRestart e onDestroy.

//onCrete: Cria a Activity, aquelas animações de loading estão aqui.

//onStart: Aqui é onde de fato carrega os dados

//onResume: Onde de fato o app fica pronto para o usuário interagir

//onPause: Quando o usuário não estiver usando o app 100%, por exemplo quando ele
// estiver em uma ligação, entrará nesse método, indo depois para o onStop ou onResume

//onStop: Este método é chamado quando a tela fica totalmente invisível para o usuario
// para liberar ou ajustar recursos que nnão precisam estra disponíveis

//onRestart: Este método é chamado quando a Activity sai do estado de pausado onStop()
// ou de interrupção onStop() e volta a ser utilizado.

//onDestroy: Esse método será chamado quando a Activity for destruída, isso poderá
// acontecer se o usuário fechar o app ou quando ocorre uma mudança de configuração
// como rotação de tela.

class MainActivity : AppCompatActivity() {
    private lateinit var b: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.i("ciclo_vida", "onCreate")
        b = ActivityMainBinding.inflate(layoutInflater)
        setContentView(b.root)


        b.btnMostrar.setOnClickListener{
            b.textoPrincipal.text = "CLICOU!!!"

            startActivity(Intent(this, telaAbrir::class.java))
        }
    }

    override fun onStart() {
        super.onStart()
        // CARREGAR DADOS
        Log.i("ciclo_vida", "onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.i("ciclo_vida", "onResume")
    }

    override fun onPause() {
        super.onPause()
        Log.i("ciclo_vida", "onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.i("ciclo_vida", "onStop")
    }

    override fun onRestart() {
        super.onRestart()
        Log.i("ciclo_vida", "onRestart")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.i("ciclo_vida", "onDestroy")
    }
}