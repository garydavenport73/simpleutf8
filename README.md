simpleutf8.py

A python script that generates UTF-8 Unicode Tables

Gary Davenport
2/4/2021

This is a python script to generate ut-8 codeblock charts.
It works reasonably well for its purpose.
It was tested in Python 3.8.6 64-bit.

I mainly made this so I could inspect characters
for video games and ther uses by visually scanning through
single condensed text file containing utf-8 characters.


It opens ok for me in notepad, but the output file is 
299kb and 5120 lines long.

If the file is too large, you can change the numbers 
in the range(2,4096) to different starting/ending numbers.

Input-none

Output-a text file that writes to the current directory
of the simpleutf8.py file.  

The output file is named simpleutf8out.txt

There is a copy of that output file in this github repository.

Output can be checked against the website:
https://www.ssec.wisc.edu/~tomw/java/unicode.html 

