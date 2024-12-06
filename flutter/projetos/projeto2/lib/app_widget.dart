import 'package:flutter/material.dart';
import 'package:projeto2/app_controller.dart';
import 'package:projeto2/home_page.dart';

class AppWidget extends StatelessWidget {
  const AppWidget({super.key});

  @override
  Widget build (BuildContext context) {

    return AnimatedBuilder(
      animation: AppController.instance, 
      builder: (context, child){

        return  MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            primarySwatch: Colors.red,

            brightness: AppController.instance.isDarkTheme 
              ? Brightness.dark 
              : Brightness.light,

            appBarTheme: const AppBarTheme(
              backgroundColor: Colors.red,
              titleTextStyle: TextStyle(
                color: Colors.white,
              )
            ),
            
            floatingActionButtonTheme: const FloatingActionButtonThemeData(
              backgroundColor: Colors.red,
              foregroundColor: Colors.white
            )
          ),
          home: const HomePage(),
        );
    });
  }
}