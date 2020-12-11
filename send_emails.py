from selenium import webdriver
import time

urlPitt = "https://my.pitt.edu"


# login pitt_email
def login_pitt():
    """
    INPUT: user credentials

    OUTPUT: driver

    logs in to Pitt

    """
    email = input("Type Pitt Email: ")
    passw = input("Type password: ")
    driver = webdriver.Chrome()
    driver.get(urlPitt)

    menu_btn = driver.find_element_by_id("headerMenuDropdown")
    menu_btn.click()

    signin_btn = driver.find_element_by_xpath(
        "/html/body/div[1]/div[4]/section[1]/div/nav/div/div[2]/ul/li[2]/ul/li[1]/a")
    signin_btn.click()

    username = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[1]/input")
    username.send_keys(email)

    password = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/div[2]/input")
    password.send_keys(passw)

    submit_btn = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/form/button")
    submit_btn.click()

    print('PLEASE CONFIRM IN BROWSER')
    key_pressed = input('Press ENTER to continue: ')

    return driver


def open_outlook(driver):
    """

    :param driver: webdriver object
    :return: driver
    """

    time.sleep(5)
    email_btn = driver.find_element_by_xpath(
        "/html/body/div[1]/div[5]/div[3]/div/div[2]/div[2]/div[3]/div[1]/div/div/a")
    email_btn.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    return driver


def new_message(driver, email, template, subject):
    """

    :param driver:
    :param email:
    :param template:
    :param subject:
    :return:
    """
    new_mess_btn = driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div > div._25oA4qBLP_b6P080cw5s2H.css-43 > div._1waWmu4XtQsneHiFwpHx7b > div.qtRcagoPZ5dw3xsr114ze > button')
    new_mess_btn.click()

    email_input = driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div > div._3mBjlqTqXMUiRuuWRKCPtX.css-42 > div._1jw6v9zFEgnOiXShpU1qqM > div > div.mm4nCLKbIRtx5HvuorDWT > div._1QDTZfBsizkS8O4Jej5a3A > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._3Yr_hO7j5doGUkhrRiP6uY > div:nth-child(1) > div:nth-child(1) > div._31eKqae41uP_KBAvjXjCLQ > div > div > div > div > div.ms-FocusZone.css-57 > div > div > input')
    email_input.send_keys(email)

    message_input = driver.find_element_by_css_selector('#app > div > div._3KAPMPOz8KsW24ooeUflK2 > div._2jR8Yc0t2ByBbcz_HIGqZ4 > div > div._3mBjlqTqXMUiRuuWRKCPtX.css-42 > div._1jw6v9zFEgnOiXShpU1qqM > div > div.mm4nCLKbIRtx5HvuorDWT > div._1QDTZfBsizkS8O4Jej5a3A > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._2_G1lB2DCB_6t73ZTT6vX3._2Hl0t2u2yIjuWmfatKUaJ2 > div._4utP_vaqQ3UQZH0GEBVQe.B1QSRkzQCtvCtutReyNZ.CAUXSSmBTHvYTez0U6p3M._17ghdPL1NLKYjRvmoJgpoK._2s9KmFMlfdGElivl0o-GZb')
    message_input.send_keys(template)

    subject_input = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input')
    subject_input.send_keys(subject)

    send_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]')
    time.sleep(30)
    send_btn.click()

    return driver
