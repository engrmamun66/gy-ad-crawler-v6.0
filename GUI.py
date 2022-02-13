from tkinter import *
from datetime import datetime
import crawler_soup
global xlsxwriter
import xlsxwriter
import glob
import os



class GUI():
    def __init__(self):
        #os.chdir(r''")
        txt_files = myFiles = glob.glob('*.txt')
        self.gui = Tk(className='google-youtube crawler')
        # set window size
        self.gui.geometry("750x350")
        self.keywords_description = Label(self.gui, text="Keywords bitte nur eins pro Zeile (mit Enter trennen)")
        self.keywords_description.place(x=20, y=20)
        self.keywords = Text(self.gui, bd=1, width=70, height=8)
        self.keywords.place(x=20, y=40)
        #self.time_start_description = Label(self.gui, text="Zu welcher Zeit möchtest du den Crawler starten? Format muss z.B (16:54) entsprechen")
        #self.time_start_description.place(x=20, y=140)
        #self.time_start = Entry(self.gui, bd=1, width=20)
        #self.time_start.place(x=20, y=160)
        self.options = txt_files
        self.variable = StringVar(self.gui)
        self.dropdownlist_init = self.variable.set(self.options[0])
        self.dropdownlist = OptionMenu(self.gui, self.variable, *self.options)
        self.dropdownlist.config(width = 30)
        self.dropdownlist.place(x=20, y= 180)
        self.start_crawler = Button(self.gui, bd=1, width=80, height=5, text="Start", command=self.start)
        self.start_crawler.place(x=20, y=240)
        self.gui.mainloop()

    def start(self):
        kw_list = self.variable.get()
        if self.keywords.compare("end-1c", "==", "1.0"):
            keywords = open(kw_list,'r', encoding='utf8') 
            results = {}
            for keyword in keywords.readlines():
                    
                    try:
                        results[keyword] = crawler_soup.read_ads(keyword,True) #fff
                        '''if len(results[keyword][0]) > 0:         debug
                            break'''
                    except Exception as e:
                        
                        pass
            self.safe(results)
        else:
            keywords = self.keywords.get("1.0",END).split("\n")
            keywords = [keyword for keyword in keywords if keyword != ""]
            results = {}
            for keyword in keywords:
                for i in range(1):
                    
                    try:
                        results[keyword] = self.crawl(keyword, False)
                        if len(results[keyword][0]) > 0:
                            break
                        # print(results)
                    except Exception as e:
                        
                        pass
            self.safe(results)
            

    def crawl(self,keyword,driver):
        return crawler_soup.read_ads(keyword, True)#fff

    def safe(self,results):
        print('=============================')
        print('========== THE END ==========')
        # print('=============================')
        # print('||||||||||||||||||||||| Stop to create excel')
        # return
        time_now = str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
        workbook = xlsxwriter.Workbook('crawl_' + time_now + '.xlsx')
        stopwords = open("stopwords.txt")
        stopwords = stopwords.readlines()
        #worksheet = workbook.add_worksheet("Anleitung")
        
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
        zahl = 1
        for i, (keyword, result) in enumerate(results.items()):
            for j in range(0, len(result[0])):
                    stopword = 0
                    for word in stopwords: 
                        if word in result[0][j] or word in result[3][j]:
                            stopword = 1
                            zahl -=1
                            break
                        else:
                            continue
                    zahl +=1
                    if stopword == 0:
                        try:
                            # print(zahl)
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
        return


if __name__ == "__main__":
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
    


gui = GUI()
