#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get('https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=1&')
name = driver.find_element_by_name("username")
name.send_keys('amos')
password = driver.find_element_by_id('password')
password.send_keys('bird')
password.send_keys(Keys.RETURN)
time.sleep(1)
driver.quit()
