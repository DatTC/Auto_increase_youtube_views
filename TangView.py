from selenium import webdriver
import time
VideoFileName = 'VideoList.txt'
SaveFile = 'ViewCount.txt'
btnPlay= "#movie_player > div.ytp-cued-thumbnail-overlay > button"
videoIndex = 0
tabIndex = 0
tabCount = 1
view = 0

#read file VideoFileName
VideoFile = open(VideoFileName)
ListVideo = VideoFile.readlines()

NUMBER_OF_VIDEO = len(ListVideo)
NUMBER_OF_TAB = 4
TIME_WAIT = 2

#start the brownser and display video
browser = webdriver.Chrome()
browser.get(ListVideo[videoIndex])

#click play button
time.sleep(2)
findPlayButton = browser.find_element_by_css_selector(btnPlay)
findPlayButton.click()

# #open new tab
# time.sleep(0.5)
# videoIndex = videoIndex + 1
# js = "window.open('"+ListVideo[videoIndex].strip()+"')"
# # print(js)
# browser.execute_script(js)

# # Go to previous tab and open new video
# time.sleep(2)
# handle = browser.window_handles[tabIndex]
# browser.switch_to.window(handle)

while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
    tabIndex = (tabIndex + 1) % NUMBER_OF_TAB
    if tabCount < NUMBER_OF_TAB:
        tabCount += 1
        browser.execute_script("window.open('"+ListVideo[videoIndex].strip()+"')")
    else:
        browser.switch_to.window(browser.window_handles[tabIndex])
        time.sleep(1)
        browser.get(ListVideo[videoIndex])
    time.sleep(TIME_WAIT)
    view += 1

    saveFile = open(SaveFile,"w")
    saveFile.write(str(view))
    saveFile.close()

    



