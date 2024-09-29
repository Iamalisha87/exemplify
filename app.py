import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = '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'

# Function to get response from OpenAI based on user input (Updated for v1.0.0+ chat completion)
def get_response(issue):
    response = openai.chat.completions.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are an AI assistant that helps students resolve issues during online exams."},
            {"role": "user", "content": issue}
        ],
        max_tokens=150,
        temperature=0.7  # Adjust the creativity of the responses
    )
    
    # Access the content of the message properly
    return response.choices[0].message.content.strip()

# Sidebar for navigation
with st.sidebar:
    st.image("https://support.examsoft.com/hc/theming_assets/01J0V5JB641M8E45VRAJBN6Z99", width=100)
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
st.image("https://png.pngtree.com/element_our/20190523/ourmid/pngtree-vector-yellow-looking-information-magnifying-glass-image_1082093.jpg", caption="Example of solving technical issue.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
    © 2024 Exemplify Inc. All rights reserved.
    </div>
""", unsafe_allow_html=True)
