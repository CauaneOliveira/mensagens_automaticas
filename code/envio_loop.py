import pyautogui as pg

#envio de uma mensagem
pg.sleep(4)
pg.typewrite("VAI COMEÇAR!", interval=0.05)
pg.press("enter")

#começar o loop de mensagem
cont=0
pg.sleep(4)
while (cont < 10):

    pg.typewrite("Teste", interval=0.01)
    pg.press('enter');
    cont+=1








