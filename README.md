# request_books

Automated tool to make books (light novels or manga) requests on learnnatively.com

# How to use

1. Clone this repo (or download it as a zip, then extract it)
2. Run `pip3 install selenium pynput`
3. Download the `geckodriver` either from your package manager or from https://github.com/mozilla/geckodriver/releases
4. Create a file called `titles.txt` and write in there all of your books (the format must be like these `のうりん;ln`; the
   first parameter (the one before `;`) is the Japanese name of the book), the second is the type (ln -> light novel, m
   -> manga); add a new line like the example for every book you want to request
5. Create a file called `cred.txt` and write down your Natively account's email and password (be sure to not share that
   file, delete it after you used this program)
6. Run `python3 main.py`
7. Answer the question the program asks you (as of now, either answering yes or no doesn't change anything)
8. Now the program will check if are there already those books on Natively, it can check autonomously if and only if the
   search yields no result else the user should answer for the program; press the Esc key if there **is** the book you
   were searching; press the Space key if there **isn't** the book you were searching (you can check the title of the
   book the program is currently checking in the search box)
9. After checking which books the program should then request, it will start opening Amazon JP pages; those pages are
   search results for the book were looking for; if you can find it, go on the product page of that book and then press
   the Space key; if you can't find anything click the Esc key
10. After that step, now comes the really autonomous part of process, you can now go and take a sip of coffee whilst the
    program is requesting the books