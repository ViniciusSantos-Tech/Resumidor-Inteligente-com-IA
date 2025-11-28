#𝗙𝗲𝗶𝘁𝗼 𝗽𝗼𝗿 𝗩𝗶𝗻𝗶𝗰𝗶𝘂𝘀 𝗦𝗮𝗻𝘁𝗼𝘀-𝗧𝗲𝗰𝗵
#𝐑𝐄𝐒𝐔𝐌𝐈𝐃𝐎𝐑-𝐈𝐍𝐓𝐄𝐋𝐈𝐆𝐄𝐍𝐓𝐄-𝐂𝐎𝐌-𝐈𝐀

import pandas as pd
from openai import OpenAI
import streamlit as st


def Ler_arquivo(arquivo):
    while True:
        try:

            arquivo1 = pd.read_csv(arquivo)
            print("Carregando...")
            conteudo_arquivo = arquivo1.to_string()
            client = OpenAI(api_key=''#sua_chave_aqui!!!!!!!')
            resposta = client.responses.create(
                model="gpt-4o-mini",
                instructions='Voce apenas ira Resumir bem Todos os arquivos que forem recebidos, e sem usar "*" para destacar..',
                input=conteudo_arquivo
            )
            st.write(resposta.output_text)
            break
        except Exception as e:
            print(e)

st.title("RESUMIDOR DE ARQUIVOS CSV!")
st.subheader("Ferramenta automatica para fazer descriçoes de arquivos csv", divider='blue')
arquivo_carregado = st.file_uploader("Clique no botao para importar o seu arquivo csv", type=['csv'])

if arquivo_carregado is not None:

    st.success("Arquivo carregado com sucesso!")
    Ler_arquivo(arquivo_carregado)
