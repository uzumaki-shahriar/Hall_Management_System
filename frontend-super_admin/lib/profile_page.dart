import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ProfilePage extends StatefulWidget {
  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  String _name = '';
  String _email = '';

  // Load stored name and email from SharedPreferences
  Future<void> _loadProfile() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      _email = prefs.getString('user_email') ?? '';
      _name = prefs.getString('user_name') ?? '';
    });
  }

  @override
  void initState() {
    super.initState();
    _loadProfile(); // Load user info when page loads
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Profile"),
        backgroundColor: Colors.blueAccent,
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Profile picture
            Center(
              child: CircleAvatar(
                radius: 50,
                backgroundColor: Colors.blueAccent,
                child: Icon(
                  Icons.person,
                  size: 50,
                  color: Colors.white,
                ),
              ),
            ),
            SizedBox(height: 30),

            // Display Name
            ListTile(
              leading: Icon(Icons.person, color: Colors.blueAccent),
              title: Text(
                'Name',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              subtitle: Text(_name),
            ),
            SizedBox(height: 16),

            // Display Email
            ListTile(
              leading: Icon(Icons.email, color: Colors.blueAccent),
              title: Text(
                'Email',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              subtitle: Text(_email),
            ),
          ],
        ),
      ),
    );
  }
}
