import os
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "../chromedriver"
abspath = os.path.abspath(path)
driver = webdriver.Chrome(abspath)

# abstract information
def getAbstract(name):
    try:
        # create new folder
        basePathDirectory = "Hudong_Coding"
        if not os.path.exists(basePathDirectory):
            os.makedirs(basePathDirectory)
        baiduFile = os.path.join(basePathDirectory,"HudongSpider.txt")
        # file name exit or not
        if not os.path.exists(baiduFile):
            info = codecs.open(baiduFile,'w','utf-8') # create and write
        else:
            info = codecs.open(baiduFile,'a','utf-8') # write

        url = "http://www.baike.com/wiki/" + name
        # url = "https://baike.baidu.com/item/" + name
        print(url)
        driver.get(url)
        elem = driver.find_element_by_xpath("//div[@class='summary']/p")
        # elem = driver.find_element_by_xpath("//div[@class='lemma-summary']/p")
        print(elem.text)

        # sum_node = soup.find('div', attrs={'class': 'lemma-summary'})
        # print(sum_node)
        info.writelines(elem.text+'\r\n')

    except ValueError:
        print("Error")
    finally:
        print('\n')
        info.write('\r\n')

# main function
def main():
    file_object = open('crawled_list.txt', 'r')
    lines = file_object.readlines()
    print('Start crawling')
    for line in lines:
        print(line)
        getAbstract(line)
    print('finish crawling')

if __name__ == '__main__':
    main()