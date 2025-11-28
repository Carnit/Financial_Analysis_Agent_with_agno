# 📈 Financial Analysis Agent with Streamlit

A sophisticated **AI-powered financial analysis platform** that generates institutional-grade investment research reports. This project combines the power of Google's Gemini AI model with real-time financial data from Yahoo Finance, presented through an intuitive Streamlit web interface.

## 🎯 Project Overview

The Financial Analysis Agent is designed to provide professional investors, traders, and financial enthusiasts with comprehensive, data-driven investment analysis. The system uses advanced natural language processing to synthesize market data into well-structured investment research reports, similar to what institutional analysts produce.

### How It Works

```
User Query/Selection
        ↓
  Streamlit Interface
        ↓
    Agno Agent
        ↓
  Gemini AI Model (2.0-Flash)
        ↓
Yahoo Finance Tools (Real-time Data)
        ↓
Financial Analysis & Report Generation
        ↓
Display in Web Browser
```

## 🚀 Features

### **Interactive Web Interface**
- Clean, responsive Streamlit UI with sidebar navigation
- Real-time market updates and responsive design
- Professional styling and organized layout

### **AI-Powered Analysis**
- Leverages Google's **Gemini 2.0-Flash** model for advanced analysis
- Institutional-grade report generation following professional standards
- Natural language processing for nuanced market insights
- Comprehensive financial commentary and investment theses

### **Real-Time Financial Data**
- Integrates **YFinanceTools** for live market data
- Fetches stock prices, company fundamentals, analyst recommendations, and news
- Supports multiple ticker symbols for comparative analysis
- Handles market data aggregation and normalization

### **Pre-configured Analysis Templates**
1. **Semiconductor Market Analysis** - NVIDIA, AMD, Intel, TSM, and others
2. **Automotive Industry Analysis** - Tesla, Ford, GM, and traditional automakers with EV focus
3. **Technology Sector Analysis** - FAANG stocks and tech leaders
4. **Energy Sector Analysis** - Oil, gas, and renewable energy companies
5. **Custom Analysis** - Define your own analysis queries

### **Professional Report Structure**
Each generated report includes:
- Executive Summary with investment thesis
- Company Overview and market positioning
- Detailed Financial Analysis with key metrics
- Competitive Landscape and industry trends
- Analyst Consensus and recent news
- Outlook, valuation, and risk assessment
- Professional disclaimer

