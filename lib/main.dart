import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: ExamDesk()));
}

class ExamDesk extends StatefulWidget {
  const ExamDesk({super.key});
  @override
  State<ExamDesk> createState() => _ExamDeskState();
}

class _ExamDeskState extends State<ExamDesk> {
  late final WebViewController controller;
  bool failed = false;
  bool loading = true;
  bool handlingBack = false;

  @override
  void initState() {
    super.initState();
    controller = WebViewController()
      ..setBackgroundColor(const Color(0xfff4f0e5))
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setNavigationDelegate(NavigationDelegate(
        onPageFinished: (_) { if (mounted) setState(() => loading = false); },
        onWebResourceError: (error) {
          if (error.isForMainFrame == true && mounted) {
            setState(() { failed = true; loading = false; });
          }
        },
        // The app has no external browsing. All content is bundled.
        onNavigationRequest: (request) => request.url.startsWith('file:///android_asset/')
            ? NavigationDecision.navigate : NavigationDecision.prevent,
      ));
    load();
  }

  Future<void> load() async {
    setState(() { failed = false; loading = true; });
    try {
      await controller.loadFlutterAsset('assets/index.html');
    } catch (_) {
      if (mounted) setState(() { failed = true; loading = false; });
    }
  }

  Future<void> back() async {
    if (handlingBack) return;
    handlingBack = true;
    try {
      final handled = await controller.runJavaScriptReturningResult(
        'window.examDeskBack ? window.examDeskBack() : false');
      if (handled != true && handled.toString() != 'true') {
        await SystemNavigator.pop();
      }
    } catch (_) {
      await SystemNavigator.pop();
    } finally {
      handlingBack = false;
    }
  }

  @override
  Widget build(BuildContext context) => PopScope(
    canPop: false,
    onPopInvokedWithResult: (didPop, result) { if (!didPop) back(); },
    child: Scaffold(
      backgroundColor: const Color(0xfff4f0e5),
      body: SafeArea(child: failed
        ? Center(child: Column(mainAxisSize: MainAxisSize.min, children: [
            const Text('Could not open the local study library.'),
            const SizedBox(height: 16),
            ElevatedButton(onPressed: load, child: const Text('Try again')),
          ]))
        : Stack(children: [
            WebViewWidget(controller: controller),
            if (loading) const LinearProgressIndicator(color: Color(0xffb94928)),
          ])),
    ),
  );
}
