
import streamlit as st

st.set_page_config(page_title="Meu Super Professor", layout="centered")

st.title("Meu Super Professor")
st.subheader("Seu agente de IA para o ENEM")
st.markdown("### Tema atual: Divisibilidade por 3")
st.markdown("Fala comigo! Me diga um número e eu te explico se ele é ou não divisível por 3, passo a passo.")

numero = st.text_input("Digite um número inteiro:")

if numero:
    try:
        n = int(numero)
        soma = sum(int(digito) for digito in numero if digito.isdigit())
        divisivel = soma % 3 == 0

        st.markdown("-----")
        st.markdown("**Boa pergunta! Vamos nessa.**")
        st.markdown(f"Você quer saber se **{n}** é divisível por 3, certo? Bora conferir juntos!")

        st.markdown("### Passo 1: Soma dos algarismos")
        st.markdown(f"{' + '.join(numero)} = **{soma}**")

        st.markdown("### Passo 2: Verificando a divisibilidade")
        if divisivel:
            st.success(f"Sim! O número **{n} é divisível por 3.**")
            st.info("Macete do prof: se a soma dos algarismos for múltiplo de 3 (tipo 3, 6, 9, 12...), pode marcar sem medo!")
        else:
            st.error(f"Não! O número **{n} não é divisível por 3.**")
            st.info("Se a soma não for múltiplo de 3, o número original também não passa no teste.")

        st.markdown("### Quer tentar mais um?")
        st.markdown("Manda outro número aqui em cima e eu te ajudo na hora!")

    except ValueError:
        st.warning("Por favor, digite apenas números inteiros válidos.")
