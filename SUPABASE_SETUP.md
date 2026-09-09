# Blasko's Pizza — secure login and persistent storage

The app now has a Supabase integration for:

- Email/password login and password reset.
- Per-user Postgres storage for the complete app data model.
- A private Storage bucket for uploaded documents and evidence.
- Row Level Security so a signed-in user can only access their own rows/files.
- Migration of the existing browser data into the first signed-in account when that account has no cloud data yet.
- Synchronisation/restoration of the app's IndexedDB file stores.

## One-time setup

1. Create a Supabase project.
2. In the Supabase SQL Editor, run `supabase-schema.sql` from this repository.
3. In Supabase Auth, keep Email enabled. Hosted Supabase projects normally require email verification for new accounts unless you change that setting.
4. Copy the Project URL and **Publishable key** into `supabase-config.js`.
5. Deploy the updated repository.
6. Open the app, create the owner account and verify the email if requested.
7. The first sign-in with an empty cloud account migrates the existing browser data into the cloud record.

## Important security rule

Only the browser-safe Publishable key belongs in `supabase-config.js`. Never put a Supabase Secret/Service Role key in this repository or in the browser. The database and Storage policies provide the access control.

## Storage model

- `blaskos_app_state` stores the app's structured records/configuration as JSONB, scoped to the authenticated user.
- `blaskos_file_records` stores the serialised IndexedDB records and references to uploaded blobs.
- `blaskos-private` is a private Storage bucket. Objects are stored under the authenticated user's UUID and protected with Storage RLS.

## Local browser storage

LocalStorage/IndexedDB are retained as a working cache so the existing app remains responsive and can continue to work during temporary connectivity loss. They are no longer intended to be the permanent source of truth once Supabase is configured and the user is signed in.
