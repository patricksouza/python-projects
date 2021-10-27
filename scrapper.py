import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import smtplib
import json


fakeAgent = UserAgent().ie

smtpServer = 'smtp.gmail.com'
port = 465
senderEmail = 'mrpatickart@gmail.com'
password = 'vlcsernipxtgklhh'


#URLs = ['https://www.amazon.com.br/OCTOO-UP-BL-Suporte-Uptable-Preto/dp/B07BTC67VS/ref=zg-bs_furniture_1/136-4710759-6740918?pd_rd_w=iw3r3&pf_rd_p=c0c0f25f-aaf5-43d0-b46e-c8c2c04a86c2&pf_rd_r=90Z5036B8AQRJP8RJDZ1&pd_rd_r=56ce361e-18a9-45c3-9090-bd65754a0acb&pd_rd_wg=bhdSh&pd_rd_i=B07BTC67VS&psc=1','https://www.amazon.com.br/Rel%C3%B3gio-Amazfit-GTS-A1914-Preto/dp/B07XWT23FZ/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=gts&qid=1635123485&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147','https://www.amazon.com.br/dp/B08NCYZTV9?smid=A1TE74VUFAYXSD&pf_rd_r=XVD8K8X4C2QCHXQNMMXE&pf_rd_p=562d4521-dc52-4141-86d5-06ef71a58c71&pd_rd_r=961eead9-1301-461b-95de-e76ecd0b7a40&pd_rd_w=uoI1p&pd_rd_wg=hvLZf&ref_=pd_gw_unk']
URLS = ['https://www.amazon.com.br/OCTOO-UP-BL-Suporte-Uptable-Preto/dp/B07BTC67VS/ref=zg-bs_furniture_1/136-4710759-6740918?pd_rd_w=iw3r3&pf_rd_p=c0c0f25f-aaf5-43d0-b46e-c8c2c04a86c2&pf_rd_r=90Z5036B8AQRJP8RJDZ1&pd_rd_r=56ce361e-18a9-45c3-9090-bd65754a0acb&pd_rd_wg=bhdSh&pd_rd_i=B07BTC67VS&psc=1']
expectedPrices = [512]

headers = {'User-Agent': fakeAgent, 'Upgrade-Insecure-Requests': '1','DNT': '1','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate'}

# A function will be create to save the URLs
fp = open('scrapperData.json', 'w')
json.dump(URLS, fp)
fp.close()

#KEYS = ['product', 'price', 'availa']

server = smtplib.SMTP_SSL(smtpServer, port)

def sendEmail(url):
        message = """\
        Subject: Hi there

        Check this Amazon link! It is a cheap one: %s""" % ((url))
        server.login(senderEmail, password)
        server.sendmail(
        senderEmail,
        'patrickrsmiranda@gmail.com',
        message)
        server.quit()
        print('Email sent!')
        
for url, expectedPrice in zip(URLS, expectedPrices):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').text

    price = soup.find(id='priceblock_ourprice').text

    convertedPrice = float(price[2:8].replace(',', '.'))
    
    if convertedPrice > expectedPrice:
            sendEmail(url)
            break
    print('Email not sent!')
            
        