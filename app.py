# Financial analysis agent with Streamlit frontend
import os
import sys
from textwrap import dedent
from dotenv import load_dotenv
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools


# Page configuration
st.set_page_config(
    page_title="Financial Analysis Agent",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }
    .stMarkdown {
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def initialize_agent():
    """Initialize the financial analysis agent with caching."""
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        st.error("Error: GOOGLE_API_KEY not found in .env file.")
        st.stop()

    finance_agent = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=google_api_key),
        tools=[YFinanceTools()],
        instructions=dedent("""\
            You are a seasoned Wall Street analyst providing institutional-grade research for sophisticated investors. Your analysis must be rigorous, objective, and data-driven. Your goal is to produce a comprehensive investment research report.

            **Report Structure:**

            1.  **Executive Summary:**
                *   Start with a clear investment thesis (e.g., "BUY: Undervalued leader in a growing market").
                *   Provide 3-4 bullet points summarizing the core arguments.

            2.  **Company Overview:**
                *   Briefly describe the company's business, primary products/services, and its position in the market.

            3.  **Financial Analysis:**
                *   **Key Metrics:** Present vital statistics like Market Cap, P/E Ratio, P/S Ratio, and Dividend Yield.
                *   **Performance:** Analyze recent revenue and earnings performance. Is it accelerating or decelerating?
                *   **Health:** Comment on the balance sheet, particularly debt levels.

            4.  **Competitive Landscape & Industry Trends:**
                *   Who are the main competitors? How does the company stack up against them?
                *   What are the key trends affecting the industry? (e.g., technological shifts, regulatory changes).

            5.  **Analyst Consensus & Recent News:**
                *   Summarize the consensus from professional analysts. Provide the breakdown of Buy/Hold/Sell ratings if available.
                *   Highlight any major recent news and explain its potential impact on the company's outlook.

            6.  **Outlook & Valuation:**
                *   Provide a forward-looking statement on the company's prospects.
                *   Identify key catalysts that could drive the stock price up and risks that could drive it down.
                *   Comment on whether the stock appears overvalued, fairly valued, or undervalued based on the data.

            **Tone and Style:**
            -   **Professional & Objective:** Maintain a formal tone. Avoid hype and emotional language.
            -   **Quantitative:** Your claims must be supported by financial data and metrics from your tools.
            -   **Structured:** Use Markdown for clear headings, subheadings, and bullet points to ensure readability.
            -   **No Code Generation:** Your entire response must be a natural language report. Do NOT write or suggest any code. If data is unavailable from your tools, state that and continue the analysis with the information you have.

            **Disclaimer:**
            -   Conclude every report with a standard disclaimer: "This report is for informational purposes only and does not constitute financial or investment advice. Please conduct your own research before making any investment decisions."
        """),
    )
    return finance_agent


