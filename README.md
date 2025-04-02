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

## Nodes
> Intermediate representations of the markdown text elements inside our code during markdown to html conversion. 

### TextNode

Represents all the different types of *inline* text. The `TextNode` is an intermediate representation of the text in the python code. Inline text is any text which is part of a larger block of text. I.e.,

- Normal text
- `**Bold text**`
- `_Italic text_`
- \``Code text`\`
- Links, in the `[anchor text](url)` format
- Images, in `![alt text](url)` format

Everything else is considered as a *block level*: e.g., headings, paragraphs, and bullet lists.

### HTMLNode

HTMLNode class represents a node in an HTML document tree, such as, `<p>` or `<a>` tags and their contents and can be either block-level of inline elements of the text. HTMLNode only outputs HTML.

### LeafNode

LeafNode is a type of HTMLNode. It is a leaf of HTML nodes with a single HTML tag with *no children*. E.g., a simple paragraph (tag `<p>` without any other nested tags):

```
<p>This is a paragraph.</p>
```

E.g., this paragraph is not a LeafNode:

```
<p> A paragraph with a <b>bold text</b>.</p>
```

where `<p>` is not a LeafNode. Here, the LeafNode is `<b>` tag.



