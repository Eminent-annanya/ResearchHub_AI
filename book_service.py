
import requests

OPEN_LIBRARY_URL = "https://openlibrary.org/search.json"


def search_books(topic, limit=8):
    params = {
        "q": topic,
        "limit": limit,
        "fields": (
            "key,title,author_name,first_publish_year,"
            "cover_i,ebook_access,has_fulltext"
        ),
    }

    response = requests.get(
        OPEN_LIBRARY_URL,
        params=params,
        timeout=15,
        headers={"User-Agent": "ResearchHubAI/1.0"}
    )
    response.raise_for_status()

    books = response.json().get("docs", [])
    results = []

    for book in books:
        access = book.get("ebook_access", "unknown")

        if access == "public":
            status = "Publicly readable"
        elif access == "borrowable":
            status = "Borrow online; availability may vary"
        elif access == "no_ebook":
            status = "No ebook listed"
        elif access == "printdisabled":
            status = "Restricted-access ebook"
        else:
            status = "Access not confirmed"

        cover_id = book.get("cover_i")

        results.append({
            "title": book.get("title", "Untitled"),
            "author": ", ".join(book.get("author_name", [])),
            "year": book.get("first_publish_year", "Unknown"),
            "url": "https://openlibrary.org" + book.get("key", ""),
            "cover": (
                f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
                if cover_id else None
            ),
            "access_status": status,
        })

    return results
