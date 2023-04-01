from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
from typing import Literal

class Test_Demo:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")])
    def test_username_password_empty(self, username: Literal[''], password: Literal['']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()
        
        self.waitForElementVisible((By.ID, "login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-login-username-password-empty-{username}-{password}.png")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and Password is required"
    
    @pytest.mark.parametrize("username,password",[("standard_user","")])
    def test_password_empty(self, username: Literal['standard_user'], password: Literal['']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        loginUserNameInput.send_keys(username)
        loginUserPasswordInput.send_keys(password)
        # actions = ActionChains(self.driver)
        # actions.send_keys_to_element(loginUserNameInput,username)
        # actions.send_keys_to_element(loginUserPasswordInput,password)
        # actions.perform()
        
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-login-password-empty-{username}-{password}.png")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage)
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_out_user(self, username: Literal['locked_out_user'], password: Literal['secret_sauce']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()
        
        self.waitForElementVisible(By.ID,"login-button")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-login-locked-user-{username}-{password}.png")

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_login(self, username: Literal["standard_user"], password: Literal["secret_sauce"]):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")

    @pytest.mark.parametrize("username,password",[("1","1")])
    def test_icon_click(self, username: Literal['1'], password: Literal['1']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-icon-click-{username}-{password}.png")

        errorIconButton = self.driver.find_element(By.CLASS_NAME,"error-button")
        errorIconButton.click()

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_site_page_redirect(self, username: Literal['standard_user'], password: Literal['secret_sauce']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-inventory-{username}-{password}.png")
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_product_number(self, username: Literal['standard_user'], password: Literal['secret_sauce']):
        self.waitForElementVisible((By.ID,"user-name"))
        loginUserNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        loginUserPasswordInput = self.driver.find_element(By.ID,"password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(loginUserNameInput,username)
        actions.send_keys_to_element(loginUserPasswordInput,password)
        actions.perform()

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        productNumber = self.driver.find_elements("inventory-item")
        self.driver.save_screenshot(f"{self.folderPath}/test-inventory-{username}-{password}.png")
        assert len(productNumber) == 6
    
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_product_filter(self, username: Literal['standard_user'], password: Literal['secret_sauce']):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(userNameInput, username)
        action.send_keys_to_element(passwordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()
        filtrele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
        filtrele.click()
        filtrele2 = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")
        self.driver.save_screenshot(f"{self.folderPath}/test-filter.png")
        filtrele2.click()

    # sepete urun ekleme ve sepete gitme senaryosu
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
    def test_add_to_cart(self, username: Literal['standard_user'], password: Literal['secret_sauce']):
        self.waitForElementVisible((By.ID, "user-name"))
        loginUserNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        loginUserPasswordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(loginUserNameInput, username)
        action.send_keys_to_element(loginUserPasswordInput, password)
        action.perform()
        logIn = self.driver.find_element(By.ID, "login-button")
        logIn.click()

        addToCart = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        addToCart.click()
        goToCart = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        goToCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-to-cart.png")

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))