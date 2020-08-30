import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier


DATE_TIME = "date/time"
DATA_URL = ('https://raw.githubusercontent.com/diegojeda/test-penguin/master/BLCat.csv')

st.title("Dashboard Para Visualizacion de Datos")
st.markdown("""Esta aplicacion le permite visualizar los datos de performance de las brocas de su campo""")


@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data=load_data() 

 
dic_uni = {'ROP' : ' (ft/hr)',
            'Footage':' (ft)',
            'Min Flow Rate' : ' (GPM)',
            'Blades' : ' (#)',
            'Cutter size' : ' (mm)',
            'Max Flow Rate' : '(GPM)',
            'TFA' : '(in2)',
            'HSI' : ' (HP/in2)',
            'Min WOB' : ' (Klb)',
            'Max WOB' : ' (Klb)',
            'Mud Weight' : '( ppg)',
            'Min_RPM' : ' (rev per min)',
            'Max_RPM' : ' (rev per min)',
            'Torque Min' : '( klb-ft)',
            'Torque Max' : '( klb-ft)'
            }

 # Definimos la Sidebar

st.sidebar.title("Seleccione Los Parametros De Su Grafica")

z = st.sidebar.selectbox(
    'Parametro a Optimizar',
    ('ROP','Footage')
    )

x = st.sidebar.selectbox(
    'Eje X',
    ('Min Flow Rate','Blades','Cutter size','Max Flow Rate','TFA',
    'HSI','Min WOB','Max WOB','Mud Weight','Min_RPM','Max_RPM',
    'Torque Min','Torque Max')
    )

y = st.sidebar.selectbox(
    'Eje Y',
    ('Min WOB','Blades','Cutter size','Min Flow Rate','Max Flow Rate','TFA',
    'HSI','Max WOB','Mud Weight','Min_RPM','Max_RPM',
    'Torque Min','Torque Max')
    )

SB_Size = st.sidebar.selectbox(
    'Tamaño de la Broca (in)',
    ('All','6.0','8.5', '10.625', '14.75', '18.5', "26.0", "36.0")
    )
    
SB_Type = st.sidebar.selectbox(
    'Tipo de Broca)',
    ('All','PDC', 'Tricone', 'Hybrid', 'Impregnated')
    )
   
SB_Structure = st.sidebar.selectbox(
    'Structure',
    ('All','Anticlinal N', 'Anticlinal M', 'Anticlinal F', 'Anticlinal P', 'Imbricate',
    'Anticlinal G', 'Anticlinal D')
    )

SB_Formation = st.sidebar.selectbox(
    'Formation',
    ('All','Colluvium','Guayabo', 'Charte', 'Leon','C1', 'C2', 'C3', 'C4','C5', 'C6', 'C7', 'C8','Sltn Market', 'Mirador', 'Los Cuervos', 'Barco', 'Guadalupe',
    'Guad. Shale', 'Guad. Upper', 'Gacheta')
    )
    
if (SB_Size!='All'):
    if (SB_Type!='All'):
        if(SB_Structure!='All'):
            if(SB_Formation!='All'):#Filtre Size, Type, Estructura y Formation
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Type==SB_Type)&(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
            else: # Filtre Size, Type y Estructura
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Type==SB_Type)&(data.Structure==SB_Structure)]
        else:
            if(SB_Formation!='All'): #Filtre Size, Type y Formation
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Type==SB_Type)&(data.Formation==SB_Formation)]
            else: # Filtre Size Type
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Type==SB_Type)]
    else:
        if(SB_Structure!='All'):
            if(SB_Formation!='All'):#Filtre Size, Estructura y Formation
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
            else:#Filtre Size y Estructura
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Structure==SB_Structure)]
        else:
            if(SB_Formation!='All'):#Filtre Size y Formation
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)&(data.Formation==SB_Formation)]
            else:#Filtre Size
                SB_Size = float(SB_Size)
                data=data.loc[(data.Size==SB_Size)]   
else: # Quitando Size
    if (SB_Type!='All'):
        if(SB_Structure!='All'):
            if(SB_Formation!='All'):#Filtre Type, Estructura y Formation
                data=data.loc[(data.Type==SB_Type)&(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
            else: # Filtre Type y Estructura
                data=data.loc[(data.Type==SB_Type)&(data.Structure==SB_Structure)]
        else:
            if(SB_Formation!='All'): #Filtre Type y Formation
                data=data.loc[(data.Type==SB_Type)&(data.Formation==SB_Formation)]
            else: # Filtre Type
                data=data.loc[(data.Type==SB_Type)]
    else:
        if(SB_Structure!='All'):
            if(SB_Formation!='All'):#Filtre Estructura y Formation
                data=data.loc[(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
            else:#Filtre Estructura
                data=data.loc[(data.Structure==SB_Structure)]
        else:
            if(SB_Formation!='All'):#Filtre Formation
                data=data.loc[(data.Formation==SB_Formation)]
            else:#Sin Filtro
                data=data             

st.dataframe(data,2000,150)

