---
title: Privacy & permissions
description: What the current pilot records and which choices you control.
---
This guide describes the current pilot’s behavior. For account-specific privacy questions, contact your pilot organizer through your existing private contact channel.

## Separate choices

| Feature | Why it asks for access |
| --- | --- |
| Nearby mosque search | Foreground location to sort configured mosques by proximity |
| Qibla direction | Foreground location and available direction sensors |
| Automatic mosque check-ins | Explicit recording consent and background location for geofence events |
| Arrival/departure alerts | Notification permission and an enabled alert setting |
| Prayer departure reminders | Notification permission; fixed lead-time reminders do not need background location |

You can use published schedules and learning without enabling automatic check-ins. You can pause detection and change relevant permissions in Android settings.

## Account and learning

The app uses hosted Auth0 sign-in. Learning progress, memberships and assignments belong to your application account. The embedded learning screen is restricted to the student experience.

Choosing another sign-in identity does not automatically merge existing accounts. Use the web profile’s explicit linked-identity flow where available; ask your organizer before creating an unintended duplicate account.

## Visit observations

When recording is enabled, raw records can include the mosque, event type, source, event/device identifiers, recorded times and the saved mosque-location configuration. These observations may be queued on your phone before upload.

Raw visit records expire after **30 days**. Derived visit summaries are kept **until deleted**. Delete-history controls remove live records; historical backup copies expire through the service’s backup retention process. Pausing recording stops collection but is not the same as deleting past history.

Sharing with authorized mosque attendance reporters is **off by default**. Application administrators have separate privileged troubleshooting access to retained raw and derived data. Mosque configuration permissions do not automatically grant attendance-reporting permission.

Geofence observations do not prove prayer attendance, and reporting should not be treated as a complete roster of who was present or absent.

## External services

Published schedules originate in Google Calendar. Sermon links and players can load official Alislam or media-provider content. Maps can open an external mapping service. Those services have their own privacy practices.

The documentation website is a static GitHub Pages site with built-in local documentation search. It does not add advertising or analytics trackers. GitHub may process ordinary hosting request information under its own policies. Public GitHub feedback is visible to other people; never post credentials or personal attendance information there.
