
def generate_report(client, topic, task, results):
    sources = "\n".join(
        f"- {item.get('title', 'Untitled')}: "
        f"{item.get('content', '')} "
        f"(Source: {item.get('url', '')})"
        for item in results[:6]
    )

    prompt = f"""
Topic: {topic}

Task:
{task}

Retrieved web results:
{sources}

Use sources as evidence where relevant.
Include source URLs for factual claims.
Never invent sources or statistics.
Separate facts from uncertain predictions.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are ResearchHub AI, a helpful research "
                    "and learning assistant. Be accurate and clear."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content
