from pathlib import Path

SITE = "https://danielle-golf-mindset.web.app"
BRAND = "Danielle Seadia"
ROOT = Path(__file__).parent
ASSET_V = "18"

# FormSubmit only accepts a real inbox until it issues its own random string
# after the first activation. MD5 of the address is not a valid endpoint.
FORM_ACTION = "https://formsubmit.co/daniellespowerteam@gmail.com"

NAV = """
      <nav class="nav" id="site-nav">
        <a href="/" data-nav="index">Home</a>
        <div class="nav-item" data-nav-group="about">
          <button class="nav-trigger" type="button" aria-expanded="false">About</button>
          <div class="nav-drop">
            <a href="/about.html" data-nav="about">Background</a>
            <a href="/philosophy.html" data-nav="philosophy">Philosophy</a>
          </div>
        </div>
        <div class="nav-item" data-nav-group="work">
          <button class="nav-trigger" type="button" aria-expanded="false">Coaching</button>
          <div class="nav-drop">
            <a href="/services.html" data-nav="services">Services</a>
            <a href="/process.html" data-nav="process">How it works</a>
            <a href="/book.html" data-nav="book">Book Now</a>
          </div>
        </div>
        <a href="/stories.html" data-nav="stories">Stories</a>
        <a href="/faq.html" data-nav="faq">FAQ</a>
        <div class="nav-actions">
          <a class="nav-btn nav-btn-alt" href="/services.html">See sessions</a>
          <a class="nav-btn" href="/book.html" data-nav="book">Book Now</a>
        </div>
      </nav>
"""

HEADER = f"""
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/">
        <img class="brand-mark" src="/icons/favicon.svg?v={ASSET_V}" alt="">
        <span class="brand-text">
          <span class="brand-name">{BRAND}</span>
          <span class="brand-sub">Golf Mindset Coaching</span>
        </span>
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <span></span>
      </button>
      {NAV}
    </div>
  </header>
"""

FOOTER = f"""
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <h3 class="footer-brand">{BRAND}</h3>
        <p>Personalized golf mindset coaching by telephone. Nationwide and worldwide, from the Boston, Massachusetts area.</p>
      </div>
      <div>
        <h3>Explore</h3>
        <div class="footer-links">
          <a href="/about.html">Background</a>
          <a href="/philosophy.html">Philosophy</a>
          <a href="/services.html">Services</a>
          <a href="/process.html">How it works</a>
          <a href="/stories.html">Golfer stories</a>
          <a href="/faq.html">FAQ</a>
          <a href="/faq.html#policy">Policies</a>
        </div>
      </div>
      <div>
        <h3>Next step</h3>
        <div class="footer-links">
          <a href="/book.html">Book Now</a>
          <a href="/contact.html">Leave a note</a>
          <a href="/book.html#refer">Refer a golfer</a>
        </div>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <span>© 2026 {BRAND}. All rights reserved.</span>
    </div>
  </footer>
  <script src="/js/site.js?v={ASSET_V}"></script>
"""


def page(slug, title, description, body, extra_head="", robots="index,follow"):
    canonical = f"{SITE}/" if slug == "index" else f"{SITE}/{slug}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="{robots}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/images/hero.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/icons/favicon.svg?v={ASSET_V}" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lato:ital,wght@0,400;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css?v={ASSET_V}">
  {extra_head}
</head>
<body data-page="{slug}">
{HEADER}
  <main id="main">
{body}
  </main>
{FOOTER}
</body>
</html>
"""


def form_html(name, subject, extra_fields, submit_label, success_copy, note=None):
    next_url = f"{SITE}/thanks.html?from={name}"
    if note is None:
        note = "Danielle receives this and calls you by telephone. No video. No camera. All sales are final. No refunds."
    return f"""
        <form class="form" name="{name}" id="{name}-form" method="POST" action="{FORM_ACTION}">
          <p class="form-success">{success_copy}</p>
          <div class="form-fields">
            <p class="honeypot">Leave blank <input name="_gotcha" tabindex="-1" autocomplete="off"></p>
            <input type="hidden" name="_next" value="{next_url}">
            <input type="hidden" name="_redirect" value="{next_url}">
            <input type="hidden" name="_subject" value="{subject}">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            {extra_fields}
            <button class="btn btn-primary" type="submit">{submit_label}</button>
            <p class="form-note">{note}</p>
          </div>
        </form>
