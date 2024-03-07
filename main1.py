import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import speedtest

# Função calcular velocidade
def calcular_speed(server_id=None):
    try:
        st = speedtest.Speedtest()
        if server_id:
            st.get_servers([server_id])
        else:
            st.get_best_server()
        download_speed = st.download() / 1000000  # Mbps
        upload_speed = st.upload() / 1000000  # Mbps
        return download_speed, upload_speed
    except Exception as e:
        print(f"Erro ao calcular a velocidade: {e}")
        return None, None

#Lista de Servidores
def listar_servidores():
    st = speedtest.Speedtest()
    servers = st.list()
    return servers

# Função para iniciar o teste
def start_test():
    info_label.config(text="Testando...")
    download_speed, upload_speed = calcular_speed()
    
    if download_speed is None or upload_speed is None:
        info_label.config(text="Erro ao realizar o teste. Por favor, tente novamente.")
        return
    
    # Atualizar as Variaveis de Velocidade
    speed_var["download"].set(f"{download_speed:.2f} Mbps")
    speed_var["upload"].set(f"{upload_speed:.2f} Mbps")
    
    # Atualizar a GUI
    janela.update()
    
    # Atualizar as labels de velocidade de download e upload
    download_label = ttk.Label(frameConteudo, text=f"Velocidade de Download: {speed_var['download'].get()}")
    download_label.grid(row=1, column=0, sticky='w', pady=(0, 5))

    upload_label = ttk.Label(frameConteudo, text=f"Velocidade de Upload: {speed_var['upload'].get()}")
    upload_label.grid(row=2, column=0, sticky='w', pady=(0, 5))
    
    # Atualizar a imagem de acordo com a velocidade de Download
    if download_speed > 8:
        image_label.config(image=rapido_image)
    elif download_speed > 4:
        image_label.config(image=normal_image)
    else:
        image_label.config(image=lento_image)
        
    info_label.config(text="Teste Concluido!")

# Cores
letras = "#ffffff"
fundo = "#233642"

# Criação da janela principal
janela = tk.Tk()
janela.title("Detectar Velocidade da Internet")
janela.geometry("450x300")
janela.resizable(False, False)
janela.configure(background=fundo)

# Estilo para Janela
style = ttk.Style()
style.configure("TFrame", background=fundo)
style.configure("TLabel", background=fundo, foreground=letras, font=("Helvetica", 10))

# Frame para o logo e nome
frameCima = ttk.Frame(janela)
frameCima.pack(pady=(20, 20))

# Carrega a imagem do logo
logo_image = Image.open('imagem/globo.png')
logo_image = logo_image.resize((50, 50))
logo_image = ImageTk.PhotoImage(logo_image)

# Label para exibir o logo
logo_label = ttk.Label(frameCima, image=logo_image)
logo_label.pack(side="left", padx=(10, 5))

# Label para exibir o nome
nome_label = ttk.Label(frameCima, text="Detectar Velocidade da Internet", font=("Helvetica", 16, "bold"))
nome_label.pack(side="left")

# Frame para o conteúdo
frameConteudo = ttk.Frame(janela)
frameConteudo.pack(pady=(20, 50))

# Label para exibir informações
info_label = ttk.Label(frameConteudo, text="Pressione o botão para testar a velocidade da internet")
info_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Adiciona uma célula vazia para separar os rótulos da imagem
ttk.Label(frameConteudo, text="").grid(row=1, column=1, pady=(0, 5))

# Label para exibir a imagem de acordo com a velocidade de download
image_label = ttk.Label(frameConteudo)
image_label.grid(row=1, column=2, rowspan=2, padx=10)

# Variáveis para armazenar as velocidades
speed_var = {
    'download': tk.StringVar(),
    'upload': tk.StringVar(),
}

# Imagens para diferentes níveis de velocidade
rapido_image_local = "imagem/rapido.jpeg"
normal_image_local = "imagem/normal.png"
lento_image_local = "imagem/lenta.jpeg"

rapido_image = Image.open(rapido_image_local)
rapido_image = rapido_image.resize((50, 50))  # Redimensionar a imagem
rapido_image = ImageTk.PhotoImage(rapido_image)

normal_image = Image.open(normal_image_local)
normal_image = normal_image.resize((50, 50))  # Redimensionar a imagem
normal_image = ImageTk.PhotoImage(normal_image)

lento_image = Image.open(lento_image_local)
lento_image = lento_image.resize((50, 50))  # Redimensionar a imagem
lento_image = ImageTk.PhotoImage(lento_image)

# Botão para iniciar o teste
iniciar_botao = ttk.Button(frameConteudo, text="Iniciar Teste", command=start_test)
iniciar_botao.grid(row=3, column=0, columnspan=3, pady=(20, 0))

janela.mainloop()