"""
INSTITUTIONAL EQUITY RESEARCH TERMINAL (SHOWCASE DEMO)
------------------------------------------------------
Version: 1.0.0-Showcase
Author: Guillaume OTTOLINI

PURPOSE:
This script serves as a structural and visual preview of the OnePager UI.
It demonstrates the front-end architecture, API authentication protocols, 
and pipeline orchestration logic. 

SECURITY NOTICE:
The core analytical engines (Data Ingestion, DCF Modeling, AI Synthesis, 
and PDF Compilation) are excluded from this public version to protect 
proprietary valuation logic and algorithmic guardrails.
"""

# =============================================================================
# --- SYSTEM & NETWORK UTILITIES ---
# =============================================================================
import os
import time
import logging

# =============================================================================
# --- STREAMLIT UI FRAMEWORK & PLUGINS ---
# =============================================================================
import streamlit as st
import requests
from streamlit_searchbox import st_searchbox

# Suppress standard Streamlit script runner logs for institutional deployment
logging.getLogger("streamlit.runtime.scriptrunner").setLevel(logging.ERROR)

# =============================================================================
# --- 1. YAHOO FINANCE SEARCH FUNCTION (PUBLIC API) ---
# =============================================================================

def search_company_yahoo(query: str) -> list[tuple[str, str]]:
    """
    Queries the public Yahoo Finance search API to retrieve company suggestions.
    Demonstrates real-time API interaction and error handling within the UI.
    """
    if not query or len(query) < 2: 
        return []
        
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": query, "quotesCount": 6, "newsCount": 0}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=3)
        response.raise_for_status() 
        data = response.json()
        
        results = []
        for quote in data.get('quotes', []):
            if quote.get('quoteType') == 'EQUITY':
                symbol = quote.get('symbol', '')
                name = quote.get('shortname', quote.get('longname', ''))
                exchange = quote.get('exchDisp', '')
                
                label = f"{symbol} - {name} ({exchange})"
                results.append((label, symbol))
                
        return results
        
    except requests.exceptions.Timeout:
        st.warning("Network Error: Yahoo Finance search is currently slow.")
        return []
    except requests.exceptions.RequestException:
        # Silently fail for UI demo purposes
        return []
    except Exception:
        return []

# =============================================================================
# --- 2. STREAMLIT UI CONFIGURATION & STYLING ---
# =============================================================================

st.set_page_config(
    page_title="OnePager Terminal", 
    page_icon="🏛️", 
    layout="centered",
    initial_sidebar_state="expanded" 
)

# Inject custom institutional CSS
st.markdown("""
    <style>
    /* 1. Controlled Pull-Up & Bottom Clearance for Footer */
    .block-container { padding-top: 2rem !important; padding-bottom: 100px !important; }
    
    /* 2. Hide unnecessary elements BUT keep sidebar toggle */
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0); }
    .stAppDeployButton, #MainMenu { display: none; }
    [data-testid="stSidebarCollapseButton"] { visibility: visible !important; color: #DC241F !important; }
    
    /* 3. Button Styling */
    .stButton>button {
        width: 100%; background-color: #DC241F; color: white;
        font-weight: bold; border-radius: 8px; padding: 10px;
        border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #B01D18; color: white; }
    
    /* 4. Spinner Styling */
    .modern-spinner {
        border: 3px solid rgba(220, 36, 31, 0.2); border-left-color: #DC241F;
        border-radius: 50%; width: 18px; height: 18px;
        animation: spin 1s linear infinite; margin-right: 10px;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    
    /* 5. Status Box */
    .status-box {
        padding: 8px 12px; border-radius: 6px; background-color: rgba(128, 128, 128, 0.1);
        border-left: 4px solid #DC241F; display: flex; align-items: center;
        margin-top: 10px; margin-bottom: 10px;
    }
    
    /* 6. Fixed Footer Styling */
    .fixed-footer {
        position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;
        padding-bottom: 15px; background-color: #0e1117; z-index: 1000;
    }
    /* Symmetry adjustment: matches the top line's width (max-width of centered layout) */
    .fixed-footer hr {
        margin: 0 auto 4px auto; width: 95%; max-width: 730px; 
        border: 0; border-top: 1px solid rgba(128, 128, 128, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: left;">
        <h1 style="margin-bottom: 0px; padding-bottom: 0px; font-size: 2.5rem;">One-Pager Generator</h1>
        <p style="font-style: italic; color: #888; margin-top: 5px; margin-bottom: 15px;">
            AI-Automated Financial Analysis by Guillaume OTTOLINI
        </p>
        <hr style="margin-top: 0px; margin-bottom: 25px; border: 0; border-top: 1px solid rgba(255,255,255,0.2);">
    </div>
""", unsafe_allow_html=True)

# =============================================================================
# --- 3. FIXED FOOTER (CONTACT LINKS) ---
# =============================================================================

st.markdown("""
    <div class="fixed-footer">
        <hr>
        <div style="margin-top: 2px; margin-bottom: 4px; font-size: 0.80em;">
            <a href="mailto:guillaume.ottolini@rennes-sb.com" target="_blank" style="text-decoration: none; margin: 0 15px; color: #a0a0a0; text-transform: uppercase; letter-spacing: 1px;">Email</a>
            <span style="color: #444;">|</span>
            <a href="https://www.linkedin.com/in/guillaume-ottolini/" target="_blank" style="text-decoration: none; margin: 0 15px; color: #a0a0a0; text-transform: uppercase; letter-spacing: 1px;">LinkedIn</a>
            <span style="color: #444;">|</span>
            <a href="https://github.com/guillaume-ottolini" target="_blank" style="text-decoration: none; margin: 0 15px; color: #a0a0a0; text-transform: uppercase; letter-spacing: 1px;">GitHub</a>
        </div>
        <p style='color: #666; font-size: 10px; margin: 0; letter-spacing: 0.5px;'>
            Tool developed for academic and research purposes.
        </p>
    </div>
""", unsafe_allow_html=True)

