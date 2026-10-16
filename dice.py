import random, re, sys
FACES = "⚀⚁⚂⚃⚄⚅"
def roll(expr):
    m = re.fullmatch(r"(\d*)d(\d+)([+-]\d+)?", expr.strip().lower())
    if not m: raise SystemExit("格式示例：2d6、1d20+3")
    n, sides, mod = int(m[1] or 1), int(m[2]), int(m[3] or 0)
    rolls = [random.randint(1, sides) for _ in range(n)]
    show = " ".join(FACES[r - 1] if sides == 6 else f"[{r}]" for r in rolls)
    total = sum(rolls) + mod
    print(f"🎲 {expr}: {show}  {'%+d' % mod if mod else ''} = {total}")
    if sides == 20 and n == 1 and rolls[0] == 20: print("✨ 大成功！")
    if sides == 20 and n == 1 and rolls[0] == 1: print("💀 大失败……")
if __name__ == "__main__":
    for e in (sys.argv[1:] or ["2d6"]): roll(e)
