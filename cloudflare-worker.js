// Cloudflare Worker for Live Countdown Image Generation
// Deploy this at workers.cloudflare.com for true live countdown

export default {
  async fetch(request, env, ctx) {
    // Target: May 5, 2026 at 11:00 AM CDT = 16:00 UTC
    const targetDate = new Date('2026-05-05T16:00:00Z');
    const now = new Date();
    const diff = targetDate - now;

    let days = 0, hours = 0, minutes = 0, seconds = 0;

    if (diff > 0) {
      days = Math.floor(diff / (1000 * 60 * 60 * 24));
      hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      seconds = Math.floor((diff % (1000 * 60)) / 1000);
    }

    // Since Cloudflare Workers can't easily run Python/Pillow,
    // this Worker returns HTML with a client-side countdown
    // For a true image, you'd need to use @vercel/og or similar

    const html = `
    <!DOCTYPE html>
    <html>
    <head>
      <meta http-equiv="refresh" content="1">
      <style>
        body { margin:0; background:#0a1628; font-family: Arial, sans-serif; }
        .container { width:1024px; height:250px; background:#0a1628; position:relative; }
        .title { color:#f2c71e; font-size:32px; font-weight:bold; text-align:center; padding-top:15px; }
        .countdown { display:flex; justify-content:center; gap:40px; padding-top:20px; }
        .block { text-align:center; }
        .number { color:white; font-size:80px; font-weight:bold; }
        .label { color:white; font-size:22px; font-weight:bold; text-transform:uppercase; }
        .separator { color:#f2c71e; font-size:60px; padding-top:20px; }
        .date { color:white; font-size:18px; text-align:center; padding-top:15px; }
        .border { position:absolute; top:10px; left:30px; right:30px; bottom:10px; 
                  border:3px solid #f2c71e; border-radius:15px; pointer-events:none; }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="border"></div>
        <div class="title">THE DATE IS ALMOST HERE!</div>
        <div class="countdown">
          <div class="block">
            <div class="number">${String(days).padStart(2,'0')}</div>
            <div class="label">DAYS</div>
          </div>
          <div class="separator">|</div>
          <div class="block">
            <div class="number">${String(hours).padStart(2,'0')}</div>
            <div class="label">HOURS</div>
          </div>
          <div class="separator">|</div>
          <div class="block">
            <div class="number">${String(minutes).padStart(2,'0')}</div>
            <div class="label">MINUTES</div>
          </div>
          <div class="separator">|</div>
          <div class="block">
            <div class="number">${String(seconds).padStart(2,'0')}</div>
            <div class="label">SECONDS</div>
          </div>
        </div>
        <div class="date">Countdown as of ${now.toLocaleDateString('en-US', {month:'long', day:'numeric', year:'numeric'})}</div>
      </div>
    </body>
    </html>`;

    return new Response(html, {
      headers: {
        'Content-Type': 'text/html',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      }
    });
  }
};
