# 📋 TODO

> 오늘 할 일 체크리스트. 작업 시작 시 확인하고, 끝나면 체크(`[x]`)합니다.

---

## 2026-11-05 — 작업 환경 구축

### 1단계: 작업 기록 파일 만들기
- [x] `tasks/` 폴더 생성
- [x] `tasks/todo.md` 생성 (이 파일)
- [x] `tasks/progress.md` 생성

### 2단계: SECURITY.md 비상 매뉴얼 작성  ✅
- [x] 키 노출 시 "멈추기 → 폐기 → 재발급 → 교체 → 이력 확인" 순서 정리
- [x] 서비스별 절차: OpenRouter API 키 / Oracle SSH 키 / WordPress 비밀번호
- [x] 예방 체크리스트 (`.gitignore`, 마스킹 등)

### 3단계: README.md 폴더 구조 정리  ✅
- [x] 폴더 트리 그림
- [x] 각 파일이 무슨 역할인지 설명
- [x] 처음 쓰는 사람을 위한 사용법

### 마무리
- [x] 생성된 파일 실제로 확인
- [x] `progress.md`에 기록

---

## 2026-11-05 — 다운로드 폴더 정리  ✅

대상: `C:\Users\user\Downloads` (파일 458개, 4.3 GB)

### 분류 규칙
| 폴더 | 확장자 | 개수 |
|---|---|---|
| `images/` | .jpeg .jpg .png | 42 |
| `docs/` | .hwp .hwpx .pptx .pdf .xlsx .docx .odt .odp .md | 310 |
| `misc/` | .exe .msi .zip .py .html .mp4 .mov .mp3 .sigstore | 99 |
| ❓ 결정 필요 | 확장자 없는 "2050년 대한민국은…" 6개 (속은 Office 문서 형식) | 6 |
| 그대로 둠 | `desktop.ini`(윈도우 시스템 파일), 폴더 2개(`4001/4002 it회계과제`) | 3 |

### 안전장치
- [ ] 이동 전 `images/docs/misc`가 비어 있는지 확인 (지금은 없음 → 새로 만듦)
- [ ] 같은 이름 파일이 있으면 **덮어쓰지 않고 건너뛰기** + 기록
- [ ] 이동 기록 `tasks/downloads-move-log.csv` 저장 → 언제든 원래 자리로 되돌리기 가능
- [ ] (선택) 전체 복사 백업 4.3 GB

### 실행 순서
- [x] 1. 미리보기(dry-run): images 42 / docs 310 / misc 105 = 457, 충돌 0 (확장자 없는 6개·.py·.html → misc로 결정)
- [x] 2. 실제 이동 + 기록 저장 (`tasks/downloads-move-log.csv`)
- [x] 3. 확인: images 42 / docs 310 / misc 105, 실패·충돌 0, 남은 파일은 desktop.ini뿐
- [x] 4. progress.md 기록

---

## 2026-11-06 — 김제 날씨·미세먼지 자동 저장  (✅ 승인됨: 덮어쓰기 방식)

### 방법 (API 키 필요 없음)
- 데이터: **Open-Meteo** 무료 API (가입·키 없음)
  - 날씨: 현재 기온·체감온도·습도·바람·날씨 상태, 오늘 최고/최저·강수확률
  - 미세먼지: PM10·PM2.5 (위성·모델 기반 추정값, 에어코리아 측정소 값과 다를 수 있음)
- 위치: 전북 김제시 (위도 35.80, 경도 126.88)
- 도구: 이미 설치된 Python 3.12 (추가 설치 없음)
- 자동 실행: Windows **작업 스케줄러**에 매일 09:00 등록

### 만들 파일 (새 파일만, 기존 파일 수정 없음)
- `scripts/gimje_weather.py` — 날씨를 가져와 저장하는 스크립트
- `weather/weather.txt` — 결과 파일 (매일 **오늘 것만 덮어쓰기**)
- `weather/error.log` — 실패했을 때만 생김 (실패하면 weather.txt는 어제 것 그대로 둠)

### 실행 순서
- [x] 1. 스크립트 작성
- [x] 2. 직접 한 번 실행해서 `weather.txt` 내용 확인
- [x] 3. 작업 스케줄러에 "매일 오전 9시" 등록 (작업 이름: `GimjeWeather`)
- [x] 4. 스케줄러로 즉시 1회 실행해서 동작 확인
- [x] 5. progress.md 기록

### 주의
- 9시에 PC가 꺼져 있으면 실행 안 됨 → "놓친 실행은 켜질 때 실행" 옵션 켜기
- 끄고 싶을 땐: 작업 스케줄러에서 `GimjeWeather` 삭제

---

## 2026-11-06 — 날씨 정보 디스코드로 보내기  ✅

