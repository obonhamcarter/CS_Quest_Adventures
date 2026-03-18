# Adding New Tracks to CS Quest Adventures

This guide explains how to add new learning tracks (languages, frameworks, topics) to the CS Quest Adventures website. The architecture is designed for easy extensibility.

## 📋 Quick Start

To add a new track (e.g., JavaScript, C++, Data Science):

1. Create track directory: `tracks/[trackname]/`
2. Copy track template files
3. Add sidebar configuration to `_quarto.yml`
4. Create track content
5. Update homepage
6. Deploy

---

## 🏗️ Track Directory Structure

Each track follows a standard structure:

```
tracks/
└── [trackname]/               # e.g., javascript, cpp, datascience
    ├── index.qmd             # Track landing page (REQUIRED)
    ├── all-quests.qmd        # Overview page (REQUIRED)
    ├── interactive.qmd       # Interactive tools page (OPTIONAL)
    ├── downloads.qmd         # Downloads page (OPTIONAL)
    ├── setup.qmd             # Setup instructions (OPTIONAL)
    │
    └── lessons/              # Main content directory
        ├── 01-topic.qmd
        ├── 02-topic.qmd
        └── ...
```

### Required Files

**`index.qmd`** - Track landing page
- Introduces the track
- Shows learning path
- Links to first quest
- See `shared/templates/track-index-template.qmd`

**`all-quests.qmd`** - Quest overview
- Lists all quests in track
- Shows difficulty, time estimates
- Quick navigation
- See `shared/templates/all-quests-template.qmd`

### Optional Files

**`interactive.qmd`** - Interactive coding environment
- Links to online compilers/REPLs
- JupyterLite (if applicable)
- Local setup vs cloud options

**`downloads.qmd`** - Downloadable resources
- Notebooks, projects, code samples
- Zip files, PDFs
- Additional materials

**`setup.qmd`** - Installation guide
- Language/framework installation
- Dependencies, tools
- Troubleshooting

---

## 🎯 Step-by-Step: Adding a New Track

### Step 1: Create Directory Structure

```bash
cd tracks
mkdir -p newtrack/lessons
cd newtrack
```

### Step 2: Copy Templates

```bash
cp ../../shared/templates/track-index-template.qmd index.qmd
cp ../../shared/templates/all-quests-template.qmd all-quests.qmd
```

### Step 3: Update Track Metadata

Edit `index.qmd`:

```yaml
---
title: "[Language] Quest Track"
subtitle: "Your descriptive subtitle"
track-id: "newtrack"         # Used for styling and routing
track-icon: "🔷"             # Emoji for navigation
track-color: "#yourcolor"    # Hex color for branding
difficulty: "Beginner"       # or Intermediate, Advanced
total-quests: 15             # Number of lessons
estimated-hours: 25          # Total learning time
---
```

### Step 4: Add Sidebar to _quarto.yml

Edit main `_quarto.yml`:

```yaml
# In navbar menu, add:
- text: "🔷 NewTrack"
  file: tracks/newtrack/index.qmd

# Add new sidebar section:
- id: newtrack-sidebar
  title: "🔷 NewTrack Quests"
  style: "docked"
  search: true
  contents:
    - section: "Foundation"
      contents:
        - text: "Quest 1: Topic"
          file: tracks/newtrack/lessons/01-topic.qmd
        - text: "Quest 2: Topic"
          file: tracks/newtrack/lessons/02-topic.qmd
    - section: "Track Resources"
      contents:
        - text: "📖 All Quests"
          file: tracks/newtrack/all-quests.qmd
```

### Step 5: Create Content

Create lessons in `lessons/` directory:

```yaml
---
title: "Quest 1: Your Topic"
subtitle: "Descriptive subtitle"
track: "newtrack"
quest-number: 1
difficulty: "Beginner"
estimated-time: "10 min"
---

::: {.quest-badge}
NewTrack Quest 1 of 15
:::

# Quest 1: Your Topic

::: {.story-box}
Your quest narrative...
:::

## What You'll Learn

- Point 1
- Point 2

## The Concept

Explanation...

## Try It Yourself

Challenge...

::: {.solution-box}
<details>
<summary>Show Solution</summary>
Solution here...
</details>
:::
```

