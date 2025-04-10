
def extract_title(markdown:str)->str:
    '''
    Reads markdown formatted string and extracts its h1 header (line staring with "# ")
    '''
    h1_headers = list(
        filter( lambda line: line[:2]=="# ", markdown.split("\n"))
    )

    if not h1_headers:
        raise(Exception("could not find any lines staring with '# '"))

    h1 = h1_headers[0][1:].strip()
    return h1
