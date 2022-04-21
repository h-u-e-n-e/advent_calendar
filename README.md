---
The app expects images in the following locations.

Full images:  
src/static/images/full

Thumbnails:  
src/static/images/thumb

Numbers 1-24  
src/static/images/numbers


To keep users from just guessing URLs, I recommend using random strings for the filenames, that's what the sqlite DB 'advent.db' is for, just create it with a table 'images', that looks like this for example:  
1|IJKCrugLkxMNyNvc29WN8  
2|lVSBrIBkvEj6x9r45AFi4

