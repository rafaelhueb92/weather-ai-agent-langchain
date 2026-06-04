def to_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and "text" in item:
                parts.append(str(item["text"]))
            elif isinstance(item, str):
                parts.append(item)
        return "\n".join(part for part in parts if part).strip()

    return str(content)


def extract_ai_text(response):
    messages = response.get("messages", []) if isinstance(response, dict) else []

    for message in reversed(messages):
        if isinstance(message, dict):
            role = message.get("role") or message.get("type")
            content = message.get("content", "")
        else:
            role = getattr(message, "role", None) or getattr(message, "type", None)
            content = getattr(message, "content", "")

        if role in {"ai", "assistant"}:
            text = to_text(content)
            if text:
                return text

    return "I couldn't generate a response right now."
