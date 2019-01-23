#!/usr/bin/env python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import selenium


def createitemlist(driver):
    item0 = driver.find_element_by_id('product0')
    item1 = driver.find_element_by_id('product1')
    item2 = driver.find_element_by_id('product2')
    item3 = driver.find_element_by_id('product3')
    item4 = driver.find_element_by_id('product4')
    item5 = driver.find_element_by_id('product5')
    item6 = driver.find_element_by_id('product6')
    item7 = driver.find_element_by_id('product7')
    item8 = driver.find_element_by_id('product8')
    item9 = driver.find_element_by_id('product9')
    item10 = driver.find_element_by_id('product10')
    item11 = driver.find_element_by_id('product11')
    item12 = driver.find_element_by_id('product12')
    item13 = driver.find_element_by_id('product13')
    item14 = driver.find_element_by_id('product14')
    item15 = driver.find_element_by_id('product15')
    item_list = [item0, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15]

    return item_list


def checkupgrade(driver):
    try:
        upgrade = driver.find_element_by_id('upgrade0')
        upgrade.click()
    except selenium.common.exceptions.ElementNotInteractableException:
        pass
    except selenium.common.exceptions.StaleElementReferenceException:
        pass


def checkitems(item_list):
    for i in range(len(item_list)):
        try:
            item_list[15-i].click()
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            pass




def main():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    assert 'Cookie' in driver.title

    sleep(2)

    bigcookie = driver.find_element_by_id("bigCookie")
    item_list = createitemlist(driver)
    checkitems(item_list)

    checkiteminterval = 15
    try:
        for i in range(checkiteminterval):
            bigcookie.click()
        checkitems(item_list)
    except selenium.common.exceptions.NoSuchWindowException:
        print("Oh no, you've closed the window or something")

    checkupgrade(driver)

    while True:
        try:
            for i in range(checkiteminterval):
                bigcookie.click()
            checkupgrade(driver)
            checkitems(item_list)
        except selenium.common.exceptions.NoSuchWindowException:
            break
    print("Oh no, you've closed the window")


if __name__ == '__main__':
    main()
