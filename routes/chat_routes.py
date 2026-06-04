from flask import Blueprint, redirect, render_template, request, session, url_for

from services.agent_service import invoke_agent
from utils.response_utils import extract_ai_text
from utils.session_utils import append_message, clear_conversation, ensure_thread_id

chat_bp = Blueprint(
    "chat",
    __name__,
)


@chat_bp.route("/")
def home():
    messages = session.get("messages", [])
    return render_template("chat.html", messages=messages)


@chat_bp.route("/send", methods=["POST"])
def send():
    user_message = request.form.get("message", "").strip()
    if not user_message:
        return redirect(url_for("chat.home"))

    thread_id = ensure_thread_id(session)
    append_message(session, "human", user_message)

    response = invoke_agent(user_message, thread_id)
    ai_message = extract_ai_text(response)
    append_message(session, "ai", ai_message)

    return redirect(url_for("chat.home"))


@chat_bp.route("/clear")
def clear():
    clear_conversation(session)
    return redirect(url_for("chat.home"))