"""


INQUIRY_FIELDS = """
            <label>Name <input name="name" required autocomplete="name"></label>
            <label>Phone number <input type="tel" name="phone" required autocomplete="tel"></label>
            <label>Email <input type="email" name="email" required autocomplete="email"></label>
            <label>Best time to call
              <select name="calltime">
                <option>Weekday morning</option>
                <option>Weekday afternoon</option>
                <option>Weekday evening</option>
                <option>Weekend</option>
                <option>Any time</option>
              </select>
            </label>
            <label>Session
              <select name="session">
                <option>Half hour</option>
                <option>1 hour</option>
                <option>Not sure yet</option>
              </select>
            </label>
            <label>Who referred you? (optional)
              <input name="referred" autocomplete="off" placeholder="Name of the golfer who sent you">
            </label>
            <label>What should I know before I call?
              <textarea name="message" required placeholder="I miss the game… the clubs are in the garage… I want to enjoy golf again…"></textarea>
            </label>
"""

CONTACT_FIELDS = """
            <label>Name <input name="name" required autocomplete="name"></label>
            <label>Phone number <input type="tel" name="phone" required autocomplete="tel"></label>
            <label>Email <input type="email" name="email" required autocomplete="email"></label>
            <label>Best time to call
              <select name="calltime">
                <option>Weekday morning</option>
                <option>Weekday afternoon</option>
                <option>Weekday evening</option>
                <option>Weekend</option>
                <option>Any time</option>
              </select>
            </label>
            <label>Where are you in the game?
              <select name="season">
                <option>The clubs are in the garage</option>
                <option>I play, but I am not enjoying it</option>
                <option>I want a winner’s mentality</option>
                <option>Somewhere in between</option>
              </select>
            </label>
            <label>Who referred you? (optional)
              <input name="referred" autocomplete="off">
            </label>
            <label>What should I know before I call?
              <textarea name="message" required placeholder="I miss the game… the clubs are in the garage… I want to enjoy golf again…"></textarea>
            </label>
"""

REFER_FIELDS = """
            <label>Your name <input name="your_name" required autocomplete="name"></label>
            <label>Your email <input type="email" name="your_email" required autocomplete="email"></label>
            <label>Golfer’s name <input name="friend_name" required></label>
            <label>Golfer’s phone or email <input name="friend_contact" required></label>
            <label>A note for Danielle
              <textarea name="message" placeholder="How do you know them? What would help them?"></textarea>
            </label>
"""

SCHEMA = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "{BRAND} Golf Mindset Coaching",
  "description": "Personalized golf mindset coaching by telephone for golfers who want to believe in themselves, hit good shots, and enjoy the game again.",
  "url": "{SITE}/",
  "areaServed": [
    {{
      "@type": "City",
      "name": "Boston",
      "containedInPlace": {{
        "@type": "State",
        "name": "Massachusetts"
      }}
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Worldwide"
    }}
  ],
  "serviceType": "Golf mindset coaching",
  "availableChannel": {{
    "@type": "ServiceChannel",
    "serviceType": "Telephone"
  }},
  "founder": {{
    "@type": "Person",
    "name": "{BRAND}",
    "jobTitle": "Golf mindset coach"
  }},
  "offers": [
    {{
      "@type": "Offer",
      "name": "Half-hour golf mindset session"
    }},
    {{
      "@type": "Offer",
      "name": "One-hour golf mindset session"
    }}
  ]
}}
</script>
"""

