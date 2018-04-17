#-*- coding: utf-8 -*-
from app.pageobjects.homepage import  home
from lib.base.baesdriver import BaseDriver

items = home.HomeElements()

class   Search(BaseDriver):
    u"""
        百度首页查询动作封装
    """
    #all button for customer list
    def search_input(self,keyword):
        self.type(items.search_input_el,keyword)

    #click query
    def click_query(self):
        self.click(items.search_button_el)

