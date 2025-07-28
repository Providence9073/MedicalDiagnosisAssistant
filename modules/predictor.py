import numpy as np

def predict_disease(symptoms, model, label_encoder, all_symptoms):
    input_vector = np.zeros(len(all_symptoms))
    for sym in symptoms:
        if sym in all_symptoms:
            input_vector[all_symptoms.index(sym)] = 1
    pred = model.predict([input_vector])
    return label_encoder.inverse_transform(pred)[0]