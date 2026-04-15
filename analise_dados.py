import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(base_dir, "vinhos.csv")

db = pd.read_csv(caminho)

#Define amostra
amostra = db.sample(frac = 0.25, random_state = 42)

#Agrupa por coluna
grupo_amostra = amostra.groupby("grape_type") 

#Amplitude absoluta
amp_abs_amostra = grupo_amostra["volume_hl"].max() - grupo_amostra["volume_hl"].min() 

# Média amostra
media_amostra = grupo_amostra["volume_hl"].mean() 

#Amplitude relativa
amp_rel_amostra = (amp_abs_amostra / media_amostra)*100 

#Variância
variancia_amostra = grupo_amostra["volume_hl"].var(ddof=0) 

#Desvio padrão
desvio_amostra = grupo_amostra["volume_hl"].std(ddof=0)

#Monta os resultados em um dataframe
resultado_amostra = pd.DataFrame({ 
    "Amplitude Absoluta":amp_abs_amostra,
    "Amplitude Relativa":amp_rel_amostra,
    "Variância":amp_abs_amostra,
    "Desvio Padrão":amp_abs_amostra
})
print(resultado_amostra.round(2))