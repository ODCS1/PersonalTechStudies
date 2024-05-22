package com.example.navigation

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.fragment.findNavController

class Tela3Fragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view3 = inflater.inflate(R.layout.fragment_tela3, container, false)
        val btnVoltarTela2 = view3.findViewById<Button>(R.id.btnVoltarTela2)

        btnVoltarTela2.setOnClickListener{
            findNavController().navigate(R.id.action_tela3Fragment_to_tela2Fragment)
        }

        return view3
    }
}