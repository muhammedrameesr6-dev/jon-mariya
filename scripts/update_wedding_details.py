import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Title and Meta tags
html = re.sub(r'<title>.*?</title>', '<title>Muhammad &amp; Mufeedha &#8211; Wedding Invitation</title>', html)
html = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Muhammad &amp; Mufeedha | Wedding Invitation">', html)
html = re.sub(
    r'<meta property="og:description" content=".*?">',
    '<meta property="og:description" content="Saturday, 12 December 2026 &middot; 7:00 PM &mdash; Le M&eacute;ridien Dubai Hotel &amp; Conference Centre, Dubai.">',
    html
)

# 2. Gate Section
# Replace cross-ico in gate
gate_bism_old = r'<div class="gate-bism">.*?</div>\s*<div class="gate-eyebrow">.*?</div>'
gate_bism_new = '''<div class="gate-bism" style="font-family:'Cormorant Garamond',serif;font-size:24px;letter-spacing:1px;color:rgba(255,255,255,0.92);font-style:italic;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
    <div class="gate-eyebrow">The Nikkah Ceremony</div>'''
html = re.sub(gate_bism_old, gate_bism_new, html, count=1, flags=re.DOTALL)

html = re.sub(
    r'<div class="gate-names">.*?</div>\s*<div class="gate-rule"></div>\s*<div class="gate-sub">.*?</div>',
    '''<div class="gate-names">Muhammad<span class="gate-amp">&amp;</span>Mufeedha</div>
    <div class="gate-rule"></div>
    <div class="gate-sub">Saturday &middot; 12 December 2026</div>''',
    html,
    count=1
)

# 3. Nav bar
html = re.sub(r'<div class="nav-logo">.*?</div>', '<div class="nav-logo">M &amp; M</div>', html)
html = html.replace('<a href="#party">Kids</a>', '')

# 4. Hero overlay
html = re.sub(
    r'<div class="hero-overlay">\s*<h1 class="ho-names">.*?</h1>\s*<div class="ho-rule"></div>\s*<div class="ho-date">.*?</div>\s*</div>',
    '''<div class="hero-overlay">
    <h1 class="ho-names">Muhammad<span class="ho-amp">&amp;</span>Mufeedha</h1>
    <div class="ho-rule"></div>
    <div class="ho-date">Saturday &middot; 12 December 2026</div>
  </div>''',
    html
)

# 5. Verse Panel
verse_old = r'<div class="hl-bism">.*?</div>\s*<div class="hl-eyebrow">.*?</div>\s*<div class="hl-verse">.*?</div>\s*<div class="hl-tagline">.*?</div>'
verse_new = '''<div class="hl-bism" style="font-family:'Cormorant Garamond',serif;font-size:26px;letter-spacing:2px;color:rgba(255,255,255,0.95);font-weight:500;margin-bottom:8px;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
  <div class="hl-eyebrow">The Auspicious Nikkah &middot; 2026</div>
  <div class="hl-verse">
    &ldquo;And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy.&rdquo;
    <cite>Surah Ar-Rum &middot; 30:21</cite>
  </div>
  <div class="hl-tagline">In the name of Allah, the Most Gracious, the Most Merciful</div>'''
html = re.sub(verse_old, verse_new, html, count=1, flags=re.DOTALL)

# Date strip in verse panel
date_strip_old = r'<div class="hl-date-strip">.*?</div>\s*</section>'
date_strip_new = '''<div class="hl-date-strip">
    <div class="ds-item"><span class="ds-val">12</span><span class="ds-lbl">Date</span></div>
    <div class="ds-item"><span class="ds-val">DEC</span><span class="ds-lbl">Month</span></div>
    <div class="ds-item"><span class="ds-val">2026</span><span class="ds-lbl">Year</span></div>
    <div class="ds-item"><span class="ds-val">7:00</span><span class="ds-lbl">PM</span></div>
  </div>
</section>'''
html = re.sub(date_strip_old, date_strip_new, html, count=1, flags=re.DOTALL)

