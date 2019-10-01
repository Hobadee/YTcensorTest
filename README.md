# YTcensorTest
Checks for search result censorship on YouTube by running a search query and reporting the results.  Compare with other queries/locations/etc.

This is currently a very quick and dirty script to help Louder with Crowder.  This can be flushed out a fair bit.

Todo:

- Take search parameter as argument
- Store result items as objects, especially so that we can...
- ...Output to a CSV or other useful formats
- Do more than 1 page of search.  (We currently get just 19 results.)

Ideally we would set this up in some docker container or something and phone home with results, then spin up a bunch of containers globally and compare results
