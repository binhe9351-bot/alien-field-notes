#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review - make.fun bounty entry."""
import os

ENTRY = "Earth is a lovely mud ball: the locals worship invisible sky data, trade shiny rocks for sleep, and call shouting at glass rectangles 'socialising'."


def main():
    print(ENTRY)
    for path in ("/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
            break
        except Exception:
            continue


if __name__ == "__main__":
    main()
