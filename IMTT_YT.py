
"""
“Copyright 2023 SOFT PRO IT” , and a statement of copying permission, saying that the program is distributed under the terms of the GNU General Public License.
https://www.gnu.org/licenses/licenses.html

EULA
https://softproit.com/google-youtube-data-crawler/#licenses

"""
# For Yourtube Text
from typing import Iterator
from inc.withimage import imgtotext
from inc.functions import isYtAd, readYtAds, getYtTitle, getYtLink



imgMap_1 = "190:1500, 0:1500"
imageText = imgtotext(imagename='3.png', image_index=1,
                      positionMap=imgMap_1, showimage=False, printText=False)

if isYtAd(imageText):    
    ads = readYtAds(imageText)
    if len(ads):
        for ad in ads:
            title = getYtTitle(ad)
            link = getYtLink(ad)            
            print(f'\nTitle: {title}\nLink: {link}\n')
else: 
    print(f'This is not an add !!!')
    pass

