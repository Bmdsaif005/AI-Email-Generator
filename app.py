import streamlit as st

from ai import generate_email

st.title("AI Email Generator")
st.header("Generate professional emails in seconds using Amazon Bedrock.")

st.write("Generate professional emails using AI")

col1,col2 = st.columns(2)

with col1:
    purpose = st.text_input("Purpose : ")
    tone = st.selectbox("Tone", ["Formal", "Friendly" , "Professional"])

with col2:
    recipient = st.text_input("Recipient : ")

points = st.text_area("Key Points : ", placeholder = "Enter the key points you want to include")

generate = st.button("Generate Email")

is_valid = purpose.strip() != "" and recipient.strip() != "" and points.strip() != ""

if generate:
    if not is_valid:
        st.error("Please fill in all the required fields.")
        
    else:
        # st.success("All inputs fields are valid. Generating Email ...")
        prompt = f"""
You are an experienced business communication expert.

Write a professional email.

Purpose:
{purpose}

Recipient:
{recipient}

Tone:
{tone}

Key Points:
{points}

Requirements:

- Proper grammar
- Professional language
- Include an appropriate subject line
- Maximum 250 words
- Return only the email
"""

if generate and is_valid:
    with st.expander("Prompt sent to AI"):
        st.code(prompt)

    with st.spinner("Generating Email ..."):

        try:
            email = generate_email(prompt)

            st.subheader("Generated Email")

            st.text_area("output", value = email, height=300)
            with st.expander("Download Email"):
                st.download_button(
                    label = "Download Email",
                    data = email,
                    file_name = "generated_email.txt",
                    mime = "text/plain"
                )

        except Exception as e:
            st.error(str(e))

st.caption("Built with ❤️ by Mohammed Saif")
st.markdown("© 2026 Mohammed Saif | Powered by Streamlit")