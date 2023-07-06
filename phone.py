from kivy.app import App
from googletrans import Translator
import googletrans
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from forex_python.converter import CurrencyRates
import requests
import json
from kivy.uix.popup import Popup

c = CurrencyRates()
API = 'f81703c1f3b81ad93e6644153c4a426e'
#url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API}'\
usersData = {
    "user1": {
        "coin": 0,
        "power": 1,
        "password": "4242"
    }
}

currentUser = "user1"

ua = {
    "wfor": "Прогноз погоди",
    "cver": "Конвертер",
    "clic": "Клікер",
    "sett": "Налаштування",
    "tr": "Перекладач",
    "convert": "Конвертувати",
    "сonmain": "Назад до головного вікна",
    "findW": "Дізнатися погоду",
    "wformain": "Назад до головного вікна",
    "bt4": "До клікера",
    "btr2": "До магазину",
    "bt3": "До головного вікна",
    "goshop": "Логін",
    "goreg": "Реєстрація",
    "reg": "Зареєструвати",
    "btr": "Клік",

}
eng = {
    "wfor": "Weather forecast",
    "cver": "Converter",
    "clic": "Clicker",
    "sett": "Settings",
    "convert": "Convert",
    "сonmain": "To main",
    "findW": "Find out weather ",
    "wformain": "To main",
    "bt4": "To Clicker",
    "btr2": "To shop",
    "bt3": "To main",
    "goshop": "Login",
    "goreg": "Registration",
    "reg": "Registration",
    "btr": "Click",
    "tr": "Translator",
}
currentlang = eng


def readData():
    global usersData
    with open("data.json", "r", encoding="utf-8")as file:
        usersData = json.load(file)

def writeData():
    global usersData
    with open("data.json", "w", encoding="utf-8")as file:
        json.dump(usersData, file, ensure_ascii=False, indent=4)
readData()
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def toWforecastScr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'wfor'
    def toConverterScr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'conver'
    def toClScr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'clicker'
    def toSettingsScr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'
    def toTrScr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'translator'
    def on_enter(self):
        self.ids.wfor.text = currentlang["wfor"]
        self.ids.cver.text = currentlang["cver"]
        self.ids.clic.text = currentlang["clic"]
        self.ids.sett.text = currentlang["sett"]
        self.ids.tr.text = currentlang["tr"]





class LoginScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def login(self):
        global currentUser
        with open("data.json", "r", encoding="utf-8") as file:
            json_data = json.load(file)
        username = self.ids.intex1.text
        password = self.ids.intex2.text
        if username in json_data and password == json_data[username]['password']:
            currentUser = self.ids.intex1.text
            self.manager.transition.direction = 'left'
            self.manager.current = 'main'

    def toreg(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'registr'
    def on_enter(self):
        self.ids.goshop.text = currentlang["goshop"]
        self.ids.goreg.text = currentlang["goreg"]
class RegistrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def registration(self):
        with open("data.json", "r", encoding="utf-8") as file:
            usersData = json.load(file)
        username = self.ids.intex_log.text
        password = self.ids.intex_pas.text
        usersData[username] = {
            "password": password,
            "coin": 0,
            "power": 1

        }
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(usersData, file, ensure_ascii=False, indent=4)

        self.manager.transition.direction = "down"
        self.manager.current = 'login'
    def on_enter(self):
        self.ids.reg.text = currentlang["reg"]
class WforecastScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def finwe(self):
        city = self.ids.w1.text
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            likefeel = data["main"]["feels_like"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            temp_min = data["main"]["temp_min"]
            sealevel = data["main"]["sea_level"]
            temp_max = data["main"]["temp_max"]
            windspeed = data["wind"]["speed"]
            clouds = data["clouds"]["all"]
            
            temp1 = temp - 273
            temp2 = round(temp1, 0)

            likefeel1 = likefeel - 273
            likefeel2 = round(likefeel1, 0)

            temp_min1 = temp_min - 273
            temp_min2 = round(temp_min1, 0)

            temp_max1 = temp_max - 273
            temp_max2 = round(temp_max1, 0)

            pon1 = "Temperature:"+" "+ str(temp2)+" "+"°C"
            pon2 = "Like feel temperature:"+" "+ str(likefeel2)+" "+"°C"
            pon3 = "Pressure:"+" "+ str(pressure)+" "+"millimeters of mercury"
            pon4 = "Humidity:"+" "+ str(humidity)+" "+"%"
            pon5 = "Min. temperature:"+" "+ str(temp_min2)+" "+"°C"
            pon6 = "Max. temperature:"+" "+ str(temp_max2)+" "+"°C"
            pon7 = "Sea level:"+" "+ str(sealevel)+" "+"m"
            pon8 = "Wind speed:"+" "+ str(windspeed)+" "+"m/s"
            pon9 = "Clouds:"+" "+ str(clouds)+" "+"%"

            self.ids.im2.opacity = 1
            self.ids.im3.opacity = 1
            self.ids.im4.opacity = 1
            self.ids.im5.opacity = 1
            self.ids.im6.opacity = 1
            self.ids.im7.opacity = 1
            self.ids.im8.opacity = 1
            self.ids.im9.opacity = 1
            self.ids.im10.opacity = 1



            self.ids.w2.text = str(pon1)
            self.ids.w3.text = str(pon2)
            self.ids.w4.text = str(pon3)
            self.ids.w5.text = str(pon4)
            self.ids.w6.text = str(pon5)
            self.ids.w7.text = str(pon6)
            self.ids.w8.text = str(pon7)
            self.ids.w9.text = str(pon8)
            self.ids.w10.text = str(pon9)
    def on_enter(self):
        self.ids.findW.text = currentlang["findW"]
        self.ids.wformain.text = currentlang["wformain"]


    def toWfroMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
class ConverterScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def toConMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
    def convert(self):
        withsomething = self.ids.wsom.text
        getrate = self.ids.insom.text
        count = int(self.ids.ccur.text)
        rate = c.get_rate(withsomething, getrate)
        result = (rate * count)
        self.ids.result.text = str(result)
    def on_enter(self):
        self.ids.convert.text = currentlang["convert"]
        self.ids.conmain.text = currentlang["conmain"]

        
class ShopScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def toMScr(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
    def toClickerScr(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'clicker'
    def buy(self, price, bonus):
        readData()
        if usersData[currentUser]["coin"] >= price:
            usersData[currentUser]["coin"] -= price
            usersData[currentUser]["power"] += bonus
            print(usersData[currentUser]["coin"])
            print(usersData[currentUser]["power"])
        elif usersData[currentUser]["coin"] < price:
            popbtn = Button(text = "Недостатньо коштів",  background_color = (255, 0, 50, 1))
            popup = Popup(title='Помилка', content = popbtn,
                auto_dismiss=False)
            popbtn.bind(on_press = popup.dismiss)
            popup.open()
        writeData()
    def buy2(self, price2, bonus2):
        readData()
        if usersData[currentUser]["coin"] >= price2:
            usersData[currentUser]["coin"] -= price2
            usersData[currentUser]["power"] += bonus2
            print(usersData[currentUser]["coin"])
            print(usersData[currentUser]["power"])
        elif usersData[currentUser]["coin"] < price2:
            popbtn2 = Button(text = "Недостатньо коштів",  background_color = (255, 0, 50, 1))
            popup2 = Popup(title='Помилка', content = popbtn2,
                          auto_dismiss=False)
            popbtn2.bind(on_press = popup2.dismiss)
            popup2.open()
        writeData()

    def buy3(self, price3, bonus3):
        readData()
        if usersData[currentUser]["coin"] >= price3:
            usersData[currentUser]["coin"] -= price3
            usersData[currentUser]["power"] += bonus3
            print(usersData[currentUser]["coin"])
            print(usersData[currentUser]["power"])
        elif usersData[currentUser]["coin"] < price3:
            popbtn3 = Button(text = "Недостатньо коштів", background_color = (255, 0, 50, 1))
            popup3 = Popup(title='Помилка', content = popbtn3,
                          auto_dismiss=False)
            popbtn3.bind(on_press = popup3.dismiss)
            popup3.open()
        writeData()
    def on_enter(self):
        self.ids.bt4.text = currentlang["bt4"]


class SettingsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    def settom(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
    def language(self):
        global currentlang
        currentlang = ua

class ClickScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def toMScr(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
    def toShop2Scr(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'shop'
    def on_enter(self):
        readData()
        self.ids.l1.text = str(usersData[currentUser]["coin"])
        self.ids.btr.text = currentlang["btr"]
        self.ids.btr2.text = currentlang["btr2"]
        self.ids.bt3.text = currentlang["bt3"]

    def click(self):
        usersData[currentUser]["coin"] += usersData[currentUser]["power"]
        writeData()
        self.ids.l1.text = str(usersData[currentUser]["coin"])
class TranslatorScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def transalte(self):
        self.translatorr = Translator()
        self.txt = self.ids.wt.text
        print(googletrans.LANGUAGES)
        self.translation = self.translatorr.translate(self.txt, src= 'uk', dest='en')
        self.translation.text  = self.ids.wt2.text

class OftenApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScr(name = 'login'))
        sm.add_widget(MainScr(name = 'main'))
        sm.add_widget(WforecastScr(name = 'wfor'))
        sm.add_widget(ConverterScr(name = 'conver'))
        sm.add_widget(ShopScr(name = 'shop'))
        sm.add_widget(SettingsScr(name = 'settings'))
        sm.add_widget(ClickScr(name =  "clicker"))
        sm.add_widget(RegistrScr(name = 'registr'))
        sm.add_widget(TranslatorScr(name='translator'))
        return sm
if __name__  == '__main__':
    app = OftenApp()
    app.run()
