def search(query, chunks):
    results = []

    query = query.lower().strip()

    for c in chunks:
        content = c["content"].lower()

        if query in content:
            results.append(c)

    return results