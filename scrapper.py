import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://articulo.mercadolibre.com.ar/MLA-769139850-camara-sony-alpha-mirrorless-a7-iii-con-lente-28-70mm-4k-_JM?searchVariation=32591287230#searchVariation=32591287230&position=5&type=item&tracking_id=d86e77f5-ce93-46d6-beb6-09661e457312'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # BUSQUEDA en el html con beautifulsoup
    title = soup.h1.string
    price = soup.find("span",{"class": "price-tag-fraction"}).string

    converted_price = float(price[0:6])
    
    print(title.strip())
    print(price)

    if(converted_price < 280.000):
        send_mail()
    else:
        print("No hay ofertas por ahora. (T_T) ")



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('MI MAIL','MICONTRASEÑA')

    subject = 'Bajo el precio del articulo que buscabas! ^_^'
    body = 'Mira el link: https://articulo.mercadolibre.com.ar/MLA-769139850-camara-sony-alpha-mirrorless-a7-iii-con-lente-28-70mm-4k-_JM?searchVariation=32591287230#searchVariation=32591287230&position=5&type=item&tracking_id=d86e77f5-ce93-46d6-beb6-09661e457312'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '', #MAIL QUE ENVIA
        '', #MAIL QUE RECIBE
        msg
    )
    print('==> OFERTA ENCONTRADA! EMAIL ENVIADO <==')
    server.quit()


# while(True):   
#     check_price()
#     time.sleep(86400) ##¡Para correr la aplicacion cada 24hs

check_price() #para correr en ejecución