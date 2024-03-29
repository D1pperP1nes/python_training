from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self): #конструктор, кот. инициализирует ссылку на драйвер и помощников
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self) #помощник получает ссылку на объект класса application фикстуру
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        wd = self.wd
        try:
            self.wd.current_url #просим браузер сказать какой текущий адрес открытой страницы (если сможет то валиден)
            return True
        except:
            return False

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0:
            return
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()