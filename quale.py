import time #for giving the script a little break
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

url = 'https://web.whatsapp.com/'

class Quale:
    def __init__(self, word):
        self.url = url #the site we are going to be scraping
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        
        self.area_digitacao = '_3FRCZ'
        
        self.word = word
        
        self.time_break(15)
        
        while True == True:
            self.digita_palavra_e_manda()
            self.time_break(1)
    
    def digita_palavra_e_manda(self):
        for elem in self.driver.find_elements_by_class_name(self.area_digitacao):
            if elem.get_attribute('spellcheck'):
                elem.send_keys(self.word)
                elem.send_keys(Keys.ENTER);
    
    def time_break(self, break_time):
        '''
        Gives the execution a break
        :Args:
        time -> amount of seconds the break will last
        '''
        time.sleep(break_time)
    
    
quale = Quale('bom dia macaca')
