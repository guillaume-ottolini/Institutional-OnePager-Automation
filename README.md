<p align="center">
  <img src="assets/logo_rsb.png" width="135">
</p>

# OnePager: Institutional Equity Research Automation

![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)
![Tier](https://img.shields.io/badge/Grade-Institutional-gold.svg)
![Architecture](https://img.shields.io/badge/Architecture-Cross--Platform-lightgrey.svg)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Online-success.svg)](https://onepager-automation.streamlit.app)

> **Author:** Guillaume OTTOLINI  
> **Concept:** A high-throughput, quantamental pipeline designed to bridge the gap between raw market data and institutional-grade investment thesis generation.  
> 
> 🖥️ **Live Interactive Terminal:** A hosted version of the UI is available for technical review. It requires a personal Gemini API key and an Institutional Access Code ("RSB2026"). *Note: To protect proprietary valuation models, the live application simulates the pipeline orchestration and outputs a placeholder PDF. Please see the `examples/` directory for actual generated reports.*

---

## 🎥 System Demonstration
The GIF below demonstrates the 30-second workflow: 
1. **Secure API Ingestion** (User-provided Gemini Key).
2. **Real-time Ticker Discovery** (Global Benchmark Search).
3. **Automated Pipeline Execution** (Quant Modeling -> AI Synthesis -> PDF Compilation).

![App Demo](assets/app_demo.gif)

---

## 🔒 Repository Notice & Scalability
> **Please Note:** To protect the proprietary logic, algorithmic guardrails, and AI sanitization loops designed for this pipeline, this repository serves as a **functional showcase**. The full backend source code (Data Engines, Mutex Orchestration, Architecture) is kept in a private repository and is available for institutional review or technical recruitment rounds upon request. 

---

## 📄 Sample Output: The Institutional OnePager
*Automated PDF rendering generated in under 30 seconds. Features dynamic typography scaling, dual-axis financial charting, and deterministic AI synthesis.*

<p align="center">
  <a href="examples/OnePager_LVMH.pdf" target="_blank">
    <img src="assets/sample_report.png" alt="Institutional OnePager Sample" width="800" style="border: 1px solid #E6E6E6; border-radius: 5px; transition: transform 0.3s;">
  </a>
</p>
<p align="center">
  <i>(Click the image above to view the full, high-resolution A4 PDF)</i>
</p>

---

## ⚡ Massive Batch Processing & Stress Testing
While the public Streamlit UI is designed for single-ticker lookups, the private backend is engineered for high-frequency parallel execution.

* **S&P 500 Benchmark:** An end-to-end stress test generating complete PDF reports (Data ingestion, DCF valuation, AI synthesis, and Vector rendering) for the entire S&P 500 executed in **3,831 seconds (~7.6 seconds per equity)** on standard, resource-constrained hardware (2017 quad-core architecture).
* **99.6% First-Pass Success Rate:** Successfully processed 501/503 tickers. The system correctly caught and logged fundamental data anomalies (e.g., historical data gaps from $GE and $GEHC corporate spin-offs) without crashing the main execution thread.
* **Resiliency & "Anti-Crash" Systems:** Implements strict fallback loops, dynamic request caching, and API rate-limit firewalls to ensure the pipeline remains unbroken during massive batch runs.
* **Thread Safety:** Leverages `concurrent.futures` and global Mutex locking to prevent memory leaks or data overlapping between different equities in concurrent environments.

### Execution Logs (S&P 500 Run)
![Batch Processing Logs](assets/batch_logs.png)

---

## 📌 Project Vision

The **OnePager Pipeline** is a specialized financial engineering ecosystem that automates the entire lifecycle of equity research. 

Going far beyond simple data extraction, this architecture orchestrates financial data scraping, Discounted Cash Flow (DCF) modeling, AI-driven qualitative synthesis, dynamic chart generation, and algorithmic PDF compilation. It operates as a massive **Quantamental Scanner**, capable of analyzing and generating professional reports for hundreds of global equities in minutes.

---

## ⚙️ Core System Capabilities (The Architecture)

The backend is strictly decoupled into specialized "Engines" to ensure scalability and maximum performance:

<p align="center">
  <a href="assets/OnePager_System_Architecture_V1.pdf" target="_blank">
    <img src="assets/OnePager_System_Architecture_V1.png" alt="OnePager System Architecture" width="800" style="border: 1px solid #E6E6E6; border-radius: 5px; transition: transform 0.3s;">
  </a>
</p>
<p align="center">
  <i>(Click the image above to view the full, high-resolution A4 PDF)</i>
</p>

### 1. The Quantitative Data Engine
* **Dynamic Valuation Modeling:** Implements a proprietary multi-stage intrinsic valuation logic with real-time macroeconomic anchoring via live 10-Year Treasury yields (`^TNX`).
* **Algorithmic Growth Cross-Check:** Validates revenue trajectories against earnings momentum. If historical anomalies are detected, it automatically blends a conservative proxy to prevent broken DCF outputs.
* **Cross-Asset Normalization:** Automated reconciliation of reporting vs. trading currencies (e.g., $USD/EUR$, $EUR/JPY$) and capital structure reconstruction for global ADRs.
* **Risk-Aware Guardrails:** Features proprietary non-linear growth decay algorithms and sector-specific WACC floor/cap calibrations to ensure valuation realism across 11 GICS sectors.

### 2. The Qualitative AI Synthesis
* **Deterministic Data Grounding:** Completely mitigates LLM hallucination by forcing the Generative AI (Gemini 2.5 Flash) to ingest and justify its thesis using the hard math calculated by the quantitative engine.
* **The "Golden Rule" Logic:** Hardcoded institutional directives that teach the AI to weigh fundamental overvaluation against market momentum and corporate "moat" premiums.
* **Defensive JSON Sanitization:** Features a "Shareholder Antivirus" that parses and standardizes unpredictable AI data structures into strict, layout-ready formats.

### 3. Algorithmic Document Engineering
* **Vector Typesetting:** Powered by a custom **ReportLab** implementation featuring an iterative execution loop that calculates text density and dynamically scales font sizes/leading to guarantee perfect A4 boundary adherence.
* **High-DPI Financial Visualization:** Thread-safe rendering of dual-axis performance charts and peer-group benchmarking with automated outlier management (visually clipping extremes while retaining true data labels).

---

## 📂 Public Repository Structure

    OnePager-Public/
    ├── assets/                   # 🖼️ Visual branding, main architecture, performance logs...
    ├── examples/                 # 📄 High-resolution generated PDFs (LVMH, NVDA, etc.)
    ├── app_demo.py               # 🖥️ UI structural preview (Frontend architecture only)
    ├── packages.txt              # 🐧 OS-level dependencies (Fonts & PDF rendering)
    ├── requirements.txt          # 🐍 Python package dependencies
    └── README.md                 # 📖 Project documentation and roadmap

---

## 🛠️ Comprehensive Tech Stack

The pipeline relies on a robust matrix of modern Python libraries, optimized for institutional finance:

* **Quantitative Data & Matrix Math:** `pandas`, `numpy`, `yfinance`
* **Optimization & Execution:** `concurrent.futures` (Parallel dispatch), `threading` (Global Mutex locking for API thread safety), `requests_cache`
* **Artificial Intelligence:** `google-genai` (Structured JSON generation)
* **Visualization & Document Engineering:** `matplotlib` (Headless 'Agg' backend), `seaborn`, `ReportLab` (Platypus layout engine)
* **Frontend:** `streamlit`, `streamlit-searchbox`

---

## 🚀 The Quantamental Roadmap

To maintain academic and professional rigor, the system is continually evolving.

**v2.0 - Infrastructure & AI Independence:**
* 🔄 **Stochastic Modeling:** Implementation of Monte Carlo simulations to generate probability distributions for the DCF intrinsic value.
* 📡 **Institutional API Migration:** Transitioning the data ingestion layer to institutional endpoints (e.g., Bloomberg B-Pipe, FactSet) for higher fidelity fundamental data.
* 🔒 **Local LLM Deployment (Privacy-First):** Migration to locally-hosted open-weights models (e.g., Llama 3 / Mistral) to guarantee zero data leakage, meeting strict institutional compliance for proprietary screening.



**v3.0 - Machine Learning Layer:**
* 📊 **Unsupervised Peer-Group Discovery:** Implementation of K-Means clustering to dynamically identify comparable companies based on high-dimensional fundamental proximity rather than static GICS sector codes.
* 🚨 **Fundamental Anomaly Detection:** Deployment of Isolation Forest models to flag statistically significant pricing dislocations.
* 🎭 **NLP Sentiment Quantification:** Integration of specialized financial transformers (e.g., FinBERT) to convert unstructured news flow into normalized "Sentiment Scores" for cross-asset ranking.
* ⚖️ **Portfolio Optimization Engine:** Transitioning from single-stock analysis to fund allocation by integrating Mean-Variance Optimization (Markowitz).

---

## 📧 Contact & Technical Inquiries

Currently pursuing an M1 in Finance at Rennes School of Business with an exchange at UC3M, I am seeking a **6-month internship in Market Finance** (Equity Research, Sales & Trading) starting in **July 2026**. 

My approach is **Quantamental**: I bridge traditional financial modeling with **Python-driven automation**. By developing data pipelines and integrating AI, I build tools to automate fundamental analysis, scale investment research, and **optimize Front-Office workflows** to support Alpha generation.

For a live demonstration of the pipeline, access to the private backend repository, or professional inquiries, please reach out:

* **LinkedIn:** [Guillaume OTTOLINI](https://www.linkedin.com/in/guillaume-ottolini/)
* **Email:** [guillaume.ottolini@rennes-sb.com](mailto:guillaume.ottolini@rennes-sb.com)
