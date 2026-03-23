import os
import json

def load_json(output_dir, input_file):
    filename = os.path.splitext(os.path.basename(input_file))[0]
    path = os.path.join(output_dir, f"{filename}.json")

    print(f"Cargando: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_chunks(data):
    chunks = []
    current_text = ""
    current_page = None

    # detectar lista
    items = None
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list):
                items = v
                break
    else:
        items = data

    for item in items:
        if not isinstance(item, dict):
            continue

        text = item.get("content", "").strip()
        page = item.get("page number", 0)

        if not text:
            continue

        # si cambia de página, guardar chunk
        if current_page is not None and page != current_page:
            chunks.append({
                "title": "",
                "content": current_text,
                "page": current_page
            })
            current_text = ""

        current_text += " " + text
        current_page = page

    # último chunk
    if current_text:
        chunks.append({
            "title": "",
            "content": current_text,
            "page": current_page
        })

    print(f"{len(chunks)} chunks creados")
    return chunks


def save_chunks(chunks):
    with open("output/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print("Chunks guardados")
