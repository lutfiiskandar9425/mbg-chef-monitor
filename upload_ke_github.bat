@echo off
title MBG Kitchen Monitor - Upload ke GitHub & Build APK Otomatis
echo ================================================================
echo   MBG KITCHEN MONITOR - UPLOAD REPOSITORI GITHUB
echo ================================================================
echo.
echo Langkah mudah:
echo 1. Buat repositori baru di https://github.com/new
echo    (Beri nama misal: mbg-chef-monitor, pilih Public atau Private)
echo 2. Salin URL repositori tersebut.
echo.
set /p REPO_URL="Tempel URL GitHub di sini (contoh: https://github.com/user/mbg-chef-monitor.git): "

if "%REPO_URL%"=="" (
    echo [ERROR] URL tidak boleh kosong.
    pause
    exit /b 1
)

echo.
echo [1/3] Mengonfigurasi remote origin...
"C:\Users\HP\Projects\Projecttools\git\cmd\git.exe" remote remove origin 2>nul
"C:\Users\HP\Projects\Projecttools\git\cmd\git.exe" remote add origin %REPO_URL%

echo [2/3] Menyimpan berkas terbaru...
"C:\Users\HP\Projects\Projecttools\git\cmd\git.exe" add .
"C:\Users\HP\Projects\Projecttools\git\cmd\git.exe" commit -m "Update otomatis: Siap build APK di GitHub Actions" 2>nul

echo [3/3] Mengunggah ke GitHub (git push -u origin main)...
"C:\Users\HP\Projects\Projecttools\git\cmd\git.exe" push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================
    echo [SUKSES] Repositori berhasil diunggah ke GitHub!
    echo.
    echo Sekarang buka tab "Actions" di repositori GitHub Anda.
    echo Alur "Build Android APK" sedang berjalan otomatis.
    echo Dalam 3-4 menit, file "app-release.apk" bisa diunduh di bagian Artifacts!
    echo ================================================================
) else (
    echo.
    echo [INFO] Jika diminta autentikasi, silakan ikuti petunjuk login browser GitHub.
)

pause

