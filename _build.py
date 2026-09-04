from pathlib import Path

SITE = "https://danielle-golf-mindset.web.app"
BRAND = "Danielle"
ROOT = Path(__file__).parent

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
          </div>
        </div>
        <a href="/stories.html" data-nav="stories">Stories</a>
        <a href="/faq.html" data-nav="faq">FAQ</a>
        <div class="nav-actions">
          <a class="nav-btn nav-btn-alt" href="/services.html">See services</a>
          <a class="nav-btn" href="/contact.html" data-nav="contact">Book a call</a>
        </div>
      </nav>
"""

HEADER = f"""
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/">
        <img class="brand-mark" src="/icons/favicon.svg?v=4" alt="">
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
        <h3>{BRAND}</h3>
        <p>Golf mindset coaching for players who want more confidence, focus, and enjoyment on the course.</p>
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
        </div>
      </div>
      <div>
        <h3>Next step</h3>
        <div class="footer-links">
          <a href="/contact.html">Book a phone call</a>
        </div>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <span>© 2026 {BRAND}. All rights reserved.</span>
    </div>
  </footer>
  <script src="/js/site.js"></script>
"""


def page(slug, title, description, body, extra_head=""):
    canonical = f"{SITE}/" if slug == "index" else f"{SITE}/{slug}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/images/hero.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/icons/favicon.svg?v=4" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lato:ital,wght@0,400;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css?v=4">
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


SCHEMA = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "{BRAND} Golf Mindset Coaching",
  "description": "Golf mindset coaching to help players rebuild confidence, sharpen focus, and enjoy the game again.",
  "url": "{SITE}/",
  "areaServed": "Online",
  "serviceType": "Golf mindset coaching",
  "founder": {{
    "@type": "Person",
    "name": "{BRAND}"
  }}
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
      "name": "What is golf mindset coaching?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Danielle offers one-to-one golf mindset coaching. Each conversation helps golfers work through mental barriers, rebuild confidence, and choose a practical next step."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to be a low handicap to work with a golf mindset coach?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Golf mindset coaching is for players of every age and ability, whether you are returning after time away, struggling with confidence, or simply enjoying the game less."
      }
    },
    {
      "@type": "Question",
      "name": "Is golf mindset coaching the same as sports psychology or therapy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. This is practical coaching for the mental game of golf. It is not clinical therapy and it does not replace a swing instructor."
      }
    },
    {
      "@type": "Question",
      "name": "How do golf mindset coaching sessions work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You share what is getting in the way, Danielle calls you by telephone, and together you identify a realistic action you can take into practice or your next round."
      }
    }
  ]
}
</script>
"""

pages = {}

