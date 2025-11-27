# Financial Analysis Agent

This project showcases a sophisticated financial analysis agent built using the `agno` library, Google's Gemini model, and Yahoo Finance data. The agent features an interactive **Streamlit web interface** for easy access to institutional-grade investment research reports.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for a modern, user-friendly experience
- **AI-Powered Analysis**: Leverages the power of Google's Gemini model for deep analysis and natural language report generation
- **Real-time Financial Data**: Integrates `YFinanceTools` to fetch up-to-the-minute stock prices, company fundamentals, analyst recommendations, and news
- **Pre-configured Analysis Templates**:

  - Semiconductor Market Analysis
  - Automotive Industry Evaluation
  - Technology Sector Deep Dive
  - Energy Sector Analysis
  - Custom Analysis for any stocks
- **Customizable Queries**: Input your own stocks and analysis questions
- **Professional Reports**: Generates comprehensive institutional-grade investment research reports
- **Streaming Output**: Real-time report generation for immediate feedback

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8 or higher (I am using Python 3.13)
- A Google API key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### 2. Project Setup

It's recommended to use a virtual environment to manage project dependencies.

```bash
# Navigate to the project directory
cd path/to/agno_project

# Create a virtual environment
python -m venv venv
```

or

```bash
uv init 
uv venv
```

```bash
# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
# or
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the `agno_project` directory and add your Google API key:

```env
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
```

## ▶️ How to Run

Once the setup is complete, you can launch the Streamlit web interface:

```bash
streamlit run app.py
```

This will open the application in your default web browser at `http://localhost:8501`. You can then:

1. **Select Analysis Type** from the sidebar
2. **Choose from pre-configured templates** or enter your own custom queries
3. **Click the "Generate Report" or "Analyze" button**
4. **View real-time financial analysis** as it's being generated

## 🔧 Customization

The Streamlit interface makes it easy to customize your analysis:

### Using Pre-configured Templates

Select from the sidebar any of the predefined analysis types (Semiconductor, Automotive, Technology, Energy) and click the "Generate Report" button.

### Custom Analysis

1. Select "Custom Analysis" from the sidebar
2. Enter your own analysis query in the text area (e.g., "Compare Apple and Microsoft in cloud computing")
3. Click the "Analyze" button to generate a custom report

### Modifying the Agent

You can modify the agent's instructions, available tools, or analysis templates by editing `app.py`:

- **Change the model**: Modify the `Gemini(id="...")` parameter
- **Modify report structure**: Update the `instructions` parameter in the `initialize_agent()` function
- **Add new analysis types**: Add new options to the `analysis_type` radio button and create corresponding report generation blocks
