import 'package:flutter/material.dart';
import 'login_signup_page.dart';
import 'dashboard_page.dart';
import 'profile_page.dart';
import 'add_hall_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Superadmin Panel',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      initialRoute: '/',  // Starting page (Login/SignUp)
      routes: {
        '/': (context) => LoginSignupPage(),
        '/dashboard': (context) => DashboardPage(),  // Dashboard page route
        '/profile': (context) => ProfilePage(),  // Profile page route
        '/add_hall': (context) => AddHallPage(),  // Add Hall page route
      },
    );
  }
}
