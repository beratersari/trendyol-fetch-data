from bs4 import BeautifulSoup
import requests
def get_price(url: str)-> str:
    sayfa = requests.get(url)

    html_sayfa = BeautifulSoup(sayfa.content, "html.parser")

    isim = html_sayfa.find("h1", class_="pr-new-br").get_text()

    fiyat = html_sayfa.find("span", class_="prc-dsc").get_text()

    return f"{isim}\n{fiyat}"

if __name__=="__main__":
    url = "https://www.trendyol.com/xiaomi/70mai-park-modu-kablosu-up02-a800-a500s-d07-d08-d05-p-144999486?boutiqueId=61&merchantId=220212&advertItems=eyJhZHZlcnRJZCI6IjcxY2M0ZDg2LTczZGYtNGRiNC1iOTBkLWFhOGM3OGQ0MDg4MyIsInNvcnRpbmdTY29yZSI6MC4wMDc2MTE2NDY2NDI5MDg0NTQ1LCJhZFNjb3JlIjowLjAxMzgzOTM1NzUzMjU2MDgyNSwiYWRTY29yZXMiOnsiMSI6MC4wMTM4MzkzNTc1MzI1NjA4MjUsIjIiOjAuMDEzODM5MzU3NTMyNTYwODI1fSwiY3BjIjowLjU1LCJtaW5DcGMiOjAuMDEsImVDcGMiOjAuNTAxNDg3NDgwNjEyMDk1MiwiYWR2ZXJ0U2xvdCI6OSwib3JkZXIiOjIsImF0dHJpYnV0ZXMiOiJTdWdnZXN0aW9uX0EsUmVsZXZhbmN5XzEsRmlsdGVyUmVsZXZhbmN5XzEsTGlzdGluZ1Njb3JpbmdBbGdvcml0aG1JZF8xLFNtYXJ0bGlzdGluZ18yLFN1Z2dlc3Rpb25CYWRnZXNfQixQcm9kdWN0R3JvdXBUb3BQZXJmb3JtZXJfQixPcGVuRmlsdGVyVG9nZ2xlXzIsU3VnZ2VzdGlvblN0b3JlQWRzX0EsQmFkZ2VCb29zdF9BLFJGXzEsUGFzdFNlYXJjaGVzX0IsU3VnZ2VzdGlvblBvcHVsYXJDVFJfQiJ9"
    print(get_price(url))

