// PACOTE QUE CONTÉM OS WIDGETS E FUNCIONALIDADES FUNDAMENTAIS PARA CRIAR UMA INTERFACE SEGUINDO OS PRINCÍPIOS DO MATERIAL DESIGN.
import 'package:flutter/material.dart';


// PONTO DE ENTRADA DO APLICATIVO
void main() {
  runApp(const MyApp());
}


// WIDGET RAÍZ SEM ESTADO (StatelessWidget)
class MyApp extends StatelessWidget {
  
// CONSTRUTOR DECLARA QUE O WIDGET É IMUTÁVEL OTIMIZANDO O DESEMPENHO
  const MyApp({super.key});

  
  
// ESSE MÉTODO BUILD DEFINE A INTERFACE DO APLICATIVO
  @override
  Widget build(BuildContext context) {
    
//     RETORNA UM MATERIALAPP QUE É O WIDGET RESPONSÁVEL POR CONFIGURAR TEMAS, ROTAS E OUTRAS CONFIGURAÇÕES GLOBAIS. 
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Text('Hello, World!'),
        ),
      ),
    );
  }
  
  
  
  
}
