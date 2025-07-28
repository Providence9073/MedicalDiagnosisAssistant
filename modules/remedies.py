def suggest_remedy(disease):
    remedies = {
        "Malaria": "Take antimalarial drugs. Stay hydrated.",
        "Diabetes": "Control sugar intake. Use insulin if prescribed.",
        "Common Cold": "Rest, hydration, and over-the-counter cold meds.",
        "Hypertension": "Exercise, avoid salt, take prescribed meds.",
    }
    return remedies.get(disease, "Consult a physician for accurate treatment.")