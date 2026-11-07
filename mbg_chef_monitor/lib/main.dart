import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
    ),
  );
  runApp(const MbgChefMonitorApp());
}

class MbgChefMonitorApp extends StatelessWidget {
  const MbgChefMonitorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MBG Chef & ASLAP Monitor',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color(0xFFF8FAFC),
        colorScheme: const ColorScheme(
          brightness: Brightness.light,
          primary: Color(0xFF0F172A),
          onPrimary: Colors.white,
          secondary: Color(0xFF059669),
          onSecondary: Colors.white,
          surface: Colors.white,
          onSurface: Color(0xFF1E293B),
          error: Color(0xFFDC2626),
          onError: Colors.white,
        ),
      ),
      home: const MbgWebMonitorScreen(),
    );
  }
}

class MbgWebMonitorScreen extends StatefulWidget {
  const MbgWebMonitorScreen({super.key});

  @override
  State<MbgWebMonitorScreen> createState() => _MbgWebMonitorScreenState();
}

class _MbgWebMonitorScreenState extends State<MbgWebMonitorScreen> {
  late final WebViewController _controller;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0xFFF8FAFC))
      ..setNavigationDelegate(
        NavigationDelegate(
          onPageStarted: (String url) {
            if (mounted) {
              setState(() {
                _isLoading = true;
              });
            }
          },
          onPageFinished: (String url) {
            if (mounted) {
              setState(() {
                _isLoading = false;
              });
            }
          },
          onWebResourceError: (WebResourceError error) {
            _controller.loadFlutterAsset('assets/web/index.html');
          },
        ),
      )
      ..loadFlutterAsset('assets/web/index.html');
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (bool didPop, dynamic result) async {
        if (didPop) return;
        if (await _controller.canGoBack()) {
          _controller.goBack();
        } else {
          SystemNavigator.pop();
        }
      },
      child: Scaffold(
        backgroundColor: const Color(0xFFF8FAFC),
        body: SafeArea(
          child: Stack(
            children: [
              WebViewWidget(controller: _controller),
              if (_isLoading)
                const Center(
                  child: CircularProgressIndicator(
                    color: Color(0xFF0F172A),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