FAQ_SCHEMA = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is golf mindset coaching with Danielle Seadia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One-to-one telephone coaching for the inner game of golf. Danielle helps golfers change the thoughts that cap their shots and their enjoyment, then choose a next step they will actually take."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to be a low handicap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Danielle works with any committed golfer, including players returning after time away and players who still go out but cannot enjoy the round."
      }
    },
    {
      "@type": "Question",
      "name": "Where is Danielle based and where does she coach?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "She is based in the Boston, Massachusetts area and coaches nationwide and worldwide by telephone. If you can answer a regular phone, you can work with her."
      }
    },
    {
      "@type": "Question",
      "name": "How long are sessions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sessions are a half hour or one hour. There is no checkout on the website. Danielle sets up payment on the telephone call. All sales are final. No refunds, because the coaching is personalized."
      }
    },
    {
      "@type": "Question",
      "name": "Are there refunds?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. All sales are final. There are no refunds. Sessions are personalized coaching, prepared for you."
      }
    },
    {
      "@type": "Question",
      "name": "Is this sports psychology or therapy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. This is practical inner-game coaching for golf. It is not clinical therapy and it does not replace a swing instructor."
      }
    }
  ]
}
</script>
"""

pages = {}

pages["index.html"] = page(
    "index",
    "Golf Mindset Coach | Danielle Seadia | Hit Good Shots Again",
    "Telephone golf mindset coaching with Danielle Seadia. Believe you can hit good shots again, enjoy the game, and book a half-hour or one-hour session from anywhere.",
    """
    <section class="hero">
      <div class="hero-media">
        <img src="/images/hero.jpg" alt="A lush green fairway at morning light, flag in the distance">
      </div>
      <div class="hero-inner">
        <p class="eyebrow">Golf mindset coaching</p>
        <h1>You can hit good shots again.</h1>
        <p class="lede">One-to-one telephone coaching for golfers who miss the game, and for golfers who still play, but cannot enjoy it. Change the inner game. Then go prove it on the grass.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
          <a class="btn btn-ghost" href="/about.html">Meet Danielle</a>
        </div>
        <div class="hero-meta">
          <div><strong>Who it is for</strong>Committed golfers, any level</div>
          <div><strong>How we talk</strong>Telephone. Nationwide and worldwide.</div>
          <div><strong>Sessions</strong>Half hour or 1 hour</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow">The real problem</p>
        <h2>Enjoyment will not return while the inner game is still against you.</h2>
        <article class="quote-card" style="margin-top:1.6rem;max-width:46rem">
          <p>“But it’s still hard to enjoy when I don’t hit any good shots.”</p>
          <span>A golfer, after being told to enjoy the game</span>
        </article>
        <p class="lede" style="margin-top:1.6rem">That line is the work. Grinding harder on the number will not fix it. A conversation that changes what you believe, before the next shot, will.</p>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap">
        <p class="eyebrow">Who this is for</p>
        <h2>If you are committed to doing the work, this call is for you.</h2>
        <div class="grid-3" style="margin-top:2rem">
          <article class="card">
            <div class="num">The garage</div>
            <h3>“I miss the game.”</h3>
            <p>The clubs are in the garage. You want to enjoy golf again. We start with one honest conversation and one way back onto the grass.</p>
          </article>
          <article class="card">
            <div class="num">Still playing</div>
            <h3>Out there, not enjoying it</h3>
            <p>You show up. The round still feels heavy. You leave knowing you can hit good shots, and that enjoyment is allowed again.</p>
          </article>
          <article class="card">
            <div class="num">Any level</div>
            <h3>A winner’s mentality</h3>
            <p>Young, middle years, older. High handicap or low. If you will put into practice what we talk about, there is a fit.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow">What only this coaching offers</p>
        <h2>Not a system. A person who can hear you.</h2>
        <div class="usp-row">
          <article class="hole">
            <div class="num">01</div>
            <h3>Personalized, not packaged</h3>
            <p>Intuitive, empathic, one golfer at a time. No canned mental-game script. We work with what is actually in the way for you.</p>
          </article>
          <article class="hole">
            <div class="num">02</div>
            <h3>Her own style</h3>
            <p>Coach background, a doctorate in metaphysics, and the warmth of a live conversation. Built around you, not a formula.</p>
          </article>
          <article class="hole">
            <div class="num">03</div>
            <h3>A phone call from anywhere</h3>
            <p>Boston-based. Nationwide and worldwide. If you can answer a regular telephone, you can do this work.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div class="silhouette">
          <img src="/images/silhouette.png?v=9" alt="A black silhouette of Danielle Seadia">
        </div>
        <div class="split-copy">
          <p class="eyebrow">Danielle Seadia</p>
          <h2>Belief first. Then the shot.</h2>
          <p>I want golfers to really believe in themselves and their potential, and then show themselves they can hit good shots. I am optimistic for other people. I tune in. I tell the truth. I leave you with hope that feels practical.</p>
          <p>This is inner-game coaching, not swing instruction and not a seminar replay. You hang up with a next step small enough to take this week.</p>
          <div class="actions">
            <a class="btn btn-dark" href="/about.html">Read the background</a>
            <a class="btn btn-outline" href="/philosophy.html">Read the philosophy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="sessions">
      <div class="wrap">
        <p class="eyebrow">Sessions</p>
        <h2>Pick a length. Get on the phone.</h2>
        <p class="lede">Telephone only. You leave your details. Danielle calls you.</p>
        <div class="price-grid" style="margin-top:2rem">
          <article class="price-card">
            <div class="num">Focused</div>
            <h3>Half hour</h3>
            <p>A sharp conversation for one barrier, one belief, and one next step you can take to the course.</p>
            <a class="btn btn-dark" href="/book.html#session">Book a half hour</a>
          </article>
          <article class="price-card featured">
            <div class="num">Full session</div>
            <h3>1 hour</h3>
            <p>Room to go deeper: the round you cannot enjoy, and a plan you will actually use.</p>
            <a class="btn btn-primary" href="/book.html#session">Book 1 hour</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section bg-forest">
      <div class="wrap split reverse">
        <div>
          <p class="eyebrow">How we talk</p>
          <h2>Phone. Not video. Not an app.</h2>
          <p>You write. Danielle calls. Two people talking about the game, about the thought that is capping you, about the next shot you can believe in. Based near Boston. Available anywhere a phone can ring.</p>
          <div class="actions">
            <a class="btn btn-primary" href="/process.html">See how a call works</a>
            <a class="btn btn-ghost" href="/book.html">Book Now</a>
          </div>
        </div>
        <div class="frame">
          <img src="/images/practice.jpg" alt="An iron addressing a ball on lush green turf">
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="band-media">
        <img src="/images/cta.jpg" alt="A golfer in the follow-through on a sunlit tee">
      </div>
      <div class="cta-band-inner">
        <p class="eyebrow">Next step</p>
        <h2>Book the call. Then go hit a good shot.</h2>
        <p class="lede">Half hour or one hour. Telephone. Nationwide and worldwide.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
        </div>
      </div>
    </section>
    """,
    SCHEMA,
)

pages["about.html"] = page(
    "about",
    "About Danielle Seadia | Golf Mindset Coach",
    "Danielle Seadia offers personalized, empathic golf mindset coaching by telephone. Inner-game training, Boston-based, available nationwide and worldwide.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Background</p>
        <h1>Danielle Seadia</h1>
        <p class="lede">Golf mindset coaching for people who want to believe they can, and then go show themselves on the course.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="silhouette">
          <img src="/images/silhouette.png?v=9" alt="A black silhouette portrait of Danielle Seadia">
        </div>
        <div class="prose">
          <p class="eyebrow">The work</p>
          <h2>I tune in. Then I help you believe it.</h2>
          <p>I have always been an optimist for other people, a source of encouragement people have called a lucky charm. I am intuitive and empathic. I like to make golfers laugh, smile, and feel possibility again.</p>
          <p>I offer a specialized, personalized approach. Not a packaged program. I care about the upliftment that makes a golfer take the next step, and I work with any level of player who is committed to putting into practice what we talk about.</p>
          <p>One fit is the golfer who says, “I miss the game… the clubs are in the garage… I want to enjoy golf again.” Another is the golfer who is still playing, and still cannot enjoy it, because the good shots will not come.</p>
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap prose">
        <h2>What I bring</h2>
        <p>I coached clients in T. Harv Eker’s Peak Potentials Training. That is part of my background as a coach. The work I do with golfers is my own: customized, one conversation at a time, not a replay of someone else’s program.</p>
        <p>I also hold a Doctorate in Metaphysics, which deepens how I listen and how I help you believe in yourself. This is not clinical psychology and it is not a replacement for a teaching pro. It is coaching for the human being who plays.</p>
        <p>My background includes work as a talent in the entertainment industry. That presence is here as warmth and connection, the ability to make a conversation feel alive, not as a performance. Together, that is the style: intuitive, empathic, and built around you.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid-3">
        <article class="card">
          <h3>Where I am</h3>
          <p>Based in the Boston, Massachusetts area. Coaching nationwide and worldwide by telephone.</p>
        </article>
        <article class="card">
          <h3>How I show up</h3>
          <p>On the phone. Direct. Human. No camera. A conversation that points you back to a shot you can believe in.</p>
        </article>
        <article class="card">
          <h3>Who I call</h3>
          <p>Committed golfers. Any age, any handicap. If you will do the work between calls, we can work.</p>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap prose">
        <h2>Ready to work on your inner game?</h2>
        <p>Start with a half-hour or one-hour telephone session. Leave your number. Danielle will call you.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
          <a class="btn btn-outline" href="/philosophy.html">See the philosophy</a>
        </div>
      </div>
    </section>
    """,
)

