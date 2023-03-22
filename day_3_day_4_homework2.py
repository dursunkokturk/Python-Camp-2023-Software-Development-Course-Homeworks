# ÖDEV TANIMI:

# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. 
# Bu classın fonksiyonlarını çağırarak test ediniz.

# Test Caseler;

##     Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak 
##     "Epic sadface: Username is required" gösterilmelidir.

##     Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak 
##     "Epic sadface: Password is required" gösterilmelidir.

##     Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
##     "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

##     Kullanıcı adı ve şifre alanları boş geçildiğinde 
##     bu iki inputun yaninda da kirmizi "X" ikonu cikmalidir. 
##     Daha sonra asagida çikan uyari mesajinin kapatma butonuna tiklandiginda 
##     bu "X" ikonlari kaybolmalidir. (Tek test casede işleyiniz)

##     Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde 
##     kullanıcı "/inventory.html" sayfasına gönderilmelidir.

##     Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Day4_Homework2:
    def test_username_password_empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        loginUserNameInput = driver.find_element(By.ID,"user-name")
        loginUserPasswordInput = driver.find_element(By.ID,"password")
        sleep(2)
        loginUserNameInput.send_keys("")
        loginUserPasswordInput.send_keys("")
        sleep(10)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and Password is required"
        print(f"Test Result : {testResult}")
        sleep(10)
        errorIcon = driver.find_element(By.CLASS_NAME,"error-button")
        errorIcon.click()
        sleep(5)
        print(errorIcon)
        sleep(10)

    def test_password_empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        loginUserNameInput = driver.find_element(By.ID,"user-name")
        loginUserPasswordInput = driver.find_element(By.ID,"password")
        sleep(2)
        loginUserNameInput.send_keys("1")
        loginUserPasswordInput.send_keys("")
        sleep(10)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result : {testResult}")
        sleep(10)

    def test_locked_out_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        loginUserNameInput = driver.find_element(By.ID,"user-name")
        loginUserPasswordInput = driver.find_element(By.ID,"password")
        sleep(2)
        loginUserNameInput.send_keys("locked_out_user")
        loginUserPasswordInput.send_keys("secret_sauce")
        sleep(10)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(10)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result : {testResult}")
        sleep(10)
    
    def test_site_page_redirect(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        loginUserNameInput = driver.find_element(By.ID,"user-name")
        loginUserPasswordInput = driver.find_element(By.ID,"password")
        sleep(2)
        loginUserNameInput.send_keys("standard_user")
        loginUserPasswordInput.send_keys("secret_sauce")
        sleep(10)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(30)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(10)
        listOfProduct = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Total Product Number {len(listOfProduct)}")

testClass = Test_Day4_Homework2()
testClass.test_username_password_empty()
testClass.test_password_empty()
testClass.test_locked_out_user()
testClass.test_site_page_redirect()