import pandas as pd
from openai import OpenAI


def Ler_arquivo():
    print("--RESUMIDOR-DE-ARQUIVOS-CSV!--")
    while True:
        try:
            print("Digite EXATAMENTE o Nome do seu arquivo! Ex: 'file.csv'")
            Arquivo1 = input("Digite aqui: ")
            
            arquivo = pd.read_csv(Arquivo1)
            print("Carregando...")
            conteudo_arquivo = arquivo.to_string()
            client = OpenAI(api_key='#sua_chave_aqui!!!!!!!')
            resposta = client.responses.create(
                model="gpt-4o-mini",
                instructions='Voce apenas ira Resumir bem Todos os arquivos que forem recebidos, e sem usar "*" para destacar..',
                input=conteudo_arquivo
            )
            print(resposta.output_text)
            break
        except Exception as e:
            print(e)
Ler_arquivo()
