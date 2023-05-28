#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from csv import writer
import re


# In[2]:


def url_predictor(url):
    list_of_lists=[]
    lst=[]
    driver = webdriver.Chrome(ChromeDriverManager().install())
    lst.append(url)
    website = requests.get(url)
    time.sleep(10)
    soup = BeautifulSoup(website.content)
    text = [''.join(s.findAll(text=True))for s in soup.findAll('p')]
    
    words=''
    for i in text:
        words+=str(i)
    print(words)
            
    from flashtext import KeywordProcessor
       
    sports = ['sports','NFL','motors','Sports','game','games','score','scores','team','player','league','points','athelete','baseball','basketball','bounce','bowling', 'boxing','cycling','dance', 'extreme sports','fishing','football','exercise', 'figure skating','fitness','free climbing','gymnastics','hockey','horse racing','hunting','ice hockey','ice skating','jumping','karate','kayak','kites','kabaddi','Little League','long distance runner','lowriding','marathon','martial arts','mountain climbing','open water swimming','Parkour','racing','record holders','runner','running','sailing','scuba diving','skateboarding','skiing','soccer','softball','sports','sportsmanship','stuntman','surfing','swimming','tennis','track and field','volleyball','wrestling','X games']
    entertainment = ['movies','showbuzz','news','magazine','technology','tickets','ticket','comedy','kids','premieres','entertainment','sports','cricket','channels','Channels','shows','originals','TV','music','musics','videos','video','songs','hits','song','top','artists','artist','singing','gallery','dj','folk','fusion','band','dance','genres','performances','musical','tracks','listen','listened','listeners','listener','hear','']
    health_care = ['health','care','healthcare','patients','patient','visitors','hospital','hospitals','clinics','clinical','clinic','medical','appointment','cancer','brain','lungs','heart','disease','diseases','life','lives','family','research','emergency','mental','surgery','service','servicing','smile','dentist','dental','visit','dentistry','medicare']
    restaurant = ['event','serve','serves','server','elegant','BBQ','sandwiches','Hours','Fancy','events','restaurant','menu','menus','dinner','brunch','lnuch','breakfast','reservations','cocktails','beers','cold','hot','order','chef','chefs','special','rice','rolls','food','bowl','wine','dining','hours','open','closed','king','working','pub','hospitality','quality','cook','cooked','cookbook','room','']
    m_learning = ['lms','mobile','mobiles','phone','phones','smart','smartphone','smartphones','improvement','building','microlearning','training','trains','course','courses','LMS','learn','learning','learners','collaborative','skills','organisation','programs','motivation','week','program','management','access','video','clip','clips','collaborative','Corporate','Training','Platform','development','holistic','growth','comprehensive','coach','Speech','Assistant','speaking','accent','accents','recognition','performance']
    real_estate = ['tours','yield','area','rentals','sale','sales','buying','selling','housing','market','savings','agent','agents','law','refinancing','discover','property','townhomes','renting','renters','place','residence','residences','neighborhood','sell','buy','rent','home','house','loan','loans','real','estate','mortage','value','sold','listings','selling','option','bid','deluxe','live','neighborhoods','homes','auction','lender','offer','rates','local','apartment','apartments','love','homes']
    finance = ['investing','finance','investments','trades','business','portfolio','earning','earnings','idea','ideas','payment','payments','invest','sell','stock','stocks','invest','valuable','property','investment','econimic','election','elections','market','buyers','inflation','earning','earnings','cryptocurrency','investing','personal','finance','crypto','bitcoin','market','markets','buy','profit','profits','money','mortage','holder','lender','investor','investors','bank','holders','repayments','lenders','payment','payments','buy','sale','sales','buyer','market','financial','economy','sell','properties','sector','sectors','property','tax','taxes','retirement','wealth','stock','stocks','taxes']
    fitness = ['fit','wellness','powerlifter','muscles','version','dietitians','trainers','fitness','wellbeing','workouts','bags','hormone','hormones','journey','plan','muscle','strong','eating','pills','pill','plans','training','trainings','movements','safety','rating','squat','press','lift','outfits','rooms','bullying',"accepted", "respected",'presses','athletes','trainings','training','trainers','trainer','workout','movement','push','swings','jump','jumps','hospital','hospitals','labs','gyms','lab','gym','spa','spas','yoga','health','healthy','food','fiet','nutrition','exercise']
    travel = ['travel','lodge','journey','land','water','guests','map','rules','world','appointment','resort','room','trip','plan','planner','traveling','travelers','planning','route','app','destination','days','day','date','guide','sightseeing','cuisine','accommodation','nearby','airport','itineraries','blog','holidays','holiday','destinations','luxury','tour','tours','trips','transport','airforce']
    business = ['business','Business','Advertising','Agriculture','Corporate','card','visiting','company','service','services','products','deal','vendor','vendors','exporter', 'exporters','manufacturer', 'manufacturers','deals','customer','customers','Banking, Finance and Investments','vendor','vendors','trade','trades','digital','advertising','marketing','hosspitals','automobiles','banking','finance','investments','']
    government = ['government','NCS','fraudulent','employment','frauds','Employment','Minister','Government','jobs','job','announcement','jobseeker','employer','center','sector','sectors','information','employee','placement','organization','counsellor','counsellors','career']
    politics = ['politics','politic','attacker','interview','perty','parties','truth','election','elections','police','crime','freedom','vote','weekday','idea','ideas','votes','voters','voter','reporter','truth','republicans','natinal','nationalism','nationalists','nationalist','violence','republic','affairs','magazine','affair','political','report','reports','weapons','weapon','news','newsletter','prime','minister','controversial']
    
    import numpy as np
    
    kp_sports = KeywordProcessor()
    for i in sports:
        kp_sports.add_keyword(i)
    kp_sports=kp_sports.extract_keywords(words)
    kp_sports = np.unique(kp_sports)
    kp_sports = list(kp_sports)
    
    kp_entertainment = KeywordProcessor()
    for i in entertainment:
        kp_entertainment.add_keyword(i)
    kp_entertainment = kp_entertainment.extract_keywords(words)
    kp_entertainment = np.unique(kp_entertainment)
    kp_entertainment = list(kp_entertainment)
    
    kp_health_care = KeywordProcessor()
    for i in health_care:
        kp_health_care.add_keyword(i)
    kp_health_care = kp_health_care.extract_keywords(words)
    kp_health_care = np.unique(kp_health_care)
    kp_health_care = list(kp_health_care)
    
    kp_restaurant = KeywordProcessor()
    for i in restaurant:
        kp_restaurant.add_keyword(i)
    kp_restaurant = kp_restaurant.extract_keywords(words)
    kp_restaurant = np.unique(kp_restaurant)
    kp_restaurant = list(kp_restaurant)
    
    kp_m_learning = KeywordProcessor()
    for i in m_learning:
        kp_m_learning.add_keyword(i)
    kp_m_learning = kp_m_learning.extract_keywords(words)
    kp_m_learning = np.unique(kp_m_learning)
    kp_m_learning = list(kp_m_learning)
    
    kp_real_estate = KeywordProcessor()
    for i in real_estate:
        kp_real_estate.add_keyword(i)
    kp_real_estate = kp_real_estate.extract_keywords(words)
    kp_real_estate = np.unique(kp_real_estate)
    kp_real_estate = list(kp_real_estate)
    
    kp_finance = KeywordProcessor()
    for i in finance:
        kp_finance.add_keyword(i)
    kp_finance = kp_finance.extract_keywords(words)
    kp_finance = np.unique(kp_finance)
    kp_finance = list(kp_finance)
    
    kp_fitness = KeywordProcessor()
    for i in fitness:
        kp_fitness.add_keyword(i)
    kp_fitness = kp_fitness.extract_keywords(words)
    kp_fitness = np.unique(kp_fitness)
    kp_fitness = list(kp_fitness)
    
    kp_travel = KeywordProcessor()
    for i in travel:
        kp_travel.add_keyword(i)
    kp_travel = kp_travel.extract_keywords(words)
    kp_travel = np.unique(kp_travel)
    kp_travel = list(kp_travel)
    
    kp_business = KeywordProcessor()
    for i in business:
        kp_business.add_keyword(i)
    kp_business = kp_business.extract_keywords(words)
    kp_business = np.unique(kp_business)
    kp_business = list(kp_business)
    
    kp_government = KeywordProcessor()
    for i in government:
        kp_government.add_keyword(i)
    kp_government = kp_government.extract_keywords(words)
    kp_government = np.unique(kp_government)
    kp_government = list(kp_government)
    
    kp_politics = KeywordProcessor()
    for i in politics:
        kp_politics.add_keyword(i)
    kp_politics = kp_politics.extract_keywords(words)
    kp_politics = np.unique(kp_politics)
    kp_politics = list(kp_politics)
    
    def findmaxlength(lst):
        maxlist = max(lst, key=len)
        return maxlist
    
    category_list = [kp_sports,kp_entertainment,kp_health_care,kp_restaurant,kp_m_learning,kp_real_estate,kp_finance,kp_fitness,kp_travel,kp_business,kp_government,kp_politics]
    max_category_list = findmaxlength(category_list)
    
    lst.append(max_category_list)
    print(max_category_list)
    
    if max_category_list == kp_sports:
        category = 'sports'
    elif max_category_list == kp_entertainment:
        category = 'entertainment'
    elif max_category_list == kp_health_care:
        category = 'health care'
    elif max_category_list == kp_restaurant:
        category = 'restaurant'
    elif max_category_list == kp_m_learning:
        category = 'm learning'
    elif max_category_list == kp_real_estate:
        category = 'real_estate'
    elif max_category_list == kp_finance:
        category = 'finance'
    elif max_category_list == kp_fitness:
        category = 'fitness'
    elif max_category_list == kp_travel:
        category = 'travel'
    elif max_category_list == kp_business:
        category = 'business'
    elif max_category_list == kp_government:
        category = 'government'
    elif max_category_list == kp_politics:
        category = 'politics'
    
    lst.append(category)
    list_of_lists.append(lst)
    
    print(list_of_lists)
    print()
    print("The category of ",url,"is ",category)
url = input()
url_predictor(url)

