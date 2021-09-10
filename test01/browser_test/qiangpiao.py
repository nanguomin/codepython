from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

url_info_dict = {'driver': 'D:\softapp\idea\chrome\chromedriver_win32\chromedriver.exe',
                 'login_url': 'https://kyfw.12306.cn/otn/resources/login.html',
                 'personal_center_url': 'https://kyfw.12306.cn/otn/view/index.html',
                 'order_tickets_url': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc',
                 'order_submit_url': 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'}

"""
注意事项:
1.该抢票程序需要手动登录12306官网,和手动输入出发地,目的地,出发日期
2.使用该程序之前需要安装chrome浏览器和配置chromedriver.exe驱动器的环境变量,要求两者版本必须相同
chromedriver.exe 可以放到 (D:\softapp\idea\chrome\chromedriver_win32)该路径下,
若没有以上的文件夹请手动创建
"""


class qiangpiao_demo:
    def __init__(self):
        self.start_station = input("出发地:")
        self.end_station = input("目的地:")
        self.start_date = input("出发时间(时间格式例:2012-09-01):")
        self.train_number = input("车次(若要抢多趟列车,请用英文逗号分隔):").split(',')
        self.passenger_name = input("乘客姓名(若有多名乘客,请用英文逗号分隔):").split(',')
        self.login_url = url_info_dict['login_url']
        self.personal_center_url = url_info_dict['personal_center_url']
        self.browser = webdriver.Chrome(executable_path=url_info_dict['driver'])

    def input_info(self):
        pass

    def logon(self):
        self.browser.get(self.login_url)
        WebDriverWait(self.browser, 1000).until(ec.url_to_be(self.personal_center_url))
        print("登录成功")

    def order_tickets(self):
        self.browser.get(url_info_dict['order_tickets_url'])
        WebDriverWait(self.browser, 1000).until(
            ec.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.start_station))
        WebDriverWait(self.browser, 1000).until(
            ec.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.end_station))
        WebDriverWait(self.browser, 1000).until(
            ec.text_to_be_present_in_element_value((By.ID, 'train_date'), self.start_date))
        query_ticket = self.browser.find_element_by_id('query_ticket')
        query_ticket.click()
        WebDriverWait(self.browser, 1000).until(
            ec.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr")))
        tickets_lists = self.browser.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        for tickets_list in tickets_lists:
            tickets_number = tickets_list.find_element_by_class_name('number').text
            if tickets_number in self.train_number:
                t_list = tickets_list.find_element_by_xpath(".//td[4]").text
                if t_list == '有' or t_list.isdigit:
                    orderBtn = tickets_list.find_element_by_class_name('btn72')
                    print(tickets_number + '有票')
                    orderBtn.click()
                    WebDriverWait(self.browser, 1000).until(
                        ec.url_to_be(url_info_dict['order_submit_url']))
                    WebDriverWait(self.browser, 1000).until(
                        ec.presence_of_element_located((By.XPATH, ".//ul[@id='normal_passenger_id']/li")))
                    passenger_lists = self.browser.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")
                    for passenger_list in passenger_lists:
                        name = passenger_list.text
                        if name in self.passenger_name:
                            passenger_list.click()
                    submit_orders = self.browser.find_element_by_id('submitOrder_id')
                    submit_orders.click()
                    WebDriverWait(self.browser, 1000).until(
                        ec.presence_of_element_located((By.CLASS_NAME, 'dhtmlx_wins_body_outer')))
                    WebDriverWait(self.browser, 1000).until(ec.presence_of_element_located((By.ID, 'qr_submit_id')))
                    confirmBtn = self.browser.find_element_by_id('qr_submit_id')
                    confirmBtn.click()
                    while confirmBtn:
                        confirmBtn.click()
                        confirmBtn = self.browser.find_element_by_id('qr_submit_id')
                    print('抢票成功')

        print("==tickets_number==", tickets_number)
        print("加载成功")
        pass

    def run(self):
        self.input_info()
        self.logon()
        self.order_tickets()


if __name__ == '__main__':
    qp = qiangpiao_demo()
    qp.run()