pages["philosophy.html"] = page(
    "philosophy",
    "Golf Mindset Philosophy | Danielle Seadia",
    "Danielle Seadia’s golf mindset philosophy: a customized conversation, belief in the next shot, and a way back to enjoying the game.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Philosophy</p>
        <h1>A customized conversation. Not a packaged program.</h1>
        <p class="lede">Each golfer is different. Danielle tunes in to you, works in her own style, and leaves you believing the next shot can be a good one.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="prose">
          <h2>The old story is still in the way</h2>
          <p>Even after a good shot or a good nine, the old story tries to pull you back to what feels familiar. That is why “just enjoy it” does not work when you are not hitting good shots.</p>
          <p>Enjoyment and skill both come back when you believe you can, not when you grind harder on the number.</p>
        </div>
        <div class="frame">
          <img src="/images/golfer.jpg" alt="A golf ball balanced on the edge of the hole">
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap">
        <p class="eyebrow">Her style</p>
        <h2>How Danielle actually works</h2>
        <div class="grid-2" style="margin-top:2rem">
          <article class="card">
            <div class="num">01</div>
            <h3>She tunes in</h3>
            <p>Intuitive and empathic. She hears what is actually in the way for you, not a script she uses with every golfer.</p>
          </article>
          <article class="card">
            <div class="num">02</div>
            <h3>She makes it yours</h3>
            <p>Entertainment-industry presence and a doctorate in metaphysics sit behind a conversation that feels alive, warm, and honest.</p>
          </article>
          <article class="card">
            <div class="num">03</div>
            <h3>Belief first</h3>
            <p>The work is helping you believe in yourself and your potential, then showing yourself you can hit good shots.</p>
          </article>
          <article class="card">
            <div class="num">04</div>
            <h3>One next step</h3>
            <p>You hang up with something small enough to take this week: the next shot, the next chip, the next nine.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap split reverse">
        <div class="frame">
          <img src="/images/course.jpg" alt="A rolling golf course in morning light">
        </div>
        <div class="prose">
          <h2>The score matters. It should not run the round.</h2>
          <p>Focusing on the score attaches you to the result. Focusing on the process is how you access your greatest skill, and how the fun comes back. Experiment with not letting the number dictate how you play. Compare the feeling.</p>
          <p>You do not have to be who you were at 25. You have to be a golfer who still believes the next shot can be a good one.</p>
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap grid-2">
        <article class="card">
          <h3>What this is</h3>
          <p>Personalized golf mindset coaching in Danielle’s own style. A telephone conversation, a belief you can stand in, and a next step small enough to do this week.</p>
        </article>
        <article class="card">
          <h3>What this is not</h3>
          <p>Not swing lessons. Not therapy. Not a seminar replay. Not a promise you will shoot your old number. The win is you believing you can, then showing yourself.</p>
        </article>
      </div>
    </section>
    <section class="section bg-forest">
      <div class="wrap">
        <h2>If you remember one thing</h2>
        <p class="lede">The clubs will wait. Belief will not return by itself. Book the call.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
          <a class="btn btn-ghost" href="/services.html">See the sessions</a>
        </div>
      </div>
    </section>
    """,
)

pages["services.html"] = page(
    "services",
    "Golf Mindset Sessions | Half hour or 1 hour | Danielle Seadia",
    "Book a half-hour or one-hour telephone golf mindset session with Danielle Seadia. Payment is arranged on the call.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Services</p>
        <h1>Personal golf mindset coaching, by the session.</h1>
        <p class="lede">Telephone. Nationwide and worldwide. Choose a half hour or one hour, leave your details, and Danielle calls you. Payment is set up on the phone, not on this site. All sales are final. No refunds.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap price-grid">
        <article class="price-card">
          <div class="num">Half hour</div>
          <h3>Focused session</h3>
          <p>One barrier. One belief. One clear next step. Right when you need a way back in, or a reset before the next round.</p>
          <a class="btn btn-dark" href="/book.html#session">Book a half hour</a>
        </article>
        <article class="price-card featured">
          <div class="num">1 hour</div>
          <h3>Full session</h3>
          <p>Time to work the round you cannot enjoy, and a plan you will actually use this week.</p>
          <a class="btn btn-primary" href="/book.html#session">Book 1 hour</a>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap split">
        <div class="prose">
          <h2>What you walk away with</h2>
          <ul>
            <li>A reason to go that is yours, not a generic pep talk</li>
            <li>A thought you can take to the next shot</li>
            <li>A small next step: chips, putts, a bucket, a nine</li>
            <li>Language for the days you talk yourself out of it</li>
            <li>A voice who will call, and who wants you to believe you can</li>
          </ul>
        </div>
        <div class="frame">
          <img src="/images/practice.jpg" alt="Clubface behind a golf ball on the grass">
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid-2">
        <article class="card">
          <p class="eyebrow">Policy</p>
          <h3>All sales are final</h3>
          <p>No refunds. Sessions are personalized coaching, prepared for you. Danielle sets up payment on the telephone when she calls to confirm.</p>
        </article>
        <article class="card">
          <p class="eyebrow">Refer a golfer</p>
          <h3>$50 toward your next call</h3>
          <p>When a golfer you refer books a session, you receive $50 credit toward your next conversation. Mention who sent you when you book.</p>
          <div class="actions">
            <a class="btn btn-outline" href="/book.html#refer">Refer a golfer</a>
          </div>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap">
        <h2>Start with a conversation.</h2>
        <p class="lede">Choose a session length, leave your number, and Danielle calls you.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
          <a class="btn btn-outline" href="/contact.html">Write first</a>
        </div>
      </div>
    </section>
    """,
)

