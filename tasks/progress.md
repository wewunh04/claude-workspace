# 📝 PROGRESS

> 한 일 요약. **append-only** — 기존 내용은 지우거나 고치지 말고, 아래에 계속 추가만 합니다.

---

## 2026-11-05

- `tasks/` 폴더, `todo.md`, `progress.md` 생성 (작업 기록 시스템 시작)
- `SECURITY.md` 비상 매뉴얼 작성 (OpenRouter / Oracle SSH / WordPress / GitHub 절차 + 예방 체크리스트)
- `README.md` 작성 (폴더 구조, 파일별 역할, 초보자 사용법)
- 결정: 문서에는 실제 위치(OneDrive\박은호\claude-workspace) 사용, `.env`는 OneDrive 밖에 두기로 함
- `Claude.md` → `CLAUDE.md` 이름 변경
- `C:\Users\user\.secrets\.env` 생성 (빈 양식, 폴더 권한을 내 계정+SYSTEM만으로 제한)
- CLAUDE.md의 `.env` 경로 수정 (수정 전 백업: `CLAUDE.md.bak`), README·SECURITY 경로도 맞춤
- 다운로드 폴더 정리: 457개 이동 (images 42 / docs 310 / misc 105), 덮어쓰기·실패 0
  - 확장자 없는 파일 6개, .py, .html → misc / desktop.ini, 과제 폴더 2개는 그대로
  - 되돌리기용 기록: `tasks/downloads-move-log.csv`
- 되돌리기 스크립트 `tasks/restore-downloads.ps1` 작성 (기본 미리보기, `-Execute`로 실행) — 미리보기 시험: 457개 복원 가능 확인

## 2026-11-06

- 관리회계 중간고사 일정 변경 안내 메일 초안 작성 (채팅으로 전달)
- `docs/resume.pdf` 기반 IT 마케팅 자기소개서 초안 (Claude Docs 문서, 777자, 연습용)
- `docs/sample_sales.csv` 분석 + 대시보드 "1분기 판매 분석" 제작 (ORD-2026-0059 매출 입력 오류 발견 → 수량×단가로 보정)
- 김제 날씨·미세먼지 자동 저장
  - `scripts/gimje_weather.py` 작성 (Open-Meteo, API 키 없음) → `weather/weather.txt` 덮어쓰기, 실패 시 `weather/error.log`
  - 작업 스케줄러 `GimjeWeather` 등록: 매일 09:00, 놓친 실행은 켜질 때 실행, 네트워크 있을 때만
  - 확인: 직접 실행 OK, 스케줄러 실행 결과코드 0, 파일 갱신 확인 (다음 실행 2026-11-07 09:00)
- 날씨 디스코드 전송
  - `scripts/send_discord.py` 작성 (Webhook 주소는 `.secrets\.env`의 `DISCORD_WEBHOOK_URL`에서 읽음, 오류 로그에서도 가림)
  - 작업 스케줄러 `GimjeWeather`에 2번째 동작 추가: 날씨 저장 → 디스코드 전송
  - 확인: 직접 전송 응답 204, 스케줄러 실행 결과코드 0, error.log 없음
  - 🚨 사고: `! notepad C:\...` 안내가 Bash에서 `\`가 사라져 webhook 주소가 `claude-workspace\tasks\.env`(OneDrive)에 저장됨
    → 진짜 `.env`로 옮기고 OneDrive 사본 삭제(은호 승인). 남은 일: OneDrive 휴지통 비우기, 웹후크 재발급 권장
- 작업 스케줄러 `GimjeWeather` 실행 시각 09:00 → **07:00** 변경 (다음 실행 2026-11-07 07:00)

## 2026-11-06 — 포트폴리오 웹페이지
- `portfolio/index.html` 새로 만듦 (HTML+CSS 한 파일, 외부 라이브러리 없음)
- 구성: 소개(은호 · 대학생) / 경력 3개(예시 내용) / 연락처(010-****-****, 전화·문자·복사 버튼)
- 반응형 + 다크모드 대응. PC(1280px)·휴대폰(375px) 폭에서 스크린샷으로 확인함
- resume.pdf는 다른 사람(김수민) 샘플이라 내용은 쓰지 않음 (사용자 선택)

## 2026-11-06 — 포트폴리오 개선
- 백업: `portfolio/index.html.bak` (개선 전 버전)
- Pretendard 웹폰트 적용
- 섹션 추가: 스킬(카드 3개) / 프로젝트(그라데이션 카드 3개) / 학력 — 일부 예시 내용(✏️ 주석 표시)
- 스크롤하면 서서히 나타나는 효과, 카드·버튼 마우스 올림 효과 (움직임 줄이기 설정 시 자동으로 꺼짐)
- PC(1280px)·휴대폰(375px) 스크린샷으로 확인함

## 2026-11-06 — GitHub CLI(gh) 설치
- winget으로 `GitHub.cli` 2.103.3 설치 → `C:\Program Files\GitHub CLI\gh.exe`
- `gh --version` 실행 확인함. 로그인(`gh auth login`)은 아직 안 함
- `gh auth login` 완료 → 계정 wewunh04, 프로토콜 HTTPS, 토큰은 윈도우 보안 저장소(keyring)에 보관
