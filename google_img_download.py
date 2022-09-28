import  time, mySeleniumDriver, os
import urllib.request
img_list = []
my_keyword = "태연" 
url = "https://www.google.co.kr/imghp?hl=ko&ogbl"
mySeleniumDriver.open_url(url)
#google 이미지 검색
######################################################################## 
mySeleniumDriver.my_find_element_send_keys('q', my_keyword)
mySeleniumDriver.my_find_element_enter('q')
########################################################################

#검색 결과를 리스트에 저장
########################################################################
#mySeleniumDriver.my_find_element_click('.rg_i.Q4LuWd')
img_list = mySeleniumDriver.my_find_elements_item('.rg_i.Q4LuWd')
########################################################################

#키워드로 폴더 만들기
os.makedirs("./" + my_keyword)

#각각의 검색결과를 클릭 후 다운로드
########################################################################
count = 1
for img in img_list :
    try :
        img.click()
        time.sleep(3)
        src = mySeleniumDriver.my_src_get('.n3VNCb.KAlRDb')
        urllib.request.urlretrieve(src, "./" + my_keyword + "/" + str(count) + '.jpg')
        count = count + 1
        time.sleep(3)
    except Exception as e :
        print('이미지 다운로드 에러 : ', e)
########################################################################
    


