# Prompter

## Introduction

Web page to upload a text file. Shows each line of the file waiting certain
time (num_chars * 0.22 + 1.5) and then shows the next one.

Shows "Line X of Y", can Pause and Resume. If closing the browser: can Resume
from the last one.

Implemented using https://pyscript.net/

## Usage

Deploy into a webserver so and browse the file `index.html` . It needs to be
deployed so the browsers can fetch the required JavaScript scripts from
https:// (instead of opening index.html locally).

It can use Python's simple HTTP server, e.g.:

```
$ python3 -m http.server -d src/
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

And use your favourite browse to load http://0.0.0.0:8000

## Author information

Carles Pina i Estany <carles@pina.cat>
