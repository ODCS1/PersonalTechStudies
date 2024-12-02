import 'package:flutter/material.dart';

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
      ),
    
      body: Container(
        height: 200,
        width: 200,
        color: Colors.purple,
        child: Align(
          alignment: Alignment.center,
          child: Container(
            height: 100,
            width: 100,
            color: Colors.cyan,
          ),
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