import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return  MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.red,
        appBarTheme: const AppBarTheme(
          backgroundColor:  Colors.red,
          titleTextStyle: TextStyle(color: Colors.white, fontSize: 20.0)
        ),
        brightness: Brightness.dark
      ),
      home: const HomePage()
    );
  }
}



class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int currentPage = 0;


  @override
  Widget build(BuildContext context) {
    Widget page = const SizedBox.shrink();
    if (currentPage == 0) {
      page = const NoticiasPage();
    }else if (currentPage == 1) {
      page = const NoticiasFavoritasPage();
    }else if (currentPage == 2){
      page = const AdicionarNoticias();
    }


    return Scaffold(
        appBar: AppBar(
          title: const Text('Meu App'),
          elevation: 0,
        ),
        drawer: Drawer(
          child: ListView(
            padding: EdgeInsets.zero,
            children: [
              const DrawerHeader(
                decoration: BoxDecoration(color: Colors.red),
                child: Text(
                  "Menu",
                  style: TextStyle(fontSize: 20.0, color: Colors.white),
                )
              ),
              ListTile(
                leading: const Icon(Icons.newspaper),
                title: const Text("Notícias"),
                onTap: () {
                  // TELA DE NOTÍCIAS
                  setState(() {
                    currentPage =  0;
                    Navigator.pop(context);
                  });
                },
              ),

              ListTile(
                leading: const Icon(Icons.favorite),
                title: const Text("Favoritas"),
                onTap: () {
                  // TELA DE NOTÍCIAS FAVORITAS
                  setState(() {
                    currentPage =  1;
                    Navigator.pop(context);
                  });
                },
              ),

              ListTile(
                leading: const Icon(Icons.add),
                title: const Text("Adicionar"),
                onTap: () {
                  // TELA DE NOTÍCIAS FAVORITAS
                  setState(() {
                    currentPage =  2;
                    Navigator.pop(context);
                  });
                },
              ),
            ],
          ),
        ),
        body: page,
      );
  }
}



class NoticiasPage extends StatefulWidget {
  const NoticiasPage({super.key});

  @override
  State<NoticiasPage> createState() => _NoticiasPageState();
}

class _NoticiasPageState extends State<NoticiasPage> {

  List<Widget> getNoticias() {
    return AppController.instance.noticias.asMap().map((index, noticia) {
      return MapEntry(
        index,
        Center(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 12.0),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 600),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // TÍTULO DA NOTÍCIA (HEADER)
                  Container(
                    width: double.infinity,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Padding(
                          padding: const EdgeInsets.symmetric(vertical: 8.0),
                          child: Text(
                            noticia['titulo']!,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.symmetric(vertical: 8.0),
                          child: Row(
                            children: [
                              IconButton(
                                onPressed: () {
                                  setState(() {
                                    AppController.instance.toggleFavorite(index);
                                  });
                                },
                                icon: Icon(
                                  AppController.instance.favoriteIndexes.contains(index)
                                      ? Icons.favorite
                                      : Icons.favorite_border,
                                  color: AppController.instance.favoriteIndexes.contains(index)
                                      ? Colors.red
                                      : Colors.white,
                                ),
                              ),
                              IconButton(
                                onPressed: () {
                                  //
                                },
                                icon: const Icon(Icons.edit),
                              ),

                              IconButton(
                                onPressed: (){
                                  setState(() {
                                    AppController.instance.toggleFavorite(index);
                                    AppController.instance.noticias.removeAt(index);
                                  });
                                },
                                icon: const Icon(Icons.delete)
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                  // IMAGEM
                  Stack(
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(10),
                        child: Image.network(
                          noticia['imagem']!,
                          height: 350,
                          width: double.infinity,
                          fit: BoxFit.cover,
                        ),
                      ),
                      Positioned(
                        bottom: 8,
                        left: 8,
                        child: Container(
                          color: Colors.black54,
                          padding: const EdgeInsets.symmetric(vertical: 2, horizontal: 8),
                          child: Text(
                            noticia['tempo']!,
                            style: const TextStyle(color: Colors.white, fontSize: 12),
                          ),
                        ),
                      ),
                    ],
                  ),
                  // DESCRIÇÃO
                  Text(
                    noticia['descricao']!,
                    style: const TextStyle(color: Colors.white70, fontSize: 14),
                  ),
                  // SEPARANDO AS NOTÍCIA COM UMA LINHA
                  const Divider(color: Colors.white54),
                ],
              ),
            ),
          ),
        ),
      );
    }).values.toList();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ListView(
          children: getNoticias(),
        ),
      ),
    );
  }
}



class NoticiasFavoritasPage extends StatefulWidget {
  const NoticiasFavoritasPage({super.key});

  @override
  State<NoticiasFavoritasPage> createState() => _NoticiasFavoritasPageState();
}

