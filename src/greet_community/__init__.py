"""A greeting package."""


def greet(name: str) -> str:
    target = name.strip() if name and name.strip() else "world"
    return f"Hello, {target}!"
