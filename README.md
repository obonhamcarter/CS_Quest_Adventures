# CS Quest Adventures 🏰

**Epic journeys through Computer Science — Learn Python, Rust, Game Dev, and more!**

A unified, extensible platform for interactive Computer Science education featuring multiple learning tracks with a consistent medieval quest theme.

[![Deploy](https://github.com/obonhamcarter/CS_Quest_Adventures/actions/workflows/deploy.yml/badge.svg)](https://github.com/obonhamcarter/CS_Quest_Adventures/actions/workflows/deploy.yml)

---

## 🎯 Overview

CS Quest Adventures combines three (and growing!) educational tracks into one cohesive learning platform:

- **🐍 Python Track** (19 quests) - Interactive Python fundamentals
- **🦀 Rust Track** (19 quests) - Systems programming with Rust  
- **🎮 Pygame Track** (7 games) - Game development with Python

Each track uses an engaging medieval quest theme to make learning fun and memorable.

---

## ✨ Features

### For Students
- **Interactive Learning** - Code runs in browser (Python track)
- **Progressive Difficulty** - Well-structured learning paths
- **Engaging Theme** - Medieval quest narrative throughout
- **Three Tracks** - Choose your adventure
- **Mobile Friendly** - Learn anywhere with responsive design
- **Completely Free** - All content freely available

### For Educators
- **Ready-to-Use Curriculum** - Complete lessons and materials
- **College Fair Friendly** - Intro content for recruiting
- **Downloadable Resources** - Notebooks and projects
- **Flexible Structure** - Use individual tracks or full curriculum

### For Developers
- **Extensible Architecture** - Easy to add new tracks
- **Modular Design** - Each track is self-contained
- **Template System** - Quick start for new tracks
- **Automated Deployment** - GitHub Actions CI/CD

---

## 🚀 Quick Start

### Initial Setup (First Time Only)

1. **Clone or navigate to the repository**
   ```bash
   cd /Users/obonhamcarter/Desktop/0_/tutorialSites/CS_Quest_Adventures
   ```

2. **Install dependencies** (if not already done)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   pip install -r requirements.txt
   python -m ipykernel install --user --name=python3
   ```

### Render the Site

**Option 1: Use the helper script** (easiest)
```bash
./render.sh
```

**Option 2: Manual command**
```bash
QUARTO_PYTHON=./venv/bin/python quarto render
```

### Preview the Site

**Option 1: Use the helper script** (easiest)
```bash
./preview.sh
```

**Option 2: Manual command**
```bash
QUARTO_PYTHON=./venv/bin/python quarto preview
```

Then visit: **http://localhost:4321**

The preview server provides live reload - changes you make will automatically refresh in the browser!

---

## 📁 Project Structure

The project uses a **modular track-based architecture** designed for easy expansion:

```
CS_Quest_Adventures/
├── _quarto.yml              # Master configuration (defines all tracks)
├── index.qmd                # Main homepage
├── custom.scss              # Shared medieval theme
├── styles.css               # Additional styling
├── theme-toggle.js          # Dark/light mode
│
├── tracks/                  # 🎯 MODULAR TRACK SYSTEM
│   ├── python/             # Python track (19 quests)
│   │   ├── index.qmd       # Track landing page
│   │   ├── all-quests.qmd  # Quest overview
│   │   ├── interactive.qmd # JupyterLite info
│   │   └── lessons/        # 01-variables.qmd ... 19-classes.qmd
│   │
│   ├── rust/               # Rust track (19 quests)
│   │   ├── index.qmd
│   │   ├── all-quests.qmd
│   │   ├── interactive.qmd
│   │   └── lessons/        # 01-variables.qmd ... 19-classes.qmd
│   │
│   └── pygame/             # Pygame track (7 games)
│       ├── index.qmd
│       ├── all-quests.qmd
│       ├── setup.qmd
│       ├── quests/         # Quest-themed tutorials
│       └── projects/       # Complete game code
│
├── intro/                  # Getting started content
│   ├── what-is-cs.qmd
│   ├── why-study-cs.qmd
│   └── try-it-now.qmd
│
├── files/                  # Downloadable resources
│   ├── python/            # Python notebooks
│   ├── rust/              # Rust notebooks  
│   └── pygame/            # Game projects
│
├── shared/                 # Shared resources
│   ├── templates/         # Track templates for future additions
│   ├── components/        # Reusable Quarto components
│   ├── scripts/           # Build and utility scripts
│   └── images/            # Shared images
│
├── jupyterlite/           # Python browser IDE
│   └── content/           # Notebooks for JupyterLite
│
├── sitedocs/              # Documentation
│   ├── ADDING_NEW_TRACKS.md    # ⭐ Guide for adding tracks
│   └── [other docs]
│
└── .github/
    └── workflows/
        └── deploy.yml     # Automated deployment
```

---

## 🆕 Adding New Tracks

**The architecture is designed to make adding new tracks easy!**

### Quick Start: Add a New Track

1. **Create track directory:**
   ```bash
   mkdir -p tracks/newtrack/lessons
   ```

2. **Copy templates:**
   ```bash
   cp shared/templates/track-index-template.qmd tracks/newtrack/index.qmd
   cp shared/templates/all-quests-template.qmd tracks/newtrack/all-quests.qmd
   ```

3. **Update metadata in `index.qmd`:**
   ```yaml
   track-id: "newtrack"
   track-icon: "⚡"
   track-color: "#yourcolor"
   ```

4. **Add to `_quarto.yml`:**
   ```yaml
   # In navbar
   - text: "⚡ NewTrack"
     file: tracks/newtrack/index.qmd
   
   # Add sidebar section
   - id: newtrack-sidebar
     title: "⚡ NewTrack Quests"
     contents: [...]
   ```

5. **Create lessons** in `tracks/newtrack/lessons/`

6. **Update homepage** to include new track

**Complete guide:** See [sitedocs/ADDING_NEW_TRACKS.md](sitedocs/ADDING_NEW_TRACKS.md)

### Future Tracks Planned

- ⚡ JavaScript Track - Web development
- 📊 Data Science Track - Python for data analysis
- 🌐 Web Dev Track - HTML, CSS, JavaScript
- ⚙️ C++ Track - Advanced systems programming

---

## 🏗️ Architecture Principles

### 1. Modularity
Each track is self-contained in its own directory with:
- Track landing page (`index.qmd`)
- Quest overview (`all-quests.qmd`)
- Lessons/content
- Track-specific resources

### 2. Shared Resources
Common elements are centralized:
- Theme (custom.scss, styles.css)
- Navigation structure (_quarto.yml)
- Templates for new tracks
- Reusable components

### 3. Scalability
Design allows for:
- Adding unlimited new tracks
- Each track independent
- Minimal interdependencies
- Easy maintenance

### 4. Consistency
All tracks follow:
- Same medieval quest theme
- Similar structure and navigation
- Consistent difficulty ratings
- Standard quest numbering

---

## 🎨 Theming

### Medieval Quest Theme

All tracks use consistent styling:

```scss
// Track colors (customize per track)
.track-python { --track-primary: #10b981; }
.track-rust { --track-primary: #f97316; }
.track-pygame { --track-primary: #ec4899; }

// Shared quest components
.quest-badge         // Quest number indicator
.story-box           // Quest narrative
.concept-box         // Explanations
.challenge-box       // Exercises
.solution-box        // Solutions
.tip-box            // Tips and tricks
```

### Adding Track-Specific Styling

Add to `custom.scss`:

```scss
.track-newtrack {
  --track-primary: #yourcolor;
  --track-secondary: #yourcolor2;
}
```

---

## 📚 Content Guidelines

### Quest Structure

Every quest should include:

1. **Story introduction** - Engage with narrative
2. **Learning objectives** - Clear goals
3. **Concepts explained** - Teach the material
4. **Interactive examples** - Show, don't just tell
5. **Challenges** - Practice exercises
6. **Solutions** - With explanations
7. **Next steps** - Guide forward

### Difficulty Levels

- **Beginner** 🌟 - No prerequisites
- **Intermediate** 🌟🌟 - Requires earlier quests
- **Advanced** 🌟🌟🌟 - Complex, assumes mastery

### Time Estimates

Be realistic:
- Short quests: 5-15 minutes
- Medium quests: 15-30 minutes  
- Long quests: 30-60 minutes

---

## 🧪 Testing

### Local Testing

```bash
# Preview changes
quarto preview

# Build site
quarto render

# Check for broken links
# (add link checker script)
```

### Quality Checklist

Before adding new content:
- [ ] All quests have consistent formatting
- [ ] Story boxes use medieval theme
- [ ] Code examples tested
- [ ] Solutions provided
- [ ] Links work correctly
- [ ] Mobile responsive
- [ ] Sidebar navigation correct

---

## 🚀 Deployment

### Automatic Deployment

GitHub Actions automatically deploys to GitHub Pages on push to `main`:

1. Renders Quarto site
2. Builds JupyterLite
3. Deploys to Pages

### Manual Deployment

```bash
# Build everything
quarto render

# JupyterLite (if needed)
cd jupyterlite
jupyter lite build --contents content --output-dir ../_site/jupyterlite

# Deploy _site/ directory
```

---

## 🤝 Contributing

### Adding Content

1. Fork repository
2. Create feature branch
3. Add/modify content
4. Test locally
5. Submit pull request

### Reporting Issues

- Use GitHub Issues for bugs
- Feature requests welcome
- Questions via email

---

## 📖 Documentation

- **[ADDING_NEW_TRACKS.md](sitedocs/ADDING_NEW_TRACKS.md)** - Complete guide for adding tracks
- **[INTEGRATION_PLAN.md](../INTEGRATION_PLAN.md)** - Original integration strategy
- **[PROJECT_COMPARISON.md](../PROJECT_COMPARISON.md)** - Analysis of original projects
- **[UNIFIED_STRUCTURE.md](../UNIFIED_STRUCTURE.md)** - Detailed structure docs

---

## 🎓 About

**CS Quest Adventures** is created and maintained by:

**Oliver Bonham-Carter**  
Department of Computer and Information Science  
Allegheny College

- 🌐 [oliverbonhamcarter.com](https://www.oliverbonhamcarter.com)
- 📧 [obonhamcarter@allegheny.edu](mailto:obonhamcarter@allegheny.edu)
- 🏫 [cs.allegheny.edu](https://cs.allegheny.edu)

---

## 📄 License

[Add your license here]

---

## 🙏 Acknowledgments

This unified platform combines and extends:
- **CS_Quest_Lessons** - Original Python track
- **CS_Rust_Quest_Lessons** - Original Rust track
- **pygameTutorials** - Original game development series

Special thanks to all students and educators who provided feedback!

---

## 🗺️ Roadmap

### Current (v1.0)
- ✅ Python track (19 quests)
- ✅ Rust track (19 quests)
- ✅ Pygame track (7 games)
- ✅ Unified theme and navigation
- ✅ Extensible architecture

### Near Future (v1.1)
- [ ] Complete all Pygame quest tutorials
- [ ] Add track progress tracking
- [ ] Improve mobile experience
- [ ] Add search functionality

### Future (v2.0)
- [ ] JavaScript track
- [ ] Data Science track
- [ ] Student progress dashboards
- [ ] Instructor portal
- [ ] Interactive challenges system

---

## 📊 Stats

- **Total Tracks:** 3 (growing)
- **Total Quests:** 45 (19 + 19 + 7)
- **Languages:** Python, Rust, Game Dev
- **Estimated Learning Time:** ~75 hours
- **Cost:** Free!

---

## 📞 Contact & Support

- 💬 [Discussion Forum](https://github.com/obonhamcarter/CS_Quest_Adventures/discussions)
- 🐛 [Report Issues](https://github.com/obonhamcarter/CS_Quest_Adventures/issues)
- 📧 [Email](mailto:obonhamcarter@allegheny.edu)
- 🌐 [Website](https://www.oliverbonhamcarter.com)

---

**Embark on your coding quest today!** 🏰⚔️🎮
