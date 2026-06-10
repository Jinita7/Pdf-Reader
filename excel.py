import pandas as pd 

def save_excel(final_sentence,file_name="output.xlsx"):
     data=pd.DataFrame(final_sentence,columns=["english"])
     data.to_excel(file_name,index=False)