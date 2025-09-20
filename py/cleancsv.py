import os
import pandas as pd

script_dir = "/Users/dustin/Developer/Bachelorthesis"
file_path = os.path.join(script_dir, "tables" , "Literaturrecherche.csv")

if os.path.exists(file_path):
    print("File found")
else:
    print("File not found")
    exit()

df = pd.read_csv(file_path)

def latex_escape(s):
    if not isinstance(s, str):
        return s
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
    }
    for key, val in replacements.items():
        s = s.replace(key, val)
    return s

df_clean = df.astype(str).apply(lambda col: col.map(latex_escape))

clean_path = os.path.join(script_dir, "tables" , "Literaturrecherche_clean.csv")
df_clean.to_csv(clean_path, sep=";", index=False, encoding="utf-8")

print("File written successfully")

clean_path

