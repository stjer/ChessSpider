from selenium import webdriver
from random import randrange
from time import sleep
from selenium.webdriver.common.by import By


def randsleep():
    """
    Delay execution with 2 to 3 seconds.
    """
    sleep(randrange(2,4))

def review(nickname, driver, page_nr, last_page_nr):
    while page_nr <= last_page_nr :
    
        print(f"Crawling page number {page_nr}...")
        driver.get(f"https://www.chess.com/games/archive/"+nickname+"?gameOwner=other_game&gameType=live&page="+str(page_nr))
        overview_tab = driver.current_window_handle
        games = driver.find_elements(By.XPATH, '//a[contains(@class,"archive-games-link") and contains(text(), "리뷰")]')#'리뷰'is korean, so if you use another language, you need to change it 'review' on your language. 
        if len(games) > 0:
            print (f"Begin analysing {len(games)} games...")
            for idx, game in enumerate(games):
                game_url = game.get_attribute('href')
                driver.switch_to.new_window('tab')
                driver.get(game_url)
                randsleep()
                sleep(6)# if you need more wait for analyze.
                driver.close()
                print(f"Analysed game {idx + 1}: {game_url}")
                #ancount+=1
                sleep(1)
                #randsleep()
                driver.switch_to.window(overview_tab)
                         
        else:
            print("No games found on the current page.")
        page_nr = page_nr + 1
        sleep(1)
        #randsleep()
    print("Analysis complete.")

def tryint():
    try : 
        a = int(input())
        if a>=1:
            return a
        elif a< 1:
            return a
        #just check is it number.
    except: 
        print("input number.")
        a = tryint()
        return a

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.chess.com/login") # after login, input nickname.
#if you can't login cause you just use google account, you can make password on chess.com's setting and login with it.


count = 1
while count >= 1:
    print("nickname : ")# who's nickname you want to analyze
    nickname = input()
    driver.get(f"https://www.chess.com/games/archive/"+nickname+"?gameOwner=other_game&gameType=live&page=1")
    # see how many games are and divide it 50 to get last page number.
    print("start page number : ")
    page_nr = tryint()
    print("end page number : ")
    last_page_nr = tryint()
    
    review(nickname, driver, page_nr, last_page_nr)
    print("If you want to continue, input number 1 or more.")
    count = tryint()

#ancount = 0
input()
