# Supreme bot SBV1 with Selenium
from audioop import add
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from datetime import datetime 
import time
import random
import string

#google_link_list = [] , google_title_list = [] , google_price_list = [] , google_seller_list = [] , youtube_link_list = [] , youtube_title_list = [] , youtube_price_list = [] , youtube_seller_list = [] ,


def read_ads(input_keyword,driver):
    screen_id = random.randint(1,9999999999)
    screen_id = random.choice(string.ascii_letters)+ random.choice(string.ascii_letters) + str(screen_id) + random.choice(string.ascii_letters)
    stamp = str(datetime.now().strftime('%H_%M_%S %Y_%m_%d'))
    # setup input and outputs
    google_link_list = []
    google_title_list = []
    google_price_list = []
    google_seller_list = []
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
    
    _except = lambda param: ''# '__not-found: res_'+ str(param)
    _filter = lambda obj : obj.text
    
    #options.add_argument('headless')
    driver.set_window_size(700, 1080) # set window size to 700*1080 pixel
    # driver.maximize_window()
    # CRAWL GOOGLE -------------------------------------------------------------------------------------------------------------------------
    # navigate to Google website and accept cookies
    driver.get("https://www.google.de/search?q={}".format(input_keyword))
    try:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,("//*[text()='Ich stimme zu']")))).click()
    except:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='zV9nZe']"))).click()
    driver.switch_to.default_content()
    # set input and start google search
    #eingabe_google = input_keyword
    #searchbar = driver.find_element_by_css_selector("[title='Suche']")
    #searchbar.send_keys(eingabe_google)

    if 1:

        try:
            searchbar.send_keys(Keys.RETURN)
        except Exception as e:
            pass

        # finding the ad section on the website if nothing found continue with youtube ads
        scrolling_carousel = driver.find_element_by_class_name("{1}".format("pla-exp-container","cu-container"))

        time.sleep(1.5)
        all_children_by_css = scrolling_carousel.find_elements_by_css_selector("[class='mnr-c pla-unit']")
        print('>>>>> --- Google Shopping Ad count: '+ str(len(all_children_by_css)))

        
        rank = 0
        for i in all_children_by_css: # filling the result lists
            try:
                res_1 = i.find_element_by_tag_name("a").get_attribute("href")
            except:
                res_1 =_except(1)
            try:
                res_2 = i.find_elements_by_css_selector("*")[1].get_attribute("aria-label")
            except:
                res_2 =_except(2)
            try:
                res_3 = i.find_element_by_css_selector("[class='pla-unit-container']").find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].text
            except:
                res_3 =_except(3)
            try:
                res_4 = i.find_element_by_class_name("span.zPEcBd").text
            except:
                try:
                    res_4 =res_2.split()[-1]
                except:
                    res_4 =_except(4)
            try:
                res_5 = i.find_element_by_css_selector("[class='pla-unit-container']").find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[1].find_elements_by_xpath("./*")[2].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].text
            except:
                res_5 =_except(5)

            # only add the results to the lists when all information was read properly
            rank += 1
            rank_list.append(rank)
            google_link_list.append(str(res_1)) #https://www.atu.de/shop/Reifen-und-Felgen-w5369/Reifen_w10523/
            google_title_list.append(str(res_2)) #Hankook Ventus V12 Evo2 K120 (XL) 225/45 R17 94Y Sommerreifen für 70,52 € von CHECK24
            google_price_list.append(str(res_3)) #30,99 €
            google_seller_list.append(str(res_4)) 
            google_ident_list.append("Google Shopping Ad")
            brand_list.append(str(res_5))
            id_list.append(str(screen_id) + "_g")
        time.sleep(1.5)
        additional_children_by_css = driver.find_elements_by_css_selector("[class='uEierd']")
        print('>>>>> --- Google Textanzeige Ad count: '+ str(len(additional_children_by_css)))
        rank = 0
        for i in additional_children_by_css: # filling the result lists
            try:
                res_1 = i.find_element_by_class_name("sVXRqc").get_attribute("href")
            except:
                res_1 =_except(1)
            try:
                res_2 = i.find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[0].find_elements_by_xpath("./*")[1].text
            except:
                res_2 =_except(2)
            # res_3: no price available in this type of ads

            try:
                res_4 = i.find_element_by_class_name("sVXRqc").get_attribute("data-pcu")
            except:
                res_4 =_except(4)
            # only add the results to the lists when all information was read properly
            rank += 1
            rank_list.append(str(rank))
            google_link_list.append(str(res_1))
            google_title_list.append(str(res_2))
            google_price_list.append("")
            google_seller_list.append(str(res_4))
            google_ident_list.append("Google Textanzeige")
            id_list.append(str(screen_id) + "_g")

    # CRAWL YOUTUBE -------------------------------------------------------------------------------------------------------------------------
    # navigate to Youtube website and click away the windows
    driver.get("https://www.youtube.com/results?search_query={}".format(input_keyword))
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button'))).click()
        # just in case but doesnt have to be clicked when already clicked from by the google crawl
        #WebDriverWait(driver,5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://consent.google.com']")))
        #WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"///*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span"))).click()
        pass
    except Exception as e:
        pass
    driver.switch_to.default_content()

    if 1:
        # set input and start youtube search
        #eingabe_youtube = input_keyword
        #searchbar = driver.find_element_by_id("search")
        #searchbar.send_keys(eingabe_youtube)
        try:
            searchbar.send_keys(Keys.RETURN)
        except Exception as e:
            pass

        # finding the ad section on the website if nothing found return empty lists
        ad_elements = None
        trys_youtube = 10 # number of tries to receive a result with ads
        while True:
            if trys_youtube <= 0: break
            trys_youtube -= 1
            try:
                time.sleep(1.5)
                ad_elements_list = driver.find_elements_by_id("items")
                for i in ad_elements_list:
                    if i.get_attribute('class') == "style-scope yt-horizontal-list-renderer": 
                        ad_elements = i
                        break
            except Exception as e:
                pass
        if ad_elements != None: # check if ad elements were found
            driver.maximize_window()
            time.sleep(1.5)
            driver.set_window_size(700, 1080) # set window size to 700*1080 pixel
            rank = 0
            for i in ad_elements.find_elements_by_xpath("./*"):
                try:
                    res_1 = i.find_element_by_css_selector("[id='title-link']").get_attribute("href")
                    res_2 = i.find_element_by_css_selector("[id='title-text']").get_attribute("title")
                    res_3 = i.find_element_by_css_selector("[id='secondary-text']").get_attribute("title")
                    res_4 = i.find_element_by_css_selector("[id='body-text']").get_attribute("title")
                except Exception as e:
                    continue
                # only add the results to the lists when all information was read properly
                rank += 1
                rank_list.append(rank)
                google_link_list.append(res_1)
                google_title_list.append(res_2)
                google_price_list.append(res_3)
                google_seller_list.append(res_4)
                google_ident_list.append("Youtube Shopping Ad")
                id_list.append(screen_id + "_yt")
                print("Yotube ad")
                            
                

    # check for additional ads
    if 1:
        additional_ad_elements = driver.find_elements_by_id("contents")
        if ad_elements != None or additional_ad_elements != None:
            driver.save_screenshot("C:\Webcrawler\Screens\{}_yt.png".format(screen_id))
        if additional_ad_elements != None: # check if additional ad elements were found
            for i in additional_ad_elements:
                if i.get_attribute('class') == "style-scope ytd-section-list-renderer": # and i.get_attribute('id') == 'contents': 
                    additional_ad_elements = i
                    break
            rank = 0
            for i in additional_ad_elements.find_elements_by_xpath("./*"):            
            # for i in additional_ad_elements.find_elements_by_xpath("//div[@id='contents'][@class='style-scope ytd-item-section-renderer']"):            
                try:
                    res_1 = i.find_element_by_id("display-url").text      
                    if (len(res_1)==0):
                        res_1 = i.find_element_by_id("website-text").text                   
                except : 
                    try:
                        res_1 = i.find_element_by_id("website-text").text   
                    except: res_1 = _except(1)
                try:
                    res_2 = i.find_element_by_xpath('//h3[@id="title"]').text
                except : res_2 = _except(2)
                
                # no price available in this type of ads
                # try:
                #     res_3 = i.find_elements_by_tag_name("img")[0].get_attribute("src")
                # except : res_3 = _except(3)
                
                try:
                    res_4 = i.find_elements_by_xpath('//yt-formatted-string[@role="link"]')
                    res_4 = ', '.join(filter(None, [_filter(i) for i in res_4]))                    
                except : res_4 = _except(4)
                
                # only add the results to the lists when all information was read properly
                if (len(res_1) and len(res_2)): 
                    rank += 1
                    rank_list.append(rank)
                    google_link_list.append(res_1)
                    google_title_list.append(res_2)
                    google_price_list.append("")
                    google_seller_list.append(res_1)
                    google_ident_list.append("Youtube Textanzeige")
                    id_list.append(screen_id + "_yt")
                    print("Youtbe Text")


    # close web driver
    driver.close()
    # setup output
    output = [google_link_list, google_title_list, google_price_list, google_seller_list,brand_list, google_ident_list ,stamp , id_list, rank_list, youtube_link_list, youtube_title_list, youtube_price_list, youtube_seller_list, youtube_ident_list]
    # print(output)
    print([len(google_link_list),len(google_title_list),len(google_price_list),len(google_seller_list),len(brand_list),len(google_ident_list),len(youtube_price_list),len(youtube_seller_list),])
    return output




if __name__ == "__main__":
    PATH = "chromedriver_win32/chromedriver.exe" #  path to chrome driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
    read_ads("Gaming PC",driver)