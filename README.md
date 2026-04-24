# WorldLink Truck Driving Academy - Live Email Countdown

## Overview
This repository generates a live countdown image for the WorldLink Truck Driving Academy 5-Year Anniversary event on **May 5, 2026**.

## How It Works
- GitHub Actions runs every 15 minutes to regenerate the countdown image
- The email references the raw GitHub URL with cache-busting
- When recipients open the email, they see the current countdown

## Files
- `generate_countdown.py` - Python script that generates the countdown PNG
- `flyer_top.png` - Static top portion of the flyer
- `flyer_bottom.png` - Static bottom portion of the flyer  
- `countdown.png` - Dynamic countdown section (auto-updated by Actions)
- `email_template.html` - Complete email HTML for Google Workspace
- `.github/workflows/update-countdown.yml` - GitHub Actions workflow

## Setup Instructions

### 1. Create a New GitHub Repository
- Go to github.com and create a new public repository
- Name it something like `wltda-countdown`

### 2. Upload These Files
Upload all files from this package to your repository:
- `generate_countdown.py`
- `flyer_top.png`
- `flyer_bottom.png`
- `email_template.html`
- `.github/workflows/update-countdown.yml`

### 3. Enable GitHub Actions
- Go to **Settings > Actions > General**
- Make sure "Allow all actions and reusable workflows" is selected
- The workflow will start running automatically

### 4. Get Your Raw GitHub URLs
Replace `YOUR_USERNAME` and `YOUR_REPO` in the email template with your actual GitHub username and repository name.

Your URLs will look like:
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/flyer_top.png
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/countdown.png
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/flyer_bottom.png
```

### 5. Send the Email
- Copy the HTML from `email_template.html`
- Paste into Google Workspace email composer (use HTML mode)
- Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual values
- The `?t={{timestamp}}` parameter is a cache-busting trick - Gmail ignores it but it forces some clients to re-check the image

## Important Notes

### Cache Busting Limitation
**Gmail aggressively caches images.** Once a recipient opens the email, Gmail caches the image and won't re-fetch it for hours or days. This means:
- First open: Shows accurate countdown
- Subsequent opens: May show stale cached image
- **Workaround:** The `?t=` parameter helps, but Gmail often ignores query strings for caching

### For TRUE Live Countdown (Best Results)
If you want a truly live countdown that updates every time the email is opened, use **Cloudflare Workers** (free tier):
1. Deploy a simple Worker that generates the image on-demand
2. Use a URL like `https://your-worker.workers.dev/countdown.png`
3. This generates a fresh image on every request with no caching issues

See the `cloudflare-worker.js` file in this repo for the Worker code.

## Event Details
- **Date:** Tuesday, May 5, 2026
- **Time:** 11:00 AM - 2:00 PM CDT
- **Location:** 330 Mid State Truck Plaza, North Little Rock, AR
- **Target:** 5 Year Anniversary Celebration
