# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import cgi
import re

form="""
<form method="post">
	<b>Sign up</b>
	<br>
	<br>
	<label> Username
		<input type"text" name="username" value="%(username)s">
	</label>
	<div style="color: red">%(error_username)s</div>
	<br>
	<label> Password
		<input type"text" name="password" value="%(password)s">
	</label>
	<div style="color: red">%(error_password)s</div>
	<br>
	<label> Verify Password
		<input type"text" name="verify" value="%(verify)s">
	</label>
	<div style="color: red">%(error_verify)s</div>
	<br>
	<label> Email(optional)
		<input type"text" name="email" value="%(email)s">
	</label>
	<div style="color: red">%(error_email)s</div>
	<br>
	<br>
	<input type="submit">
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if month.capitalize() in months:
        return month.capitalize()
    else:
        return None

def valid_day(day):
    if day and day.isdigit():
        if 0 < int(day) < 32:
            return int(day)

def valid_year(year):
    if year and year.isdigit():
        if 1900 < int(year) <2020:
            return int(year)
def escape_html(s):
	return cgi.escape(s, quote=True)

def valid_username(username):
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	return USER_RE.match(username)

def valid_password(password):
	if password:
		return True

def valid_verify(password1, password2):
	if password1 == password2:
		return True
	else:
		False
	

def valid_email(email):
	if "@" in email:
		if ".com" in email.split("@")[1]:
			return True


class MainPage(webapp2.RequestHandler):
	def write_form(self, error_username="", error_password="",
		           error_verify="", error_email="",
		           username="", password="", verify="", email=""):
		self.response.out.write(form % {"error_username": error_username,
										"error_password": error_password,
										"error_verify": error_verify,
										"error_email": error_email,
										"username": escape_html(username),
										"password": escape_html(password),
										"verify": escape_html(verify),
										"email": escape_html(email)})

	def get(self):
		self.write_form()

	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')

		# validate answers

		username = valid_username(user_username)
		if username:
			error_username = ""
		else:
			error_username = "That's not a valid username"
		password = valid_password(user_password)
		if password:
			error_password = ""
		else:
			error_password = "Your wasn't a valid password"
		# set passwords to empty in case there is an error
		user_password = ""
		user_verify = ""
		verify = valid_verify(user_password, user_verify)
		if verify:
			error_verify = ""
		else:
			error_verify = "Your passwords didn't match"
		if user_email:
			email = valid_email(user_email)
			if email:
				error_email = ""
			else:
				error_email = "That's not a valid email"
		else:
			user_email = ""
			email = True


		if not (username and password and verify and email):
			self.write_form(error_username,
							error_password,
							error_verify,
							error_email,
				            user_username,
				            user_password,
				            user_verify,
				            user_email
				            )
		else:
			self.redirect("/welcome")

class WelcomeHandler(webapp2.RequestHandler):
	def get(self, Username):
		self.response.out.write("Welcome %s!" %username)

app = webapp2.WSGIApplication([('/', MainPage),
							   ('/welcome', WelcomeHandler)], debug=True)

