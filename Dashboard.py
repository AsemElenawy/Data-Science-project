import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")
df=pd.read_csv("data2.csv")
colors=['darkorange','lightblue','darkgreen','darkblue','lightgreen']
# st.write(df.head(5))
# cols = st.columns(2)
# with cols[0]:
#    option = st.radio("Select an option",["Gender","Race","Parental Level of education","Lunch","Test partcipation"])

# with cols[1]:
#     if option=="Gender":
#         sns.countplot(data=df, x=features[0])
#         plt.tight_layout()
#         plt.show()
#         st.pyplot(fig1)
#     elif option=="Race":
#         sns.countplot(data=df, x=features[1])
#         plt.tight_layout()
#         plt.show()
#         st.pyplot(fig1)
#     elif option=="Parental Level of education":
#         sns.countplot(data=df, x=features[2])
#         plt.tight_layout()
#         plt.show()
#         st.pyplot(fig1)
#     elif option=="Lunch":
#         sns.countplot(data=df, x=features[3])
#         plt.tight_layout()
#         plt.show()
#         st.pyplot(fig1)
#     elif option=="Test partcipation":
#         sns.countplot(data=df, x=features[4])
#         plt.tight_layout()
#         plt.show()
#         st.pyplot(fig1)
sidebar, main1,main2  = st.columns([1,2,2])
# Sidebar column
with sidebar:
    st.title('Your selection')
    st.write("Univariate")
    option1 = st.selectbox('Select Option', ["Gender","Race","Parental Level of education","Lunch","Test partcipation","Math score","Reading score","Writing score"])
    st.write("Bivarite")
    #option2= st.selectbox('Select Option',["Gender","Race","Parental Level of education","Lunch","Test partcipation"])
    option2=st.selectbox('Select Option',["Maths score","Reading score","Wrting Score"])

# Main content column
with main1:
    features=df.columns
    fig1, axes1 = plt.subplots(figsize=(8,6))
    st.title("Univariate")
    if option1=="Gender":
        op1=0
    elif option1=="Race":
        op1=1
    elif option1=="Parental Level of education":
        op1=2
    elif option1=="Lunch":
        op1=3
    elif option1=="Test partcipation":
        op1=4
    elif option1=="Math score":
        op1=5
    elif option1=="Reading score":
        op1=6
    elif option1=="Writing score":
        op1=7
    if(op1<5):
        sns.countplot(data=df, x=features[op1])
    else:
        sns.histplot(data=df, x=features[op1], color='skyblue')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig1)
with main2:
    st.title("Bivariate")
    if option2=="Maths score":
        op2="math score"
    elif option2=="Reading score":
        op2="reading score"
    elif option2=="Wrting Score":
        op2="writing score"
    #removing outliers
    df=df[df['reading score']>=29]
    df=df[df['writing score']>=20]
    df=df[df['math score']>=18]
    features=df.columns
    fig2, axes1 = plt.subplots(figsize=(8, 6))
    if(op1<5):
        df.groupby(features[op1])[op2].mean().plot(kind='bar', color=colors)
    else:
        sns.scatterplot(data=df, x=features[op1],y=op2 , color='skyblue')
    axes1.set_ylabel(option2) 
    plt.tight_layout()
    plt.show()
    st.pyplot(fig2)
st.title("Your input for maths score prediction")
feature1=st.selectbox("gender", ["male", "female"])
if feature1 == "male":
    x1=0
else:
    x1=1
feature2=st.selectbox("race", ["group a", "group b","group c","group d","group e"])
if feature2 == "group a":
    x2=1
    x3=0
    x4=1
elif feature2 == "group b":
    x2=0
    x3=1
    x4=1
elif feature2 == "group c":
    x2=0
    x3=0
    x4=1
elif feature2 == "group d":
    x2=0
    x3=1
    x4=0
elif feature2 == "group e":
    x2=1
    x3=0
    x4=0    

feature3=st.selectbox("parental level of education", ["some high school", "high school","some college","associate's degree","bachelor's degree","master's degree"])
if feature3 == "some high school":
    x5=1
elif feature3 == "high school":
    x5=2   
elif feature3 == "some college":
    x5=3
elif feature3 == "associate's degree":
    x5=4 
elif feature3 == "master's degree":
    x5=5    
feature4=st.selectbox("lunch" ,["free/reduced","standard"])
if feature4 == "free/reduced":
    x6=1
if feature4 == "standard":
    x6=0   
feature5=st.selectbox("test preparation course" ,["completed","none"])
if feature5 == "completed":
    x7=1
if feature5 == "none":
    x7=0    

feature6=st.number_input("your reading score",0,100)
x8= (feature6-30)/(70)
feature7=st.number_input("Your writing score",0,100)
x9=(feature7-26)/(74)
model=37.580725982633666 + -12.852 * x1 + 2.212 * x2 + -0.389 * x3 + -1.171 * x4 + 0.047 * x5 + -4.278 * x6 + -4.119 * x7 + 18.615 * x8 + 49.858 * x9

if model < 0 :
   model=0
if model > 100 :
   model=100    

st.header("your predicted score is :")
st.header (int(model))


st.progress(int(model))

    

