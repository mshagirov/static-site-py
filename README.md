# static-site-py
## Architecture of the Static Site Project

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

 Represents all the different types of *inline* text. The `TextNode` is an intermediate representation of the text in the python code. Inline text is any text which is part of a larger block of text. I.e.,

- Normal text
- `**Bold text**`
- `_Italic text_`
- \``Code text`\`
- Links, in the `[anchor text](url)` format
- Images, in `![alt text](url)` format

Everything is considered as a *block level*: e.g., headings, paragraphs, and bullet lists.
