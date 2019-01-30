from config import *
from robobrowser import RoboBrowser

browser = RoboBrowser(parser="html.parser")
browser.open(SPEED_TEST_WEB)
form = browser.get_form(id="ps")
print(form)
form['v'] = '4'
form['host'] = 'game-a.granbluefantasy.jp'
print(form['area[]'].options)
form['area[]'].value = ['china', 'hmt', 'asia']
form['a'] = 'send'
browser.session.headers['Referer'] = SPEED_TEST_WEB
browser.submit_form(form)
src = str(browser.parsed)
print(src)