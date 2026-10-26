RETAIL MEDIA SHOWCASE — CLIENT PRESENTATION UPDATE

Run locally: open index.html, or use a static file server.
Technology: original HTML / CSS / JavaScript; no new libraries.

Cloudflare Pages connected to GitHub:
- Upload the CONTENTS of this project folder to the repository.
- Framework preset: None
- Build command: python3 build.py
- Build output directory: dist
- Root directory: / (if project files are at repository root)
The build excludes original videos and reference screenshots; they remain in Pic.
Deployment uses compressed H.264/AAC MP4 with faststart.
All active asset paths are relative and included in dist.

Changed: app.js, data.js, styles.css, README.txt.
Added: build.py, assets/videos/featured.mp4, assets/videos/campaign-hero.mp4.

Home: editorial text/image split, Featured video, campaign hero video,
Our Campaign with supplied images 01–04, Categories, full contact details.
Category pages: readable typography, uniform edge-to-edge image frames, responsive gallery.
L'ORÉAL is first in HBA and its anchor now matches the section.
Back to Category returns to the homepage category index.
Existing section content and missing-image placeholders are retained.
Original stock URLs replaced with supplied execution photos.
Chiller retains its original link to the category index because the source
contains no Chiller category page. No category or information was invented.

Validation: JavaScript syntax; rendering all 5 views; local asset existence;
sidebar anchors; category back links; build output and asset size check.
Browser visual QA was unavailable in this environment. Test the layout and
video playback on your target desktop/tablet/mobile before presentation.

Image frames: gallery and homepage cards 4:3; category hero images 16:9.
Images fill each frame without stretching; centered cropping may trim edges.

Homepage intro: Pic/001.mp4 original retained; assets/videos/001.mp4 used for deployment.
All three homepage videos use autoplay, muted, loop and playsinline.
Playback controls remain available for pausing or enabling sound.
