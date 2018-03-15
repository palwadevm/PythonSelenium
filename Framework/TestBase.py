from selenium import webdriver
import os as system

class TestBase:
    #TestBase Class Constructor
    def __init__(self, message):
        print(message)