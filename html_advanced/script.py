for i in range(38):
    filename = f"{i}-index.html"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Page {i}</title>
</head>
<body>
    <h1>Page {i}</h1>
</body>
</html>
""")

print("38 fichiers HTML créés.")