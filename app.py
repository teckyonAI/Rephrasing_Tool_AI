
import streamlit as slt
import translate

if slt.checkbox("Text_File"):
    slt.sidebar.title("ZAINX Paraphrasing Tool ")
    uploaded_file = slt.sidebar.file_uploader("Choose a File")
    if uploaded_file is not None :
        lines=[]
        if uploaded_file:
            for line in uploaded_file:
                data = line.decode("utf-8")
                lines.append(data)
            
                data  =' '.join([str(elem) for elem in lines])
           
    
    
       
        if slt.sidebar.button("Rephrase File"):
            with slt.spinner("ZAINX.."):
           
                df = translate.preprocess(data)
                data1,english = translate.translate(df)
                #colu1 = slt.columns(1)
            
                #with colu1:
                slt.header("Need to Rephrase")
                slt.write(data)
                slt.header("Rephrased")
                eng=' '.join([str(elem) for elem in english])
                slt.write(eng)
                slt.download_button('Download some text', eng)
    
        if slt.sidebar.button("Result Accuracy"):
            with slt.spinner("ZAINX.."):
                df = translate.preprocess(data)
                data,english = translate.translate(df)
                ratio = translate.ratio(data)
                #slt.write(ratio)
                def color_survived(val):
                    color = 'lightgreen' if val >89   else 'lightpink'
                    return f'background-color: {color}'
                slt.header("Ratio of Matching")
                slt.dataframe(ratio.style.applymap(color_survived, subset=['Ratio']))
            
            

    

elif slt.checkbox("Only_Text"):
    slt.sidebar.title("ZAINX Paraphrasing Tool ")
    try:
        text_file = slt.text_area("English Text :",placeholder="Write here")
        
    
        if text_file is not None :
            if slt.sidebar.button("Rephrase Text"):
                with slt.spinner("ZAINX.."):
                
                    df = translate.preprocess(text_file)
                    
                    data1,english = translate.translate(df)
                    slt.header("Repharased")
                    eng=' '.join([str(elem) for elem in english])
                    slt.write(eng)
        
                    slt.download_button('Download some text', eng)
    
            if slt.sidebar.button("Result Accuracy"):
                with slt.spinner("ZAINX.."):
                     df = translate.preprocess(text_file)
                     data,english = translate.translate(df)
                     ratio = translate.ratio(data)
                     #slt.write(ratio)
                     def color_survived(val):
                        color = 'lightgreen' if val >89 else 'lightpink'
                        return f'background-color: {color}'
                     slt.header("Ratio of Matching")
                     slt.dataframe(ratio.style.applymap(color_survived, subset=['Ratio']))
    
    except ValueError:
        slt.error("Please enter a valid input")
       
        
