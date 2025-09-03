# Last20 Website Archive

This repository contains an archived copy of the Last20 website (www.last20.ca), a Canadian startup that created plastic-infused pavement by combining traditional pavement with low-density polyethylene.

## About Last20

Last20 was a cleantech startup founded by siblings who developed an innovative solution to plastic waste by upcycling plastic into pavement. Their mission was "paving the way to a sustainable future" through plastic pavement technology.

## Archive Information

- **Original URL**: https://www.last20.ca/
- **Archived Date**: September 3, 2025
- **Original Platform**: Square Online
- **Archive Purpose**: Preserving the website for memories and historical reference

## Local Development

### Running the Website Locally

1. **Using the Custom Server (Recommended)**:
   ```bash
   python3 server.py
   ```
   This will start a local server on http://localhost:8000 and automatically open your browser. The server provides:
   - A landing page with two viewing options
   - Mock API responses to reduce 404 errors
   - Automatic browser opening

2. **Direct File Access**:
   - Open `complete.html` for the full multi-page archive (recommended)
   - Open `simple.html` for a single-page experience
   - Open `index.html` for the original version (may have some broken features)

3. **Alternative Servers**:
   ```bash
   python3 -m http.server 8000
   # or
   npx serve .
   ```

### File Structure

```
├── complete.html           # Complete multi-page archive with all content (recommended)
├── simple.html             # Simplified single-page version 
├── index.html              # Original homepage (requires external resources)
├── server.py              # Enhanced Python server with mock API responses
├── css/                   # Stylesheets
│   ├── site.css          # Main site styles
│   └── wcko.css          # Checkout styles
├── js/                    # JavaScript files
│   ├── runtime.js        # Runtime scripts
│   ├── vue-modules.js    # Vue.js modules
│   ├── languages-en_CA.js # Language files
│   └── site.js           # Main site scripts
├── uploads/               # Website assets
│   └── b/                # Original image directories
│       ├── 3cb2ec90.../favicon.png
│       └── 590d76c8.../Last20_Logo_1693167311.png
└── robots.txt            # Robots.txt file
```

## Features Archived

### Complete Archive (complete.html) - Recommended
- ✅ **All 7 pages**: Home, About, Learn, Projects, Partners, News, Contact
- ✅ **Full content extraction** from original website including founder information
- ✅ **Interactive navigation** between all pages
- ✅ **All news articles** and project descriptions preserved
- ✅ **Social media links** and contact information
- ✅ **Responsive design** that works perfectly on all devices
- ✅ **No external dependencies** - completely self-contained
- ✅ **Fast loading** with smooth page transitions

### Simple Version (simple.html)
- ✅ Clean, modern single-page design preserving original branding
- ✅ Core company information and messaging
- ✅ Responsive layout that works on all devices
- ✅ Self-contained with no external dependencies

### Original Version (index.html)
- ✅ Original Square Online structure preserved
- ✅ Company logo and favicon
- ✅ Meta tags and SEO information
- ✅ Original CSS and JavaScript files
- ⚠️  Limited JavaScript functionality (some features may not work offline)
- ❌ External API calls and dynamic content

## Technical Notes

This is a static archive of a dynamic Square Online website. Some features that relied on external services or server-side functionality may not work in the archived version:

- Contact forms
- Analytics tracking
- Social media integrations
- E-commerce functionality
- Dynamic content loading

The archived version preserves the visual appearance and basic structure of the original website for historical reference.

## Contributing

This is an archived website for historical preservation. No active development is planned.

## License

This archive is for historical and personal reference purposes. All original content belongs to Last20 and its creators.

---

*"Upcycling plastic into pavement - Canadian clean-tech innovators paving the way to a sustainable future!"*
