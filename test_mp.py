import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class Testcase:
    @classmethod
    def setup_class(self):
        #配置chrome，自行下载自己电脑对应谷歌浏览器版本chromedriver并放到项目根目录并与下方的chromedriver.exe文件名一致，网址在readme.md
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://pc-toutiao-python.itheima.net/#/login')
    @classmethod
    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    #设置测试order为0 （提示：课本126页）
    @pytest.mark.run(order=0)
    def test_mp_login(self):
        #通过xpath匹配方式获取 手机号文本框元素 (如果使用完整xpth定位元素扣1分）
        phone_number = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div/div/form/div[1]/div/div/input')
        # 通过xpath匹配方式获取 验证码文本框元素 (如果使用完整xpth定位元素扣1分）
        verfy_code = self.driver.find_element(By.XPATH,value='//*[@id="app"]/div/div/form/div[2]/div/div/input')
        #获取文本框中提供的手机号默认值 并存到phone_number_value             提示：不能使用.text直接获取，要用get_attribute
        phone_number_value = phone_number.get_attribute("value")
        # 获取文本框中提供的验证码默认值 并存到verfy_code_value              提示：不能使用.text直接获取，要用get_attribute
        verfy_code_value = verfy_code.get_attribute("value")
        # 通过ctrl+A全选 手机号文本框的内容
        phone_number.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        # 通过退格键删除所选  手机号文本框的内容
        phone_number.send_keys(Keys.BACKSPACE)
        sleep(2)
        # 通过ctrl+A全选 验证码文本框的内容
        verfy_code.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        # 通过退格键删除所选  验证码文本框的内容
        verfy_code.send_keys(Keys.BACKSPACE)
        sleep(2)
        #手机号文本框输入前面存的默认值
        phone_number.send_keys(phone_number_value)
        sleep(2)
        # 验证码文本框输入前面存的默认值
        verfy_code.send_keys(verfy_code_value)
        sleep(2)
        # 通过classname定位登录按钮并点击(如果使用完整xpth定位元素扣1分）,注意这里是find_elements，说明有多个classname相同，要看清楚所需要的登录按钮是第几个,[0]表示选第一个
        self.driver.find_elements(by=By.CLASS_NAME, value='el-button')[1].click()
        sleep(2)
        # 通过classname定位右上角的用户名并获取文本(如果使用完整xpth定位元素扣1分）
        username = self.driver.find_element(by=By.CLASS_NAME, value='user-name').text
        # 通过assert判断获取到的用户名不为空
        assert username != ""
    #设置测试order为1 （提示：课本126页）
    @pytest.mark.run(order=1)
    def test_mp_publish(self):
        # 通过xpath匹配方式获取内容管理并点击(如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[1]/ul/div[2]/li/div').click()
        sleep(2)
        # 通过完整xpth路径查找发布文章并点击
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[1]/ul/div[2]/li/ul/li[1]').click()
        sleep(2)
        # 通过xpath匹配方式获取文章名称输入框并输入:测试文章发布         (如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div/input').send_keys("测试文章发布")
        sleep(2)
        # 切换到内容文本框内的iframe                      提示：课本54-55页
        self.driver.switch_to.frame(self.driver.find_element(by=By.ID,value='publishTinymce_ifr'))
        sleep(2)
        # 通过ID找到内容文本框元素，并输入:这是测试内容        (如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.ID,value='tinymce').send_keys("这是测试内容")
        sleep(2)
        #将iframe返回主页面                          提示：课本54-55页
        self.driver.switch_to.default_content()
        sleep(2)
        # 通过完整xpth路径 查找自动的单选框并点击
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[2]/section/div/form/div[3]/div/div/label[4]/span[2]').click()
        sleep(2)
        # 通过xpath匹配方式获取 请选择下拉框(如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[2]/section/div/form/div[4]/div/div/div/span/span/i').click()
        sleep(2)
        #通过xpth多重匹配选择数据库，此处不用修改。 如果在实验报告代码截图后面能说清楚这个是怎么匹配的，加3分。
        self.driver.find_element(By.XPATH,"//*[@class='el-select-dropdown__wrap el-scrollbar__wrap']//*[text()='数据库']").click()
        sleep(2)
        #通过xpath匹配方式获取 发表按钮 并点击 (如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/button[1]/span').click()
        successful=False
        try:
            sleep(2)
            # 通过xpath匹配查找弹出文字，若存在'新增文章成功'弹出文字，则测试通过，此处不用修改。
            self.driver.find_element(By.XPATH, "//*[text()='新增文章成功']")
            successful=True
        except Exception as e:
            print(e)
        assert successful
