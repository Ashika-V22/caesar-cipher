import streamlit as st

# ==========================
# CAESAR CIPHER FUNCTIONS
# ==========================

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ==========================
# STREAMLIT UI
# ==========================

st.title("🔐 Caesar Cipher Tool")
st.write("Encrypt or decrypt text using the classical Caesar Cipher.")

mode = st.radio("Choose Mode:", ["Encrypt", "Decrypt"])

text = st.text_area("Enter your message:")

shift = st.number_input("Enter shift value:", min_value=-1000, max_value=1000, value=3)

if st.button("Process"):
    if mode == "Encrypt":
        result = caesar_encrypt(text, shift)
        st.success("🔒 Encrypted Message:")
    else:
        result = caesar_decrypt(text, shift)
        st.success("🔓 Decrypted Message:")

    st.code(result, language="text")
