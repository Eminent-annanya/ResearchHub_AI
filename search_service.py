
def search_resources(client, topic, resource_type, max_results=8):
    search_query = topic.strip()

    if resource_type == "Books & PDFs":
        search_query += " free legal books PDFs open access"

    elif resource_type == "YouTube tutorials":
        search_query += " site:youtube.com tutorials"

    elif resource_type == "Research papers":
        search_query += " research papers open access"

    response = client.search(
        query=search_query,
        max_results=max_results
    )

    return response.get("results", [])
