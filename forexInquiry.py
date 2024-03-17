import sys
import os
import tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def forex_inquiry(date, name, currency_code):
    # 启动WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 模拟访问网页
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        # 日期
        date_input = driver.find_element(by=By.ID, value="erectDate")
        date_input.clear()
        date_input.send_keys(date)

        # 货币
        currency = driver.find_element(by=By.ID, value="pjname")
        currency.send_keys(currency_code)

        # 查询按钮
        button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[5]/div[1]/div["
                                                        "2]/div/form/div/table/tbody/tr/td[7]/input")
        button.click()

        # 等待页面出现, 确保存在元素可以抓取
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "publish")))

        # 找到并打印结果
        rate = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[4]/table/tbody/tr[2]/td[2]").text
        print(rate)
        # 写入本地文件
        result_file_path = "result.txt"
        mode = "w" if not os.path.exists(result_file_path) else "a"
        with open(result_file_path, mode) as file:
            file.write(f"Exchange rate for {date} and currency {name}: {rate}\n")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
    else:
        date = sys.argv[1]
        currency = sys.argv[2]
        currency_code = tools.convert(currency)
        forex_inquiry(date, currency, currency_code)