def main():
    st.title("📈 Financial Analysis Agent")
    st.markdown("*Institutional-grade investment research powered by AI*")

    # Initialize agent
    finance_agent = initialize_agent()

    # Sidebar for navigation and options
    st.sidebar.header("Navigation")
    analysis_type = st.sidebar.radio(
        "Select Analysis Type",
        [
            "Custom Analysis",
            "Semiconductor Market",
            "Automotive Industry",
            "Technology Sector",
            "Energy Sector",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.markdown(
        "This agent provides comprehensive financial analysis using real-time data from Yahoo Finance and AI-powered insights from Google's Gemini model."
    )

    # Main content area
    if analysis_type == "Custom Analysis":
        st.header("Custom Stock Analysis")
        st.markdown("Enter your own stocks or query for custom financial analysis.")

        # Create columns for input
        col1, col2 = st.columns([3, 1])
        with col1:
            custom_query = st.text_area(
                "Enter your analysis query:",
                placeholder="e.g., Analyze Apple (AAPL) and Microsoft (MSFT) competition in cloud services...",
                height=100,
            )
        with col2:
            analyze_button = st.button("🔍 Analyze", use_container_width=True)

        if analyze_button and custom_query:
            with st.spinner("Generating analysis..."):
                st.markdown("---")
                try:
                    response = finance_agent.run(custom_query)
                    # Handle RunOutput object
                    if hasattr(response, "messages") and response.messages:
                        full_response = response.messages[-1].content
                    elif hasattr(response, "content"):
                        full_response = response.content
                    else:
                        full_response = str(response)

                    if full_response:
                        st.markdown(full_response)
                    else:
                        st.info(
                            "Analysis generated. Please check back shortly for results."
                        )
                except Exception as e:
                    st.error(f"Error generating analysis: {str(e)}")

    elif analysis_type == "Semiconductor Market":
        st.header("🔬 Semiconductor Market Analysis")
        st.markdown(
            "Deep dive into the semiconductor industry leaders and market trends."
        )

        if st.button("📊 Generate Report", key="semi", use_container_width=True):
            with st.spinner("Analyzing semiconductor market..."):
                st.markdown("---")
                try:
                    response = finance_agent.run(
                        dedent("""\
                        Analyze the semiconductor market performance focusing on:
                        - NVIDIA (NVDA)
                        - AMD (AMD)
                        - Intel (INTC)
                        - Taiwan Semiconductor (TSM)
                        - Qualcomm (QCOM)
                        - Broadcom (AVGO)
                        - Micron Technology (MU)
                        - Texas Instruments (TXN)
                        - Samsung Electronics (SSNLF)
                        Provide insights on their recent earnings, market trends, and competitive landscape.
                        Include their latest earnings reports, market trends, and competitive landscape.
                        Compare their market positions, growth metrics, and future outlook.""")
                    )
                    # Handle RunOutput object
                    if hasattr(response, "messages") and response.messages:
                        full_response = response.messages[-1].content
                    elif hasattr(response, "content"):
                        full_response = response.content
                    else:
                        full_response = str(response)

                    if full_response:
                        st.markdown(full_response)
                    else:
                        st.info(
                            "Analysis generated. Please check back shortly for results."
                        )
                except Exception as e:
                    st.error(f"Error generating analysis: {str(e)}")

    elif analysis_type == "Automotive Industry":
        st.header("🚗 Automotive Industry Analysis")
        st.markdown(
            "Comprehensive evaluation of the automotive sector with focus on EV transition."
        )
        if st.button("📊 Generate Report", key="auto", use_container_width=True):
            with st.spinner("Analyzing automotive industry..."):
                st.markdown("---")
                try:
                    response = finance_agent.run(
                        dedent("""\
                        Evaluate the automotive industry's current state:
                        - Tesla (TSLA)
                        - Ford (F)
                        - General Motors (GM)
                        - Toyota (TM)
                        - Volkswagen (VWAGY)
                        - Honda (HMC)
                        - BMW (BMWYY)
                        - Mercedes-Benz (MBGYY)
                        - Audi (AUDVF)
                        - Porsche (POAHF)
                        - Ferrari NV (RACE)
                        Focus on their market shares, EV transition progress, and traditional auto metrics.
                        Include EV transition progress and traditional auto metrics.""")
                    )
                    # Handle RunOutput object
                    if hasattr(response, "messages") and response.messages:
                        full_response = response.messages[-1].content
                    elif hasattr(response, "content"):
                        full_response = response.content
                    else:
                        full_response = str(response)

                    if full_response:
                        st.markdown(full_response)
                    else:
                        st.info(
                            "Analysis generated. Please check back shortly for results."
                        )
                except Exception as e:
                    st.error(f"Error generating analysis: {str(e)}")

    elif analysis_type == "Technology Sector":
        st.header("💻 Technology Sector Analysis")
        st.markdown("In-depth analysis of major technology companies and trends.")

        if st.button("📊 Generate Report", key="tech", use_container_width=True):
            with st.spinner("Analyzing technology sector..."):
                st.markdown("---")
                try:
                    response = finance_agent.run(
                        dedent("""\
                        Analyze the technology sector focusing on:
                        - Apple (AAPL)
                        - Microsoft (MSFT)
                        - Google/Alphabet (GOOGL)
                        - Amazon (AMZN)
                        - Meta (META)
                        - Tesla (TSLA)
                        - NVIDIA (NVDA)
                        - Oracle (ORCL)
                        Compare their market positions, innovation pipelines, profitability, and future outlook.
                        Include analysis on AI adoption, cloud services, and digital transformation trends.""")
                    )
                    # Handle RunOutput object
                    if hasattr(response, "messages") and response.messages:
                        full_response = response.messages[-1].content
                    elif hasattr(response, "content"):
                        full_response = response.content
                    else:
                        full_response = str(response)

                    if full_response:
                        st.markdown(full_response)
                    else:
                        st.info(
                            "Analysis generated. Please check back shortly for results."
                        )
                except Exception as e:
                    st.error(f"Error generating analysis: {str(e)}")

    elif analysis_type == "Energy Sector":
        st.header("⚡ Energy Sector Analysis")
        st.markdown("Analysis of energy companies and renewable energy market trends.")

        if st.button("📊 Generate Report", key="energy", use_container_width=True):
            with st.spinner("Analyzing energy sector..."):
                st.markdown("---")
                try:
                    response = finance_agent.run(
                        dedent("""\
                        Evaluate the energy sector covering:
                        - ExxonMobil (XOM)
                        - Chevron (CVX)
                        - Shell (SHEL)
                        - BP (BP)
                        - NextEra Energy (NEE)
                        - Duke Energy (DUK)
                        Analyze their traditional oil/gas assets, renewable energy investments, and transition strategies.
                        Include carbon pricing, renewable energy growth, and geopolitical factors.""")
                    )
                    # Handle RunOutput object
                    if hasattr(response, "messages") and response.messages:
                        full_response = response.messages[-1].content
                    elif hasattr(response, "content"):
                        full_response = response.content
                    else:
                        full_response = str(response)

                    if full_response:
                        st.markdown(full_response)
                    else:
                        st.info(
                            "Analysis generated. Please check back shortly for results."
                        )
                except Exception as e:
                    st.error(f"Error generating analysis: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown(
        """
    **Disclaimer:** This report is for informational purposes only and does not constitute financial or investment advice. 
    Please conduct your own research before making any investment decisions.
    """
    )


if __name__ == "__main__":
    main()
