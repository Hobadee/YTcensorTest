#!/usr/local/bin/python3

#
# Requirements:
# pip3 install requests htmldom
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