pages["process.html"] = page(
    "process",
    "How Golf Mindset Coaching Works | Danielle Seadia",
    "How Danielle Seadia’s telephone golf mindset sessions work: choose a length, leave your details, she calls, you leave with one next step.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">How it works</p>
        <h1>Write. She calls. You go play.</h1>
        <p class="lede">No login. No camera. A telephone call with someone who wants you believing in the next shot.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap grid-2">
        <article class="hole">
          <div class="num">01 · Choose</div>
          <h3>Half hour or 1 hour</h3>
          <p>Choose a length and leave your name, number, and what feels difficult right now. Payment is set up on the call, not on this site. All sales are final. No refunds.</p>
        </article>
        <article class="hole">
          <div class="num">02 · The call</div>
          <h3>She telephones you</h3>
          <p>Not a Zoom link. A real phone call, nationwide or worldwide. Two voices. No screen in the way.</p>
        </article>
        <article class="hole">
          <div class="num">03 · The conversation</div>
          <h3>Customized for you</h3>
          <p>She works in her own style. No canned script. You hang up with a next step you can take to the next shot.</p>
        </article>
        <article class="hole">
          <div class="num">04 · The follow-up</div>
          <h3>Come back if it helped</h3>
          <p>Book another session when you are ready. Refer a golfer you know.</p>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap split reverse">
        <div class="frame">
          <img src="/images/course.jpg" alt="A winding path across a quiet golf course">
        </div>
        <div class="prose">
          <h2>What a call feels like</h2>
          <p>You answer. Danielle asks how the game has been, not how you scored. You talk about the thought that shows up, the round you cannot enjoy, or why the clubs are still in the garage.</p>
          <p>You hang up with one clear next step. No homework packet. No video recap. A plan, and a person who will call.</p>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Ready when you are.</h2>
        <p class="lede">A half hour or one hour. Payment is set up when Danielle calls. All sales are final.</p>
        <a class="btn btn-primary" href="/book.html">Book Now</a>
      </div>
    </section>
    """,
)

pages["stories.html"] = page(
    "stories",
    "Golf Mindset Stories | Danielle Seadia",
    "Named feelings golfers bring to Danielle Seadia: clubs in the garage, rounds they cannot enjoy, and the belief they can hit good shots again.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Stories</p>
        <h1>Every golfer gets stuck differently.</h1>
        <p class="lede">Your challenge may be pressure, a crowded schedule, a loss of confidence, or the feeling that good shots and enjoyment have left the bag. Naming it is the first step.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="frame">
          <img src="/images/presence.jpg" alt="A golfer standing still on the tee, looking out at the hole ahead">
        </div>
        <article class="quote-card">
          <p>“I miss the game… the clubs are in the garage… I want to enjoy golf again.”</p>
          <span>The golfer this coaching was built for</span>
        </article>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>If you feel the same way</h2>
        <div class="grid-3" style="margin-top:2rem">
          <article class="card">
            <h3>The garage</h3>
            <p>The bag is quiet. You still think about Saturday. You need a reason that belongs to you, said out loud.</p>
          </article>
          <article class="card">
            <h3>The unenjoyable round</h3>
            <p>“It’s still hard to enjoy when I don’t hit any good shots.” That is an inner-game problem, not a character problem.</p>
          </article>
          <article class="card">
            <h3>The old story</h3>
            <p>You had a good hole. Then the old story came back. That is the call.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap prose">
        <h2>Choose your next chapter in golf</h2>
        <p>Whether you want to enjoy practice again, return after a long break, or believe you can hit good shots, we can define a first step that feels like yours.</p>
        <a class="btn btn-primary" href="/book.html">Book Now</a>
      </div>
    </section>
    """,
)

