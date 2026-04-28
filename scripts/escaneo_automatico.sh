#!/bin/bash

echo "[*] Iniciando escaneo automatico..."
echo "[*] Fecha: $(date)"

cd /home/kali/security-dashboard
sudo python3 scanner.py

echo "[*] Escaneo completado."
