from extract import readpdf
from clean import cleaned_text
from excel import save_excel

text =readpdf("data1.pdf") #read and extract text from pdf

cleaned=cleaned_text(text)# cleaned the text
print (type(cleaned))
save_excel(cleaned,"output.xlsx") #created into excel

print ("Done!!! output created")


