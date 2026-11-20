---
title: Web attendance reports
description: Find the application administrator’s raw-event and attendance diagnostics.
---
These reports are in the **Smart Learning Buddy web application**, not the embedded Learn screen. They require an active **application administrator** account. Mosque configuration roles alone are insufficient.

## Open the reports

1. Open the learning website in your browser and sign in with your administrator identity.
2. Choose the **Administrator** workspace.
3. In the left menu, open **Mosque attendance reports**.
4. Choose **Raw data** or **Attendance**.
5. Enter any combination of last name, first name, primary identity email and Jamat, then select **Search**.

Filters use literal partial matches. An optional date range uses your browser’s timezone. Results are paged; an empty filter shows retained records across users.

## Raw data

Use this mode to troubleshoot observed events, upload delays, repeated entries, unmatched exits and corrections. Expand diagnostics to see stored event/device/site fields and interpretation retry details.

The report does not hide retained rows because they are uncertain or corrected. Exact HTTP retries were already deduplicated at ingestion, so they cannot appear as separate events. Erased history and records already purged after raw-data retention cannot be recovered through this report.

## Attendance

This mode shows interpreted entry/exit, person, duration, uncertainty flags and calendar matches. Prayer names include available original calendar titles. Other activity candidates can display **activity name (calendar tag)** when a subscribed calendar overlaps the visit.

The reporting job must process raw data before interpreted visits appear. Opening this page does not run that job. Earlier visits may lack activity matches if the required raw/calendar evidence was never retained.

## Understand the time columns

Raw records show UTC, your browser timezone, and the recorded mosque-local timezone. **Person / mosque-local** is not a recorded phone timezone: historical devices did not send that value. Daylight-saving labels matter when comparing events.

## Privileged access

This diagnostic view includes retained records regardless of a person’s mosque-report-sharing choice, including inactive accounts. Report views are audited. Use this access only for authorized administration and troubleshooting; do not export or post people’s records publicly.

Ordinary phone mosque reports continue to require their separate reporting permissions and user sharing. The global diagnostic screen does not prove attendance or absence.
