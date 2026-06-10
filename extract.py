from pypdf import PdfReader
def readpdf(file_path):
    text =PdfReader(file_path)
    all_text=""

    for pages in text.pages:
    
       text1=pages.extract_text()
       if text1:
            all_text=all_text+text1

    return all_text    