### Step 6: Add Downloads (if applicable)

Create download structure:

```bash
cd ../../../files
mkdir -p newtrack/lessons
# Add notebooks, code files, etc.
```

Update `tracks/newtrack/downloads.qmd` with links.

### Step 7: Update Homepage

Edit `index.qmd` to add your track card:

```markdown
::: {.quest-card}
### 🔷 NewTrack Track
**Brief description**

- Feature 1
- Feature 2

**Time:** X hours | **Difficulty:** Level

[Start Track →](tracks/newtrack/index.qmd)
:::
```

### Step 8: Add to Tracks Overview

Edit `tracks-overview.qmd`:

```markdown
## 🔷 NewTrack Track

Description, learning path, prerequisites...

[Explore NewTrack →](tracks/newtrack/index.qmd)
```

---

## 🎨 Styling Your Track

### Track Colors

Each track should have a primary color for visual distinction:

```scss
// Add to custom.scss
.track-newtrack {
  --track-primary: #yourcolor;
  --track-secondary: #yourcolor2;
}

.quest-badge.track-newtrack {
  background: linear-gradient(135deg, var(--track-primary), var(--track-secondary));
}
```

### Track Icons

Use emoji or custom icons:
- Python: 🐍
- Rust: 🦀
- Pygame: 🎮
- JavaScript: ⚡
- C++: ⚙️
- Data Science: 📊
- Web Dev: 🌐

---

## 🔧 Interactive Features

### For Languages with Browser Support

If your language runs in browser (like Python with Pyodide):

```yaml
# In lesson frontmatter:
format:
  live-html:
    engine: pyodide  # or other engine
```

### For Languages Requiring External Tools

Link to online compilers:

```markdown
::: {.callout-tip}
## Try This Code

1. Copy the code above
2. Go to [Online Compiler](https://link.com)
3. Paste and run
:::
```

### JupyterLite Setup

For languages with Jupyter kernel support:

```bash
# Create jupyterlite config
mkdir -p jupyterlite_newtrack
cd jupyterlite_newtrack
# Copy notebooks, configure kernel
```

---

## 📊 Track Metadata Best Practices

### Quest Numbering

Use consistent 2-digit numbering:
- `01-topic.qmd` through `99-topic.qmd`
- Makes sorting reliable
- Easy to insert new quests

### Difficulty Levels

Be consistent:
- **Beginner:** No prerequisites
- **Intermediate:** Requires completing earlier quests
- **Advanced:** Complex concepts, assumes mastery of earlier material

### Time Estimates

Realistic estimates help students:
- Include reading + coding + challenges
- 5-15 min for short quests
- 15-30 min for medium quests
- 30-60 min for deep dives

### Learning Objectives

Each quest should have clear objectives:

```markdown
## 🎯 What You'll Learn

By the end of this quest, you'll be able to:
- ✅ Objective 1
- ✅ Objective 2
- ✅ Objective 3
```

---

## 🧪 Testing Your Track

### Before Publishing

1. **Build locally:**
   ```bash
   quarto preview
   ```

2. **Check all links:**
   ```bash
   # Use link checker
   npm run check-links
   ```

3. **Test navigation:**
   - Visit each quest
   - Verify sidebar shows correctly
   - Check breadcrumbs

4. **Validate code:**
   - Run all code examples
   - Test interactive features
   - Verify downloads work

### Quality Checklist

- [ ] All quests have consistent formatting
- [ ] Story boxes use medieval quest theme
- [ ] Code examples are tested and working
- [ ] Solutions are provided for challenges
- [ ] Download links function correctly
- [ ] Images/assets load properly
- [ ] Mobile responsive
- [ ] Sidebar navigation works
- [ ] Search includes new content

---

## 📚 Content Guidelines

### Medieval Quest Theme

Maintain the quest narrative style:

