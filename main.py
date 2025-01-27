import openai
import streamlit as st

# Step 2: Define Functions for Prompt Interaction
def get_openai_response(api_key, prompt):
    """Send a prompt to OpenAI's GPT model and return the response."""
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI travel assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Step 3: Streamlit UI for User Interaction
st.title("AI-Powered Travel Planner")
st.write("Plan your dream trip with a personalized itinerary!")

# Collect user input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")
user_name = st.text_input("What's your name?")
destination = st.text_input("Where are you planning to travel?")
duration = st.slider("How many days are you planning to stay?", min_value=1, max_value=30)
budget = st.selectbox("What's your budget?", ["Low", "Moderate", "Luxury"])
purpose = st.text_area("What's the purpose of your trip? (e.g., leisure, adventure, business)")
preferences = st.text_area("Any specific preferences? (e.g., food, museums, adventure sports)")

# Validate input
if st.button("Generate Itinerary"):
    if not api_key:
        st.error("Please provide a valid OpenAI API key.")
    elif not destination or not user_name:
        st.error("Please provide your name and destination to proceed.")
    else:
        # Build prompt based on user inputs
        system_prompt = "You are an AI travel assistant. Your task is to create a personalized, day-by-day travel itinerary based on user preferences."
        user_prompt = f"""
        Create a travel itinerary for:
        Name: {user_name}
        Destination: {destination}
        Duration: {duration} days
        Budget: {budget}
        Purpose: {purpose}
        Preferences: {preferences}
        """
        final_prompt = system_prompt + "\n" + user_prompt

        # Get AI response
        with st.spinner("Generating your itinerary..."):
            try:
                itinerary = get_openai_response(api_key, final_prompt)
                st.success("Here's your personalized itinerary:")
                st.text(itinerary)
            except openai.error.AuthenticationError:
                st.error("Invalid API key. Please check and try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Optional: Add a section for feedback
st.write("\n---")
feedback = st.text_area("Share your feedback on the itinerary:")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
