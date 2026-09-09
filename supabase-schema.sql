-- Blasko's Pizza — persistent cloud storage schema
-- Run this in the Supabase SQL Editor after creating your project.
-- Never put a Supabase service-role/secret key in the browser.

create table if not exists public.blaskos_app_state (
  user_id uuid primary key references auth.users(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.blaskos_app_state enable row level security;

drop policy if exists "Users can read their own app state" on public.blaskos_app_state;
drop policy if exists "Users can insert their own app state" on public.blaskos_app_state;
drop policy if exists "Users can update their own app state" on public.blaskos_app_state;
drop policy if exists "Users can delete their own app state" on public.blaskos_app_state;

create policy "Users can read their own app state"
on public.blaskos_app_state for select to authenticated
using (user_id = auth.uid());

create policy "Users can insert their own app state"
on public.blaskos_app_state for insert to authenticated
with check (user_id = auth.uid());

create policy "Users can update their own app state"
on public.blaskos_app_state for update to authenticated
using (user_id = auth.uid())
with check (user_id = auth.uid());

create policy "Users can delete their own app state"
on public.blaskos_app_state for delete to authenticated
using (user_id = auth.uid());

grant select, insert, update, delete on public.blaskos_app_state to authenticated;
revoke all on public.blaskos_app_state from anon;

insert into storage.buckets (id, name, public)
values ('blaskos-private', 'blaskos-private', false)
on conflict (id) do update set public = false;

drop policy if exists "Blaskos users can read their own files" on storage.objects;
drop policy if exists "Blaskos users can upload their own files" on storage.objects;
drop policy if exists "Blaskos users can update their own files" on storage.objects;
drop policy if exists "Blaskos users can delete their own files" on storage.objects;

create policy "Blaskos users can read their own files"
on storage.objects for select to authenticated
using (
  bucket_id = 'blaskos-private'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "Blaskos users can upload their own files"
on storage.objects for insert to authenticated
with check (
  bucket_id = 'blaskos-private'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "Blaskos users can update their own files"
on storage.objects for update to authenticated
using (
  bucket_id = 'blaskos-private'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
)
with check (
  bucket_id = 'blaskos-private'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create policy "Blaskos users can delete their own files"
on storage.objects for delete to authenticated
using (
  bucket_id = 'blaskos-private'
  and (storage.foldername(name))[1] = (select auth.uid()::text)
);

create table if not exists public.blaskos_file_records (
  user_id uuid not null references auth.users(id) on delete cascade,
  db_name text not null,
  store_name text not null,
  record_key text not null,
  data jsonb not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, db_name, store_name, record_key)
);

alter table public.blaskos_file_records enable row level security;

drop policy if exists "Users can read their own file records" on public.blaskos_file_records;
drop policy if exists "Users can insert their own file records" on public.blaskos_file_records;
drop policy if exists "Users can update their own file records" on public.blaskos_file_records;
drop policy if exists "Users can delete their own file records" on public.blaskos_file_records;

create policy "Users can read their own file records" on public.blaskos_file_records for select to authenticated using (user_id = auth.uid());
create policy "Users can insert their own file records" on public.blaskos_file_records for insert to authenticated with check (user_id = auth.uid());
create policy "Users can update their own file records" on public.blaskos_file_records for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "Users can delete their own file records" on public.blaskos_file_records for delete to authenticated using (user_id = auth.uid());

grant select, insert, update, delete on public.blaskos_file_records to authenticated;
revoke all on public.blaskos_file_records from anon;
