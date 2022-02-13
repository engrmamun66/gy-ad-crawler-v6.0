# For Yourtube Text
from typing import Iterator
from inc.withimage import imgtotext
from inc.functions import isYtAd, readYtAds, getYtTitle, getYtLink



imgMap_1 = "190:1500, 0:1500"
imageText = imgtotext(imagename='assets/try-6.png', image_index=1,
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