# 6. Marquee track
marquee_old = r'<div class="marquee-track">.*?</div>'
marquee_new = '''<div class="marquee-track">
    <span class="marquee-item">Muhammad Azeez <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Mufeedha Musthafa <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Nikkah Ceremony &middot; 12 December 2026 <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Le M&eacute;ridien Dubai Hotel &amp; Conference Centre <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Dubai &middot; UAE <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Muhammad Azeez <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Mufeedha Musthafa <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Nikkah Ceremony &middot; 12 December 2026 <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Le M&eacute;ridien Dubai Hotel &amp; Conference Centre <span class="marquee-sep">&#10022;</span></span>
    <span class="marquee-item">Dubai &middot; UAE <span class="marquee-sep">&#10022;</span></span>
  </div>'''
html = re.sub(marquee_old, marquee_new, html, count=1, flags=re.DOTALL)

# 7. Details / Celebrations Section
details_old = r'<section class="details-section" id="details">.*?</section>\s*<!-- GALLERY -->'
details_new = '''<section class="details-section" id="details">
  <div class="details-inner">
    <div class="reveal">
      <p class="s-label">The Auspicious Occasion</p>
      <h2 class="s-title">A blessed union,<br><em>a lifetime of love</em></h2>
      <div class="s-rule"></div>
      <p class="invite-lead">
        In the name of Allah, the Most Gracious, the Most Merciful.<br><br>
        Together with our families, we,<br>
        <b>Mr. Azeez &amp; Mrs. Aruva</b> and <b>Mr. Musthafa &amp; Mrs. Jaseela</b>,<br>
        cordially request the honour of your presence and prayers at the Nikkah Ceremony &amp; Wedding of our beloved children<br>
        <b style="font-size:1.18em;display:inline-block;margin-top:8px;color:#fff;">Muhammad Azeez</b><br>
        <span style="font-family:'Caveat',cursive;font-size:1.4em;color:var(--rose);margin:2px 8px;display:inline-block;">with</span><br>
        <b style="font-size:1.18em;display:inline-block;color:#fff;">Mufeedha Musthafa</b>
      </p>
    </div>

    <div class="ev-list">
      <article class="ev-card ev-card-hero reveal">
        <span class="ev-num">01</span>
        <p class="ev-kicker">Saturday &middot; 12 December 2026</p>
        <h3 class="ev-name">The Nikkah Ceremony</h3>
        <div class="udc-card">
          <div class="udc-row">
            <div class="udc-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></svg>
            </div>
            <div class="udc-text">
              <span class="udc-label">Time</span>
              <span class="udc-val-main">7:00 PM</span>
            </div>
          </div>
          <div class="udc-divider"></div>
          <div class="udc-row">
            <div class="udc-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.6-7-11a7 7 0 0 1 14 0c0 4.4-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
            </div>
            <div class="udc-text">
              <span class="udc-label">Venue</span>
              <span class="udc-val-main">Le M&eacute;ridien Dubai Hotel &amp; Conference Centre</span>
              <span class="udc-val-sub">Airport Road, Garhoud, Dubai, UAE</span>
            </div>
          </div>
          <div class="udc-divider"></div>
          <div class="udc-row">
            <div class="udc-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 21V10l8-6 8 6v11"/><path d="M9 21v-6h6v6"/></svg>
            </div>
            <div class="udc-text">
              <span class="udc-label">Celebration</span>
              <span class="udc-val-main">Royal Wedding Dinner</span>
              <span class="udc-val-sub">Followed immediately after Nikkah</span>
            </div>
          </div>
        </div>
        <div class="udc-actions">
          <a class="udc-btn udc-btn-primary" href="https://maps.app.goo.gl/pz21fAhQ1RfaBLWg9" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-6.6-7-11a7 7 0 0 1 14 0c0 4.4-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
            Venue Location
          </a>
          <a class="udc-btn udc-btn-secondary cal-link" data-ev="nikkah">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/></svg>
            Add to Calendar
          </a>
        </div>
      </article>

      <article class="ev-card reveal">
        <span class="ev-num">02</span>
        <p class="ev-kicker">Saturday &middot; 12 December 2026</p>
        <h3 class="ev-name">Dinner &amp; Reception</h3>
        <div class="udc-card">
          <div class="udc-row">
            <div class="udc-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></svg>
            </div>
            <div class="udc-text">
              <span class="udc-label">Time</span>
              <span class="udc-val-main">8:00 PM onwards</span>
            </div>
          </div>
          <div class="udc-divider"></div>
          <div class="udc-row">
            <div class="udc-icon-box">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.6-7-11a7 7 0 0 1 14 0c0 4.4-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
            </div>
            <div class="udc-text">
              <span class="udc-label">Venue</span>
              <span class="udc-val-main">The Great Ballroom, Le M&eacute;ridien</span>
              <span class="udc-val-sub">Airport Road, Garhoud, Dubai, UAE</span>
            </div>
          </div>
        </div>
        <div class="udc-actions">
          <a class="udc-btn udc-btn-primary" href="https://maps.app.goo.gl/pz21fAhQ1RfaBLWg9" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-6.6-7-11a7 7 0 0 1 14 0c0 4.4-7 11-7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
            Venue Location
          </a>
          <a class="udc-btn udc-btn-secondary cal-link" data-ev="wedding">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/></svg>
            Add to Calendar
          </a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- GALLERY -->'''
