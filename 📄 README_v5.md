# Capital Care 360 – Tuku AI Health Strategy Simulator

## 📦 Version: v5.0.0  
**Release Date:** July 2025  
**Status:** 🚀 Public Beta

## 🚀 Overview
Capital Care 360 is a dynamic simulator designed to help individuals and families plan for lifetime healthcare costs and optimize financial decisions. Powered by Tuku, your AI health adviser, the platform blends investment logic, care access, and insurance strategy into a single streamlined experience.

This version introduces a fully integrated lifetime simulation across 6 steps, including:

1. **Profile & Insurance Inputs**
2. **Financial Inputs & Savings Strategy**
3. **Health Outlook & Projected Costs**
4. **Retirement Readiness & Capital Drawdown**
5. **Summary Dashboard with Blind Spot Detection**
6. **AI-Powered Recommendations & Savings Insights**

## 🧠 Key Features
- Real-time surplus/deficit detection
- Capital Care Fund simulation (short/mid/long-term)
- Insurance premium vs. actual care cost comparison
- Retirement drawdown visualization across savings, 401(k), and pension
- Revised retirement income source pie chart (Social Security, 401(k), savings)
- AI-generated care and financial recommendations
- JSON profile upload/download
- Streamlit UI and mobile-friendly display

## ⚠️ Known Limitations

1. **Social Security Estimate:** Calculated as 40% of retirement income. For individuals not eligible, this estimate may be inaccurate.
2. **Other Retirement Income:** Sources such as alimony, annuities, dividends, rental income, or secondary pensions are not yet modeled.
3. **Simplified Healthcare Costs:** Age- and risk-adjusted estimates are used. Specific disease and procedure costs will be available in the subscription release.

## 🖥️ How to Run
From terminal:
```bash
streamlit run main.py
```

## 🗂️ Folder Structure
```
/health_strategy_simulator-v5
├── main.py
├── step_1.py ... step_6.py
├── simulator_core.py
├── /modules/
│   ├── chronic_module.py
│   ├── pension_utils.py
│   ├── cost_library.py
│   ├── recommendation_logic.py
├── /assets/
│   ├── Tuku_Analyst.png
│   ├── Tuku_Concerned.png
├── FAQ.md
├── Capital_Care_360_FAQ_FINAL_v5.pdf
├── Health_Strategy_App_Variable_Lexicon.xlsx
```

## 🏷️ Git Tag
If using Git:
```bash
git tag -a v5.0.0 -m "Tuku AI Health Strategy Simulator v5.0.0 – Public Beta"
```

---

© 2025 Capital Care 360. All rights reserved.
