import re
import os


def get_terminal_width() -> int:
    return os.get_terminal_size().columns


ANSI_RE = re.compile(r"\x1b\[[0-9;]*m", re.UNICODE)


def center_line(text: str, width: int) -> str:
    visible = ANSI_RE.sub("", text).rstrip("\n")
    pad = max(0, (width - len(visible)) // 2)
    return " " * pad + text


def lerp_color(hex_start, hex_end, t):
    start = [int(hex_start[i : i + 2], 16) for i in (1, 3, 5)]
    end = [int(hex_end[i : i + 2], 16) for i in (1, 3, 5)]
    rgb = tuple(round(a + (b - a) * t) for a, b in zip(start, end))
    return rgb


def colorize(text, r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m"


word = "hello"
for i, ch in enumerate(word):  # распаковали: i = номер, ch = буква
    t = i / (len(word) - 1)  # нормируем t в [0, 1]
    r, g, b = lerp_color("#4ea8ff", "#7f88ff", t)
    print(colorize(ch, r, g, b), end="")  # красим БУКВУ, end="" = без переноса
print()  # финальный перенос строки