pages["faq.html"] = page(
    "faq",
    "Golf Mindset Coaching FAQ | Danielle Seadia",
    "Answers about Danielle Seadia’s telephone golf mindset coaching: sessions, payment, refunds, worldwide calls, referrals, and how this differs from therapy.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">FAQ</p>
        <h1>Clear answers before you book.</h1>
        <p class="lede">You should know how we talk, what it costs, and what this coaching is, and is not.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap" style="max-width:46rem">
        <details class="faq-item" open>
          <summary>What is this coaching?</summary>
          <p>One-to-one golf mindset coaching with Danielle Seadia. We work the inner game: belief, focus, enjoyment, and a next step you will actually take.</p>
        </details>
        <details class="faq-item">
          <summary>Do we talk on Zoom or FaceTime?</summary>
          <p>No. Telephone only. If you can answer a regular phone, you can do this nationwide or worldwide.</p>
        </details>
        <details class="faq-item">
          <summary>Where is Danielle based?</summary>
          <p>The Boston, Massachusetts area. Sessions are by phone, so you do not need to be local.</p>
        </details>
        <details class="faq-item">
          <summary>How long are sessions?</summary>
          <p>Sessions are a half hour or one hour. There is no checkout on the website. Danielle sets up payment when she calls you. All sales are final. No refunds.</p>
        </details>
        <details class="faq-item">
          <summary>Is this only for low handicaps?</summary>
          <p>No. Any committed golfer. Score is not the door. Showing up to the work is.</p>
        </details>
        <details class="faq-item">
          <summary>Is this therapy or a swing lesson?</summary>
          <p>Neither. It is practical inner-game coaching for golf. Bring swing mechanics to a teaching professional. Bring clinical concerns to a qualified mental health professional. Danielle’s doctorate is in metaphysics: inner-game depth, not sport psychology.</p>
        </details>
        <details class="faq-item">
          <summary>How do I pay?</summary>
          <p>There is no checkout on this website. Danielle sets up payment on the telephone when she calls to confirm your session. All sales are final. No refunds, because the coaching is personalized.</p>
        </details>
        <details class="faq-item" id="policy">
          <summary>What is the refund policy?</summary>
          <p>All sales are final. There are no refunds. Sessions are personalized coaching, prepared for you. Please book only when you are ready to take the call.</p>
        </details>
        <details class="faq-item">
          <summary>How does the referral credit work?</summary>
          <p>Use the refer form on the Book page, or have them mention your name when they book. When they book a session, you receive $50 credit toward your next call.</p>
        </details>
        <details class="faq-item">
          <summary>How do I start?</summary>
          <p>Book a half-hour or one-hour session, or leave your name and number on the contact page. Danielle will telephone you.</p>
        </details>
        <div class="actions" style="margin-top:2rem">
          <a class="btn btn-primary" href="/book.html">Book Now</a>
        </div>
      </div>
    </section>
    """,
    FAQ_SCHEMA,
)

pages["contact.html"] = page(
    "contact",
    "Contact Danielle Seadia | Golf Mindset Coaching",
    "Write Danielle Seadia to book golf mindset coaching by telephone. Nationwide and worldwide.",
    f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Contact</p>
        <h1>Leave a note. She will call you.</h1>
        <p class="lede">Telephone only. Nationwide and worldwide. Ready to book? Choose a session. Prefer to write first? Use the form.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        {form_html(
            "contact",
            "Golf mindset inquiry",
            CONTACT_FIELDS,
            "Send the note",
            "Got it. Danielle will telephone you. Keep your phone close.",
            "Danielle receives this and calls you by telephone. No video. No camera.",
        )}
        <div class="prose">
          <h2>What happens next</h2>
          <p>Danielle reads the note and calls you. If there is a fit, you choose a half hour or one hour and set the time.</p>
          <p>If you already know you want a session, skip ahead and book.</p>
          <div class="actions">
            <a class="btn btn-dark" href="/book.html">Book Now</a>
          </div>
        </div>
      </div>
    </section>
    """,
)

