# Golf Mindset

Website for [Danielle Seadia Golf Mindset Coaching](https://danielle-golf-mindset.web.app/) — personalized telephone coaching for golfers who want to believe in themselves, hit good shots, and enjoy the game again.

**Live site:** https://danielle-golf-mindset.web.app/

## Pages

- Home, Background, Philosophy
- Services, How it works, Book Now
- Stories, FAQ, Contact

## Edit and rebuild

Page copy, navigation, and forms are generated from `_build.py`.

```bash
python3 _build.py
```

That writes the HTML files, `robots.txt`, and `sitemap.xml`.

Styles live in `css/styles.css`. Client scripts live in `js/site.js`. After CSS or JS changes, bump `ASSET_V` in `_build.py` so browsers load the new files.

Booking and contact forms submit through FormSubmit.

## Deploy

The site is hosted on Firebase Hosting (`danielle-golf-mindset`).

```bash
firebase deploy --only hosting
```
