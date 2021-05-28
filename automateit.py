import tkinter
import sys
import time 
import random
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from tkinter import*
import re 
def creat_fb():
    global x,y,driver
    while 1:
    
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
       
        driver.get("https://www.facebook.com")
        file = open("names.txt","r")
        read=file.read()
        file.close()
        read=read.replace("\n",":")
        names=read.split(":")
        x=random.choice(names)
        driver.find_element_by_name("firstname").send_keys(x)
        y=random.choice(names)
        driver.find_element_by_name("lastname").send_keys(y)
        driver.find_element_by_name("reg_email__").send_keys(x+"."+y+"1992"+"@99pubblicita.com")
        driver.find_element_by_name("reg_email_confirmation__").send_keys(x+"."+y+"1992"+"@99pubblicita.com")
        driver.find_element_by_name("reg_passwd__").send_keys("azertyuiop123é@@@@")
        driver.find_element_by_id("u_0_a").click()
        driver.find_element_by_name("websubmit").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div[3]/button""").click()
        email_confirmation()
    

def email_confirmation():
    global x,y,driver
    global email
   
    driver2=webdriver.Chrome()
    driver2.get("https://temp-mail.org/fr/option/change/")
    driver2.refresh()
    driver2.find_element_by_name("mail").send_keys(x+"."+y+"1992")
    driver2.find_element_by_xpath("""//*[@id="domain"]/option[@value='@99pubblicita.com']""").click()
    driver2.find_element_by_id("postbut").click()
    driver2.get("https://temp-mail.org/fr/option/refresh/")

    source=driver2.page_source

    precode=re.search("(?P<group1>.{6})est votre code de confirmation",source)
    while precode is None:
        source=driver2.page_source
        precode=re.search("(?P<group1>.{6})est votre code de confirmation",source)

    code = precode.group("group1")
    driver2.close()
    




    driver.find_element_by_name("code").send_keys(code)
    driver.find_element_by_name("confirm").click()
    try:
        driver.find_element_by_xpath("""//*[@id="facebook"]/body/div[4]/div[2]/div/div/div/div[3]/div/a""").click()
    except:
        print("no alert")

    with open ("emails.txt","a")as file:
        file.write(x+"."+y+"1992"+"@99pubblicita.com\n")
    time.sleep(3)
    driver.close()
        
     
def facebook_connect():
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com")
    file = open("emails.txt","r")
    read=file.read()
    file.close()
    read=read.replace("\n",":")
    emails=read.split(":")
    x=random.choice(emails)
    driver.find_element_by_name("email").send_keys(x)
    driver.find_element_by_name("pass").send_keys("azertyuiop123é@@@@")
    driver.find_element_by_id("u_0_2").click()
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}

def join_groups():
    username = "alphee.jobin@hotmail.fr"
    password = "HelloWorld"
    Keyword = e.get()
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #driver = webdriver.Chrome(chrome_options=chrome_options)

    file = open("emails.txt","r")
    read=file.read()
    file.close()
    read=read.replace("\n",":")
    emails=read.split(":")

    for x in emails:

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.facebook.com")
        y = "azertyuiop123é@@@@"


        try:
            driver.find_element_by_name("email").send_keys(x)
            driver.find_element_by_name("pass").send_keys(y)
            j = driver.find_elements_by_tag_name("input")
            for k in j:
                if k.get_attribute("data-testid") == "royal_login_button":
                    try:
                        k.submit()
                        break
                    except:
                        pass
        except:
            print("Cant login to that account")
        time.sleep(3)
        driver.get("https://www.facebook.com/search/groups/?q={}".format(Keyword))

        z = driver.find_elements_by_tag_name("a")
        for y in z:
            try:
                if y.get_attribute("rel") == "async-post":
                    try:
                        y.click()
                    except:
                        pass
            except:
                pass

        driver.close()

def ShareIt():
    
    comment = t.get(0.0,END)
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    
    file = open("emails.txt","r")
    read=file.read()
    file.close()
    read=read.replace("\n",":")
    emails=read.split(":")

    for x in emails:

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.facebook.com")
        y = "someexample"
        y = "HelloWorld"
        

        try:
            driver.find_element_by_name("email").send_keys(x)
            driver.find_element_by_name("pass").send_keys(y)
            j = driver.find_elements_by_tag_name("input")
            for k in j:
                if k.get_attribute("data-testid") == "royal_login_button":
                    try:
                        k.submit()
                        break
                    except:
                        pass
        except:
            print("Cant login to that account")
        time.sleep(3)
   

        time.sleep(3)
        driver.get("https://www.facebook.com/groups/")
        source = driver.page_source
        ss = re.findall("""href="/groups/(?P<grp1>[0-9]+)/""",source)
        for jj in ss:
            try:
                driver.get("https://m.facebook.com/groups/{}/?soft=composer".format(jj))
                driver.find_element_by_xpath("""//*[@id="MRoot"]/div/div[3]/div[1]/table/tbody/tr/td[1]/button""").click()
            except:
                pass
            try:
                driver.find_element_by_css_selector(""".composerInput.mentions-input""").send_keys(comment)
                driver.find_element_by_xpath("""//*[@id="composer-main-view-id"]/div[1]/div/div[3]/div/button""").click()
            except:
                pass






window=Tk()

C = Canvas(window, bg="blue", height=450, width=845)
C.config(background="deep sky blue")
filename = PhotoImage("1.gif")

C.pack()
window.title("Automate it")
mbutton1=Button(text=" Create accounts",command=creat_fb,relief=RAISED,cursor="hand2",bg="#CEF6F5",bd=5).place(x=160,y=115)

e = Entry(window,width=30)
e.place(x=160,y=200)
mlabel=Label(text="Keyword",relief=RAISED,bg="white").place(x=70,y=200)
b1 = Button(window,text="Join groups",relief=RAISED,cursor="hand2",bg="#CEF6F5", command = join_groups)
b1.place(x=350,y=200)
t = Text(window, height=10, width=40)
t.place(x=160,y=250)
nlabel=Label(text="Comment",relief=RAISED,bg="white").place(x=70,y=250)
b2 = Button(window,text="  Share  ",relief=RAISED,cursor="hand2",bg="#CEF6F5",command = ShareIt)
b2.place(x=500,y=320)
window.mainloop()    


        
