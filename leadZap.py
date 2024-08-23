import streamlit as st
import pywhatkit as kit
import time

# Função para enviar mensagem
def enviar_mensagem(numero, mensagem):
    try:
        kit.sendwhatmsg_instantly(numero, mensagem)
        st.success(f"Mensagem enviada para {numero}")
    except Exception as e:
        st.error(f"Erro ao enviar mensagem para {numero}: {e}")

# Interface do Streamlit
st.title("Envio de Mensagens pelo WhatsApp")
st.write("Insira os números de telefone e a mensagem que deseja enviar.")

# Entrada de dados
numeros = st.text_area("Números de Telefone (um por linha)")
mensagem = st.text_area("Mensagem")

if st.button("Enviar Mensagens"):
    lista_numeros = numeros.splitlines()  # Divide os números por linha
    for numero in lista_numeros:
        numero = numero.strip()  # Remove espaços em branco
        if numero:
            enviar_mensagem(numero, mensagem)
            time.sleep(10)  # Intervalo de 10 segundos entre cada envio
    st.write("Envio de mensagens concluído!")

