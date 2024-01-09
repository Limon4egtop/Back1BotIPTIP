
comicsTabel = [["https://i.imgur.com/mFrUAMp.png", "https://i.imgur.com/b1Vamjk.png", "https://i.imgur.com/m3t8rGO.png",
                "https://i.imgur.com/6bYcTwX.png", "https://i.imgur.com/LaIHRaz.png"],
               ["https://i.imgur.com/o7FtG1o.png", "https://i.imgur.com/3A7Bc5S.png", "https://i.imgur.com/qYeLojd.png",
                "https://i.imgur.com/p2eEBhA.png", "https://i.imgur.com/PGxkCaW.png"],
               ["https://i.imgur.com/YlwrmKd.png", "https://i.imgur.com/4KX0p16.png", "https://i.imgur.com/pE2xEgU.jpg",
                "https://i.imgur.com/flER8El.jpg", "https://i.imgur.com/lMUh02A.png", "https://i.imgur.com/0gM1Xpa.png",
                "https://i.imgur.com/ACZogxS.jpg"]]

def getComicsPage(comicsId, pageNumber):
    return comicsTabel[comicsId][pageNumber]

def getComicsLen(comicsId):
    return len(comicsTabel[int(comicsId)-1])