html = re.sub(details_old, details_new, html, count=1, flags=re.DOTALL)

# 8. Gallery captions
html = html.replace('<b>Arnold &amp; Angel</b><span>07 &middot; 01 &middot; 2027</span>', '<b>Muhammad &amp; Mufeedha</b><span>12 &middot; 12 &middot; 2026</span>')
html = html.replace('<b>Two hearts, one faith</b><span>Odemthode</span>', '<b>Two hearts, one soul</b><span>Dubai</span>')

# 9. Family Section
family_old = r'<div class="family-grid">.*?</div>\s*<div class="compliments-strip reveal">.*?</div>'
family_new = '''<div class="family-grid">
      <div class="fam-block reveal reveal-d1">
        <div class="fam-head">
          <div class="fam-photo-wrap"><div class="wp-avatar" data-party="groom">M<button class="wp-add no-pdf" type="button" onclick="adminUploadParty('groom')">+ Photo</button><button class="wp-del no-pdf" type="button" aria-label="Remove photo" onclick="adminRemoveParty('groom')">&times;</button></div></div>
          <div class="fam-head-text">
            <div class="fb-name">Muhammad Azeez</div>
            <div class="fb-role">Son of</div>
          </div>
        </div>
        <div class="fb-details">
          <strong>Mr. Azeez</strong><br>
          &amp; <strong>Mrs. Aruva</strong>
        </div>
        <div class="fb-addr">Dubai, United Arab Emirates</div>
      </div>

      <div class="fam-center reveal">
        <div class="fc-line"></div>
        <div class="fc-ring"><div class="fc-inner">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1" aria-hidden="true">
            <circle cx="9" cy="13" r="5.4"/>
            <circle cx="15" cy="13" r="5.4"/>
            <path d="M14 5.2l1-1.6 1 1.6-1 1.2z"/>
          </svg>
        </div></div>
        <div class="fc-line"></div>
      </div>

      <div class="fam-block reveal reveal-d2">
        <div class="fam-head">
          <div class="fam-photo-wrap"><div class="wp-avatar" data-party="bride">M<button class="wp-add no-pdf" type="button" onclick="adminUploadParty('bride')">+ Photo</button><button class="wp-del no-pdf" type="button" aria-label="Remove photo" onclick="adminRemoveParty('bride')">&times;</button></div></div>
          <div class="fam-head-text">
            <div class="fb-name">Mufeedha Musthafa</div>
            <div class="fb-role">Daughter of</div>
          </div>
        </div>
        <div class="fb-details">
          <strong>Mr. Musthafa</strong><br>
          &amp; <strong>Mrs. Jaseela</strong>
        </div>
        <div class="fb-addr">Dubai, United Arab Emirates</div>
      </div>
    </div>

    <div class="compliments-strip reveal">
      <span class="compliments-lbl">With love and best compliments from</span>
      <b>Azeez &amp; Musthafa Families</b>, relatives, and friends
    </div>'''
html = re.sub(family_old, family_new, html, count=1, flags=re.DOTALL)

# Hide #party section since no page boys/flower girls specified
party_old = r'<section class="party-section" id="party">.*?</section>'
html = re.sub(party_old, '<!-- party section hidden -->', html, flags=re.DOTALL)

# 10. Blessing Section
blessing_old = r'<section class="family-blessing">.*?</section>'
blessing_new = '''<section class="family-blessing">
  <div class="fbl-inner reveal">
    <img class="fbl-art" src="assets/dance-couple-red.png" alt="Decorative motif" loading="lazy">
    <div class="fbl-text">
      <p class="fbl-quote">
        &ldquo;May Allah bless your union, shower His blessings upon you, and unite you both in goodness.&rdquo;
      </p>
      <div class="fbl-names">Muhammad &amp; Mufeedha</div>
      <div class="fbl-sub">Saturday, 12 December 2026 &middot; Dubai</div>
    </div>
  </div>
</section>'''
html = re.sub(blessing_old, blessing_new, html, count=1, flags=re.DOTALL)

