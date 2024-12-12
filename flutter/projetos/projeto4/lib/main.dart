import 'package:flutter/material.dart';

void main(){
  runApp(const AppWidget());
  AppController.instance = AppController();
}

class AppWidget extends StatelessWidget {
  const AppWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: AppController.instance,
      builder: (context, child) {
        return MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            primarySwatch: Colors.red,
            appBarTheme: const AppBarTheme(
              backgroundColor: Colors.red,
              titleTextStyle: TextStyle(color: Colors.white, fontSize: 20.0)
            ),

            brightness: AppController.instance.isDarkTheme
                ? Brightness.dark
                : Brightness.light
          ),

          home: const HomePage(),
        );
      },
    );
  }
}


class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text("Notícias App"),
        actions: [
          AnimatedBuilder(
            animation: AppController.instance,
            builder: (context, child) {
              return Switch(
                value: AppController.instance.isDarkTheme, 
                onChanged: (value) {
                  AppController.instance.changeTheme();  
                },
              );
            },
          ),
          IconButton(
            onPressed: () {
              //
            },
            icon: const Icon(Icons.search)
          ),
          IconButton(
            onPressed: () {
              //
            },
            icon: const Icon(Icons.more_vert)
          ) 
        ],
      ),
    );
  }
}


class NewsPage extends StatefulWidget {
  const NewsPage({super.key});

  @override
  State<NewsPage> createState() => _NewsPageState();
}

class _NewsPageState extends State<NewsPage> {
  int currentNews = 0;

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}


class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Row(
        children: [
          Text("Configurações", style: TextStyle(fontSize: 24.0)),
          Icon(Icons.thumb_up)
        ]
        ),
    );
  }
}

class AppController extends ChangeNotifier {
  static AppController instance = AppController();

  bool isDarkTheme = false;
  void changeTheme() {
    isDarkTheme = !isDarkTheme;
    notifyListeners();
  }
}