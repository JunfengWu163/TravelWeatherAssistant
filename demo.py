#!/usr/bin/env python3
"""
Example/Demo script for the AI Travel Weather Assistant
This shows how the app works without requiring user input.
"""

import json
from travel_weather_assistant import (
    get_weather_by_city,
    analyze_travel_with_ai,
    print_recommendations
)


def run_demo():
    """
    Run a demo with pre-configured travel plan.
    """
    print("="*70)
    print("🌍 AI Travel Weather Assistant - DEMO MODE")
    print("="*70)
    
    # Sample travel plan
    travel_plan = """
    I'm flying from Los Angeles to Tokyo on February 20th for a 6-day business 
    and leisure trip. My schedule:
    
    - Day 1-2: Meetings in downtown Tokyo (Shibuya/Shinjuku area)
    - Day 3: Day trip to Mount Fuji
    - Day 4: Visit TeamLab Borderless and shopping in Harajuku
    - Day 5: Free day - considering Nikko or staying in the city
    - Day 6: Morning flight back to LA
    
    I'll be doing a mix of indoor meetings and outdoor sightseeing.
    """
    
    origin_city = "Los Angeles"
    destination_city = "Tokyo"
    
    print(f"\n📝 SAMPLE TRAVEL PLAN:")
    print(travel_plan)
    print(f"\n🏠 Origin: {origin_city}")
    print(f"✈️  Destination: {destination_city}")
    
    print("\n" + "-"*70)
    print("🌐 Fetching weather data...")
    print("-" * 70)
    
    try:
        # Fetch weather for both cities
        origin_weather = get_weather_by_city(origin_city)
        destination_weather = get_weather_by_city(destination_city)
        
        print("\n✓ Weather data retrieved successfully!")
        
        # Show sample weather data
        print("\n📊 Sample Weather Data (Tokyo):")
        if "daily" in destination_weather:
            daily = destination_weather["daily"]
            print(f"   Dates: {daily.get('time', [])[:3]}")
            print(f"   Max Temps: {daily.get('temperature_2m_max', [])[:3]} °C")
            print(f"   Min Temps: {daily.get('temperature_2m_min', [])[:3]} °C")
            print(f"   Precipitation: {daily.get('precipitation_sum', [])[:3]} mm")
        
        # Analyze with AI
        print("\n" + "="*70)
        recommendations = analyze_travel_with_ai(
            travel_plan, 
            origin_city, 
            destination_city,
            origin_weather, 
            destination_weather
        )
        
        # Display results
        if recommendations:
            print_recommendations(recommendations)
            
            # Save demo output
            filename = "demo_recommendations.json"
            with open(filename, 'w') as f:
                json.dump(recommendations, f, indent=2)
            print(f"\n💾 Demo output saved to {filename}")
        else:
            print("\n❌ Failed to generate recommendations")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    import os
    
    # Check for API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("\n⚠️  WARNING: OPENAI_API_KEY not set!")
        print("This demo requires an OpenAI API key to run.")
        print("\nSet it with:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
        print("\nOr the demo will fail when calling the AI.")
        print("\nContinuing anyway...\n")
        input("Press Enter to continue...")
    
    run_demo()