pages["book.html"] = page(
    "book",
    "Book a Golf Mindset Session | Danielle Seadia",
    "Book a half-hour or one-hour telephone golf mindset session with Danielle Seadia. Choose a length, leave your details, and she will call you.",
    f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Book</p>
        <h1>Choose a session. Then she calls.</h1>
        <p class="lede">Choose a session, leave your details, and Danielle telephones you. Payment is set up on that call, not on this site. All sales are final. No refunds.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap book-flow" id="book-flow">
        <ol class="book-steps" aria-label="Booking steps">
          <li class="book-step is-current" data-step="session">
            <span class="book-step-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
            </span>
            <span class="book-step-label">Session</span>
          </li>
          <li class="book-step" data-step="form">
            <span class="book-step-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 4h9l3 3v13H6z"/><path d="M15 4v4h4"/><path d="M8 12h8M8 16h6"/></svg>
            </span>
            <span class="book-step-label">Form</span>
          </li>
        </ol>

        <div class="book-panel is-active" data-panel="session" id="session">
          <h2>Choose your session</h2>
          <p class="lede">Telephone only. Nationwide and worldwide.</p>
          <div class="price-grid" style="margin-top:1.6rem">
            <button type="button" class="price-card" data-session="Half hour">
              <div class="num">Focused</div>
              <h3>Half hour</h3>
              <p>One barrier. One belief. One next step you can take to the course.</p>
            </button>
            <button type="button" class="price-card featured" data-session="1 hour">
              <div class="num">Full session</div>
              <h3>1 hour</h3>
              <p>Room to go deeper on the round you cannot enjoy, and a plan you will actually use.</p>
            </button>
          </div>
          <p class="book-error" hidden>Choose a half hour or 1 hour to continue.</p>
          <div class="book-actions">
            <button type="button" class="btn btn-primary" data-next="form">Continue to form</button>
          </div>
        </div>

        <div class="book-panel" data-panel="form">
          <h2>Your details</h2>
          <p class="lede">Danielle uses this to call you. Payment happens on that phone call.</p>
          <form class="form" name="book" id="book-form" method="POST" action="{FORM_ACTION}" novalidate>
            <p class="honeypot">Leave blank <input name="_gotcha" tabindex="-1" autocomplete="off"></p>
            <input type="hidden" name="_next" value="{SITE}/thanks.html?from=book">
            <input type="hidden" name="_redirect" value="{SITE}/thanks.html?from=book">
            <input type="hidden" name="_subject" value="Golf mindset booking">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="session" id="book-session-field" value="">
            <div class="form-fields">
              <label>Name <input name="name" required autocomplete="name"></label>
              <label>Phone number <input type="tel" name="phone" required autocomplete="tel"></label>
              <label>Email <input type="email" name="email" required autocomplete="email"></label>
              <label>Best time to call
                <select name="calltime">
                  <option>Weekday morning</option>
                  <option>Weekday afternoon</option>
                  <option>Weekday evening</option>
                  <option>Weekend</option>
                  <option>Any time</option>
                </select>
              </label>
              <label>Who referred you? (optional)
                <input name="referred" autocomplete="off" placeholder="Name of the golfer who sent you">
              </label>
              <label>What should I know before I call?
                <textarea name="message" required placeholder="I miss the game… the clubs are in the garage… I want to enjoy golf again…"></textarea>
              </label>
            </div>
            <p class="book-error" hidden>Please fill in your name, phone, email, and a short note.</p>
            <div class="book-actions">
              <button type="button" class="btn btn-outline" data-back="session">Back</button>
              <button type="submit" class="btn btn-primary">Send to Danielle</button>
            </div>
            <p class="form-note">No video. No camera. Danielle will call you and set up payment on the phone. All sales are final. No refunds.</p>
          </form>
        </div>
      </div>
    </section>
    <section class="section bg-cream" id="refer">
      <div class="wrap split">
        <div class="prose">
          <p class="eyebrow">Refer a golfer</p>
          <h2>$50 toward your next call</h2>
          <p>Send Danielle a golfer you know. When they book a session, you receive $50 credit toward your next conversation. They can also mention your name on the booking form.</p>
        </div>
        {form_html(
            "refer",
            "Golf mindset referral",
            REFER_FIELDS,
            "Send the referral",
            "Got it. Danielle will reach out to them. You receive the $50 credit when they book.",
            "Danielle receives this and contacts them. No video. No camera.",
        )}
      </div>
    </section>
    """,
)

pages["thanks.html"] = page(
    "thanks",
    "Thank you | Danielle Seadia Golf Mindset",
    "Danielle Seadia has your note and will be in touch by telephone.",
    """
    <section class="page-hero">
      <div class="wrap thanks-wrap">
        <div class="confirm-box">
          <span class="book-step-icon is-large" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="m4 8 8 6 8-6"/></svg>
          </span>
          <p class="eyebrow">Thank you</p>
          <h1 id="thanks-title">You’re all set.</h1>
          <p class="lede" id="thanks-copy">Danielle has your details. She will telephone you and set up payment on that call. All sales are final.</p>
          <p class="form-note" id="thanks-note">Watch your inbox. Keep your phone close.</p>
          <div class="book-actions" style="justify-content:center">
            <a class="btn btn-primary" href="/">Back to home</a>
            <a class="btn btn-outline" href="/book.html" id="thanks-book">Book Now</a>
          </div>
        </div>
      </div>
    </section>
    """,
    robots="noindex,follow",
)

pages["404.html"] = page(
    "404",
    "Page not found | Danielle Seadia Golf Mindset",
    "That page is off the map. Head back to Danielle Seadia’s golf mindset coaching home.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">404</p>
        <h1>That page is in the trees.</h1>
        <p class="lede">The next shot is the home page, or a session with Danielle.</p>
        <div class="actions">
          <a class="btn btn-dark" href="/">Back to the fairway</a>
          <a class="btn btn-outline" href="/book.html">Book Now</a>
        </div>
      </div>
    </section>
    """,
)

for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
urls = [
    f"{SITE}/",
    f"{SITE}/about.html",
    f"{SITE}/philosophy.html",
    f"{SITE}/services.html",
    f"{SITE}/process.html",
    f"{SITE}/stories.html",
    f"{SITE}/faq.html",
    f"{SITE}/contact.html",
    f"{SITE}/book.html",
]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    sitemap += ["  <url>", f"    <loc>{url}</loc>", "  </url>"]
sitemap.append("</urlset>\n")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
print("wrote robots + sitemap")