pages["index.html"] = page(
    "index",
    "Golf Mindset Coach | Build Confidence & Enjoy Golf Again",
    "One-to-one golf mindset coaching to help golfers of every age rebuild confidence, improve focus, and enjoy playing again.",
    """
    <section class="hero">
      <div class="hero-media">
        <img src="/images/hero.jpg" alt="A still green beside the water, flag in the cup">
      </div>
      <div class="hero-inner">
        <p class="eyebrow">Golf mindset coaching</p>
        <h1>Build confidence. Find your focus. Enjoy golf again.</h1>
        <p class="lede">One-to-one mindset coaching for golfers who feel stuck, discouraged, or disconnected from the game. We turn what is holding you back into a clear, realistic next step.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
          <a class="btn btn-ghost" href="/about.html">Hear the story</a>
        </div>
        <div class="hero-meta">
          <div><strong>Who it is for</strong>Golfers of every age who miss the game</div>
          <div><strong>How we talk</strong>Telephone. No video. Old school.</div>
          <div><strong>The goal</strong>Get you back out there</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow">Who this is for</p>
        <h2>If the clubs have gone quiet, this call is for you.</h2>
        <p class="lede">Confidence can fade at any stage of the game. Whether pressure has replaced the fun, life has crowded out your tee time, or returning feels harder than it used to, coaching gives you a way forward.</p>
        <div class="grid-3" style="margin-top:2rem">
          <article class="card">
            <div class="num">Young</div>
            <h3>When the fun left</h3>
            <p>The game got heavy. Scores, pressure, comparison. You still have years of golf in you. Let’s get the joy back in the bag.</p>
          </article>
          <article class="card">
            <div class="num">Middle years</div>
            <h3>When life crowded the tee</h3>
            <p>Work, family, the week that never ends. The clubs sit. You miss the walk, the putts, the Saturday version of yourself.</p>
          </article>
          <article class="card">
            <div class="num">Older</div>
            <h3>When you think you’re done</h3>
            <p>The body changed. The friends play less. That does not mean the game is over. Chipping and putting are still a way back in.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="wrap split">
        <div class="frame">
          <img src="/images/golfer.jpg" alt="A golf ball resting on the lip of the cup">
          <span class="frame-caption">The next roll still matters</span>
        </div>
        <div class="split-copy">
          <p class="eyebrow">Why I started this</p>
          <h2>A conversation can change your next round.</h2>
          <p>I saw how patient encouragement and the right next step helped someone close to me return to chipping, putting, and playing. That experience became the foundation of my coaching.</p>
          <p>If you feel stuck, rusty, embarrassed to return, or tired of talking yourself out of a round, we will work through the mental barrier and make getting started feel possible.</p>
          <div class="actions">
            <a class="btn btn-dark" href="/philosophy.html">Read the philosophy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow">The work</p>
        <h2>Golf mindset coaching you can take to the course.</h2>
        <div class="grid-4" style="margin-top:2rem">
          <article class="hole">
            <div class="num">01</div>
            <h3>A reason to show up</h3>
            <p>Not a lecture. A reason that belongs to you, said out loud so it sticks.</p>
          </article>
          <article class="hole">
            <div class="num">02</div>
            <h3>A small way back in</h3>
            <p>Chip. Putt. A bucket. You do not have to play 18 to be a golfer again.</p>
          </article>
          <article class="hole">
            <div class="num">03</div>
            <h3>A voice on the line</h3>
            <p>Telephone. No camera. The old-school way — two people talking.</p>
          </article>
          <article class="hole">
            <div class="num">04</div>
            <h3>A longer game</h3>
            <p>Young, middle-aged, older. The goal is the same: keep you in the game.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section bg-forest">
      <div class="wrap split reverse">
        <div>
          <p class="eyebrow">How we talk</p>
          <h2>Phone calls. Not video. Not an app.</h2>
          <p>You leave your number. I call you. We talk like people used to talk — about the game, about why you stopped, about the next small step that gets you back on the grass.</p>
          <div class="actions">
            <a class="btn btn-primary" href="/process.html">See how a call works</a>
            <a class="btn btn-ghost" href="/services.html">See what you get</a>
          </div>
        </div>
        <div class="frame">
          <img src="/images/practice.jpg" alt="An iron addressing a ball in morning light">
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow">About Danielle</p>
        <h2>A practical way to strengthen your mental game.</h2>
        <p class="lede">Together, we identify what is getting in the way, reconnect you with what you value about golf, and choose a next step that fits your life and your game.</p>
        <div class="stat-row">
          <div class="stat"><b>Phone</b>Old-school telephone. No Zoom.</div>
          <div class="stat"><b>Every age</b>Young, middle, and older golfers</div>
          <div class="stat"><b>Practical</b>One clear next step after every call</div>
        </div>
        <div class="actions">
          <a class="btn btn-dark" href="/about.html">Read the background</a>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="band-media">
        <img src="/images/cta.jpg" alt="A golfer in the follow-through on a sunlit tee">
      </div>
      <div class="cta-band-inner">
        <p class="eyebrow">Next step</p>
        <h2>Leave your number. I’ll call you.</h2>
        <p class="lede">Tell me where the game went quiet. We will talk on the phone and find a way back.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
        </div>
      </div>
    </section>
    """,
    SCHEMA,
)