# =============================================================================
# --- 4. SIDEBAR: THE GATEKEEPER & API SECURITY ---
# =============================================================================

with st.sidebar:
    st.markdown("### 🏛️ Institutional Access")
    
    # Initialize session state for access validation
    if "access_granted" not in st.session_state:
        st.session_state["access_granted"] = False
        
    # 1. THE GATEKEEPER (Hides itself after successful validation)
    if not st.session_state["access_granted"]:
        st.info("Demo Mode: This public version simulates pipeline execution.")
        access_code = st.text_input("Invitation Code", type="password", placeholder="Enter access code...")
        
        VALID_CODES = "RSB2026"
        
        if access_code:
            if access_code in VALID_CODES:
                st.session_state["access_granted"] = True
                st.rerun() # Immediately refreshes the UI to hide the input box
            else:
                st.warning("⛔ Valid Invitation Code required to access the terminal.")
        st.stop() # Halts execution for unauthorized users

    # If code is valid, show success and proceed directly to API Key
    st.success("🔓 Access Granted. Welcome.")
    st.markdown("---")

    # 2. THE BYOK PROTOCOL (Bring Your Own Key) with Helper Link
    st.markdown("### 🔑 API Authentication")
    st.caption("Your key is not stored and is only used for this session.")
    
    with st.form("api_key_form"):
        temp_key = st.text_input(
            "Gemini API Key", 
            type="password", 
            placeholder="AIzaSy...",
            help="Get a free API key at https://aistudio.google.com/app/apikey"
        )
        submit_key = st.form_submit_button("Authenticate")

    if submit_key:
        if temp_key.startswith("AIza"):
            st.session_state['user_api_key'] = temp_key
            st.success("✅ Secure Connection Established!")
        else:
            st.error("❌ Invalid Key Format. Should start with 'AIza'.")
    
    user_api_key = st.session_state.get('user_api_key', '')

    if not user_api_key:
        st.info("💡 Enter your key and validate to enable analysis.")
        st.stop() # Prevents pipeline execution without a key

# =============================================================================
# --- 5. MAIN INPUTS ---
# =============================================================================

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**🔍 Search Company:**")
    ticker_input = st_searchbox(
        search_company_yahoo,
        key="searchbox_yahoo",
        placeholder="Type a name or ticker (e.g., LVMH)...",
        clear_on_submit=False
    )

with col2:
    st.markdown("**🧠 AI Engine:**")
    ai_mode = st.selectbox(
        "Selection", 
        ["Gemini-2.5-Flash"], 
        label_visibility="collapsed"
    )

st.markdown("<p style='font-size: 0.85em; color: #b8860b; margin-top: -10px;'>⚠️ Pipeline execution takes approximately 10-15 seconds.</p>", unsafe_allow_html=True)

# =============================================================================
# --- 6. PIPELINE ORCHESTRATION SIMULATOR ---
# =============================================================================

if ticker_input:
    if st.button(f"🚀 INITIATE ANALYSIS ({ticker_input})"):
        
        progress_bar = st.progress(0)
        status_container = st.empty()
        
        def update_ui_progress(message: str, percent: int):
            html_content = f"""
                <div class="status-box">
                    <div class="modern-spinner"></div>
                    <span style="font-weight: 600; font-size: 0.95em;">{message}...</span>
                </div>
            """
            status_container.markdown(html_content, unsafe_allow_html=True)
            progress_bar.progress(percent)
        
        # --- SIMULATION OF THE PRE-FLIGHT CHECK ---
        update_ui_progress("Verifying API Key and checking quotas", 5)
        time.sleep(1)
        
        # --- SIMULATION OF THE QUANTAMENTAL PIPELINE ---
        update_ui_progress(f"Acquiring global Mutex lock for {ticker_input}", 15)
        time.sleep(1.5)
        
        update_ui_progress("Fetching live market data and computing Two-Stage DCF", 35)
        time.sleep(2)
        
        update_ui_progress("Executing Gemini AI synthesis (Deterministic Grounding)", 65)
        time.sleep(2.5)
        
        update_ui_progress("Rendering vector graphics and benchmarking peers", 85)
        time.sleep(1.5)
        
        update_ui_progress("Compiling final ReportLab PDF Layout", 95)
        time.sleep(1)
        
        # --- SUCCESS STATE ---
        progress_bar.progress(100)
        status_container.success(f"✅ One-Pager successfully generated for {ticker_input} in 8.5s!")
        
        st.download_button(
            label="📥 DOWNLOAD REPORT (DEMO)",
            data=b"Simulated PDF content. The actual PDF engine is restricted.",
            file_name=f"Equity_Research_{ticker_input}_DEMO.pdf",
            mime='application/pdf'
        )
        
        st.info("ℹ️ **Showcase Notice:** This public application simulates the orchestration logic. The proprietary quantitative models (`data_engine`) and AI sanitization layers (`ai_engine`) are executed securely in the private backend.")