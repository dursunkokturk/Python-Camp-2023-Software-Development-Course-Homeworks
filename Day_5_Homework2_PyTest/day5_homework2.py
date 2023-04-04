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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class Test_Day5_Homework2:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_username_password_empty(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"")
        actions.send_keys_to_element(loginUserPasswordInput,"")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Username and Password is required"
        print(f"Test Result : {testResult}")
        errorIcon = self.driver.find_element(By.CLASS_NAME,"error-button")
        errorIcon.click()
        print(errorIcon)

    def test_password_empty(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"1")
        actions.send_keys_to_element(loginUserPasswordInput,"")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result : {testResult}")

    def test_locked_out_user(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"locked_out_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result : {testResult}")
    
    def test_valid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: invalid login."
        print(f"Test Result : {testResult}")

    def test_icon_click(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"1")
        actions.send_keys_to_element(loginUserPasswordInput,"1")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.CLASS_NAME,"error-button")
        print(errorMessage)
        testResult = errorMessage.text == "Epic sadface: Sorry, icon click."
        print(f"Test Result : {testResult}")

    def test_total_product_number(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        listOfProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Total Product Number {len(listOfProduct)}")

    def test_product_filter(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        listOfProduct = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Total Product Number {len(listOfProduct)}")

    def test_add_to_cart(self, username, password):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element((By.ID, "user-name"))
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID, "password")
        action = ActionChains(self.driver)
        action.send_keys_to_element(loginUserNameInput, username)
        action.send_keys_to_element(loginUserPasswordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def test_site_page_redirect(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,"standard_user")
        actions.send_keys_to_element(loginUserPasswordInput,"secret_sauce")
        actions.perform()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        
testClass = Test_Day5_Homework2()
testClass.test_username_password_empty()
testClass.test_password_empty()
testClass.test_locked_out_user()
testClass.test_add_to_cart()
testClass.test_icon_click()
testClass.test_product_filter()
testClass.test_total_product_number()
testClass.test_valid_login()
testClass.test_site_page_redirect()