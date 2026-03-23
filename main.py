from parser import parse_pdf
from processor import load_json, create_chunks, save_chunks
from search import search

INPUT = "input/test.pdf"
OUTPUT = "output"

def run():
    # 1. Parsear PDF
    parse_pdf(INPUT, OUTPUT)

    # 2. Cargar JSON
    data = load_json(OUTPUT, INPUT)
    print(data)

    print("\n--- DEBUG JSON ---")
    print(type(data))
    print(data)
    
    # 3. Crear chunks
    chunks = create_chunks(data)

    # 4. Guardar chunks
    save_chunks(chunks)

    # 5. Buscar
    while True:
        q = input("\nBuscar (o 'exit'): ")

        if q == "exit":
            break

        results = search(q, chunks)

        print(f"\nResultados: {len(results)}\n")

        for r in results[:3]:
            print(r["title"])
            print(r["content"][:500])
            print("Página:", r["page"])
            print("---")

        print("\n--- EJEMPLO DE CHUNK ---")
        print(chunks[0])


if __name__ == "__main__":
    run()