import 'dart:convert';  // Para converter o JSON
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Exemplo de API',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  // FUNÇÃO PARA A REQUISIÇÃO
  Future<List<Map<String, dynamic>>> fetchData() async {
    final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/users'));

    if (response.statusCode == 200) {
      // PARSEIA O JSON PORUQE DEU CERTO
      List<dynamic> data = json.decode(response.body);
      return data.map((user) => user as Map<String, dynamic>).toList();
    } else {
      throw Exception('Falha ao carregar os dados');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Exemplo de API com Flutter'),
      ),
      body: FutureBuilder<List<Map<String, dynamic>>>(
        // CHAMA A FUNÇÃO QUE FAZ A REQUISIÇÃO
        future: fetchData(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Erro: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('Nenhum dado encontrado'));
          } else {
            // A LISTA DE DADOS SERÁ GERADA COM OS VALORES DO DICIONÁRIO
            var data = snapshot.data!;
            List<Widget> items = [];
            data.forEach((user) {
              user.forEach((key, value) {
                items.add(ListTile(
                  title: Text('$key: $value'),
                ));
              });
            });

            return ListView(
              children: items, // EXITE TODOS OS VALORES
            );
          }
        },
      ),
    );
  }
}
