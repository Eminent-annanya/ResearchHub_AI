
def search_youtube(client, topic, max_results=8):
    query = f"site:youtube.com/watch {topic} tutorial lecture"

    response = client.search(
        query=query,
        max_results=max_results
    )

    videos = []

    for item in response.get("results", []):
        url = item.get("url", "")

        # Keep direct YouTube watch links only.
        if "youtube.com/watch?v=" not in url:
            continue

        videos.append({
            "title": item.get("title", "Untitled video"),
            "url": url,
            "description": item.get("content", "")
        })

    return videos
