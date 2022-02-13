import time
from tkinter import *
from datetime import datetime
import crawler_soup
global xlsxwriter
import xlsxwriter
import os
import sys
import glob

code_start_time = time.time()
def get_inputed_keyword_file_name_by_cli():
    myFiles = glob.glob('*.txt')
    myFiles = [file for file in myFiles if(file != 'stopwords.txt')]
    filetext = '\t# Your Text File List:\n\t--------------------------\n'
    for i in range(len(myFiles)):
       filetext += "\t  " + str(i+1)+") " + myFiles[i] + "\n"

    filetext += '\t--------------------------\n'
    _index = int(input(f"{filetext}\t# Type Index Of keyword File: "))
    try:
        inputeFileName = myFiles[_index-1]
    except: inputeFileName = '' 
    return inputeFileName


def crawl(keyword,driver):
    return crawler_soup.read_ads(keyword,False)

def safe(results):
    time_now = str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
    workbook = xlsxwriter.Workbook('crawl_' + time_now + '.xlsx')
    stopwords = open("stopwords.txt")
    stopwords = stopwords.readlines()
    worksheet = workbook.add_worksheet("Crawlresults")
    #worksheet = workbook.add_worksheet("Anleitung")
    worksheet.write('A1', "Screen ID")# google result
    worksheet.write('B1', "Rank")# google result
    worksheet.write('C1', "Datum/Uhrzeit")# google result
    worksheet.write('D1', "Keyword")# google result
    worksheet.write('E1', "Link")# google result
    worksheet.write('F1', "Titel")# google result
    worksheet.write('G1', "Preis")# youtube result
    worksheet.write('H1', "Anbieter")# youtube result
    worksheet.write('I1', "Ad Anbieter")# youtube result
    worksheet.write('J1', "Ad Type")# youtube result
    #print("--------------------------------------", len(result))
    zahl = 1
    for i, (keyword, result) in enumerate(results.items()):
        for j in range(0, len(result[0])):
                stopword = 0
                for word in stopwords: 
                    if word in result[0][j] or word in result[3][j]:
                        print("stopword-----------")
                        stopword = 1
                        zahl -=1
                        break
                    else:
                        continue
                zahl +=1
                if stopword == 0:
                    try:
                        print(zahl)
                        worksheet.write('A{}'.format(zahl), result[7][j]) # screen id
                        worksheet.write('B{}'.format(zahl), result[8][j])# rank
                        worksheet.write('C{}'.format(zahl), result[6]) #datum uhrzeit
                        worksheet.write('D{}'.format(zahl), keyword) #datum uhrzeit
                        worksheet.write('E{}'.format(zahl), result[0][j])# google result
                        worksheet.write('F{}'.format(zahl), result[1][j])# google result
                        worksheet.write('G{}'.format(zahl), result[2][j])# google result
                        worksheet.write('H{}'.format(zahl), result[3][j])# google result
                        worksheet.write('J{}'.format(zahl), result[5][j])# google ident result
                        worksheet.write('I{}'.format(zahl), result[4][j])# Von Google / ..                        

                    except:
                        continue
    workbook.close()
    print("\n\n\n Total Execution Time:")
    print("======================")
    print("--- %s seconds ---" % (round(time.time() - code_start_time, 2)))
    print("======================")
    wait_=input()

    return

try:
    # Directory
    directory = "Webcrawler"
    # Parent Directory path
    parent_dir = "C:/"
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except:
    pass
    
try:
    # Directory
    directory = "Screens"
    # Parent Directory path
    parent_dir = "C:/Webcrawler"
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except:
    pass


# showBrowser = str(input("\tOpen brower(y/n): "))
# if isinstance(showBrowser, str):
#     if(showBrowser=='y'): showBrowser = True
#     if(showBrowser=='n'): showBrowser = False
# else:
#     open_brower = False
open_brower = True

fileName_fromCli = get_inputed_keyword_file_name_by_cli()
print(f'\n\t({fileName_fromCli}) Crawl is starting...  ')
time.sleep(2)

keywords = open(fileName_fromCli,'r', encoding='utf8') 
results = {}
for keyword in keywords.readlines():
        try:
            results[keyword] = crawler_soup.read_ads(keyword,showBrowser)
            '''if len(results[keyword][0]) > 0:         debug
                break'''
        except Exception as e:
            pass
safe(results)

