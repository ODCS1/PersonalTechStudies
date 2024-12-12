import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

// Exemplo de Widget Stateless
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Project 5',
      home: ItemListScreen(),
    );
  }
}

// Exemplo de Widget Stateful
class ItemListScreen extends StatefulWidget {
  const ItemListScreen({super.key});

  @override
  State<ItemListScreen> createState() => _ItemListScreenState();
}

class _ItemListScreenState extends State<ItemListScreen> {
  // LIST
  final List<Map<String, dynamic>> _items = [
    {'id': 1, 'name': 'Item 1', 'quantity': 10},
    {'id': 2, 'name': 'Item 2', 'quantity': 5},
  ];

  // Função para adicionar item
  void _addItem(String name, int quantity) {
    setState(() {
      _items.add({
        'id': _items.length + 1,
        'name': name,
        'quantity': quantity,
      });
    });
  }

  // REMOVING AN ITEM
  void _removeItem(int id) {
    setState(() {
      _items.removeWhere((item) => item['id'] == id);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Lista de Itens'),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _items.length,
              itemBuilder: (context, index) {
                final item = _items[index];
                return ListTile(
                  title: Text('${item['name']}'),
                  subtitle: Text('Quantidade: ${item['quantity']}'),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () => _removeItem(item['id']),
                  ),
                );
              },
            ),
          ),
          AddItemForm(
            onAddItem: _addItem, // NOMINAL 
          ),
        ],
      ),
    );
  }
}


// STATELESS COM PARÂMETROS NOMINAIS E POSICIONAIS
class AddItemForm extends StatelessWidget {
  final void Function(String name, int quantity) onAddItem;

  const AddItemForm({super.key, required this.onAddItem});

  @override
  Widget build(BuildContext context) {
    final TextEditingController nameController = TextEditingController();
    final TextEditingController quantityController = TextEditingController();

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Row(
        children: [
          Expanded(
            child: TextField(
              controller: nameController,
              decoration: const InputDecoration(labelText: 'Nome do Item'),
            ),
          ),
          Expanded(
            child: TextField(
              controller: quantityController,
              decoration: const InputDecoration(labelText: 'Quantidade'),
              keyboardType: TextInputType.number,
            ),
          ),
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () {
              final name = nameController.text;
              final quantity = int.tryParse(quantityController.text) ?? 0;

              if (name.isNotEmpty && quantity > 0) {
                onAddItem(name, quantity);
                nameController.clear();
                quantityController.clear();
              }
            },
          ),
        ],
      ),
    );
  }
}
