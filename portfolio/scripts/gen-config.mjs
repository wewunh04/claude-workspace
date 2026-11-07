// .env.local(또는 환경변수)을 읽어 브라우저용 config.js 를 만듭니다.
// 사용법:
//   로컬 테스트: node scripts/gen-config.mjs          → portfolio/config.js 생성
//   배포(Vercel): node scripts/gen-config.mjs dist     → dist/ 에 index.html + config.js 만 담음
//                (dist/ 에 없는 파일은 인터넷에 공개되지 않아요)
//
// - 환경변수(SUPABASE_URL, SUPABASE_ANON_KEY)가 있으면 그걸 우선 사용 → 나중에 Vercel에서도 그대로 동작
// - 없으면 portfolio/.env.local 에서 읽음
// - 안전장치: anon 키가 아니면(service_role 등) 만들지 않고 멈춤
// - 키 값은 화면에 출력하지 않음
import { readFileSync, writeFileSync, existsSync, mkdirSync, rmSync, copyFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const envPath = join(root, ".env.local");

function readEnvFile(path) {
  if (!existsSync(path)) return {};
  const out = {};
  for (const raw of readFileSync(path, "utf8").replace(/^﻿/, "").split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith("#")) continue;
    const i = line.indexOf("=");
    if (i < 0) continue;
    out[line.slice(0, i).trim()] = line.slice(i + 1).trim().replace(/^["']|["']$/g, "");
  }
  return out;
}

const file = readEnvFile(envPath);
const url = process.env.SUPABASE_URL || file.SUPABASE_URL;
const key = process.env.SUPABASE_ANON_KEY || file.SUPABASE_ANON_KEY;

function fail(msg) {
  console.error(`❌ ${msg}`);
  process.exit(1);
}

if (!url || !key) fail("SUPABASE_URL 과 SUPABASE_ANON_KEY 가 없어요. 로컬: .env.local 에 적기 / Vercel: Settings → Environment Variables 에 추가");
if (!/^https:\/\/[a-z0-9-]+\.supabase\.co\/?$/.test(url)) fail("SUPABASE_URL 형식이 이상해요. (예: https://xxxx.supabase.co)");

// JWT 가운데 부분을 열어 role 확인
let role;
try {
  const payload = JSON.parse(Buffer.from(key.split(".")[1], "base64url").toString("utf8"));
  role = payload.role;
} catch {
  fail("SUPABASE_ANON_KEY 형식이 이상해요.");
}
if (role !== "anon") {
  fail(`이 키의 역할은 "${role}" 이에요. 웹페이지에는 anon 키만 넣어야 해요. 🚨 키 노출 의심 — service_role 키라면 Supabase에서 즉시 재발급하세요.`);
}

const js =
  "// 자동 생성 파일 (scripts/gen-config.mjs) — 직접 고치지 마세요. GitHub에 올라가지 않아요.\n" +
  `window.GUESTBOOK_CONFIG = ${JSON.stringify({ url: url.replace(/\/$/, ""), anonKey: key })};\n`;
const outArg = process.argv[2];
if (outArg) {
  // 배포용: 공개할 파일만 담은 폴더를 새로 만듦
  const outDir = join(root, outArg);
  rmSync(outDir, { recursive: true, force: true });
  mkdirSync(outDir, { recursive: true });
  copyFileSync(join(root, "index.html"), join(outDir, "index.html"));
  writeFileSync(join(outDir, "config.js"), js, "utf8");
  console.log(`✅ ${outArg}/ 준비 완료: index.html, config.js (URL: ${url}, 키: ${key.slice(0, 8)}***, 역할: ${role})`);
} else {
  writeFileSync(join(root, "config.js"), js, "utf8");
  console.log(`✅ config.js 생성 완료 (URL: ${url}, 키: ${key.slice(0, 8)}***, 역할: ${role})`);
}
