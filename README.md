🧠 SDLC Recommender Tool

A teaching-focused decision support tool for selecting Software Development Life Cycle models.

⚡ Live Demo (Streamlit Cloud)

👉 https://<https://sdlc-recommender-nn.streamlit.app/
<img width="1291" height="133" alt="image" src="https://github.com/user-attachments/assets/48143aa6-1406-4695-8087-3b544e7b7f74" />
>
(Replace this with your actual URL after deployment)

Try the fully interactive version directly in your browser — no installation required.

📊 Demo Preview

(Replace the placeholder with an actual GIF later)

<p align="center"> <img src="https://via.placeholder.com/700x380.gif?text=Demo+GIF+Placeholder" alt="Demo GIF"/> </p>

🏷️ Badges
<p align="left"> <img src="https://img.shields.io/badge/Python-3.10+-blue" /> <img src="https://img.shields.io/badge/Streamlit-Enabled-red" /> <img src="https://img.shields.io/badge/Status-Active-brightgreen" /> <img src="https://img.shields.io/badge/License-MIT-yellow" /> </p>
📁 Repository Contents
File	Description
sdlc_recommender.py	Main Streamlit application (interactive UI + logic).
requirements.txt	Python dependencies needed to run the app locally.
README.md	Project documentation.
🧠 What This Tool Does

The SDLC Recommender is an interactive teaching tool designed to help students understand how different SDLC methodologies apply to different types of software projects.

It evaluates factors such as:

Requirement stability

Technical & domain risk

Safety/regulatory constraints

Client availability

Deadline rigidity

Reusable components

Need for early prototyping

Team experience

Based on these inputs, the tool recommends one of:

Waterfall

Incremental

Prototyping

Spiral

V-Model

Reuse-based model

Each recommendation includes a justification explaining why the model fits the scenario — ideal for teaching and classroom discussion.

🖥️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2️⃣ (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
streamlit run sdlc_recommender.py


The app will open automatically in your browser.

🎯 Purpose of the Project

This tool supports teaching in:

Software Engineering

Systems Analysis & Design

Requirements Engineering

Project Management

It helps students:

Understand the strengths and weaknesses of SDLC models

Experiment with project parameters

Learn how methodological choices affect outcomes

Develop practical reasoning beyond textbook definitions

👨‍🏫 How It Works (Summary)

Internally, the tool uses a transparent rule-based system:

if safety_critical:
    return "V-Model"
if high_risk:
    return "Spiral"
if unclear_requirements and high_client_availability:
    return "Prototyping"
# …and so on


This makes the logic easy for students to follow and discuss.

🌐 Deployment

The app is deployed using Streamlit Cloud, which offers:

Free hosting

Automatic updates on push

Built-in version control

No server maintenance

Once you link your GitHub repo, deployment is automatic.

👥 Contributors
Name	Role
<Nonso Nnamoko>	Lecturer in Computer Science at Edge Hill University
Students in Software Engineering Programme
Streamlit Community	Open-source components
📬 Contact & Feedback

Have suggestions or want to contribute?

Open an issue

Submit a pull request

Or email: <nonsonnamoko@yahoo.com>

📜 License

This project is licensed under the GNU License — feel free to use, modify, and distribute.
