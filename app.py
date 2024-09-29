import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = 'api_key'

# Customize page layout
st.set_page_config(page_title="Exemplify Exam Support Bot", layout="wide", page_icon=":robot_face:")

# Function to get response from OpenAI based on user input
def get_response(issue):
    prompt = f"Provide a helpful and reassuring solution to the following exam-related issue: {issue}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo", # GPT-4 if available
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Sidebar for navigation
with st.sidebar:
    st.image("logo.png", width=100)
    st.title("Exemplify Support")
    st.write("Quick solutions for exam issues.")
    issue_type = st.selectbox("Select Issue Type", ["Technical Issues", "Software Issues", "Submission Issues", "Other"])

# Main container
st.title("📝 Exemplify Exam Support Bot")
st.markdown("""
<style>
    .reportview-container {
        background-color: #F5F7FA;
    }
    .sidebar .sidebar-content {
        background-color: #2F3136;
        color: white;
    }
    .stButton > button {
        background-color: #007BFF;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
    h1 {
        color: #333;
    }
    .block-container {
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.write("Facing issues during your exam? Enter your problem below and get an instant solution.")

# User input
issue = st.text_area("Describe your issue", height=150, placeholder="Eg: My screen froze, Excel is not working, etc.")

# Display a button for submission
if st.button("Get Solution"):
    if issue:
        with st.spinner('Fetching solution...'):
            solution = get_response(issue)
            st.success("Here's your solution:")
            st.write(f"**Solution:** {solution}")
    else:
        st.error("Please describe your issue first!")

# Add some GenAI generated image for visual aid (Placeholder)
st.image("genai_image_placeholder.png", caption="Example of solving technical issue.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
    © 2024 Exemplify Inc. All rights reserved.
    </div>
""", unsafe_allow_html=True)
