🧠 SDLC Recommender Tool

A teaching-focused decision support tool for selecting Software Development Life Cycle models.

⚡ Live Demo (Streamlit Cloud)

👉 https://sdlc-recommender-nn.streamlit.app/

Try the fully interactive version directly in your browser — no installation required.

🏷️ Badges
<p align="left"> <img src="https://img.shields.io/badge/Python-3.10+-blue" /> <img src="https://img.shields.io/badge/Streamlit-Enabled-red" /> <img src="https://img.shields.io/badge/Status-Active-brightgreen" /> <img src="https://img.shields.io/badge/License-GNU-yellow" /> </p>

📁 Repository Contents
File	Description
sdlc_recommender.py	Main Streamlit application (interactive UI + logic).
requirements.txt	Python dependencies needed to run the app locally.
README.md	Project documentation.

🧠 What This Tool Does

The SDLC Recommender is an interactive teaching tool designed to help students understand how different SDLC methodologies apply to different types of software projects.

It evaluates factors such as Requirement stability, Technical & domain risk, Safety/regulatory constraints, Client availability, Deadline rigidity, Reusable components, Need for early prototyping and Team experience.

Based on these inputs, the tool recommends one of Waterfall, Incremental, Prototyping, Spiral, V-Model, and Reuse model.

Each recommendation includes a justification explaining why the model fits the scenario — ideal for teaching and classroom discussion.

🖥️ Run Locally

1️⃣ Clone the repository

```bash
git clone https://github.com/nnnamoko/SDLC-Recommender.git
cd SDLC-Recommender
```


2️⃣ (Optional) Create a virtual environment

```bash
python -m venv venv

source venv/bin/activate     # macOS/Linux

venv\Scripts\activate        # Windows
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Run the app

```bash
streamlit run sdlc_recommender.py
```

The app will open automatically in your browser.

🎯 Purpose of the Project

This tool supports teaching in Software Engineering. It helps students understand the strengths and weaknesses of SDLC models, Experiment with project parameters, Learn how methodological choices affect outcomes and Develop practical reasoning beyond textbook definitions

👨‍🏫 How It Works (Summary)

Internally, the tool uses a transparent rule-based system:

```python
if safety_critical:
    return "V-Model"
if high_risk:
    return "Spiral"
if unclear_requirements and high_client_availability:
    return "Prototyping"
# …and so on
```



This makes the logic easy for students to follow and discuss.

🌐 Deployment

The app is deployed using Streamlit Cloud, which offers: Free hosting, Automatic updates on push, Built-in version control and No server maintenance.

Once you link your GitHub repo, deployment is automatic.

👥 Contributors

| Name                                          | Role                               |
|-----------------------------------------------|------------------------------------|
| **Dr Nonso Nnamoko**                          | SL in Computer Science             |
| **Students in Software Engineering**          | Feedback & Testing                 |
| **Streamlit Community**                       | Open-source components             |


📬 Contact & Feedback

Have suggestions or want to contribute?

Open an issue

Submit a pull request

Or email: nonsonnamoko@yahoo.com

📜 License

This project is licensed under the GNU License — feel free to use, modify, and distribute.
