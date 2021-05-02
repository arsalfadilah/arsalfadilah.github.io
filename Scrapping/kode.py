from selenium import webdriver
import urllib.request
import json

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/c/CenelKITA45/videos")

videolist = []
#sebagai nama file png
i = 1

for video in driver.find_elements_by_tag_name("ytd-grid-video-renderer"):
    try:
        link = video.find_element_by_tag_name("ytd-thumbnail").find_element_by_tag_name("a").get_attribute("href").split("=")
        print(link)
        videolist.append({"link" : link[1]})
    except:
        print("error")
    # for img in video.find_elements_by_tag_name("img"):
    #     try:
    #         url = img.get_attribute("src")
    #         urllib.request.urlretrieve(url, str(i)+".png")
    #         print(url)
    #         videolist.append({"No": video.text.split("\n")[0],"Judul": video.text.split("\n")[1],"Rating": video.text.split("\n")[6],"Image": img.get_attribute("src")})
    #     except:
    #         continue     
    

hasilScrap = open("hasilscraping.json", "w")
fixData = json.dumps(videolist, indent=4, sort_keys=True)
hasilScrap.writelines(fixData)
hasilScrap.close()

driver.close()
driver.quit()