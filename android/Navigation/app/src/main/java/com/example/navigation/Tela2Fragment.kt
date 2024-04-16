package com.example.navigation

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.fragment.findNavController

class Tela2Fragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view2 = inflater.inflate(R.layout.fragment_tela2, container, false)
        val btnVoltarTela1 = view2.findViewById<Button>(R.id.btnVoltarTela1)
        val btnIrTela3 = view2.findViewById<Button>(R.id.btnIrTela3)

        btnVoltarTela1.setOnClickListener{
            findNavController().navigate(R.id.action_tela2Fragment_to_homeFragment)
        }

        btnIrTela3.setOnClickListener{
            findNavController().navigate(R.id.action_tela2Fragment_to_tela3Fragment)
        }


        return view2
    }
}