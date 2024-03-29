
"""
“Copyright 2023 SOFT PRO IT” , and a statement of copying permission, saying that the program is distributed under the terms of the GNU General Public License.
https://www.gnu.org/licenses/licenses.html

EULA
https://softproit.com/google-youtube-data-crawler/#licenses

"""
from PIL import Image
import PIL

# =======================================================
# =======================================================
# ==============                       ==================
# ============= Youtube Textanzeige Ad ==================
# ==============                       ==================
# =======================================================
# =======================================================


def isYtAd(text):
    if(isinstance(text, str)):
        return "Anzeige" in text or "Ad " in text or "VISIT SITE" in text or "WEBSITE BESUCHEN" in text
    else:
        return False


def exclude(line):
    if 'Showing results' in line: line = ''
    return line

def titleCleaner(title):
    title = title.replace("VISIT SITE", "")
    title = title.replace("WEBSITE BESUCHEN", "")
    title = title.replace("[4", "")
    title = title.replace("[erty", "")
    title = title.replace("[erty", "")
    title = title.replace("    ", " ")
    title = title.replace("   ", " ")
    title = title.replace(" ", " ")
    title = title.replace("®", " ")
    title = title.split('...')[0]
    title = title.lstrip(" ,-“@!~$%^&*(){}[]\"'|\\/?<,>.`+*©€,")
    title = title.rstrip(" ,-“@!~$%^&*(){}[]\"'|\\/?<,>.`+*©€,")
    title = title.replace("#SYNTAX", "")
    return title

def getYtTitle(text):
    try:
        arr = text.split('\n')
        title = ''
        for line in arr:
            line = exclude(line)
            line = line.lstrip('@ ')
            if('Ad' in line or 'Anzeige' in line):
                break
            title += " " + line
        theTitle = title.split('Visit')[0]
        theTitle = title.split('Anzeige')[0]
        theTitle = title.split('http')[0]
        return titleCleaner(theTitle)
    except: return ''

def getYtLink(text):
    try:
        arr = text.split('\n')
        title = ''
        url = ''
        for line in arr:
            if('http' in line):
                for word in line.split(" "):
                    if 'http' in word:
                        url = word
                        break
        return url.strip()
    except: return ''


def getPrice(text):
    arr = text.split('\n')
    title = ''
    url = ''
    for line in arr:
        if('http' in line): 
            for word in line.split(" "):               
                if 'http' in word:
                    url = word
                    break
    return url.strip()

   
def readYtAds(text):
    ads = []
    singleAd = ''
    for line in text.split('\n'):
        singleAd += '\n' + line
        # if "http" in line:
        if "http" in line:
            ads.append(singleAd)
            singleAd = ''
 
    # c = len(ads)
    # print(f"------------------------------\n\nTotle ad is : {c}")
    return ads


# ====================================================
# ====================================================
# ==============                    ==================
# ============= Youtube Shopping Ad ==================
# ==============                    ==================
# ====================================================
# ====================================================

def isYsAd(text):
    if(isinstance(text, str)):
        return "Suggested products" in text or "Vorgeschlagene Produkte" in text
    else:
        return False

def lineArray(adText):
    arr = []
    for line in adText.split('\n'):
        if(len(line)):
            arr.append(line)
    return arr



def getYsTitle(text):
    arr = lineArray(text)
    del(arr[-1])
    del(arr[-1])
    
    title = '' 
    for line in arr:        
        title += " " + line
        
    theTitle = title.split('...')[0]
    return titleCleaner(theTitle)


def getYsPrice(text):
    return lineArray(text)[-1]

def getYsAnbieter(text):
    return lineArray(text)[-2]


def resizeImage(filename, fixed_width=1374):
    image = Image.open(filename)
    width_percent = (fixed_width / float(image.size[0]))
    height_size = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((fixed_width, height_size), PIL.Image.NEAREST)
    image.save(filename)
