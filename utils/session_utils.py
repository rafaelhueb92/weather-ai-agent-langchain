from uuid import uuid4


def ensure_thread_id(session_obj):
    thread_id = session_obj.get("thread_id")
    if not thread_id:
        thread_id = str(uuid4())
        session_obj["thread_id"] = thread_id
    return thread_id


def append_message(session_obj, message_type, content):
    messages = session_obj.get("messages", [])
    messages.append({"type": message_type, "content": content})
    session_obj["messages"] = messages
    return messages


def clear_conversation(session_obj):
    session_obj["messages"] = []
    session_obj["thread_id"] = str(uuid4())
