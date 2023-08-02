def make_header(text: str, level: int = 1):
    "установка хидера"
    return f'<h{level}>{text}</h{level}>'

print(make_header('уровень 1'))