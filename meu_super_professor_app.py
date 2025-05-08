
import streamlit as st

st.set_page_config(page_title="Meu Super Professor", layout="centered")

st.title("Meu Super Professor")
st.subheader("Seu agente de IA para o ENEM")

st.markdown("**Tema atual: Divisibilidade por 3**")
st.markdown("Digite um número para saber se ele é divisível por 3, com explicação passo a passo!")

numero = st.text_input("Digite um número inteiro:")

if numero:
    try:
        n = int(numero)
        soma = sum(int(digito) for digito in numero)
        divisivel = soma % 3 == 0

        st.markdown(f"**Soma dos algarismos:** {soma}")

        if divisivel:
            st.success(f"Sim! O número {n} é divisível por 3.")
            st.info("Dica do prof: Se a soma dos algarismos for um múltiplo de 3 (tipo 3, 6, 9, 12...), o número também é!")
        else:
            st.error(f"Não! O número {n} não é divisível por 3.")
            st.info("Se a soma dos algarismos não for múltiplo de 3, o número não passa no teste.")

    except ValueError:
        st.warning("Por favor, digite apenas números inteiros.")
