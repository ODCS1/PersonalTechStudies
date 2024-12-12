import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ItemListScreen(),
    );
  }
}

class Item {
  String name;

  Item({required this.name});
}

class ItemListScreen extends StatefulWidget {
  @override
  _ItemListScreenState createState() => _ItemListScreenState();
}

class _ItemListScreenState extends State<ItemListScreen> {

  List<Item> items = [];

  // CONTROLADOR DE TEXTO PARA TER O CAMPO DE ENTRADA
  TextEditingController itemController = TextEditingController();

  // ADD FUNCTION
  void addItem() {
    setState(() {
      items.add(Item(name: itemController.text));
      itemController.clear();
    });
  }


  // FUNÇÃO PARA EDITAR O ITEM PELA POSIÇÃO
  void editItem(int index) {
    itemController.text = items[index].name;
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Editar Item'),
          content: TextField(
            controller: itemController,
            decoration: InputDecoration(labelText: 'Nome do Item'),
          ),
          actions: [
            TextButton(
              onPressed: () {
                setState(() {
                  items[index].name = itemController.text;
                  itemController.clear();
                });
                Navigator.pop(context);
              },
              child: Text('Salvar'),
            ),
          ],
        );
      },
    );
  }

  // FUNÇÃO PARA EXCLUIR O ITEM PELA POSIÇÃO
  void deleteItem(int index) {
    setState(() {
      items.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('CRUD com Lista'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // CAMPO PARA ADICIONAR NOVO ITEM
            TextField(
              controller: itemController,
              decoration: InputDecoration(
                labelText: 'Nome do Item',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: addItem,
              child: Text('Adicionar Item'),
            ),
            SizedBox(height: 20),

            // EXIBIR A LISTA DE ITENS
            Expanded(
              child: ListView.builder(
                itemCount: items.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(items[index].name),
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [

                        IconButton(
                          icon: Icon(Icons.edit),
                          onPressed: () => editItem(index),
                        ),

                        IconButton(
                          icon: Icon(Icons.delete),
                          onPressed: () => deleteItem(index),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