pages["about.html"] = page(
    "about",
    "About Danielle | Golf Mindset Coach for Every Age",
    "Learn how Danielle’s experience helping a golfer return to the game inspired practical, one-to-one golf mindset coaching.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Background</p>
        <h1>Helping golfers find their way back to the game.</h1>
        <p class="lede">Danielle’s approach began with a simple experience: thoughtful encouragement helped someone close to her start chipping, putting, and playing again. Now she brings that same personal focus to other golfers.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="frame">
          <img src="/images/presence.jpg" alt="A golfer looking down the fairway before the next shot">
        </div>
        <div class="prose">
          <p class="eyebrow">In Danielle’s words</p>
          <h2>Mindset comes before momentum.</h2>
          <p>I learned that returning to golf rarely begins with a perfect plan. It begins when someone feels understood, sees a manageable way forward, and decides to take one small action.</p>
          <p>I coach golfers of every age: players carrying too much pressure, people whose clubs were crowded out by life, and longtime golfers wondering whether they still belong in the game.</p>
          <p>Not on video. Not in a webinar. On the telephone, the old-school way. Two voices. A plan to get you back on the grass.</p>
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap grid-3">
        <article class="card">
          <h3>Why this work</h3>
          <p>Because the mental side of golf shapes whether you practise, how you respond to setbacks, and how much you enjoy the game.</p>
        </article>
        <article class="card">
          <h3>Who I call</h3>
          <p>Golfers of every age who miss the game and need a voice that will not let them stay on the couch.</p>
        </article>
        <article class="card">
          <h3>How I show up</h3>
          <p>On the phone. Direct. Human. No camera, no performance. Just a conversation that points you back to the course.</p>
        </article>
      </div>
    </section>
    <section class="section">
      <div class="wrap prose">
        <h2>Ready to work on your mental game?</h2>
        <p>Start with a one-to-one phone conversation about what has changed, what you want from golf now, and the next step that feels both useful and achievable.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
          <a class="btn btn-outline" href="/philosophy.html">See the philosophy</a>
        </div>
      </div>
    </section>
    """,
)

pages["philosophy.html"] = page(
    "philosophy",
    "Golf Mindset Coaching Philosophy | Confidence & Focus",
    "A practical golf mindset coaching approach built around confidence, focus, enjoyment, and small actions that help you keep playing.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Philosophy</p>
        <h1>A stronger golf mindset starts with one clear step.</h1>
        <p class="lede">The goal is not a perfect swing thought. The goal is a golfer who picks up a wedge again, rolls a few putts, and remembers why this game is worth it.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="prose">
          <h2>You do not have to be who you were at 25.</h2>
          <p>You have to be a golfer who still shows up. Young players need the fun back. Middle-aged players need permission to take a morning. Older players need someone to say the game is not finished with them.</p>
          <p>We explore the thoughts, expectations, and routines that are keeping you stuck, then turn the conversation into a practical next step: a chip, a putt, a bucket, or nine holes.</p>
        </div>
        <div class="frame">
          <img src="/images/golfer.jpg" alt="A golf ball balanced on the edge of the hole">
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap">
        <div class="grid-2">
          <article class="card">
            <div class="num">01</div>
            <h3>The spark is still there</h3>
            <p>If you miss the game, you are not done. You are between rounds. We start from that truth.</p>
          </article>
          <article class="card">
            <div class="num">02</div>
            <h3>Small is how you come back</h3>
            <p>Chipping and putting count. A short-game hour counts. You do not owe anyone 18 holes on day one.</p>
          </article>
          <article class="card">
            <div class="num">03</div>
            <h3>A voice beats a pep-talk post</h3>
            <p>Telephone. Old school. You hear a person who will not let the week swallow the game.</p>
          </article>
          <article class="card">
            <div class="num">04</div>
            <h3>Every age has a way in</h3>
            <p>The words change. The goal does not: get you back to playing some golf.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid-2">
        <article class="card">
          <h3>What this is</h3>
          <p>Practical golf mindset coaching. A focused conversation, a reason that matters to you, and a next step small enough to do this week.</p>
        </article>
        <article class="card">
          <h3>What this is not</h3>
          <p>Not swing lessons. Not video therapy. Not a promise you will shoot your old number. The win is you playing again.</p>
        </article>
      </div>
    </section>
    <section class="section bg-forest">
      <div class="wrap">
        <h2>If you remember one thing</h2>
        <p class="lede">The clubs will wait. Your spark will not wait forever. Leave a number. Let’s talk.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/services.html">See the services</a>
          <a class="btn btn-ghost" href="/contact.html">Book a phone call</a>
        </div>
      </div>
    </section>
    """,
)

