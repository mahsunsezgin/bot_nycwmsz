# bot_nycwmsz
## Web sitesinden Python ile veri çekme

> Projenin amacı python'un requests BeautifulSoup kütüphaneleri kullanılarak https://www.nytimes.com/crosswords/game/mini adlı web sitesindeki ilgili verileri çekmek. Requests ve BeautifulSoup kütüphanelerini projemize dahil ettikten sonra belirlediğimiz web sitedeki verileri işlemeye hazır duruma getirmemize yarar. Bu sayede gerçekleştirdiğimiz projeye bot ismini veriyoruz.

### Pip paket yükleyicisi kullanarak kurulum ve projeye dahil etme

Komut satırına aşağıdaki kodu yazarak requests kütüphanesini kuruyoruz.
```
pip install requests
```
Requests kütüphanesini projemizde kullanmak için ilgili kütüphaneyi çağırmamız gerekmektedir.
```python
import requests
```
BeautifulSoup kütüphanesini dahil ediyoruz.
```python
from bs4 import BeautifulSoup
```
Kod düzenimizi standartlara uygun seviyede tutmak için pylint aracını terminal ekranından aşağıdaki gibi yüklüyoruz
```
pip install pylint
```









