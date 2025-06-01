from datetime import datetime
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestCase:
    @classmethod
    def setup_class(self):
        #配置chrome，自行下载自己电脑对应谷歌浏览器版本chromedriver并放到项目根目录并与下方的chromedriver.exe文件名一致，网址在readme.md
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://mis-toutiao-python.itheima.net/#/')
    @classmethod
    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    # 设置测试order为2 （提示：课本126页）
    @pytest.mark.run(order=2)
    def test_mis_login(self):
        # 通过执行js脚本直接跳过人机验证，此处不用修改
        js = "document.getElementById('inp1').removeAttribute('disabled')"
        self.driver.execute_script(js)
        #通过ID定位登录按钮并点击(如果使用完整xpth定位元素扣2分）
        self.driver.find_element(by=By.ID,value="inp1").click()
        sleep(2)
        # 通过PARTIAL_LINK_TEXT定位退出元素并获取文本值存到result (如果使用完整xpth定位元素扣2分）
        result = self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value="退出")
        #如果result包含“退出”则测试通过
        assert result != ""

    # 设置测试order为3 （提示：课本126页）
    @pytest.mark.run(order=3)
    def test_mis_audit(self):
        sleep(2)
        # 通过PARTIAL_LINK_TEXT定位 信息管理 元素并点击 (如果使用完整xpth定位元素扣2分）
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value="信息管理").click()
        sleep(2)
        # 通过PARTIAL_LINK_TEXT定位 内容审核 元素并点击 (如果使用完整xpth定位元素扣2分）
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value="内容审核").click()
        sleep(2)
        # 通过xpath匹配方式获取   请输入: 文章名称 输入框并输入:测试文章发布         (如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[3]/div/div[2]/div/div[1]/div/input').send_keys("测试文章发布 ")
        sleep(2)
        # 通过xpath匹配方式获取   请选择状态 输入框并点击        (如果使用完整xpth定位元素扣1分）
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/input').click()
        sleep(2)
        # 通过xpth多重匹配选择审核通过并点击，此处不用修改
        self.driver.find_element(By.XPATH, "//*[@class='el-select-dropdown__wrap el-scrollbar__wrap']//*[text()='审核通过']").click()
        sleep(2)
        # 通过xpth匹配选择定位结束时间日期框并存入endtime
        endtime=self.driver.find_element(By.XPATH,"//*[@placeholder='选择结束时间']")
        print(endtime)
        #清除endtime的文本内容
        endtime.clear()
        sleep(2)
        # 往endtime输入当前日期时间，此处不用修改
        endtime.send_keys(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sleep(2)
        #通过class_name定位查找按钮并点击 (如果使用完整xpth定位元素扣1分）
        # self.driver.find_element(By.CLASS_NAME,value="find").click()
        # sleep(2)
        #使用右边第一个 通过 的完整xpath路径定位并点击
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[3]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button[2]').click()
        sleep(2)
        # 点击确定（此处不用修改）
        self.driver.find_element(By.CSS_SELECTOR,".el-button--primary").click()
        successful = False
        try:
            sleep(2)
            self.driver.find_element(By.XPATH, "//*[text()='审核通过']")
            successful = True
        except Exception as e:
            print(e)
        assert successful