### 방법
- 디스코드 **Webhook**(채널 전용 주소)으로 `weather.txt` 내용을 메시지로 보냄
- Webhook 주소는 비밀번호와 같음 → **`C:\Users\user\.secrets\.env`에 직접 저장** (`DISCORD_WEBHOOK_URL=`)
  - 스크립트는 .env에서 읽기만 함, 코드에 주소를 적지 않음, 화면에 출력하지 않음

### 만들 파일 / 바꿀 것
- `scripts/send_discord.py` (새 파일) — weather.txt를 읽어 디스코드로 전송
- 작업 스케줄러 `GimjeWeather`에 2번째 동작 추가: 날씨 저장 → 디스코드 전송 (기존 스크립트는 수정 안 함)

### 실행 순서
- [x] 0. (은호) 디스코드에서 Webhook 만들고 .env에 주소 붙여넣기
- [x] 1. `send_discord.py` 작성
- [x] 2. 직접 한 번 보내서 채널에 메시지 오는지 확인
- [x] 3. 작업 스케줄러에 전송 동작 추가 → 즉시 1회 실행해서 확인
- [x] 4. progress.md 기록

---

## 📌 다음에 할 일 (제안)
- [ ] OneDrive 웹 휴지통에서 `.env` 완전 삭제 (2026-11-06 실수로 tasks\ 에 저장됐던 webhook 주소)
- [ ] (권장) 디스코드 웹후크 삭제 후 새로 만들어 .env 교체
- [x] `.env` 파일을 OneDrive 밖(`C:\Users\user\.secrets\`)에 만들기
- [x] `Claude.md` → `CLAUDE.md` 이름 변경
- [x] CLAUDE.md의 `.env` 경로를 새 위치로 수정 (백업: `CLAUDE.md.bak`)
- [ ] `.env`에 실제 키 값 채워 넣기 (직접 메모장으로)
- [ ] Claude.md의 메인 폴더 경로를 실제 위치로 고칠지 결정하기
- [ ] SECURITY.md의 WordPress 사이트 주소 채워 넣기

---

## 2026-11-06 — 포트폴리오 웹페이지  ✅

결과물: `claude-workspace/portfolio/index.html` (새 파일 1개, 기존 파일 수정 없음)

### 단계
- [x] 1. 내용 정리: 이름·직업·자기소개(CLAUDE.md) + 경력 3개 + 스킬/프로젝트(resume.pdf 참고) + 연락처
- [x] 2. `portfolio/index.html` 작성 — HTML+CSS 한 파일, 외부 라이브러리 없음
      - 섹션: 상단 소개 → 경력 3개(타임라인) → 연락처
      - 반응형: 휴대폰 폭(약 375px)~PC까지, 다크모드 자동 대응
- [x] 3. 기본 브라우저로 열어서 실제로 보이는지 확인
- [x] 4. `progress.md`에 기록

### ❓ 결정 필요
- CLAUDE.md는 "은호 / 대학생", resume.pdf는 "김수민 / 마케팅 매니저(경력 5년+)" — 서로 다른 사람
- resume.pdf 연락처는 `example.com` 등 샘플 값 → 실제 연락처 확인 필요

---

## 2026-11-06 — 포트폴리오 개선 (글꼴 · 섹션 추가 · 움직임)
- [x] 0. `index.html` → `index.html.bak` 백업
- [x] 1. Pretendard 웹폰트 적용
- [x] 3. 섹션 추가: 스킬 / 프로젝트(카드) / 학력 — 예시 내용
- [x] 4. 스크롤 등장 효과 + 마우스 올림(hover) 효과
- [x] 5. PC·휴대폰 폭 스크린샷 확인 → 브라우저 열기 → progress 기록

---

## 2026-11-06 — claude-workspace GitHub 업로드  ✅

### 민감정보 점검 결과
- ✅ API 키·토큰·비밀번호·웹훅 주소: **없음** (`send_discord.py`는 `.secrets\.env`에서 읽음)
- ⚠️ 전화번호: `portfolio/index.html`, `index.html.bak`, `tasks/progress.md`
- ⚠️ 학번·실명이 포함된 파일 이름 목록: `tasks/downloads-move-log.csv` (다운로드 파일 458개 이름)
- ⚠️ `docs/resume.pdf`: 강의 자료 샘플(2.2MB) + 내 이메일 워터마크

### 단계
- [x] 1. `.gitignore` 작성 — `.env`, `*.key`, `*.pem`, `id_rsa*`, `credentials*`, `*.bak`, `__pycache__/`, `desktop.ini` 등 + 결정한 제외 파일
- [x] 2. `README.md` 정리 — 전체 폴더 구조(docs·portfolio·scripts·weather 추가) 반영 (기존본은 `README.md.bak`으로 백업, `.bak`은 업로드 제외)
- [x] 3. `git init` → `git add` → 올라갈 파일 목록 확인 (민감 파일 없는지 재확인)
- [x] 4. 커밋 "Initial setup"
- [x] 5. `gh repo create claude-workspace --private` 로 비공개 저장소 만들고 push
- [x] 6. 비공개 여부·파일 목록 GitHub에서 확인 → progress 기록

---

## 2026-11-06 — 포트폴리오 다크모드 (브랜치 작업)  ✅

### ❓ 결정 필요
- `portfolio/`는 `.gitignore`로 제외 중(전화번호) → git에 올리려면 제외를 풀어야 함

### 단계
- [x] 1. 아직 안 올린 작업 기록(todo/progress) 먼저 main에 커밋
- [x] 2. 새 브랜치 `feature/dark-mode` 만들기
- [x] 3. (결정에 따라) `.gitignore` 수정 / 전화번호 처리
- [x] 4. `portfolio/index.html` 다크 배경 적용 (수정 전 `.bak` 백업)
- [x] 5. 스크린샷으로 PC·휴대폰 확인 → 브라우저로 열어 보여주기
- [x] 6. 확인되면 main에 머지 → GitHub push → 저장소에서 확인 → progress 기록

---

## 2026-11-06 — 포트폴리오 Vercel 배포 준비  ✅
배포(Vercel 연결·Deploy 버튼)는 은호가 직접. Claude는 준비만.

### 단계
- [x] 1. `portfolio/vercel.json` — 깔끔한 주소, 보안 헤더 설정
- [x] 2. `portfolio/.vercelignore` — `*.bak` 백업(진짜 번호 포함)이 배포되지 않게 이중 차단
- [x] 3. `index.html`에 링크 미리보기 정보(설명·제목)와 탭 아이콘 추가
- [x] 4. `portfolio/DEPLOY.md` — Vercel 화면 순서대로 따라 하는 배포 안내서 (Root Directory = `portfolio` 핵심)
- [x] 5. 로컬 확인 → 커밋 → GitHub push → progress 기록

### ⚠️ 알아둘 것
- 배포하면 포트폴리오 페이지가 **인터넷에 공개**됨 (이름 은호, 전주대학교 회계세무학과, 예시 경력 등)
- Root Directory를 `portfolio`로 지정하면 CLAUDE.md·SECURITY.md 등 다른 파일은 공개되지 않음

---

## 2026-11-08 — 포트폴리오 방명록 (Supabase)  ✅
- Supabase 프로젝트: fgkztmdbonqhppgsacqa / anon key: eyJhbGci*** (공개용 키, 값은 .env.local에만)

### 단계
- [x] 1. `supabase/messages.sql` 작성 — messages(id, name, content, created_at) + 글자 수 제한 + RLS(누구나 읽기·쓰기, 수정·삭제 불가)
- [x] 2. 👤 은호: Supabase 대시보드 → SQL Editor 에 붙여 넣고 Run
- [x] 3. `portfolio/.env.local` 에 URL·anon key 저장 + 루트 `.gitignore`·`.vercelignore` 에 추가
- [x] 4. `portfolio/scripts/gen-config.mjs` — .env.local → config.js 생성 (config.js도 git 제외)
- [x] 5. `index.html` 맨 아래(연락처 다음)에 방명록 폼 + 목록 UI (수정 전 .bak 백업)
- [x] 6. 로컬 테스트 준비: `start-local.ps1` 한 번 실행 → http://localhost:5500 열림
- [x] 7. 테스트: 읽기 OK / 수정·삭제는 막히는지 / (OK 받으면) 테스트 글 1개 작성 → 대시보드에서 삭제
- [x] 8. progress 기록 (GitHub 업로드·배포는 하지 않음)

---

## 2026-11-08 — 방명록 배포 사이트 반영
- [ ] 1. `gen-config.mjs`에 배포용 모드 추가: `dist/` 폴더에 index.html + config.js 만 담기 (나머지 파일은 공개 안 됨)
- [ ] 2. `vercel.json`에 빌드 명령·출력 폴더 지정, `dist/`는 git 제외
- [ ] 3. 로컬에서 빌드 시험 (환경변수 방식 + 키 없을 때 실패하는지)
- [ ] 4. 👤 은호: Vercel → claude-workspace-portfolio → Settings → Environment Variables 에 SUPABASE_URL, SUPABASE_ANON_KEY 추가
- [ ] 5. 커밋 → GitHub push → 자동 배포
- [ ] 6. 배포 사이트에서 방명록 동작 + CLAUDE.md 등 404 확인 → progress 기록
