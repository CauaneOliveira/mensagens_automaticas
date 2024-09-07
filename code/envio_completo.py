import pyautogui as pg

#abrir navegador
pg.press("winleft")
pg.typewrite("opera")
pg.press("enter")

#abrir whatsapp no navegador
pg.sleep(4)
pg.typewrite("https://web.whatsapp.com")
pg.press("enter")


#procurar nome
pg.sleep(15)
pg.click(150,185)
pg.typewrite("Teste", interval=0.05)
pg.press("enter")


#envio de uma mensagem
pg.sleep(2)
pg.typewrite("Vai começar!!", interval=0.05)
pg.press("enter")

#começar o loop de mensagem
cont=0
pg.sleep(3)
while (cont < 5):

    pg.typewrite("Olá", interval=0.01)
    pg.press('enter');
    cont+=1