pages["services.html"] = page(
    "services",
    "Golf Mindset Coaching Services | Telephone Sessions",
    "Explore one-to-one golf mindset coaching for confidence, focus, motivation, and a more enjoyable return to the game.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Services</p>
        <h1>Personal golf mindset coaching, one call at a time.</h1>
        <p class="lede">In a focused telephone conversation, we work through what is holding you back and create a practical plan for practice, play, and a healthier relationship with the game.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap grid-2">
        <article class="service-card">
          <div class="num">First call</div>
          <h3>A get-to-know-you phone call</h3>
          <p>You leave your number. I call. You tell me how the game got quiet. I tell you if I can help and what the next call would be for.</p>
        </article>
        <article class="service-card">
          <div class="num">Ongoing</div>
          <h3>Regular telephone talks</h3>
          <p>One golfer, one phone line. We work on confidence, focus, motivation, and the smallest next step that gets you to the practice green or first tee.</p>
        </article>
        <article class="service-card">
          <div class="num">Every age</div>
          <h3>Young, middle, and older</h3>
          <p>The words change with the season of life. The goal does not: get you back to chipping, putting, and playing some golf.</p>
        </article>
        <article class="service-card">
          <div class="num">Old school</div>
          <h3>Telephone only</h3>
          <p>No video. No webinar. If you can answer a phone, you can do this work. That is the point.</p>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap split">
        <div class="prose">
          <h2>What you walk away with</h2>
          <ul>
            <li>A reason to go that is yours, not a generic pep talk</li>
            <li>A small next step: chips, putts, a bucket, a nine</li>
            <li>A voice that will call you back and check that you went</li>
            <li>Language for the days you talk yourself out of it</li>
            <li>A plan that fits your age and your life, not someone else’s</li>
          </ul>
        </div>
        <div class="frame">
          <img src="/images/practice.jpg" alt="Clubface behind a golf ball in the last quiet second before the shot">
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Start with a conversation.</h2>
        <p class="lede">Share what you are experiencing and what you want from the game. If the coaching is a good fit, you will know the format and next steps before you commit.</p>
        <div class="actions">
          <a class="btn btn-primary" href="/contact.html">Leave your number</a>
          <a class="btn btn-outline" href="/process.html">See how a call works</a>
        </div>
      </div>
    </section>
    """,
)

pages["process.html"] = page(
    "process",
    "How Golf Mindset Coaching Works | Danielle",
    "See how Danielle’s telephone golf mindset coaching turns mental barriers into clear, realistic steps for practice and play.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">How it works</p>
        <h1>Leave a number. Answer the phone. Go play.</h1>
        <p class="lede">No login. No camera. The old-school way of communicating — a telephone call with someone who wants you back on the course.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap grid-2">
        <article class="hole">
          <div class="num">01 · Write</div>
          <h3>Leave your number</h3>
          <p>Tell me your name, phone number, and what feels difficult right now—confidence, motivation, pressure, focus, or returning after time away.</p>
        </article>
        <article class="hole">
          <div class="num">02 · The call</div>
          <h3>I telephone you</h3>
          <p>Not a Zoom link. A real phone call. We talk like people used to talk: honestly, without a screen in the way.</p>
        </article>
        <article class="hole">
          <div class="num">03 · The step</div>
          <h3>A small way back in</h3>
          <p>Chip. Putt. A bucket. A walk nine. Something you can do this week so the clubs are not a museum piece.</p>
        </article>
        <article class="hole">
          <div class="num">04 · The follow-up</div>
          <h3>I call again</h3>
          <p>Change is easier with accountability. I call back, we review what you tried, and we decide what comes next.</p>
        </article>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap split reverse">
        <div class="frame">
          <img src="/images/course.jpg" alt="A winding path across a quiet, rolling golf course">
        </div>
        <div class="prose">
          <h2>What a call feels like</h2>
          <p>You answer. I ask how the game has been, not how you scored. We talk about why you stopped, what you miss, and what would feel like a win this month — even if that win is twenty minutes on the putting green.</p>
          <p>Then you hang up with one clear next step. No homework packet. No video recap. Just a plan and a person who will call.</p>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Ready when you are.</h2>
        <p class="lede">The first step is your phone number.</p>
        <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
      </div>
    </section>
    """,
)

