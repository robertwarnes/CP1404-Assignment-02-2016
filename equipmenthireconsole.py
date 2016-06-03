"""
CP1404 Assignment 2
Items for Hire
Robert Warnes
Due 27/05/2016
Github URL - https://github.com/robertwarnes/CP1404-Assignment-02-2016
"""

import csv

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from item import Item
from itemlist import ItemList

class EquipmentHire(App):

    footer_label = StringProperty()
    item = ItemList() #list of items imported from items.csv

    def build(self):
        Window.size = (800, 600)
        self.title = "Equipment Hire"
        self.root = Builder.load_file('app.kv')
        self.footer_label = "Choose action from the left menu, then select items on the right"

    def list_items_button(self):
        self.footer_label = "Choose action from the left menu, then select items on the right"

    def hire_items_button(self):
        self.footer_label = "Select available items for hire"

    def return_items_button(self):
        self.footer_label= "Select items to return"

    def confirm_button(self):
        self.footer_label = "Choose action from the left menu, then select items on the right"

    def add_new_item_button(self): #pressing button opens up pop up window with form
        self.footer_label = "Enter Details For New Item"

    def save_button(self):
        self.footer_label = "Choose action from the left menu, then select items on the right"

EquipmentHire().run()