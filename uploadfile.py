from selenium import webdriver
import os

driver = webdriver.Chrome()  # 打开上传功能页面
file_path =  'file:///' + os.path.abspath('upload.html')
driver.get(file_path)    #点击打开上传窗口
driver.find_element_by_name("file").click()    #调用 upfile.exe 上传程序
os.system(os.path.abspath('upload.exe'))
# driver.quit()