class _NoticiasFavoritasPageState extends State<NoticiasFavoritasPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          width: 600,
          
          child: AnimatedBuilder(
            animation: AppController.instance,
            builder: (context, child) {
              final favoritas = AppController.instance.favoriteNoticias;

              return ListView.builder(
                itemCount: favoritas.length,
                itemBuilder: (context, index) {
                  final noticia = favoritas[index];
                  return Padding(
                    padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 12.0),
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 600),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            width: double.infinity,
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Padding(
                                  padding: const EdgeInsets.symmetric(vertical: 8.0),
                                  child: Text(
                                    noticia['titulo']!,
                                    style: const TextStyle(
                                      color: Colors.white,
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ),
                                const Row(
                                  children: [
                                    Icon(
                                        Icons.favorite,
                                        color: Colors.red,
                                      ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(10),
                            child: Image.network(
                              noticia['imagem']!,
                              height: 350,
                              width: double.infinity,
                              fit: BoxFit.cover,
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.symmetric(vertical: 8.0),
                            child: Text(
                              noticia['descricao']!,
                              style: const TextStyle(color: Colors.white70, fontSize: 14),
                            ),
                          ),
                          const Divider(color: Colors.white54),
                        ],
                      ),
                    ),
                  );
                },
              );
            },
          ),
        ),
      ),
      
    );
  }
}


class AdicionarNoticias extends StatefulWidget {
  const AdicionarNoticias({super.key});

  @override
  State<AdicionarNoticias> createState() => _AdicionarNoticiasState();
}

class _AdicionarNoticiasState extends State<AdicionarNoticias> {
  final _tituloController = TextEditingController();
  final _descricaoController = TextEditingController();
  final _imagemController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Campo de título
            TextField(
              controller: _tituloController,
              decoration: const InputDecoration(
                labelText: 'Título da Notícia',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),

            // Campo de descrição
            TextField(
              controller: _descricaoController,
              decoration: const InputDecoration(
                labelText: 'Descrição da Notícia',
                border: OutlineInputBorder(),
              ),
              maxLines: 4, // Permite várias linhas para descrição
            ),
            const SizedBox(height: 16),

            // Campo de URL da imagem
            TextField(
              controller: _imagemController,
              decoration: const InputDecoration(
                labelText: 'URL da Imagem',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),

            // Botão para salvar a notícia
            ElevatedButton(
              onPressed: () {
                final String titulo = _tituloController.text;
                final String descricao = _descricaoController.text;
                final String imagem = _imagemController.text;

                // Adiciona a notícia ao controlador
                if (titulo.isNotEmpty && descricao.isNotEmpty && imagem.isNotEmpty) {
                  AppController.instance.noticias.add({
                    'titulo': titulo,
                    'descricao': descricao,
                    'imagem': imagem,
                    'tempo': 'Agora',
                  });

                  // Limpa os campos
                  _tituloController.clear();
                  _descricaoController.clear();
                  _imagemController.clear();

                  // Exibe uma mensagem de sucesso
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Notícia adicionada com sucesso!')),
                  );

                } else {
                  // Exibe um erro se algum campo estiver vazio
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Preencha todos os campos!')),
                  );
                }
              },
              child: const Text('Salvar Notícia'),
            ),
          ],
        ),
      ),
    );
  }
}





class AppController extends ChangeNotifier {
  static AppController instance = AppController();

  List<Map<String, String>> noticias = [
    {
      'titulo': 'Hotéis Accor.',
      'descricao': 'Aproveite o calor para relaxar ainda mais: encontre o hotel Accor com piscina mais pr...',
      'imagem':
          'https://images.unsplash.com/photo-1585081514381-429d5275c855?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      'tempo': '1 sem.'
    },
    {
      'titulo': 'Resorts Maravilhosos.',
      'descricao': 'Conheça os melhores resorts com experiências exclusivas para você e sua família!',
      'imagem':
          'https://images.unsplash.com/photo-1733392898848-72e6a57df7fe?q=80&w=2671&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      'tempo': '2 dias'
    },
    {
      'titulo': 'Praias Incríveis.',
      'descricao': 'Descubra as praias mais paradisíacas para suas férias perfeitas!',
      'imagem':
          'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      'tempo': '5 h'
    },
  ];


  List<int> favoriteIndexes = [];

  // TROCAR O ESTADO DE FAVORITO
  void toggleFavorite(int index) {
    if (favoriteIndexes.contains(index)) {
      favoriteIndexes.remove(index);
    } else {
      favoriteIndexes.add(index);
    }

    notifyListeners();
  }


  // GET DAS NOTÍCIAS FAVORITAS
  List<Map<String, String>> get favoriteNoticias {
    return favoriteIndexes.map((index) => noticias[index]).toList();
  }
}