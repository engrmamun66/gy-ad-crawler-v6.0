from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random
import string
import re
import base64
import os


# For Yourtube Text
from inc.withimage import imgtotext
from inc.functions import isYtAd, readYtAds, getYtTitle, getYtLink
from inc.functions import isYsAd, getYsTitle, getYsPrice, getYsAnbieter


#google_link_list = [] , google_title_list = [] , google_price_list = [] , google_anbieter_list = [] , youtube_link_list = [] , youtube_title_list = [] , youtube_price_list = [] , youtube_seller_list = [] ,

def read_ads(input_keyword, open_browser=True):
    screen_id = random.randint(1, 9999999999)
    screen_id = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + str(screen_id) + random.choice(string.ascii_letters)
    stamp = str(datetime.now().strftime('%H_%M_%S %Y_%m_%d'))
    # setup input and outputs
    google_link_list = []
    google_title_list = []
    google_price_list = []
    google_anbieter_list = []
    google_ident_list = []
    youtube_link_list = []
    youtube_title_list = []
    youtube_price_list = []
    youtube_seller_list = []
    youtube_ident_list = []
    brand_list = []
    rank_list = []
    id_list = []
    rank = 0

    def getPriceFromTitle(title=''):
        myTitle = title.strip().replace('    ', '   ').replace('   ', '  ').replace(
            '  ', ' ').replace(' €', '€').replace('*, \d', ',\d')
        result = ''
        if('€' in myTitle):
            for x in myTitle.split():
                if('€' in x):
                    result = x
        return result.rstrip(" ,-“@!~$%^&*(){}[]\"'|\\/?<,>.`+*©zxcvbnm,.asdfghjklqwertyuiopZXCVBNM<ASDFGHJKL:QWERTYUIOP")

    # open_browser = 1
    if not open_browser:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--log-level=1')  # To stop warnings
        ser = Service("chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=ser, options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    # =======================================
    # =======================================
    # ========== WITH GOOGLE ================
    # =======================================
    # =======================================

    if 1:

        trys_google = 10
        while True:
            if trys_google <= 0:
                break
            trys_google -= 1
            driver.get(
                "https://www.google.de/search?q={}".format(input_keyword.replace(" ", "+")))
            time.sleep(1)
            

        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (By.XPATH, ("//*[text()='Ich stimme zu']")))).click()
        except Exception as e:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='zV9nZe']"))).click()
        # driver.switch_to.default_content()

        # ==============================
        # =========== Google Shopping Ad
        # ==============================

        # Controll Screen Shot
        driver.set_window_size(700, 1080)
        time.sleep(1)
        imageFileName = "C:\\Webcrawler\\Screens\\{}_g.png".format(screen_id)
        driver.save_screenshot(imageFileName)
        keepScreenShot = False

        contents = soup.find_all('div', class_='mnr-c pla-unit')
        rank = 0
        for eachBlock in contents:

            try:
                link = eachBlock.find('div', class_='ropLT').find('a')['href']
            except:
                link = ''

            try:
                title = eachBlock.find('div', class_='r4awE').get_text()
            except:
                title = ''

            # try: price = eachBlock.find('span', class_='e10twf').get_text()
            try:
                price = eachBlock.find(
                    'span', text=re.compile(".*€.*")).get_text()
            except:
                price = '0.00 €'

            try:
                anbieter = eachBlock.find(
                    'div', class_='LbUacb').find('span').get_text()
            except:
                anbieter = ''

            try:
                ident_von = eachBlock.find('div', class_='Qp6aMc').get_text()
            except:
                ident_von = ''

            if(
                len(link) and link[0:4] == 'http'
                and len(title)
                and len(price)
                and len(anbieter)
                and len(ident_von)
            ):
                print(
                    f"\n=============Google Shopping Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nident_von : {ident_von}\keyword: {input_keyword}")
                keepScreenShot = True
                rank += 1
                rank_list.append(str(rank))
                google_link_list.append(str(link))
                google_title_list.append(str(title))
                google_price_list.append(price)
                google_anbieter_list.append(str(anbieter))
                brand_list.append(str(ident_von))
                google_ident_list.append("Google Shopping Ad")
                id_list.append(str(screen_id) + "_gs")

        # =================================
        # =================================
        # =========== Google Textanzeige Ad
        # =================================
        # =================================

        contents = soup.find_all('div', class_='uEierd')
        rank = 0
        for eachBlock in contents:
            try:
                link = eachBlock.find('span', role="text").get_text()
            except:
                link = ''

            try:
                title = eachBlock.find('div', role='heading', class_='CCgQ5').find(
                    'span').get_text()  # Note: may be change class_ name
            except:
                title = ''

            try:
                price = getPriceFromTitle(title)
            except:
                price = ''

            try:
                anbieter = eachBlock.find(
                    'div', class_='v5yQqb').find('a')['href']
            except:
                anbieter = link

            if(
                len(link) and link[0:4] == 'http'
                and len(title)
                and len(anbieter)
                and anbieter[0:4] == 'http'
            ):
                print(
                    f"\n=============Google Textanzeige Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nkeyword: {input_keyword}")
                keepScreenShot = True
                rank += 1
                rank_list.append(str(rank))
                google_link_list.append(str(link))
                google_title_list.append(str(title))
                google_price_list.append(str(price))
                google_anbieter_list.append(str(anbieter))
                google_ident_list.append("Google Textanzeige")
                id_list.append(str(screen_id) + "_gt")

        if not keepScreenShot:  # found not fount any add delete the image
            try:
                os.remove(imageFileName)
            except:
                print("\nFailed Delete To Image!")

    # =======================================
    # =======================================
    # ========== WITH YOUTUBE ===============
    # =======================================
    # =======================================

    if 1:
        # options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
        trys_youtube = 10
        while True:
            if trys_youtube <= 0:
                break
            trys_youtube -= 1
            driver.get(
                "https://www.youtube.com/results?search_query={}".format(input_keyword.replace(" ", "+")))
            time.sleep(1)

        driver.set_window_size(700, 1080)

        try:
            WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(
                (By.XPATH, ("//*[text()='I Agree']")))).click()
        except:
            try:
                WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='yDmH0d']"))).click()
            except:
                pass

        # driver.switch_to.default_content()
        time.sleep(1)
        imageFileName = "C:\\Webcrawler\\Screens\\{}_y.png".format(screen_id)
        driver.save_screenshot(imageFileName)
        keepScreenShot = False

        # ===============================
        # ===============================
        # =========== Youtube Shopping Ad
        # ===============================
        # ===============================

        hasShoppinAdd = isYsAd(imgtotext(
            imagename=imageFileName, image_index=1, positionMap="200:900, 0:1500"))
        if hasShoppinAdd:
            gridMaps = ["300:860, 0:335",  # grid1
                        "300:860, 335:620",  # grid2
                        "300:860, 620:905",  # grid3
                        "300:860, 905:1200",  # grid4
                        ]
            rank = 0
            for gridMap in gridMaps:
                imageText = imgtotext(imagename=imageFileName, image_index=1,
                                      positionMap=gridMap, showimage=False, printText=False)

                link = "https://www.youtube.com/results?search_query={}".format(
                    input_keyword.replace(" ", "+"))
                title = getYsTitle(imageText)
                anbieter = getYsAnbieter(imageText)
                price = getYsPrice(imageText)

                if len(link) and len(title) and len(anbieter) and len(price):
                    print(
                        f'\n=============Youtube Shopping Ad===============\nLink: {link}\nTitle: {title}\nAnbieter: {anbieter}\nkeyword: {input_keyword}')
                    rank += 1
                    keepScreenShot = True
                    rank_list.append(str(rank))
                    google_link_list.append(str(link))
                    google_title_list.append(str(title))
                    google_price_list.append(price)
                    google_anbieter_list.append(str(anbieter))
                    google_ident_list.append("Youtube Shopping")
                    id_list.append(str(screen_id) + "_ys")

        # ==================================
        # ==================================
        # =========== Youtube Textanzeige Ad
        # ==================================
        # ==================================

        imgMap_1 = "190:1500, 0:1500"
        imageText = imgtotext(imagename=imageFileName, image_index=1,
                              positionMap=imgMap_1, showimage=False, printText=False)

        if isYtAd(imageText):
            ads = readYtAds(imageText)
            if len(ads):
                rank = 0
                for ad in ads:

                    title = getYtTitle(ad)
                    link = getYtLink(ad)
                    anbieter = link

                    if len(title) and len(link):
                        print(
                            f'\n=============Youtube Textanzeige Ad===============\nTitle: {title}\nLink: {link}\nkeyword: {input_keyword}')
                        rank += 1
                        keepScreenShot = True
                        rank_list.append(str(rank))
                        google_link_list.append(str(link))
                        google_title_list.append(str(title))
                        google_price_list.append('')
                        google_anbieter_list.append(str(anbieter))
                        google_ident_list.append("Youtube Textanzeige")
                        id_list.append(str(screen_id) + "_yt")

        else:
            print(f'\nThis is not an add !!!')

        if not keepScreenShot:  # found not fount any add delete the image
            os.remove(imageFileName)

    # close web driver
    driver.close()
    # setup output
    output = [google_link_list, google_title_list, google_price_list, google_anbieter_list, brand_list, google_ident_list, stamp,
              id_list, rank_list, youtube_link_list, youtube_title_list, youtube_price_list, youtube_seller_list, youtube_ident_list]
    #print(output)
    print([len(google_link_list), len(google_title_list), len(google_price_list), len(google_anbieter_list), len(
        brand_list), len(google_ident_list), len(youtube_price_list), len(youtube_seller_list), ])
    return output


if __name__ == "__main__":
    read_ads("sommerreifen")
