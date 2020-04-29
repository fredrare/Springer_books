# Springer_books
Get free books from springer for a given category
# Usage
## Out of the box
You can use this command to run the script
```bash
./books.py list.json output
```
This way, the books from the categories you select will be downloaded in
the output folder. books.json contains a list of books grouped by
category. *Please keep in mind that all the books from the selected category are downloaded and the download speed is very low.*
## Customization
If you want to modify the json for the books list, you can do it from a
.csv file. Just use the jsongen.py and give the appropriate parameters
(you can check the code for that.
## Comments
If you would like to contribute to this code, just message me. It would
be good to have some kind of search engine or multiprocessing embedded.
I have tried multiprocessing, but I get scrambled results, so I did not
continue further improving the script.

