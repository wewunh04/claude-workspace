"""weather/weather.txt 내용을 디스코드 채널로 보냅니다.

- Webhook 주소는 C:\\Users\\user\\.secrets\\.env 의 DISCORD_WEBHOOK_URL 에서 읽어요.
  (코드에 적지 않고, 화면이나 로그에도 남기지 않아요)
- 오늘 날씨가 아니면(가져오기 실패) 경고 문구를 붙여서 보내요.
- 실패하면 weather/error.log 에 이유를 남겨요.
"""
import json
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ENV = Path(r"C:\Users\user\.secrets\.env")
BASE = Path(__file__).resolve().parent.parent
WEATHER = BASE / "weather" / "weather.txt"
ERR = BASE / "weather" / "error.log"


def webhook_url():
    for line in ENV.read_text(encoding="utf-8-sig").splitlines():
        key, _, value = line.strip().partition("=")
        if key.strip() == "DISCORD_WEBHOOK_URL" and value.strip():
            return value.strip().strip('"\'')
    raise RuntimeError(".env 에 DISCORD_WEBHOOK_URL 이 없어요")


def main():
    text = WEATHER.read_text(encoding="utf-8").strip()
    today = f"{datetime.now():%Y-%m-%d}"
    if today not in text.splitlines()[0]:
        text = "⚠️ 오늘 날씨를 가져오지 못해 마지막 기록을 보내요.\n\n" + text

    body = json.dumps({"username": "김제 날씨", "content": f"```\n{text}\n```"}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url(), data=body, method="POST",
        headers={"Content-Type": "application/json", "User-Agent": "DiscordBot (gimje-weather, 1.0)"},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        print(f"디스코드 전송 완료 (응답 {r.status})")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        msg = repr(e)
        try:  # 혹시라도 오류 문구에 주소가 섞이면 가림
            msg = msg.replace(webhook_url(), "https://discord.com/api/webhooks/***")
        except Exception:
            pass
        ERR.parent.mkdir(parents=True, exist_ok=True)
        with ERR.open("a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} 디스코드 전송 실패: {msg}\n")
        print(f"디스코드 전송 실패: {msg}", file=sys.stderr)
        sys.exit(1)
