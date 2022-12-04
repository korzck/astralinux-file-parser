# Astralinux file parser
This parser prints giant repo tree from dl.astralinux.ru/astra/ and calculates its size. The `size.py` makes size calculation and `main.py` parses and downloads folders tree and all the files.
#### reuirements.txt
```
requests
bs4
lxml
urllib.request
```
Also it needs `wkhtmltopdf` to run, so for less painful installation don't use win :)
Size calculation example

![](https://github.com/korzck/astralinux_file_parser/blob/main/code.gif)

To change loading directory you need to change `ulr` variable in `main.py` to correct path
