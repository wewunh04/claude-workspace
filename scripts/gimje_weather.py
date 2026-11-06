"""전북 김제 날씨·미세먼지를 가져와 weather/weather.txt 에 저장합니다 (덮어쓰기).

- 데이터: Open-Meteo 무료 API (가입·API 키 필요 없음)
- 미세먼지 값은 위성·모델 기반 추정값이라 에어코리아 측정소 값과 다를 수 있어요.
- 실패하면 weather.txt는 그대로 두고 weather/error.log 에 이유를 남겨요.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

LAT, LON = 35.80, 126.88  # 전북 김제시
PLACE = "전북 김제"

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "weather" / "weather.txt"
ERR = BASE / "weather" / "error.log"

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    "&current=temperature_2m,apparent_temperature,relative_humidity_2m,"
    "weather_code,wind_speed_10m,wind_direction_10m"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
    "&timezone=Asia%2FSeoul&wind_speed_unit=ms&forecast_days=1"
)
AIR_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
    f"?latitude={LAT}&longitude={LON}"
    "&current=pm10,pm2_5&timezone=Asia%2FSeoul"
)

# WMO 날씨 코드 → 한국어
WMO = {
    0: "맑음", 1: "대체로 맑음", 2: "구름 조금", 3: "흐림",
    45: "안개", 48: "서리 안개",
    51: "약한 이슬비", 53: "이슬비", 55: "강한 이슬비",
    56: "약한 어는 이슬비", 57: "어는 이슬비",
    61: "약한 비", 63: "비", 65: "강한 비",
    66: "약한 어는 비", 67: "어는 비",
    71: "약한 눈", 73: "눈", 75: "강한 눈", 77: "싸락눈",
    80: "약한 소나기", 81: "소나기", 82: "강한 소나기",
    85: "약한 눈 소나기", 86: "강한 눈 소나기",
    95: "뇌우", 96: "우박 동반 뇌우", 99: "강한 우박 동반 뇌우",
}
DIRS = ["북", "북동", "동", "남동", "남", "남서", "서", "북서"]
DAYS = "월화수목금토일"


def grade_pm10(v):  # 환경부 기준
    return "좋음" if v <= 30 else "보통" if v <= 80 else "나쁨" if v <= 150 else "매우 나쁨"


def grade_pm25(v):
    return "좋음" if v <= 15 else "보통" if v <= 35 else "나쁨" if v <= 75 else "매우 나쁨"


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "gimje-weather-script"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def main():
    w = get_json(WEATHER_URL)
    a = get_json(AIR_URL)
    c, d, ac = w["current"], w["daily"], a["current"]

    now = datetime.now()
    wind_dir = DIRS[round(c["wind_direction_10m"] / 45) % 8]
    pm10, pm25 = ac["pm10"], ac["pm2_5"]
    rain = d["precipitation_probability_max"][0]

    text = "\n".join([
        f"===== {now:%Y-%m-%d} ({DAYS[now.weekday()]}) {now:%H:%M} · {PLACE} =====",
        f"날씨: {WMO.get(c['weather_code'], '알 수 없음')} / 기온 {c['temperature_2m']:.1f}℃ "
        f"(체감 {c['apparent_temperature']:.1f}℃) / 습도 {c['relative_humidity_2m']}%",
        f"오늘: 최저 {d['temperature_2m_min'][0]:.0f}℃ · 최고 {d['temperature_2m_max'][0]:.0f}℃ · "
        f"강수확률 {rain if rain is not None else '-'}%",
        f"바람: {wind_dir} {c['wind_speed_10m']:.1f}m/s",
        f"미세먼지 PM10: {pm10:.0f}㎍/㎥ ({grade_pm10(pm10)}) · "
        f"초미세먼지 PM2.5: {pm25:.0f}㎍/㎥ ({grade_pm25(pm25)})",
        "",
        "※ 출처: Open-Meteo (미세먼지는 모델 추정값)",
        "",
    ])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, OUT)  # 다 쓴 뒤에 한 번에 교체 → 중간에 끊겨도 파일이 깨지지 않음
    print(text)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        ERR.parent.mkdir(parents=True, exist_ok=True)
        with ERR.open("a", encoding="utf-8") as f:
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} 실패: {e!r}\n")
        print(f"실패: {e!r}", file=sys.stderr)
        sys.exit(1)
