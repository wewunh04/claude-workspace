-- ─────────────────────────────────────────────────────────────
-- 포트폴리오 방명록 (messages)
-- 사용법: Supabase 대시보드 → SQL Editor → New query → 전체 붙여 넣기 → Run
-- 여러 번 실행해도 안전하게 작성했어요 (if not exists / drop policy if exists).
-- ─────────────────────────────────────────────────────────────

-- 1) 테이블
create table if not exists public.messages (
  id          bigint generated always as identity primary key,
  name        text        not null check (char_length(btrim(name)) between 1 and 30),
  content     text        not null check (char_length(btrim(content)) between 1 and 500),
  created_at  timestamptz not null default now()
);

-- 최신 글부터 빠르게 불러오기
create index if not exists messages_created_at_idx on public.messages (created_at desc);

-- 2) RLS 켜기 (켜는 순간 "허락한 것만" 가능해져요)
alter table public.messages enable row level security;

-- 읽기: 누구나
drop policy if exists "messages_read_all" on public.messages;
create policy "messages_read_all"
  on public.messages for select
  to anon, authenticated
  using (true);

-- 쓰기: 누구나
drop policy if exists "messages_insert_all" on public.messages;
create policy "messages_insert_all"
  on public.messages for insert
  to anon, authenticated
  with check (true);

-- 수정·삭제 정책은 일부러 만들지 않음 → 방문자는 고치거나 지울 수 없음
-- (관리자는 대시보드 Table Editor에서 지울 수 있어요)

-- 3) 방문자는 name, content 두 칸만 넣을 수 있게 (작성 시간 조작 방지)
revoke insert, update, delete on public.messages from anon, authenticated;
grant  select on public.messages to anon, authenticated;
grant  insert (name, content) on public.messages to anon, authenticated;
