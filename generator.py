import json
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("tarifler.json", "r", encoding="utf-8") as f:
    tarifler = json.load(f)

# En yakın tarihteki tarifi seç
tarif = next((t for t in tarifler if t["tarih"] == now), None)

if tarif:
    html = f"""<!DOCTYPE html>
<html lang='tr'>
<head>
  <meta charset='UTF-8'>
  <title>Lezzetin Evi - {tarif['baslik']}</title>
</head>
<body>
  <h1>{tarif['baslik']}</h1>
  <img src="{tarif['resim']}" width="500">
  <h2>Malzemeler</h2>
  <ul>{''.join(f"<li>{m}</li>" for m in tarif['malzemeler'])}</ul>
  <h2>Hazırlık</h2>
  <ol>{''.join(f"<li>{h}</li>" for h in tarif['hazirlik'])}</ol>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as out:
        out.write(html)
else:
    print("Bugüne uygun tarif bulunamadı.")
