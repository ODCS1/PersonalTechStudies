import 'dart:convert';
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

  // FUNÇÃO QUE FAZ A REQUISIÇÃO PARA A API
  Future<List<String>> fetchData() async {
    final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/users'));

    if (response.statusCode == 200) {

      List<dynamic> data = json.decode(response.body);

      return data.map((user) => user['name'] as String).toList();
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
      body: FutureBuilder<List<String>>(
        future: fetchData(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Erro: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return Center(child: Text('Nenhum dado encontrado'));
          } else {
            // EXIBE OS DADOS SE DEU CERTO
            return ListView(
              children: snapshot.data!.map((name) => ListTile(title: Text(name))).toList(),
            );
          }
        },
      ),
    );
  }
}
