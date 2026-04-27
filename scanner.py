import subprocess
import datetime

def escanear_red(red):
    print(f"\n[*] Escaneando red: {red}")
    print(f"[*] Hora: {datetime.datetime.now()}\n")
    
    resultado = subprocess.run(
        ["nmap", "-sn", red],
        capture_output=True,
        text=True
    )
    
    print(resultado.stdout)

if __name__ == "__main__":
    escanear_red("10.0.2.0/24")