pages["stories.html"] = page(
    "stories",
    "Golf Mindset Challenges | Find Your Way Forward",
    "Common golf mindset challenges at every age, from performance pressure and lost motivation to returning confidently after time away.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Stories</p>
        <h1>Every golfer gets stuck differently.</h1>
        <p class="lede">Your challenge may be pressure, a crowded schedule, a loss of confidence, or the feeling that the game has moved on without you. Naming it clearly is the first step forward.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <div class="frame">
          <img src="/images/presence.jpg" alt="A golfer standing still on the tee, looking out at the hole ahead">
        </div>
        <article class="quote-card">
          <p>“You do not need to solve your whole game today. You need one honest conversation and one next step you are willing to take.”</p>
          <span>— Danielle</span>
        </article>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>If you feel the same way</h2>
        <p class="lede">Golf mindset coaching meets you at the stage of life—and the stage of the game—you are in now.</p>
        <div class="grid-3" style="margin-top:2rem">
          <article class="card">
            <h3>The young golfer</h3>
            <p>The game stopped being fun. Everyone else is grinding. You miss playing without the weight.</p>
          </article>
          <article class="card">
            <h3>The middle years</h3>
            <p>The bag is in the garage. The calendar won. You still think about Saturday mornings.</p>
          </article>
          <article class="card">
            <h3>The older golfer</h3>
            <p>You wonder if you are done. You are not. Chipping and putting are still a door back in.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section bg-cream">
      <div class="wrap prose">
        <h2>Choose your next chapter in golf</h2>
        <p>Whether you want to enjoy practice again, return after a long break, or feel calmer on the course, we can define a first step that feels like yours.</p>
        <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
      </div>
    </section>
    """,
)

pages["faq.html"] = page(
    "faq",
    "Golf Mindset Coaching FAQ | Danielle",
    "Answers about golf mindset coaching, including who it helps, how sessions work, and what makes it different from swing instruction.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">FAQ</p>
        <h1>Clear answers before you leave a number.</h1>
        <p class="lede">You should know how we talk, who this is for, and what happens after you write.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap" style="max-width:46rem">
        <details class="faq-item" open>
          <summary>What is this coaching?</summary>
          <p>One-to-one golf mindset coaching. We work on confidence, focus, motivation, and practical actions that help you practise or play with more enjoyment.</p>
        </details>
        <details class="faq-item">
          <summary>Do we talk on Zoom or FaceTime?</summary>
          <p>No. Telephone only. Old-school. No camera, no video app. If you can answer a phone, you can do this.</p>
        </details>
        <details class="faq-item">
          <summary>Is this only for low handicaps?</summary>
          <p>No. This is for golfers who miss the game. Score is not the door. Showing up is.</p>
        </details>
        <details class="faq-item">
          <summary>I’m older. Is it too late?</summary>
          <p>No. Chipping and putting are still a way back in. The game is not finished with you.</p>
        </details>
        <details class="faq-item">
          <summary>I’m young and I just lost the fun. Does that count?</summary>
          <p>Yes. That is exactly the kind of golfer I want on the phone.</p>
        </details>
        <details class="faq-item">
          <summary>Is this therapy or a swing lesson?</summary>
          <p>Neither. It is practical coaching for the mental side of golf. Bring swing mechanics to a teaching professional and clinical concerns to a qualified mental health professional.</p>
        </details>
        <details class="faq-item">
          <summary>How do I start?</summary>
          <p>Leave your name, number, and a few sentences on the contact page. Danielle will call you.</p>
        </details>
        <div class="actions" style="margin-top:2rem">
          <a class="btn btn-primary" href="/contact.html">Book a phone call</a>
        </div>
      </div>
    </section>
    """,
    FAQ_SCHEMA,
)

pages["contact.html"] = page(
    "contact",
    "Book a Golf Mindset Coaching Call | Danielle",
    "Book a one-to-one telephone golf mindset coaching call with Danielle and take a practical step toward more confidence, focus, and enjoyment.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Contact</p>
        <h1>Leave your number. I’ll call you.</h1>
        <p class="lede">Telephone only. No Zoom, no camera. Tell me where the game went quiet and the best time to ring you.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="wrap split">
        <form class="form" name="contact" method="POST" action="/contact.html?success=true" data-netlify="true" netlify-honeypot="company">
          <p class="form-success">Got it. Danielle will telephone you. Keep your phone close.</p>
          <div class="form-fields">
            <p class="honeypot">Company <input name="company" tabindex="-1" autocomplete="off"></p>
            <input type="hidden" name="form-name" value="contact">
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
                <option>Young golfer — I lost the fun</option>
                <option>Middle years — life crowded the tee</option>
                <option>Older golfer — I wonder if I’m done</option>
                <option>Somewhere in between</option>
              </select>
            </label>
            <label>What should I know before I call?
              <textarea name="message" required placeholder="I miss the game… the clubs are in the garage… I want to chip and putt again…"></textarea>
            </label>
            <button class="btn btn-primary" type="submit">Book a call</button>
            <p class="form-note">Danielle will telephone you. This is not a video call. Nothing is sold or posted.</p>
          </div>
        </form>
        <div class="prose">
          <h2>What happens next</h2>
          <p>I read the note and I call you. We talk on the phone, old school. If there is a fit, we set the next call and a small step back to the grass.</p>
          <p>The first job is a real conversation—your voice, my voice, no screen—followed by a clear explanation of the coaching options that fit your goals.</p>
        </div>
      </div>
    </section>
    """,
)

pages["404.html"] = page(
    "404",
    "Page not found | Danielle Golf Mindset",
    "That page is off the map. Head back to Danielle’s golf mindset coaching home.",
    """
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">404</p>
        <h1>That page is in the trees.</h1>
        <p class="lede">The next shot is the home page, or a note to Danielle.</p>
        <div class="actions">
          <a class="btn btn-dark" href="/">Back to the fairway</a>
          <a class="btn btn-outline" href="/contact.html">Book a phone call</a>
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
]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    sitemap += ["  <url>", f"    <loc>{url}</loc>", "  </url>"]
sitemap.append("</urlset>\n")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
print("wrote robots + sitemap")
