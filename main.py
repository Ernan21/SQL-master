import os
import subprocess
import time

# Defina o diretório onde seu repositório está localizado
repo_directory = 'SQL-master/'

# Defina o intervalo de verificação em segundos
intervalo = 1  # Verificar a cada 1 hora

def verificar_atualizacoes():
    os.chdir(repo_directory)
    try:
        subprocess.run(['git', 'fetch'])
        # Verifique se há atualizações disponíveis
        resultado = subprocess.run(['git', 'status', '-uno'], capture_output=True, text=True)
        output = resultado.stdout.lower()
        if 'your branch is behind' in output:
            subprocess.run(['git', 'pull'])
            print("Atualização aplicada com sucesso!")
        else:
            print("Nenhuma atualização encontrada.")
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    while True:
        os.chdir('..')
        verificar_atualizacoes()
        time.sleep(intervalo)