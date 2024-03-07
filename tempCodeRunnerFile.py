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