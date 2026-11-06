# 🗂️ claude-workspace

> 은호의 Claude Code 작업 공간입니다.
> 📍 내 컴퓨터 위치: `C:\Users\user\OneDrive\박은호\claude-workspace`

---

## 📁 폴더 구조

```
claude-workspace/
│
├── 📘 CLAUDE.md              Claude의 지침서 (규칙·말투·보안 원칙)
├── 🚨 SECURITY.md            키 노출 시 비상 매뉴얼
├── 📖 README.md              지금 보고 있는 이 파일 (폴더 안내서)
├── 🙈 .gitignore             GitHub에 올리지 않을 파일 목록
│
├── 📂 tasks/                 작업 기록 보관함
│   ├── ✅ todo.md            할 일 · 계획 (체크리스트)
│   ├── 📝 progress.md        한 일 기록 (추가만, 삭제 금지)
│   └── ↩️ restore-downloads.ps1   다운로드 정리 되돌리기 스크립트
│
├── 📂 scripts/               자동화 스크립트
│   ├── 🌤️ gimje_weather.py   김제 날씨·미세먼지 → weather/weather.txt 저장
│   └── 💬 send_discord.py    weather.txt 내용을 디스코드로 전송
│
├── 📂 weather/
│   └── 📄 weather.txt        가장 최근 날씨 결과
│
├── 📂 docs/
│   └── 📊 sample_sales.csv   연습용 매출 샘플 데이터
│
└── 📂 portfolio/             포트폴리오 (다크 테마, 전화번호는 가림)
    └── 🌐 index.html         포트폴리오 웹페이지
```

---

## 📄 파일별 역할

| 파일 | 한 줄 설명 | 언제 보나요? |
|---|---|---|
| [CLAUDE.md](CLAUDE.md) | Claude가 지켜야 할 규칙 모음 | 규칙을 바꾸고 싶을 때 |
| [SECURITY.md](SECURITY.md) | 키 노출 시 대처 순서 | 🚨 비상시 |
| [tasks/todo.md](tasks/todo.md) | 해야 할 일 · 계획 | 작업 **시작** 전 |
| [tasks/progress.md](tasks/progress.md) | 끝낸 일 기록 | 작업 **끝난** 후 |
| [scripts/gimje_weather.py](scripts/gimje_weather.py) | 날씨 가져오기 (API 키 필요 없음) | 날씨 확인할 때 |
| [scripts/send_discord.py](scripts/send_discord.py) | 디스코드 알림 보내기 | 날씨 공유할 때 |

---

## 🔒 GitHub에 올리지 않는 것

| 대상 | 이유 |
|---|---|
| `.env`, `*.key`, `*.pem`, `id_rsa` 등 | 비밀 키·인증 정보 |
| `docs/resume.pdf` | 강의 샘플 자료 (이메일 워터마크) |
| `tasks/downloads-move-log.csv` | 다운로드 파일 이름 목록 (개인정보) |
| `*.bak` | 백업 파일 |

> 🔑 비밀 키 파일 `.env`는 이 폴더에 **없어요**. OneDrive·GitHub에 올라가지 않도록
> 바깥 **`C:\Users\user\.secrets\.env`** 에 둡니다. 자세한 내용은 [SECURITY.md](SECURITY.md) 참고.
>
> ↩️ `restore-downloads.ps1`은 `downloads-move-log.csv`가 있어야 동작해요.
> 이 기록 파일은 **내 컴퓨터에만** 있으니 지우지 마세요.

---

## 🚀 사용법 (처음 쓰는 분용)

### 1. 작업 시작하기
1. 이 폴더에서 Claude Code 실행
2. Claude가 `CLAUDE.md`를 자동으로 읽어요
3. "오늘 할 일 확인해줘" → `todo.md` 확인

### 2. 큰 작업 맡기기
- Claude가 먼저 `todo.md`에 **계획**을 적어 보여줘요
- 계획을 읽고 **"OK"** 해야 실행해요

### 3. 작업 끝내기
- "오늘 한 일 기록해줘" → `progress.md`에 추가돼요

### 4. GitHub에 변경사항 올리기
```
git add .
git commit -m "무엇을 바꿨는지 한 줄"
git push
```

### 5. 🚨 비상시
- Claude에게 **"키 노출 의심"**이라고 말하기
- 또는 [SECURITY.md](SECURITY.md)를 직접 열어서 순서대로 따라 하기

---

## 🔒 꼭 기억할 3가지

1. **비밀 키는 `.env`에만**, 그리고 `.env`는 OneDrive 밖에
2. **위험한 작업**(삭제·덮어쓰기)은 Claude가 먼저 물어봐요 → 꼭 읽고 답하기
3. 키가 새어나간 것 같으면 **지우기보다 폐기가 먼저**

---

*마지막 수정: 2026-11-06 (포트폴리오 추가)*
