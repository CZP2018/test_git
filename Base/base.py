from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    # 定位单个元素 封装
    def base_find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    # 定位一组元素 封装
    def base_find_elements(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_elements(*loc))

    # 点击元素 封装
    def base_click_btn(self,loc):
        self.base_find_element(loc).click()

    # 输入元素 封装
    def base_input_text(self,loc,value):
        self.base_find_element(loc).send_keys(value)


    # 获取元素 文本值 封装
    def base_get_test(self,loc):
        return self.base_find_element(loc).text