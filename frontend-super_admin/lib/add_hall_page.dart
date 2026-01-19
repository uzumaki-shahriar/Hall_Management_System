import 'package:flutter/material.dart';
import 'dashboard_page.dart';

class AddHallPage extends StatefulWidget {
  @override
  State<AddHallPage> createState() => _AddHallPageState();
}

class _AddHallPageState extends State<AddHallPage> {
  final TextEditingController _hallNameController = TextEditingController();
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  void _submit() {
    if (_formKey.currentState!.validate()) {
      // Send data back to previous page
      
      Navigator.pop(context, _hallNameController.text);
    }
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Add New Hall"),
        backgroundColor: Colors.blueAccent,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _hallNameController,
                decoration: InputDecoration(
                  labelText: "Hall Name",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return "Please enter hall name";
                  }
                  return null;
                },
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _submit,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueAccent,
                  padding: EdgeInsets.symmetric(vertical: 14, horizontal: 30),
                ),
                child: Text(
                  "Submit",
                  style: TextStyle(fontSize: 16),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
