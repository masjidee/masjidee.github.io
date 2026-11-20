---
title: Check-ins & automatic detection
description: Understand manual check-ins, background location, notifications and queued events.
---
Check-ins record observations of entering or leaving a mosque. They do not certify participation in prayer.

## Check in manually

Use the compact **In** and **Out** controls beneath the next-congregation area on Home. Visit-recording consent may be requested first.

Open **☰ → My check-ins / privacy** to review raw records and the available correction/privacy actions. A correction preserves the original observation rather than silently replacing history.

## Enable automatic detection

1. Open **☰ → Automatic detection / device status**.
2. Review the explanation and choose **Enable automatic detection**.
3. Grant the foreground and background location permissions Android requests for this feature.
4. Allow notifications if you want arrival/departure alerts.
5. Check the device-status information after setup.

Automatic detection is optional and can be paused. It uses the phone’s geofence support, not a promise of continuous, exact tracking. A registered geofence does not guarantee the phone will deliver every crossing immediately.

## When you enter or leave

When Android delivers an event, Masjidee first saves it on the phone. If enabled, a local arrival/departure notification does not need to wait for a server response.

Uploads can happen later if the phone is offline or the server is waking. The original recorded event time is preserved. Upload retries depend on Android giving the app an opportunity to run or on reopening Masjidee; reconnecting to the network alone is not a guaranteed immediate retry.

Exact upload retries do not create multiple stored copies of the same event. Separate repeated phone observations can still exist and may be flagged during interpretation.

## If detection is unreliable

Check location permissions, automatic-detection status, the selected mosque and its geofence, notification settings and phone battery restrictions. Force-stopping the app can interrupt background operation. Use manual In/Out as a fallback and report the timing privately to your organizer.

Raw events are retained for **30 days**. [Attendance reports](../attendance/) are separate interpretations of those events.
