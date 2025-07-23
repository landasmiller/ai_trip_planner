# AI Trip Planner 🧭

**AI Trip Planner** is a smart, agentic travel planning application built with Streamlit, FastAPI, and OpenAI. It generates personalized multi-day itineraries, pulls live location data, and adapts plans dynamically based on your preferences.

---

## 🚀 Features

- **Conversational interface** for trip planning with natural language input  
- **Multi-day itinerary generation** via OpenAI LLM  
- **Live location & place data** (e.g., “weather”, “top sights”, “local tips”) pulled from integrated tools  
- **Intelligent workflow**: builds and updates trip graphs to ensure context-aware planning  
- **Downloadable** or shareable trip summaries

---

## 📁 Project Structure

## 🧩 How It Works

User submits a trip request (e.g., "Plan a 3-day trip to Greece") via Streamlit.

The frontend sends a POST to the FastAPI endpoint /query.

The agentic workflow constructs a planning graph and invokes tools (OpenAI, place info, weather).

The AI responds with a detailed itinerary based on context and data.

The frontend displays the plan as markdown.

## ⭐ Why It Stands Out

Agent-driven design enables context retention and dynamic updates

Integrated tools give real-time data alongside AI-generated text

Modular architecture makes it easy to add new capabilities (e.g., flight search, hotel booking)
