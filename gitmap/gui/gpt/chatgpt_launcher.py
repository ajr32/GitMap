"""Browser handoff; no ChatGPT API usage or billing."""
import webbrowser


def open_chatgpt() -> bool:
    return webbrowser.open("https://chatgpt.com/", new=1)
