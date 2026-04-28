import subprocess
import datetime

def guardar_log(contenido):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"logs/escaneo_{fecha}.txt"
    with open(nombre_archivo, "w") as f:
        f.write(contenido)
    print(f"[+] Log guardado en: {nombre_archivo}")

def escanear_red(red):
    print(f"\n[*] Escaneando red: {red}")
    print(f"[*] Hora: {datetime.datetime.now()}\n")
    resultado = subprocess.run(["nmap", "-sn", red], capture_output=True, text=True)
    print(resultado.stdout)
    guardar_log(resultado.stdout)

if __name__ == "__main__":
    escanear_red("192.168.1.0/24")