# 11. Footer
footer_old = r'<div class="ft-center">.*?</div>\s*St\. Sebastian&#8217;s Church<br>\s*Odemthode &middot; Peravoor'
footer_new = '''<div class="ft-center">Muhammad &amp; Mufeedha</div>
    Le M&eacute;ridien Dubai Hotel &amp; Conference Centre<br>
    Airport Road, Garhoud &middot; Dubai, UAE'''
html = re.sub(footer_old, footer_new, html, count=1, flags=re.DOTALL)

html = html.replace('download="Arnold-and-Angel-Wedding-Card.jpg"', 'download="Muhammad-and-Mufeedha-Wedding-Card.jpg"')

# 12. Script Configuration
html = html.replace('var COUPLE_LABEL     = "Arnold & Angel";', 'var COUPLE_LABEL     = "Muhammad & Mufeedha";')
html = html.replace('var WISH_PATH        = "arnold-angel-v1/wishes";', 'var WISH_PATH        = "azeez-mufeedha/wishes";')
html = html.replace('var BGM_PATH         = "arnold-angel/bgm-url";', 'var BGM_PATH         = "azeez-mufeedha/bgm-url";')
html = html.replace('var COVER_PATH       = "arnold-angel/cover-url";', 'var COVER_PATH       = "azeez-mufeedha/cover-url";')
html = html.replace('var HERO_VIDEO_PATH  = "arnold-angel/hero-video-url";', 'var HERO_VIDEO_PATH  = "azeez-mufeedha/hero-video-url";')
html = html.replace('var IMG_PATH         = "arnold-angel/media";', 'var IMG_PATH         = "azeez-mufeedha/media";')
html = html.replace('var PARTY_PATH       = "arnold-angel/party";', 'var PARTY_PATH       = "azeez-mufeedha/party";')
html = html.replace('var COUPLE_FOLDER    = "digiwed-invitations/arnold-angel";', 'var COUPLE_FOLDER    = "digiwed-invitations/azeez-mufeedha";')
html = html.replace('var LS               = "aa_";', 'var LS               = "am_";')
html = html.replace('var ADMIN_PIN        = "2026AA";', 'var ADMIN_PIN        = "2026AM";')
html = html.replace('var DEFAULT_BGM      = "assets/bgm_track.mp3";', 'var DEFAULT_BGM      = "assets/noor-ul-nikah.mp3";')

# Wedding countdown date and CAL
cal_old = r'var WEDDING_UTC = ".*?";\s*/\*.*?\*/\s*var CAL = \{.*?\};'
cal_new = '''var WEDDING_UTC = "2026-12-12T15:00:00Z";           /* Sat 12 Dec 2026, 7:00 PM GST (UTC+4) */
var CAL = {
  nikkah:{
    title:"Nikkah of Muhammad & Mufeedha",
    start:"20261212T150000Z", end:"20261212T180000Z",
    loc:"Le Méridien Dubai Hotel & Conference Centre, Airport Road, Garhoud, Dubai, UAE",
    desc:"The Nikkah Ceremony & Wedding Celebration of Muhammad Azeez & Mufeedha Musthafa — Saturday, 12 December 2026 at 7:00 PM at Le Méridien Dubai Hotel & Conference Centre."
  },
  wedding:{
    title:"Wedding Reception of Muhammad & Mufeedha",
    start:"20261212T160000Z", end:"20261212T200000Z",
    loc:"Le Méridien Dubai Hotel & Conference Centre, Airport Road, Garhoud, Dubai, UAE",
    desc:"Wedding Dinner & Reception of Muhammad Azeez & Mufeedha Musthafa — Saturday, 12 December 2026 at Le Méridien Dubai Hotel & Conference Centre."
  }
};'''
html = re.sub(cal_old, cal_new, html, count=1, flags=re.DOTALL)

# PDF filename
html = html.replace('pdf.save("Arnold-and-Angel-Wedding-Invitation.pdf");', 'pdf.save("Muhammad-and-Mufeedha-Wedding-Invitation.pdf");')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully with new couple details!")
