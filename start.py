import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 0.5
driver = webdriver.Chrome()
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')

vice_url = 'https://www.youtube.com/watch?v=pIVG3mDL9RI&ab_channel=MangaVEVO' # Url

try:
    driver.get(vice_url)
    time.sleep(5)
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(3)
    kac_yorum_var = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/h2/yt-formatted-string/span[1]').text
    #. var ise sil
    kac_yorum_var = kac_yorum_var.replace(".", "")
    log('Toplam ' + kac_yorum_var + ' yorum var.')
    for i in range(int(kac_yorum_var)):
        try:
            yorum = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[' + str(i) + ']/ytd-comment-renderer/div[3]/div[2]/ytd-expander/div').text
            yorum_sahibi = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[' + str(i) + ']/ytd-comment-renderer/div[3]/div[2]/div/div[2]/h3/a/span').text
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            log('Sahibi: ' + yorum_sahibi + ' Yorum: ' + yorum)
            #yorum boş ise geç
            if yorum == "":
                continue
            yorum_file.write('Sahibi: ' + yorum_sahibi + ' Yorum: ' + yorum + '\n')
            html = driver.find_element_by_tag_name('html')
            html.send_keys(Keys.END)
            time.sleep(global_delay)
        except:
            continue
except Exception as e:
    log('Hata: ' + str(e))
    log('Program sonlandı')
    driver.quit()
    exit()
