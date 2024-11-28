import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Notícias Flutter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: NoticiasPage(),
    );
  }
}

class NoticiasPage extends StatefulWidget {
  @override
  _NoticiasPageState createState() => _NoticiasPageState();
}

class _NoticiasPageState extends State<NoticiasPage> {
  // Lista inicial de notícias
  List<Map<String, dynamic>> noticias = [
    {
      'imagem': 'https://via.placeholder.com/150',
      'titulo': 'Hotéis Accor',
      'descricao': 'Aproveite o calor para relaxar ainda mais: encontre o hotel Accor com piscina mais próximo de você.',
      'favorito': false,
    },
    {
      'imagem': 'https://via.placeholder.com/150',
      'titulo': 'Promoção de Viagens',
      'descricao': 'Descubra as melhores promoções de viagens para o verão!',
      'favorito': false,
    },
    {
      'imagem': 'https://via.placeholder.com/150',
      'titulo': 'Eventos de Verão',
      'descricao': 'Participe dos melhores eventos de verão na sua cidade.',
      'favorito': false,
    },
  ];

  // Lista de backup (para a pesquisa)
  late List<Map<String, dynamic>> noticiasOriginal;

  @override
  void initState() {
    super.initState();
    noticiasOriginal = List.from(noticias); // Backup para a pesquisa
  }

  // Alternar favorito
  void toggleFavorito(int index) {
    setState(() {
      noticias[index]['favorito'] = !noticias[index]['favorito'];
    });
  }

  // Filtrar notícias por título
  void filtrarNoticias(String texto) {
    setState(() {
      noticias = noticiasOriginal
          .where((noticia) =>
              noticia['titulo'].toLowerCase().contains(texto.toLowerCase()))
          .toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Notícias'),
        bottom: PreferredSize(
          preferredSize: Size.fromHeight(60),
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Pesquisar',
                prefixIcon: Icon(Icons.search),
                border: OutlineInputBorder(),
              ),
              onChanged: filtrarNoticias,
            ),
          ),
        ),
      ),
      body: ListView.builder(
        itemCount: noticias.length,
        itemBuilder: (context, index) {
          final noticia = noticias[index];

          return Card(
            margin: EdgeInsets.all(8),
            elevation: 4,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Image.network(
                  noticia['imagem'],
                  height: 200,
                  width: double.infinity,
                  fit: BoxFit.cover,
                ),
                ListTile(
                  title: Text(
                    noticia['titulo'],
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  subtitle: Text(
                    noticia['descricao'],
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  trailing: IconButton(
                    icon: Icon(
                      noticia['favorito'] ? Icons.favorite : Icons.favorite_border,
                      color: noticia['favorito'] ? Colors.red : null,
                    ),
                    onPressed: () => toggleFavorito(index),
                  ),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => DetalhesNoticiaPage(
                          titulo: noticia['titulo'],
                          descricao: noticia['descricao'],
                          imagem: noticia['imagem'],
                        ),
                      ),
                    );
                  },
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}

class DetalhesNoticiaPage extends StatelessWidget {
  final String titulo;
  final String descricao;
  final String imagem;

  DetalhesNoticiaPage({
    required this.titulo,
    required this.descricao,
    required this.imagem,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(titulo),
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Image.network(imagem,
                width: double.infinity, height: 200, fit: BoxFit.cover),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                titulo,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                descricao,
                style: TextStyle(fontSize: 16),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
