

class homePage():

    def __init__(self,page):
      print('into init')
      self.page = page




    def click_on_login_button(self):
      print('clicking on login button')
      login_button = self.page.locator("[id='login-button']")
      login_button.click()



    def set_user_and_password(self,user_text,password_text):
        print('Setting user and password')
        user = self.page.locator("[id='user-name']")
        password = self.page.locator("[name='password']")
        user.click()
        user.clear()
        user.type(user_text)
        # user.type("standard_user")
        password.click()
        password.clear()
        password.fill(password_text)
        # password.fill("secret_sauce")






