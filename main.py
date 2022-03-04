import pandas as pd
import numpy as np

def detectar_nulos(df):
    return df.isnull().sum()

def calcular_media(df):
    return df.mean()

def calcular_info(df):
    return df.info()
