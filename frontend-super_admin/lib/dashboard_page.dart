import 'package:flutter/material.dart';

class DashboardPage extends StatefulWidget {
  @override
  _DashboardPageState createState() => _DashboardPageState();
}

class _DashboardPageState extends State<DashboardPage> {
  final _formKey = GlobalKey<FormState>();

  // Controllers for hall fields
  final _hallNameController = TextEditingController();
  final _adminEmailController = TextEditingController();
  final _adminContactController = TextEditingController();
  final _universityController = TextEditingController();
  final _diningFeeController = TextEditingController();
  final _totalRoomsController = TextEditingController();

  // Temporary list to store halls
  List<Map<String, String>> halls = [];

  void _logout(BuildContext context) {
    Navigator.pushReplacementNamed(context, '/');
  }

  void _addHall() {
    if (!_formKey.currentState!.validate()) return;

    // Save hall data to list
    final hall = {
      "hallName": _hallNameController.text,
      "adminEmail": _adminEmailController.text,
      "adminContact": _adminContactController.text,
      "university": _universityController.text,
      "diningFee": _diningFeeController.text,
      "totalRooms": _totalRoomsController.text,
    };

    setState(() {
      halls.add(hall);

      // Clear form
      _hallNameController.clear();
      _adminEmailController.clear();
      _adminContactController.clear();
      _universityController.clear();
      _diningFeeController.clear();
      _totalRoomsController.clear();
    });

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Hall added successfully!')),
    );

    print("Saved Hall: $hall"); // For debugging
  }

  Widget _buildField(TextEditingController controller, String label,
      {TextInputType keyboardType = TextInputType.text}) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: TextFormField(
        controller: controller,
        keyboardType: keyboardType,
        decoration: InputDecoration(
          labelText: label,
          filled: true,
          fillColor: Colors.blue.shade50,
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: BorderSide.none,
          ),
          contentPadding:
              EdgeInsets.symmetric(horizontal: 16, vertical: 18),
        ),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Please enter $label';
          }
          return null;
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dashboard"),
        backgroundColor: Colors.blueAccent,
      ),
      drawer: Drawer(
        child: Container(
          color: Colors.blue.shade50,
          child: ListView(
            padding: EdgeInsets.zero,
            children: <Widget>[
              DrawerHeader(
                decoration: BoxDecoration(
                  color: Colors.blueAccent,
                  borderRadius:
                      BorderRadius.vertical(bottom: Radius.circular(20)),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    CircleAvatar(
                      backgroundColor: Colors.white,
                      radius: 30,
                      child: Icon(
                        Icons.person,
                        size: 40,
                        color: Colors.blueAccent,
                      ),
                    ),
                    SizedBox(height: 8),
                    Text(
                      'Superadmin',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      'superadmin@example.com',
                      style: TextStyle(
                        color: Colors.white70,
                        fontSize: 14,
                      ),
                    ),
                  ],
                ),
              ),
              ListTile(
                leading: Icon(Icons.dashboard),
                title: Text('Dashboard'),
                onTap: () {
                  Navigator.pushNamed(context, '/dashboard');
                },
              ),
              ListTile(
                leading: Icon(Icons.person),
                title: Text('Profile'),
                onTap: () {
                  Navigator.pushNamed(context, '/profile');
                },
              ),
              ListTile(
                leading: Icon(Icons.exit_to_app),
                title: Text('Logout'),
                onTap: () {
                  _logout(context);
                },
              ),
            ],
          ),
        ),
      ),

      // Body: Form for hall input + Add Hall button
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              _buildField(_hallNameController, "Hall Name"),
              _buildField(_adminEmailController, "Hall Admin Email",
                  keyboardType: TextInputType.emailAddress),
              _buildField(_adminContactController, "Hall Admin Contact No",
                  keyboardType: TextInputType.phone),
              _buildField(_universityController, "Associate University Name"),
              _buildField(_diningFeeController, "Hall Dining Fee",
                  keyboardType: TextInputType.number),
              _buildField(_totalRoomsController, "Total Rooms",
                  keyboardType: TextInputType.number),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _addHall,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueAccent,
                  padding: EdgeInsets.symmetric(vertical: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                ),
                child: Text(
                  "Add Hall",
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
