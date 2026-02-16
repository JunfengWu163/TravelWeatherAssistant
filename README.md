# 🌍 AI Travel Weather Assistant

An intelligent travel assistant powered by OpenAI's ChatGPT that analyzes your travel plans with real-time weather forecasts to provide personalized recommendations, packing lists, and risk assessments.

## Features

- 🤖 **AI-Powered Analysis**: Uses OpenAI's ChatGPT to understand your travel plans
- 🌤️ **7-Day Weather Forecasts**: Fetches real-time weather data from Open-Meteo API
- 🎒 **Smart Packing Lists**: Recommends items based on weather conditions
- 📅 **Day-by-Day Advice**: Provides specific suggestions for each day of your trip
- ⚠️ **Risk Assessment**: Evaluates return trip risks based on weather patterns
- 💾 **Export Results**: Save recommendations as JSON for future reference

## Prerequisites

- Python 3.7 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Installation

1. **Clone or download** this project

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key:**
   
   **On Linux/Mac:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   set OPENAI_API_KEY=your-api-key-here
   ```
   
   **On Windows (PowerShell):**
   ```powershell
   $env:OPENAI_API_KEY="your-api-key-here"
   ```

   **Permanent setup (recommended):**
   Add the export command to your `~/.bashrc`, `~/.zshrc`, or equivalent shell config file.

## Usage

Run the application:

```bash
python travel_weather_assistant.py
```

You'll be prompted to enter:
1. **Travel plan**: Describe your itinerary in natural language
2. **Origin city**: Where you're traveling from
3. **Destination city**: Where you're traveling to

### Example Input

```
📝 Enter your travel plan:
> I'm flying from New York to Paris on March 15th for a 5-day vacation. 
  I plan to visit the Eiffel Tower, Louvre Museum, and do lots of outdoor 
  sightseeing. I'll return on March 20th.

🏠 Enter origin city: New York
✈️  Enter destination city: Paris
```

### Example Output

The app will provide:
- **Travel Summary**: Overview of your trip with weather considerations
- **Packing List**: Customized items based on forecasted conditions
- **Daily Recommendations**: Specific advice for each day
- **Return Trip Risk**: Low/Medium/High assessment
- **Alerts**: Important weather warnings or advisories

## Configuration

### Change AI Model

Edit the `model` parameter in `travel_weather_assistant.py`:

```python
response = client.chat.completions.create(
    model="gpt-4o",  # Change to "gpt-4o" for better quality (higher cost)
    ...
)
```

Available models:
- `gpt-4o-mini`: Fast and cost-effective (default)
- `gpt-4o`: Higher quality, more expensive
- `gpt-4-turbo`: Alternative high-quality option

### Customize Weather Parameters

Modify the `get_weather_json()` function to add more weather data:

```python
params = {
    "latitude": lat,
    "longitude": lon,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,windspeed_10m_max,uv_index_max",
    "timezone": "auto"
}
```

See [Open-Meteo API docs](https://open-meteo.com/en/docs) for available parameters.

## Output Format

The AI returns structured JSON:

```json
{
  "travel_summary": "Your 5-day trip from NYC to Paris...",
  "packing_list": [
    "Waterproof jacket",
    "Comfortable walking shoes",
    "Umbrella"
  ],
  "daily_recommendations": [
    {
      "day": "Day 1",
      "advice": "Expect mild temperatures around 12°C..."
    }
  ],
  "return_trip_risk": "medium",
  "alerts": [
    "High precipitation expected on March 18-19"
  ]
}
```

## Troubleshooting

### "OPENAI_API_KEY environment variable not set"
- Make sure you've exported your API key before running the script
- Verify with: `echo $OPENAI_API_KEY` (Linux/Mac) or `echo %OPENAI_API_KEY%` (Windows)

### "City not found"
- Try using the full city name with country: "Paris, France"
- Check spelling

### JSON parsing errors
- The AI occasionally returns malformed JSON
- The app will display the raw response for debugging
- Try running again or adjust the temperature parameter (lower = more consistent)

## API Costs

- **Weather API**: Free (Open-Meteo)
- **OpenAI API**: 
  - GPT-4o-mini: ~$0.01 per request
  - GPT-4o: ~$0.05 per request
  
Check current pricing at https://openai.com/api/pricing/

## Privacy & Data

- Your travel plans are sent to OpenAI's API for analysis
- Weather data is fetched from Open-Meteo's public API
- No data is stored by this application (except optional JSON export)

## License

MIT License - feel free to modify and use as needed!

## Contributing

Suggestions and improvements welcome! Feel free to fork and submit pull requests.

## Credits

- Weather data: [Open-Meteo](https://open-meteo.com/)
- AI analysis: [OpenAI ChatGPT](https://openai.com/)
