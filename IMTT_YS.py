# For Yourtube Text
from typing import Iterator
from inc.withimage import imgtotext
from inc.functions import isYtAd, readYtAds, getYtTitle, getYtLink
from inc.functions import isYsAd, getYsTitle, getYsPrice, getYsAnbieter


hasShoppinAdd = isYsAd(imgtotext(
    imagename='assets/try_1.png', image_index=1, positionMap="200:900, 0:1500"))

if hasShoppinAdd:
    gridMaps = ["300:860, 0:335", #grid1
                "300:860, 335:620", #grid2
                "300:860, 620:905", #grid3
                "300:860, 905:1200", #grid4
                ]
    for gridMap in gridMaps:
        imageText = imgtotext(imagename='assets/try_3.png', image_index=1, positionMap=gridMap, showimage=False, printText=False)
        title = getYsTitle(imageText)
        anbieter = getYsAnbieter(imageText)
        price = getYsPrice(imageText)

        print(f"Title: {title}, \nAnbieter: {anbieter}\nprice: {price}\n")


