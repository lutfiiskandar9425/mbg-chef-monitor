import 'package:webview_flutter_android/webview_flutter_android.dart' as android_webview;
import 'package:image_picker/image_picker.dart';
import 'dart:io';
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

class _MbgWebMonitorScreenState extends State<MbgWebMonitorScreen> with WidgetsBindingObserver {
  late final WebViewController _controller;
  bool _isLoading = true;
  final String _baseUrl = 'https://lutfiiskandar9425.github.io/mbg-chef-monitor/';

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);

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
            // Jika koneksi internet terputus, fallback otomatis ke aset offline internal
            _controller.loadFlutterAsset('assets/web/index.html');
          },
        ),
      );

    _initFileSelector();
    _loadFreshUrl();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    // Otomatis refresh saat aplikasi dibuka kembali dari background
    if (state == AppLifecycleState.resumed) {
      _refreshData();
    }
  }

  Future<void> _initFileSelector() async {
    try {
      if (Platform.isAndroid && _controller.platform is android_webview.AndroidWebViewController) {
        final androidController = _controller.platform as android_webview.AndroidWebViewController;
        await androidController.setOnShowFileSelector((android_webview.FileSelectorParams params) async {
          final picker = ImagePicker();
          final bool useCamera = params.isCaptureEnabled;
          final XFile? photo = await picker.pickImage(
            source: useCamera ? ImageSource.camera : ImageSource.gallery,
            imageQuality: 85,
          );
          if (photo != null) {
            final uri = Uri.file(photo.path).toString();
            return [uri];
          }
          return [];
        });
      }
    } catch (_) {}
  }

  Future<void> _loadFreshUrl() async {
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    final freshUrl = '$_baseUrl?v=$timestamp';
    // Timeout pengaman agar loading indikator tidak macet di HP
    Future.delayed(const Duration(seconds: 3), () {
      if (mounted && _isLoading) {
        setState(() {
          _isLoading = false;
        });
      }
    });
    await _controller.loadRequest(Uri.parse(freshUrl));
  }

  Future<void> _refreshData() async {
    if (!mounted) return;
    setState(() {
      _isLoading = true;
    });

    try {
      await _controller.clearCache();
      await _controller.clearLocalStorage();
    } catch (_) {}

    await _initFileSelector();
    _loadFreshUrl();
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
                const Positioned(
                  top: 0,
                  left: 0,
                  right: 0,
                  child: LinearProgressIndicator(
                    minHeight: 3,
                    color: Color(0xFF059669),
                    backgroundColor: Colors.transparent,
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
