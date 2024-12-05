import 'package:flutter/material.dart';
import 'package:ola_mundo/app_controller.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

class HomePageState extends State<HomePage> {
  int counter = 0;

  @override
  Widget build (BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "Home Page",
          style: TextStyle(fontSize: 20.0)
          ),
        actions:  [
          AnimatedBuilder(
          animation: AppController.instance,
          builder:(context, child) {
            return Switch(
              value: AppController.instance.isDarkTheme,
              onChanged: (value) {
                AppController.instance.changeTheme();
              }
            );
          }),
        ],
      ),
    
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children:  [
            const DrawerHeader(
              decoration: BoxDecoration(color: Colors.red),
              child: Text(
                "Menu",
                style: TextStyle(fontSize: 24.0),
              ),
            ),
            ListTile(
              leading: const  Icon(Icons.home),
              title: const Text("Inicio"),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: const  Icon(Icons.settings),
              title: const Text("Configurações"),
              onTap: () {
                Navigator.pop(context);
              },
            )
          ],
        ),
      ),

      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Clicou: $counter",
              style: const TextStyle(fontSize: 20.0),
            ),
            ElevatedButton(
              onPressed: ()  {
                setState(() {
                  counter = 0;
                });
              },
              child: const Icon(Icons.clear)
            ),
          ],
          
          
        ),
      ),

      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        onPressed: () {
          setState(() {
            counter++;
          });
        }
      ),


    );
  }
}