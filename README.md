# Meeting Prep Assistant

A Streamlit-based application that helps prepare for business meetings by analyzing company information, participants, industry trends, and generating strategic insights using AI agents.

## Features

- **Company Analysis**: Gathers and summarizes company overview, key products/services, and recent developments.
- **Participant Insights**: Researches professional backgrounds and likely priorities of meeting participants.
- **Industry Trends**: Identifies industry trends, risks, and opportunities.
- **Strategic Planning**: Generates meeting objectives, talking points, questions, and risk preparations.
- **Executive Brief**: Creates a clean, executive-ready meeting brief.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Chat_with_gmail
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r req.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   TAVILY_API_KEY=your_tavily_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Usage

1. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your browser to the provided URL (usually http://localhost:8501).

4. Enter the meeting details:
   - Meeting Title
   - Company Name
   - Participants (comma-separated)
   - Expected Outcome
   - Meeting Goal (select from options)

5. Click "Generate Prep" to get the meeting brief.

## Project Structure

- `app.py`: Main Streamlit application
- `graph.py`: LangGraph workflow definition
- `state.py`: State management for the workflow
- `agents/`: AI agents for different analysis tasks
  - `company_agent.py`: Company analysis
  - `participant_agent.py`: Participant research
  - `industry_agent.py`: Industry insights
  - `strategy_agent.py`: Strategic planning
  - `brief_agent.py`: Brief generation
- `tools/`: Utility tools
  - `tavily_search.py`: Web search tool using Tavily API

## Requirements

- Python 3.8+
- API keys for Tavily and Groq services

## Dependencies

See `req.txt` for a full list of Python packages.

## License

[Add license information if applicable]
