#!/usr/local/bin/python3


#
# YTcensorTest
# Copyright (C) 2019

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import requests
import html
from htmldom import htmldom

CURLURL = 'https://www.youtube.com/results'
CURLparams = (
	('search_query', 'louder with crowder change my mind'),
)


r = requests.get(CURLURL, params=CURLparams)
html_string = r.text

dom = htmldom.HtmlDom().createDom(html_string)

# Find the results section of the DOM
results = dom.find("div[id=results]")
if (results.length() != 1):
	raise LookupError('Error fetching results!')

# Split the results into individual items
#results = results.find("li").has("div[data-context-item-id]")
results = results.find("ol[class=item-section] > li")

#print(results.html())
#exit()

i = 1
# Iterate the individual items
for result in results:
	print("Listing: ",i)
	if(result.find("div").attr("data-context-item-id") != "Undefined Attribute"):
		# Extract the video ID
		id = result.find("div").attr("data-context-item-id")
		
		# Extract the video title
		title = result.find("h3[class=yt-lockup-title]").find("a").text()
		
		# Extract the video channel
		channel = result.find("div[class=yt-lockup-byline]").find("a").text()
		
		# Print the results.
		print("ID: ",id)
		print("Title: ",html.unescape(title))
		print("Channel: ",html.unescape(channel))
	else:
		print("Non-Video Listing")

	print()
	i = i + 1
