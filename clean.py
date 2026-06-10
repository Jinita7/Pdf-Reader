def cleaned_text(all_text):
    sentence=all_text.split(".")
    
    final_sentence=[]
    for s in sentence:
        if s.strip():
            final_sentence.append(s) 
    return final_sentence    