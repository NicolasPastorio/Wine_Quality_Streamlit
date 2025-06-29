import pandas as pd

def load_and_process_data(file_path):
    df = pd.read_csv(file_path, sep=';', encoding='utf-8')

    # Tradução dos nomes das colunas
    column_translation = {
        'fixed acidity': 'acidez fixa',
        'volatile acidity': 'acidez volátil',
        'citric acid': 'ácido cítrico',
        'residual sugar': 'açúcar residual',
        'chlorides': 'cloretos',
        'free sulfur dioxide': 'dióxido de enxofre livre',
        'total sulfur dioxide': 'dióxido de enxofre total',
        'density': 'densidade',
        'pH': 'pH',
        'sulphates': 'sulfatos',
        'alcohol': 'álcool',
        'quality': 'qualidade'
    }

    df.rename(columns=column_translation, inplace=True)
    return df