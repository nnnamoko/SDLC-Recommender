import streamlit as st

st.set_page_config(page_title="SDLC Recommender", layout="wide")

st.title("SDLC Recommender (EHU Demo)")

left, right = st.columns([1, 1])

with left:
    st.header("Project Characteristics")

    req_stability = st.slider("Requirements stability", 0, 10, 5)
    risk_level    = st.slider("Technical/Domain risk", 0, 10, 5)
    client_avail  = st.slider("Client availability for frequent feedback", 0, 10, 6)
    deadline_rigid= st.slider("Deadline rigidity", 0, 10, 5)
    team_experience = st.slider("Team experience with domain", 0, 10, 5)
    safety_crit   = st.checkbox("Safety/Regulatory critical system?")
    need_prototype   = st.checkbox("Is an early prototype essential?")
    reuse_assets     = st.checkbox("Significant reusable components exist?")
    parallel_test    = st.checkbox("Strong emphasis on early verification & validation? (V-model)")

def recommend():
    if safety_crit or parallel_test:
        return "V-Model", "High emphasis on verification/validation and traceability suits safety-critical contexts."
    if risk_level >= 7:
        return "Spiral", "High risk → iterative risk mitigation and prototyping each cycle."
    if need_prototype and client_avail >= 6 and req_stability <= 5:
        return "Prototyping", "Unclear requirements + available users → learn by building throwaway/evolutionary prototypes."
    if reuse_assets and req_stability >= 6:
        return "Reuse-based", "Stable goals + existing assets/components → composition and integration."
    if req_stability >= 7 and deadline_rigid >= 7 and client_avail <= 4:
        return "Waterfall", "Stable, well-understood scope with fixed deadline and limited feedback windows."
    if 4 <= req_stability <= 7 and client_avail >= 5:
        return "Incremental", "Deliver functionality in increments while refining requirements."
    return "Incremental", "Balanced choice when signals are mixed; supports staged delivery and learning."

model, why = recommend()

with right:
    st.header("Recommendation")

    st.subheader(f"Recommended model: **{model}**")
    st.write(why)

    st.markdown("#### Rationale snapshot")
    st.json({
        "requirements_stability": req_stability,
        "risk_level": risk_level,
        "safety_critical": safety_crit,
        "client_availability": client_avail,
        "deadline_rigidity": deadline_rigid,
        "team_experience": team_experience,
        "need_prototype": need_prototype,
        "reuse_assets": reuse_assets,
        "emphasis_on_VV": parallel_test
    })

