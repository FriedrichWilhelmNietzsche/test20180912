#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# F12, find_element_by_id\ name()\ class_name()\ tag_name()\<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# driver.find_element_by_id("kw").send_keys("test")

# find_element_by_link_text\ partial_link_text()
# driver.find_element_by_link_text("登录").click()

# F12, find_element_by_xpath\ css_selector()
driver.find_element_by_xpath(' //*[@id="kw"] ').send_keys("test")