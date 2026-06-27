#plans
#This is a program that lets you pick symptoms from a list, then tells you which diseases match those symptoms and what percentage match you have. It's like a simple symptom checker.
# Database of diseases and their symptoms
database = [
        {
                    "name": "Type 2 Diabetes",
                            "symptoms": ["Excessive thirst", "Frequent urination", "Blurred vision", "Fatigue", "Slow-healing sores"],
                                    "treatments": ["Metformin", "Insulin", "Low-carb diet", "Weight loss", "Blood sugar monitoring"]
        },
            {
                        "name": "Hypertension (High Blood Pressure)",
                                "symptoms": ["Asymptomatic", "Headaches", "Shortness of breath", "Nosebleeds", "Visual changes"],
                                        "treatments": ["ACE inhibitors", "Beta-blockers", "Low-sodium diet", "Diuretics", "Exercise"]
            },
                {
                            "name": "Influenza (Flu)",
                                    "symptoms": ["High fever", "Muscle aches", "Chills", "Dry cough", "Fatigue"],
                                            "treatments": ["Rest", "Hydration", "Antivirals (Tamiflu)", "Fever reducers", "Steam inhalation"]
                },
                    {
                                "name": "Pneumonia",
                                        "symptoms": ["Productive cough", "Chest pain", "Fever", "Difficulty breathing", "Nausea"],
                                                "treatments": ["Antibiotics", "Oxygen therapy", "Rest", "Fluids", "Cough suppressants"]
                    },
                        {
                                    "name": "GERD (Acid Reflux)",
                                            "symptoms": ["Heartburn", "Regurgitation", "Chest pain", "Difficulty swallowing", "Sore throat"],
                                                "treatments": ["PPIs", "Antacids", "Small meals", "Avoid trigger foods", "Sleep elevated"]
                        },
                            {
                                        "name": "Asthma",
                                                "symptoms": ["Wheezing", "Shortness of breath", "Chest tightness", "Chronic coughing", "Sleep interruption"],
                                                        "treatments": ["Inhaled corticosteroids", "Albuterol", "Leukotriene modifiers", "Trigger avoidance", "Breathing exercises"]
                            },
                                {
                                            "name": "Hypothyroidism",
                                                    "symptoms": ["Fatigue", "Weight gain", "Cold intolerance", "Dry skin", "Thinning hair"],
                                                            "treatments": ["Levothyroxine", "Hormone monitoring", "Dietary iodine", "Vitamin D", "Exercise"]
                                },
                                    {
                                                "name": "Ania",
                                                        "symptoms": ["Pale skin", "Dizziness", "Cold hands/feet", "Heart palpitations", "Weakness"],
                                                                "treatments": ["Iron supplements", "Vitamin B12", "Folic acid", "Dietary changes", "Treat underlying cause"]
                                    },
                                        {
                                                    "name": "Migraine",
                                                            "symptoms": ["Pulsing head pain", "Nausea", "Light sensitivity", "Sound sensitivity", "Aura"],
                                                                    "treatments": ["Triptans", "NSAIDs", "Dark room rest", "Hydration", "Botox"]
                                        },
                                            {
                                                        "name": "Osteoarthritis",
                                                                "symptoms": ["Joint pain", "Stiffness", "Tenderness", "Loss of flexibility", "Bone spurs"],
                                                                        "treatments": ["Physical therapy", "Weight management", "NSAIDs", "Cortisone shots", "Heat/Cold therapy"]
                                            },
                                                {
                                                            "name": "UTI",
                                                                    "symptoms": ["Burning urination", "Pelvic pain", "Cloudy urine", "Frequent urge", "Strong-smelling urine"],
                                                                            "treatments": ["Antibiotics", "Increased water", "Cranberry supplements", "Phenazopyridine", "Heating pad"]
                                                },
                                                    {
                                                               "name": "Depression",
                                                                       "symptoms": ["Persistent sadness", "Loss of interest", "Sleep changes", "Appetite shift", "Low energy"],
                                                                               "treatments": ["SSRIs", "CBT Therapy", "Exercise", "Mindfulness", "Light therapy"]
                                                    },
                                                        {
                                                                    "name": "Generalized Anxiety",
                                                                            "symptoms": ["Excessive worry", "Restlessness", "Irritability", "Muscle tension", "Difficulty focusing"],
                                                                                    "treatments": ["Benzodiazepines", "SSRIs", "Talk therapy", "Breathing exercises", "Caffeine reduction"]
                                                        },
                                                            {
                                                                        "name": "Appendicitis",
                                                                                "symptoms": ["Sharp lower-right pain", "Nausea", "Vomiting", "Abdominal swelling", "Low-grade fever"],
                                                                                        "treatments": ["Appendectomy", "Antibiotics", "IV fluids", "Pain management", "Rest"]
                                                            },
                                                                {
                                                                            "name": "COPD",
                                                                                    "symptoms": ["Chronic cough", "Shortness of breath", "Wheezing", "Excess mucus", "Cyanosis"],
                                                                                            "treatments": ["Bronchodilators", "Oxygen therapy", "Smoking cessation", "Pulmonary rehab", "Steroids"]
                                                                },
                                                                    {
                                                                                "name": "Rheumatoid Arthritis",
                                                                                        "symptoms": ["Swollen joints", "Morning stiffness", "Fatigue", "Fever", "Symmetrical joint pain"],
                                                                                                "treatments": ["DMARDs", "Biologics", "Steroids", "Physical therapy", "Low-impact exercise"]
                                                                    },
                                                                        {
                                                                                    "name": "Psoriasis",
                                                                                            "symptoms": ["Red skin patches", "Silvery scales", "Dry/cracked skin", "Itching", "Swollen joints"],
                                                                                                    "treatments": ["Topical steroids", "Phototherapy", "Biologics", "Moisturizers", "Salicylic acid"]
                                                                        },
                                                                            {
                                                                                        "name": "Sleep Apnea",
                                                                                                "symptoms": ["Loud snoring", "Gasping during sleep", "Morning headache", "Excessive sleepiness", "Irritability"],
                                                                                                        "treatments": ["CPAP machine", "Weight loss", "Sleep on side", "Oral appliances", "Surgery"]
                                                                            },
                                                                                {
                                                                                            "name": "Crohns Disease",
                                                                                                    "symptoms": ["Diarrhea", "Abdominal cramps", "Blood in stool", "Weight loss", "Fever"],
                                                                                                            "treatments": ["Immunosuppressants", "Biologics", "Low-residue diet", "Anti-inflammatory drugs", "Surgery"]
                                                                                },
                                                                                    {
                                                                                                "name": "Hyperthyroidism",
                                                                                                        "symptoms": ["Rapid heartbeat", "Weight loss", "Increased appetite", "Tremors", "Sweating"],
                                                                                                                "treatments": ["Methimazole", "Radioactive iodine", "Beta-blockers", "Thyroidectomy", "Dietary changes"]
                                                                                    }
]