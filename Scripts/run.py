import os
import subprocess

# Script 1: separate_subject_content
subprocess.run(["python", "separator.py"])

# Script 2: sort_emails
subprocess.run(["python", "sortareEmail.py"])

# Script 3: extract_subject_and_content
subprocess.run(["python", "SeparareSubiectDeContinut.py"])

# Script 4: calculate_probabilities
subprocess.run(["python", "CalculProbabilitati.py"])

# Script 5: classify_emails
subprocess.run(["python", "ClasificareaBayesiana.py"])
