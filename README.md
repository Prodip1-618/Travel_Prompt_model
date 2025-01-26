# AI-Powered Travel Planner

This project is a Streamlit-based web application that uses OpenAI's GPT model to generate personalized, day-by-day travel itineraries based on user preferences.

## Features
- Collects user input for:
  - Name
  - Travel destination
  - Duration of the trip
  - Budget (Low, Moderate, Luxury)
  - Purpose (e.g., leisure, adventure, business)
  - Preferences (e.g., food, museums, adventure sports)
- Generates a detailed travel itinerary using OpenAI's GPT model.
- Displays a structured day-by-day travel plan.
- Allows users to provide feedback on the generated itinerary.

---

## Installation
### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key:
   - Open the `main.py` file.
   - Replace `"your_openai_api_key_here"` with your actual API key.

4. Run the application:
   ```bash
   streamlit run main.py
   ```

---

## File Structure
- `main.py`: The main application script.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation for the project.

---

## Usage
1. Open the app in your browser after running it.
2. Fill in the details:
   - Name, destination, trip duration, budget, purpose, and preferences.
3. Click **Generate Itinerary** to get your travel plan.
4. Review the itinerary and provide feedback if desired.

---

## Prompts Documentation
### System Prompt
```plaintext
You are an AI travel assistant. Your task is to create a personalized, day-by-day travel itinerary based on user preferences.
```

### User Prompts
Example Input:
```plaintext
Name: John Doe
Destination: Paris
Duration: 5 days
Budget: Moderate
Purpose: Leisure
Preferences: Food, art, and cultural tours
```

### Model Response (Example Output):
```plaintext
Day 1: Arrival in Paris, visit Eiffel Tower, and enjoy a Seine River cruise.
Day 2: Explore the Louvre Museum and Montmartre art district.
Day 3: Day trip to Versailles and a French cooking class.
Day 4: Discover hidden gems in Paris and savor local cuisine.
Day 5: Relax at Luxembourg Gardens before departure.
```

Each prompt refines the user inputs and aligns them to create a structured output.

---

## Sample Input and Output
### Input
- **Destination**: Tokyo  
- **Duration**: 7 days  
- **Budget**: Luxury  
- **Purpose**: Honeymoon  
- **Preferences**: Scenic views, romantic dinners, and cultural experiences

### Output
**Day 1**: Arrival in Tokyo, dinner at a rooftop restaurant.  
**Day 2**: Visit Meiji Shrine and Shibuya Crossing.  
**Day 3**: Day trip to Mount Fuji and Hakone.  
**Day 4**: Explore Asakusa and a tea ceremony.  
**Day 5**: Romantic cruise on Tokyo Bay.  
**Day 6**: Shopping at Ginza and Ikebukuro.  
**Day 7**: Relaxation at Odaiba and departure.

---

## Hosting Instructions
To host this application:
1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub account.
3. Deploy the app and share the link.

---

## Deliverables
1. **Final Set of Prompts**: Includes the system prompt, user prompts, and example responses.
2. **Sample Input and Output**: Provides detailed examples for generating itineraries.
3. **Documentation**: Explains the process and reasoning behind each prompt.
4. **Hosted Application**: A live link to the hosted app for user testing.

---

## Bonus Challenge (Optional)
- Improve flexibility in input formats (e.g., "I want a mix of famous and offbeat places").
- Add logic to refine vague or incomplete inputs through follow-up prompts.

---

## Troubleshooting
### Common Issues
1. **API Key Error**:
   - Ensure your API key is correct and has enough quota.
   - Check the [API Keys Page](https://platform.openai.com/account/api-keys).

2. **Rate Limit Error**:
   - Reduce the number of tokens or API requests.
   - Upgrade your OpenAI plan if needed.

3. **Streamlit Not Found**:
   - Ensure Streamlit is installed: `pip install streamlit`

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [OpenAI](https://platform.openai.com/) for the GPT model.
- [Streamlit](https://streamlit.io/) for the web framework.GPT model.
- [Streamlit](https://streamlit.io/) for the web framework.
