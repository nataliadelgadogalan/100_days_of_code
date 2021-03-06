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

form="""
<form method="post">
	What is your birthday?
	<br>
	<label> Month
		<input type"text" name="month" value="%(month)s">
	</label>
	<label> Day
		<input type"text" name="day" value="%(day)s">
	</label>
	<label> Year
		<input type"text" name="year" value="%(year)s">
	</label>
	<div style="color: red">%(error)s</div>
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

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error,
										"month": month,
										"day": day,
										"year": year})

	def get(self):
		self.write_form()

	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)

		if not (month and day and year):
			self.write_form("Uups, that doesnt look like a valid date",
				            user_month,
				            user_day,
				            user_year
				            )
		else:
			self.response.out.write("Thanks!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)