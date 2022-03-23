# selenium - launches and controls a web browser
# (able to fill in forms and simulate mouse clicks)

# Controlling the browser with the selenium module

from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))

browser.get('https://inventwithpython.com')

# WebDriver methods
# browser.find_element_by_class_name(name)
# browser.find_element_by_id(id)
# browser.find_element_by_tag_name(name)

# WebElement attributes and methods
# tag_name
# get_attribute(name)
# clean()
# is_display()
# click()

# Filling Out and Submitting Forms
# userElem = browser.find_element_by_id('user_name')
# userElem.send_keys('username')
# passwordElem.submit()

# Sending Special Keys
# Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
# Keys.ENTER, Keys.RETURN
# Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
# Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
# Keys.F1, Keys.F2, . . . , Keys.F12
# Keys.TAB

# htmlElem.send_keys(Keys.HOME)

# Clicking Browser Buttons
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()