### **User-Friendly Features**
- One-click report generation
- Custom query input for flexible analysis
- Loading indicators and error handling
- Professional formatting with Markdown output

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web interface and user interaction |
| **AI Model** | Google Gemini 2.0-Flash | Natural language processing and analysis |
| **Financial Data** | Yahoo Finance | Real-time market data |
| **Agent Framework** | Agno | AI agent orchestration |
| **Python** | 3.13+ | Runtime environment |
| **Package Manager** | UV | Dependency management |

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8 or higher** (Tested with Python 3.13)
- **Google API Key** - Get one free from [Google AI Studio](https://aistudio.google.com/)
- **Internet connection** - For Yahoo Finance and Google API access
- **Git** (optional) - For version control

## 🔧 Installation & Setup

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd agno_project
```

### Step 2: Create Virtual Environment

Using UV (recommended):
```bash
uv venv
```

Or using Python's built-in venv:
```bash
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

Using UV:
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `streamlit>=1.28.0` - Web interface
- `agno>=1.7.2` - Agent framework
- `google-genai>=1.25.0` - Gemini API access
- `yfinance>=0.2.65` - Financial data
- `python-dotenv>=0.9.9` - Environment variables

### Step 4: Configure Google API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY="your_api_key_here"
```

Get your API key:
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Click "Get API Key"
3. Create a new API key
4. Copy and paste it into the `.env` file

## ▶️ Running the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

Or if using pip:
```bash
streamlit run app.py
```

The app will launch in your default browser at `http://localhost:8501`

### Application Interface

**Left Sidebar:**
- **Navigation Radio Buttons** - Select analysis type
- **About Section** - Project information

**Main Content Area:**
- **Header** - Current analysis type and description
- **Input Area** - Query or report generation buttons
- **Results Area** - Generated financial reports

## 📊 Usage Examples

### Example 1: Pre-configured Semiconductor Analysis
1. Select "Semiconductor Market" from the sidebar
2. Click "📊 Generate Report"
3. Wait for Gemini to analyze NVIDIA, AMD, Intel, and others
4. Review the comprehensive market analysis

### Example 2: Custom Stock Analysis
1. Select "Custom Analysis" from the sidebar
2. Enter query: "Compare Apple and Microsoft in AI capabilities and market dominance"
3. Click "🔍 Analyze"
4. Get a tailored analysis based on your specific question

### Example 3: Sector Comparison
1. Use "Energy Sector" template
2. Get analysis on ExxonMobil, Chevron, Shell, and renewable energy plays
3. Understand the energy transition and investment opportunities

## 🔧 Customization Guide

### Adding New Analysis Templates

Edit `app.py` and add a new elif block:

```python
elif analysis_type == "Your New Sector":
    st.header("🏷️ Your Sector Analysis")
    st.markdown("Description of the analysis")
    
    if st.button("📊 Generate Report", key="your_key"):
        try:
            response = finance_agent.run(
                dedent("""\
                Your analysis query here with relevant stocks and focus areas.""")
            )
            # Process and display response
```

### Modifying the AI Agent Instructions

Edit the `initialize_agent()` function in `app.py`:

```python
instructions=dedent("""\
    Your custom instructions for the agent...
    Define report structure, tone, and focus areas
""")
```

### Changing the AI Model

Update the model in `initialize_agent()`:

```python
model=Gemini(id="gemini-2.0-flash", api_key=google_api_key)
# Change "gemini-2.0-flash" to another available model
```

## 📁 Project Structure

```
agno_project/
├── app.py                 # Main Streamlit application
├── pyproject.toml         # Project dependencies and metadata
├── requirements.txt       # Python dependencies
├── .env                   # Google API Key (not in repo)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🎓 Understanding the Report Structure

Each generated report follows an institutional format:

1. **Executive Summary** - Clear investment thesis with bullet points
2. **Company Overview** - Business description and market position
3. **Financial Analysis** - Key metrics, performance, and health assessment
4. **Competitive Landscape** - Competitor comparison and industry trends
5. **Analyst Consensus** - Professional ratings and recent news impact
6. **Outlook & Valuation** - Forward-looking statement and risk assessment
7. **Disclaimer** - Legal and informational disclaimer

## ⚙️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **404 API Error** | Check if `gemini-2.0-flash` is available; try alternative model |
| **Yahoo Finance 404** | Some tickers may not be available; verify ticker symbols |
| **API Key Error** | Ensure `.env` file exists and contains valid `GOOGLE_API_KEY` |
| **Streamlit Won't Start** | Run `uv sync` to ensure all dependencies are installed |
| **No Results** | Check internet connection and API key validity |

## 🔐 Security Notes

- **Never commit `.env` file** to version control
- **Keep your API key secret** - Treat it like a password
- Use `.gitignore` to exclude sensitive files
- Consider using environment variable management tools for production

## 📝 Sample Analysis Output

The agent generates reports like:

```
## Executive Summary
**BUY: Semiconductor leader positioned for AI boom growth**

- Strong Q3 earnings with 40% YoY revenue growth
- Dominant market position in AI accelerators
- Valuation reasonable at 35x forward earnings
- Key catalysts: New product launches Q1 2026

## Financial Analysis
- Market Cap: $2.5T
- P/E Ratio: 35.2
- Revenue Growth: 40% YoY
- Operating Margin: 45%
...
```

## 🚀 Future Enhancements

Potential improvements for future versions:

- **Multi-language support** - Generate reports in multiple languages
- **Historical analysis** - Track recommendation changes over time
- **Portfolio analysis** - Analyze entire investment portfolios
- **Risk metrics** - Include advanced risk assessment models
- **Export functionality** - PDF/Excel report generation
- **Caching system** - Faster repeated analyses
- **Database** - Store historical analyses

## 📄 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## ❓ FAQ

**Q: Can I use this for real investment decisions?**
A: This tool is for informational purposes. Always conduct your own research and consult with financial advisors.

**Q: How accurate are the analyses?**
A: Analyses are AI-generated and should be used as one input among many investment research sources.

**Q: Can I run this locally without internet?**
A: No, the app requires internet for Google API and Yahoo Finance access.

**Q: What's the cost of using this?**
A: Google provides free API access up to certain limits. Check their pricing page for details.

**Q: Can I modify the analysis templates?**
A: Yes! Edit `app.py` to customize analysis queries and templates.

## 📞 Support

For issues, questions, or feedback:
- Check the troubleshooting section above
- Review the code comments in `app.py`
- Check Google Gemini API documentation

---

**Built with ❤️ using Agno, Streamlit, and Google Gemini**
