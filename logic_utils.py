"""
 Logic utilities for the guessing game.

This module intentionally contains only two functions used by the app/tests:
- check_guess(guess, secret) -> "Win" | "Too High" | "Too Low"
- get_hint_message(outcome) -> user-facing hint string
"""


def check_guess(guess, secret):
    g, s = int(guess), int(secret)
    if g == s:
        return "Win"
    if g > s:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome):
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""
