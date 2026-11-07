@echo off
echo ===================================================
echo   MBG Kitchen Monitor - Local APK Build Script
echo ===================================================
echo.

where flutter >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Flutter SDK tidak ditemukan di PATH sistem.
    echo Silakan pastikan Flutter telah terpasang atau gunakan GitHub Actions CI yang telah disiapkan.
    echo.
    pause
    exit /b 1
)

echo [1/3] Mengambil dependensi Flutter (flutter pub get)...
call flutter pub get

echo [2/3] Membangun APK Release...
call flutter build apk --release

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===================================================
    echo [SUKSES] APK berhasil dibangun!
    echo File APK tersedia di:
    echo build\app\outputs\flutter-apk\app-release.apk
    echo ===================================================
) else (
    echo.
    echo [GAGAL] Terjadi kesalahan saat build APK.
)

pause

