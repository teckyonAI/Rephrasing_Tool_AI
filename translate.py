
from textblob import TextBlob
import pandas as pd
from fuzzywuzzy import fuzz



def preprocess(data):

    # f = open("file.txt", "r",encoding='utf-8')
    # file= f.read()
    # Convert paragragh into sentences
    lis = []
    lis = data.split('. ')
    # MAke a DataFrame
    data =pd.DataFrame(lis)
    data = data.rename(columns={0:'Real_Eng'})

    return data


def translate(df):
    # Convert English into urdu
    urdu = []
    for i in df.Real_Eng:
        blob = TextBlob(i)
        ur = str(blob.translate(to='ur'))
        urdu.append(ur)
    
    df['Urdu_text'] =pd.DataFrame(urdu)
    # Convert Urdu into English
    english = []
    for i in df.Urdu_text:
        blob = TextBlob(i)
        en = str(blob.translate(to='en'))
        english.append(en)
    
    df['Repharazing'] =pd.DataFrame(english)

    # Convert Again Predicted English into Urdu 
    pred_urdu = []
    for i in df.Repharazing:
        blob = TextBlob(i)
        pred_ur = str(blob.translate(to='ur'))
        pred_urdu.append(pred_ur)
    
    df['pred_urdu'] =pd.DataFrame(pred_urdu)

    return df , english
def ratio(df):
    df['Ratio']= [fuzz.ratio(a, b)  for a, b in zip(df['Urdu_text'],df['pred_urdu'])]
    df =df.drop(['Urdu_text','pred_urdu'],axis=1)
    

    return df

                 