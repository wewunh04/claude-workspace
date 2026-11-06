# 🚀 포트폴리오 Vercel 배포 안내서

> 이 문서는 나만 보는 안내서예요. 배포되는 사이트에는 포함되지 않아요 (`.vercelignore`).

---

## ✅ 준비된 것

| 파일 | 역할 |
|---|---|
| `index.html` | 포트폴리오 페이지 (이름·학교 일부 가림, 전화번호 가림) |
| `vercel.json` | 깔끔한 주소 + 기본 보안 설정 |
| `.vercelignore` | 백업 파일(`*.bak`)과 이 안내서는 배포 안 함 |

빌드 과정이 없는 **정적 사이트**(HTML 파일 하나)라서 설정할 게 거의 없어요.

---

## 🧭 배포 순서 (처음 한 번만)

1. **https://vercel.com** 접속 → **Continue with GitHub** 로 로그인
   - GitHub 계정 `wewunh04` 로 로그인돼요.
2. 오른쪽 위 **Add New… → Project**
3. **Import Git Repository** 목록에서 `claude-workspace` 옆 **Import**
   - 목록에 안 보이면 **Adjust GitHub App Permissions** → `claude-workspace` 저장소 접근 허용
4. 설정 화면에서 **딱 하나만** 바꾸기:

   | 항목 | 값 |
   |---|---|
   | **Root Directory** | **`portfolio`** ← ⚠️ 가장 중요! **Edit** 눌러서 선택 |
   | Framework Preset | `Other` (자동으로 잡힘) |
   | Build / Output 설정 | 건드리지 않기 |
   | Environment Variables | **넣지 않기** (이 사이트엔 비밀 키가 필요 없어요) |

5. **Deploy** 클릭 → 30초쯤 기다리면 🎉
6. 생긴 주소(예: `https://claude-workspace-xxxx.vercel.app`)로 접속해서 확인

> ⚠️ **Root Directory를 `portfolio`로 꼭 바꾸세요.**
> 안 바꾸면 저장소 전체가 기준이 되어 페이지가 안 보이고,
> `CLAUDE.md`·`SECURITY.md` 같은 파일이 공개될 위험이 있어요.

---

## 🔁 그다음부터 (수정할 때)

`portfolio/index.html` 을 고치고 GitHub에 올리기만 하면 **Vercel이 자동으로 다시 배포**해요.

```
git add portfolio/index.html
git commit -m "포트폴리오 수정"
git push
```

---

## ✏️ (선택) 주소 이름 바꾸기

Vercel 프로젝트 → **Settings → Domains** 에서
`claude-workspace-xxxx.vercel.app` → `원하는이름.vercel.app` 으로 바꿀 수 있어요.

---

## 🔍 배포 후 확인 체크리스트

- [ ] 주소로 접속하면 어두운 배경의 포트폴리오가 보인다
- [ ] 이름이 **박\*호**, 학교가 **전\*대학교**, 번호가 **010-\*\*\*\*-\*\*\*\*** 로 보인다
- [ ] `주소/CLAUDE.md` 로 접속하면 **404 (없는 페이지)** 가 나온다
- [ ] `주소/index.html.bak` 으로 접속하면 **404** 가 나온다
- [ ] 휴대폰으로 열어도 잘 보인다

---

## 📝 공개 전에 바꾸면 좋은 것

페이지에 ✏️ 표시된 **예시 내용**(스킬·경력 1·2번·동아리 캠페인 카드·주요 수강)은
실제 내용으로 바꾸고 배포하는 걸 추천해요.
