import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
  AppController.instance = AppController();
}


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: AppController.instance,
      builder: (context, child) {

        return MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            primarySwatch: Colors.red,
            brightness: AppController.instance.isDarkTheme 
                ? Brightness.dark 
                : Brightness.light,

            appBarTheme: const AppBarTheme(
              backgroundColor: Colors.red,
              titleTextStyle: TextStyle(color: Colors.white, fontSize: 20.0)
            ),
            
          ),
          home: const HomePage(),
        );


      },
    );
  }

}


class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int counter = 0;
  int page = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Meu App"),
        actions:[
          AnimatedBuilder(
            animation: AppController.instance,
            builder: (context, child) {
              return Switch (
                value: AppController.instance.isDarkTheme,
                onChanged: (value) {
                  AppController.instance.changeTheme();
                },
              );
            },
          ),
          IconButton(
            onPressed: (){

            },
            icon: const Icon(Icons.search)
          ),
          IconButton(
            onPressed: (){

            },
            icon: const Icon(Icons.more_vert)
          )
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children:  [
            const DrawerHeader(
              decoration: BoxDecoration(color: Colors.red),
              child: Text("Menu", style: TextStyle(color: Colors.white))
            ),
            ListTile(
              leading: const Icon(Icons.home),
              title: const Text("Inicío"),
              onTap: () {
                setState(() {
                  page = 0;
                  Navigator.pop(context);
                });
              },
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text("Configurações"),
              onTap: () {
                setState(() {
                  page = 1;
                  Navigator.pop(context);
                });
              },
            )
          ],
        ),
      ),
      
      body: page != 0
          ? const SettingsPage()
          : const CounterHome(),
    );
  }
}


class CounterHome extends StatefulWidget {
  const CounterHome({super.key});

  @override
  State<CounterHome> createState() => _CounterHomeState();
}

class _CounterHomeState extends State<CounterHome> {
  int counter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text("CLICOU $counter"),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  counter = 0;
                });
              },
              child: const Text("Limpar")
            )
          ],
        ),
      ),

      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            counter++;
          });
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(

      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: const Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            "Configurações",
            style: TextStyle(fontSize: 26.0),
          ),
          Icon(Icons.hail_sharp)
        ],
      )
    )

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