```markdown
::: {.story-box}
Brave code warrior! You've entered the Ancient Library of Algorithms.
The wise keeper challenges you to master the art of sorting...
:::
```

### Code Examples

Always include:
1. **Working example** - Demonstrates concept
2. **Interactive version** - Students can modify
3. **Challenge** - Apply the concept
4. **Solution** - With explanation

### Progression

Structure tracks for gradual learning:
1. **Foundation (Quests 1-8):** Core concepts
2. **Practice (Quests 9-12):** Apply fundamentals
3. **Intermediate (Quests 13-16):** Advanced topics
4. **Mastery (Quests 17+):** Complex applications

---

## 🚀 Deployment

### Automatic Deployment

GitHub Actions automatically deploys on push to main:

```yaml
# Already configured in .github/workflows/deploy.yml
# Your track will be included automatically
```

### Manual Testing

Test in staging before production:

```bash
# Build to staging
quarto render
# Check _site/ directory
# Deploy to test server
```

---

## 🔗 Track Interconnections

### Suggested Prerequisites

In your track's `index.qmd`, link to prerequisite tracks:

```markdown
## 📚 Prerequisites

This track assumes familiarity with:
- [Python basics](../python/index.qmd) (recommended)
- [Programming fundamentals](../intro/what-is-cs.qmd)

New to programming? [Start here](../python/index.qmd)!
```

### Next Steps

Guide students to related tracks:

```markdown
## 🎯 What's Next?

Completed this track? Great! Consider:
- [🦀 Rust Track](../rust/index.qmd) - Systems programming
- [🎮 Pygame Track](../pygame/index.qmd) - Build games!
```

---

## 📝 Example: Adding JavaScript Track

Complete example of adding a JavaScript track:

### 1. Directory Structure

```bash
mkdir -p tracks/javascript/lessons
```

### 2. Track Index (`tracks/javascript/index.qmd`)

```yaml
---
title: "JavaScript Quest Track"
subtitle: "Master Web Development with Interactive Quests"
track-id: "javascript"
track-icon: "⚡"
track-color: "#F7DF1E"
difficulty: "Beginner to Intermediate"
total-quests: 16
estimated-hours: 20
---

::: {.hero}
# ⚡ JavaScript Quest Track

Master the language of the web! Learn to create interactive websites
and dynamic applications through engaging quests.
:::

## 🗺️ Your Learning Path

[Quest cards here...]
```

### 3. Add to Navigation (`_quarto.yml`)

```yaml
# In navbar:
- text: "⚡ JavaScript Track"
  file: tracks/javascript/index.qmd

# Add sidebar:
- id: javascript-sidebar
  title: "⚡ JavaScript Quests"
  # ... contents
```

### 4. First Quest (`tracks/javascript/lessons/01-variables.qmd`)

```yaml
---
title: "Quest 1: Variables & Data"
track: "javascript"
quest-number: 1
---

::: {.quest-badge}
JavaScript Quest 1 of 16
:::

# Quest 1: The Variable Vault

::: {.story-box}
Welcome to the JavaScript realm! Your first challenge awaits
in the Variable Vault, where data takes many forms...
:::

[Content here...]
```

### 5. Test and Deploy

```bash
quarto preview
# Check everything works
git add .
git commit -m "Add JavaScript track"
git push
```

---

## 🤝 Getting Help

When adding new tracks:

1. Review existing tracks (Python, Rust, Pygame) as examples
2. Use templates in `shared/templates/`
3. Follow the style guide in `sitedocs/STYLE_GUIDE.md`
4. Check component examples in `shared/components/`

### Common Issues

**Sidebar not showing:**
- Check `sidebar-id` matches `_quarto.yml`
- Ensure paths are correct

**Styling not applied:**
- Add track-specific CSS to `custom.scss`
- Use track class: `track-[trackname]`

**Code not executing:**
- Verify engine configuration
- Check if language has browser support

---

## 🎉 Congratulations!

You've added a new track! The modular architecture makes it easy to:
- Maintain tracks independently
- Share common resources
- Keep consistent user experience
- Scale to dozens of tracks

Happy quest creation! 🏰⚔️
