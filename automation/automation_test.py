# 自动化案例
from selenium import webdriver
# 键盘鼠标点击事件
from selenium.webdriver.common.keys import Keys

# 加载驱动
browser = webdriver.Chrome()
# 访问网站url
url = 'https://accounts.douban.com/passport/login?source=movie'
browser.get(url)

# 快照
browser.save_screenshot('./douban.png')
# 密码登录
browser.find_element_by_class_name('account-tab-account').click()   
# 获取账号在界面上的ID属性并设置用户名和密码
browser.find_element_by_id('username').send_keys('username')
browser.find_element_by_id('password').send_keys('password')
# 获取登录按钮，通过键盘enter操作直接登录 以下是两种实现方式，随意使用
browser.find_element_by_link_text('登录豆瓣').click()
# browser.find_element_by_link_text('登录豆瓣').send_keys(Keys.ENTER)

# 退出
browser.quit()
