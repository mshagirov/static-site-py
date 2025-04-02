# static-site-py
## Architecture of the Project

```mermaid
%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart LR
    static["`**static/**
static assets, e.g.: images, CSS`"]
    
    src["`**src/**
Python code: the static site generator. Creates all the stuff in the public directory`"]

    content["`**content/**
Markdown files`"]

    templatehtml[\"`**template.html**`"\]
    
    public["`**public/**
The output directory for
python3 src/main.py
removes all files and generates the new ones. Contains the final HTML and CSS`"]
    
    fileserver(["`**File Server**
python3 -m http.server 8888
Serves the public files for to the browser`"])
    browser(["`**browser**
Renders the HTML and CSS`"])

static --> public
src --> public
content --> src
templatehtml --> src

public --> fileserver
fileserver --> public
fileserver --> browser
browser --> fileserver
```

## TextNode

