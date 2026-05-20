@echo off
start "" cmd /c "D: && cd \HR_ATTRITION_PREDICTION_APP && streamlit run app.py"
timeout /t 4 > nul
start http://localhost:8501
exit