# Contributing to CS Quest Adventures

Thank you for your interest in contributing to CS Quest Adventures! This project thrives on community contributions — whether you're fixing typos, adding new quests, or creating entirely new learning tracks.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Adding New Tracks](#adding-new-tracks)
- [Adding New Quests](#adding-new-quests)
- [Improving Existing Content](#improving-existing-content)
- [Style Guidelines](#style-guidelines)
- [Pull Request Process](#pull-request-process)
- [Development Setup](#development-setup)
- [Testing Guidelines](#testing-guidelines)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. This project follows these principles:

- **Be Respectful:** Treat everyone with respect and kindness
- **Be Inclusive:** Welcome contributors of all skill levels and backgrounds
- **Be Collaborative:** Work together and help each other learn
- **Be Patient:** Remember that everyone is learning
- **Be Constructive:** Provide helpful, actionable feedback

### Unacceptable Behavior

- Harassment, intimidation, or discrimination of any kind
- Offensive comments or personal attacks
- Trolling or deliberately derailing discussions
- Publishing others' private information
- Any conduct inappropriate in a professional setting

### Reporting

If you experience or witness unacceptable behavior, please contact: obonhamcarter@allegheny.edu

---

## 🤝 How Can I Contribute?

### Reporting Bugs

**Before Submitting:**
- Check the [FAQ](faq.md) for common issues
- Search existing GitHub Issues to avoid duplicates
- Try to reproduce the bug in the latest version

**When Reporting Include:**
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details:
  - Browser and version
  - Operating system
  - Quarto version (for build issues)

**Example Bug Report:**
```markdown
**Title:** Code cell fails to execute in Python Quest 3

**Description:**
When clicking "Run Code" on the conditional example in Quest 3,
nothing happens. No output appears and no error is shown.

**Steps to Reproduce:**
1. Navigate to tracks/python/lessons/03-conditionals.qmd
2. Scroll to first code cell
3. Click "Run Code" button
4. Wait 10 seconds

**Expected:** Code executes and shows output
**Actual:** Nothing happens

**Environment:**
- Browser: Firefox 120.0
- OS: macOS 14.0
- Tested date: 2025-01-15
```

### Suggesting Enhancements

**Before Suggesting:**
- Check if the feature already exists
- Search existing feature requests
- Consider if it fits the project's goals

**When Suggesting Include:**
- Clear, descriptive title
- Detailed explanation of the enhancement
- Why this would be useful
- Examples or mockups (if applicable)

### Contributing Content

**Types of Content Contributions:**
- New quests for existing tracks
- Entirely new learning tracks (JavaScript, Java, etc.)
- Additional challenge boxes
- Improved explanations
- Better examples
- Practice exercises
- Solutions to challenges

---

## 🚀 Getting Started

### 1. Fork the Repository

Click "Fork" on GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/CS_Quest_Adventures.git
cd CS_Quest_Adventures
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

**Branch Naming Conventions:**
- `feature/` — New features or content
- `fix/` — Bug fixes
- `docs/` — Documentation updates
- `style/` — Formatting, theme changes
- `refactor/` — Code restructuring

Examples:
- `feature/javascript-track`
- `fix/python-quest-3-typo`
- `docs/improve-setup-guide`

### 4. Make Your Changes

Follow the guidelines in this document.

### 5. Commit Your Changes

```bash
git add .
git commit -m "Brief description of changes"
```

**Commit Message Guidelines:**
- Use present tense ("Add feature" not "Added feature")
- Start with capital letter
- Keep first line under 50 characters
- Add detailed description after blank line (if needed)

**Examples:**
```
Add JavaScript track with basic lessons

- Created tracks/javascript directory
- Added 5 initial quests (variables through loops)
- Updated _quarto.yml with javascript-sidebar
- Created track landing page
```

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

Go to the original repository on GitHub and click "New Pull Request".

---

## 🎨 Adding New Tracks

The modular architecture makes adding new tracks straightforward. See the comprehensive guide: [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md)

**Quick Checklist:**
- [ ] Create `tracks/trackname/` directory structure
- [ ] Create track landing page (`index.qmd`)
- [ ] Add at least 3-5 quests to start
- [ ] Update `_quarto.yml` with new sidebar
- [ ] Add track card to main `index.qmd`
- [ ] Create `all-quests.qmd` overview page
- [ ] Update navigation in navbar
- [ ] Test rendering with `quarto render`
- [ ] Document track in README

**Example PR Title:**
`Add C++ Track with Systems Programming Lessons`

---

## ✍️ Adding New Quests

### For Existing Tracks

**1. Choose the Right Track**
- `tracks/python/lessons/` — Python programming
- `tracks/rust/lessons/` — Rust programming
- `tracks/pygame/quests/` — Game development

**2. Follow Naming Convention**
```
[number]-[topic-name].qmd
```
Examples:
- `20-file-handling.qmd` (Python)
- `20-error-handling.qmd` (Rust)
- `08-platformer.qmd` (Pygame)

**3. Use The Medieval Quest Theme**

Every quest should include:

```markdown
---
title: "Quest [N]: [Quest Name]"
subtitle: "[Subtitle about the topic]"
---

# 🎯 Quest [N]: [Quest Name]

::: {.story-box}
**Greetings, Code Warrior!**

[Medieval-themed introduction to the concept]
:::

## 📚 [Concept Name]

::: {.concept-box}
**Concept: [Name]**

[Clear explanation of the programming concept]
:::

## 💻 [Examples Section]

[Code examples with explanations]

## 🏆 Challenge

::: {.challenge-box}
**Challenge: [Name]**

[Problem description]

**Your Quest:**
- [Task 1]
- [Task 2]

<details>
<summary>💡 Hint</summary>
[Helpful hint]
</details>

<details>
<summary>✅ Solution</summary>
```python
# Solution code
```
</details>
:::
```

**4. Test Your Quest**
```bash
quarto render tracks/python/lessons/20-file-handling.qmd
```

**5. Submit Pull Request**
Include description of what concept is taught.

---

## 🔧 Improving Existing Content

### Types of Improvements

**Typo Fixes:**
- Minor spelling/grammar fixes
- Broken links
- Formatting issues

**Content Enhancements:**
- Clearer explanations
- Better examples
- Additional challenges
- Improved hints

**Code Improvements:**
- More idiomatic code
- Better variable names
- Added comments
- Fixed bugs in examples

### Before Making Changes

1. **Read the entire quest** to understand context
2. **Test any code changes** to ensure they work
3. **Maintain the medieval theme** in any new content
4. **Keep difficulty level** appropriate for quest position

### Pull Request Requirements

**For Typo Fixes:**
- Simple description: "Fix typo in Quest 5"
- Can include multiple files

**For Content Changes:**
- Explain why the change improves the content
- Show before/after if significant
- Ensure medieval theme maintained

---

## 🎨 Style Guidelines

### Content Style

**Writing Tone:**
- Friendly and encouraging
- Medieval quest theme (warriors, treasures, battles, etc.)
- Clear and concise
- Avoid jargon (or explain when necessary)

**Structure:**
- Start with story box
- Introduce concept with concept box
- Provide clear examples
- End with challenge box
- Include hints and solutions

**Code Style:**
- Follow language conventions (PEP 8 for Python, Rust style guide for Rust)
- Use meaningful variable names
- Add comments for complex logic
- Keep examples simple and focused

### Markdown Style

**Headings:**
```markdown
# Main Title (H1) — Quest title only
## Section Title (H2) — Major sections
### Subsection (H3) — Detailed sections
```

**Code Blocks:**
````markdown
```python
# Always specify language
def example():
    pass
```
````

**Custom Boxes:**
```markdown
::: {.story-box}
Medieval-themed narrative
:::

::: {.concept-box}
**Concept:** Clear explanation
:::

::: {.challenge-box}
**Challenge:** Problem to solve
:::

::: {.tip-box}
💡 Helpful tips
:::
```

**Links:**
```markdown
[Descriptive text](relative/path/to/file.qmd)
```

---

## 📝 Pull Request Process

### Before Submitting

**Checklist:**
- [ ] Branch has descriptive name
- [ ] Code/content tested locally
- [ ] `quarto render` works without errors
- [ ] Medieval theme maintained
- [ ] Commit messages are clear
- [ ] No unrelated changes included

### Pull Request Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature/content
- [ ] Documentation update
- [ ] Style/formatting
- [ ] Refactoring

## Related Issues
Fixes #123 (if applicable)

## Testing
Describe how you tested:
- [ ] Rendered locally with `quarto render`
- [ ] Tested code examples execute correctly
- [ ] Checked links work
- [ ] Reviewed in browser

## Screenshots (if applicable)
[Add screenshots of new content]

## Checklist
- [ ] Medieval theme maintained
- [ ] Code follows style guidelines
- [ ] Documentation updated (if needed)
- [ ] No breaking changes
```

### Review Process

1. **Automated Checks:** GitHub Actions will test the build
2. **Maintainer Review:** A maintainer will review your PR
3. **Feedback:** Address any requested changes
4. **Approval:** Once approved, a maintainer will merge

**Review Timeline:**
- Minor fixes (typos): Usually within 1-3 days
- Content additions: 3-7 days
- New tracks: 1-2 weeks (requires thorough review)

### After Merge

- Your contribution will appear on the live site
- You'll be added to contributors list (if significant contribution)
- Thank you! 🎉

---

## 💻 Development Setup

### Prerequisites

**Required:**
- Git
- Quarto 1.7+
- Python 3.9+ (for Python-related features)
- Modern browser

**Optional:**
- Rust (if working on Rust track)
- Pygame (if working on Pygame track)
- Node.js (if modifying build scripts)

### Local Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/CS_Quest_Adventures.git
cd CS_Quest_Adventures

# Install Python dependencies
pip install -r requirements.txt

# Preview the site
quarto preview

# Or render specific file
quarto render index.qmd
```

**Live Preview:**
The `quarto preview` command starts a local server with live reload.
Visit `http://localhost:4321` (port may vary).

### Editor Setup

**VS Code (Recommended):**
```bash
# Install extensions
code --install-extension quarto.quarto
code --install-extension ms-python.python
code --install-extension rust-lang.rust-analyzer
```

**Settings:**
- Enable format on save
- Markdown linting
- Spell check

---

## 🧪 Testing Guidelines

### Before Submitting PR

**1. Render Test**
```bash
# Test specific file
quarto render tracks/python/lessons/20-file-handling.qmd

# Test entire site
quarto render
```

**2. Link Test**
- Click all links in your changes
- Verify they go to correct pages
- Check for broken links

**3. Code Execution Test**
For Python quests:
- Open in browser
- Click "Run Code" on all cells
- Verify output is correct
- Check for errors

**4. Visual Test**
- Check formatting looks correct
- Boxes render properly
- Images display
- Mobile responsive (if applicable)

**5. Cross-Browser Test** (for significant changes)
- Chrome
- Firefox
- Safari
- Edge

### Test Checklist

- [ ] `quarto render` completes without errors
- [ ] No broken links
- [ ] All code examples execute correctly
- [ ] Formatting looks correct
- [ ] Medieval theme maintained
- [ ] Navigation works
- [ ] Images load
- [ ] Mobile responsive (if applicable)

---

## 🎯 Contribution Ideas

Not sure what to contribute? Here are some ideas:

### Easy (Good for First Contributions)
- Fix typos or grammar
- Improve code comments
- Add hints to challenges
- Update broken links
- Enhance documentation

### Medium
- Add new challenges to existing quests
- Create practice exercises
- Improve explanations
- Add more examples
- Create additional tests

### Advanced
- Add new quests to existing tracks
- Create new learning track (JavaScript, Java, etc.)
- Implement progress tracking system
- Add interactive visualizations
- Improve Pyodide integration

---

## 📞 Getting Help

### Questions About Contributing?

- **Email:** obonhamcarter@allegheny.edu
- **GitHub Discussions:** Ask in discussions forum
- **GitHub Issues:** Open an issue with "question" label

### Documentation

- [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md) — Comprehensive track creation guide
- [README.md](../README.md) — Project overview
- [FAQ](faq.md) — Common questions
- [Teaching Guide](teaching-guide.md) — Educational use

---

## 🏆 Recognition

### Contributors

All contributors are recognized in:
- GitHub contributors page
- Project README (for significant contributions)
- Release notes

### Becoming a Maintainer

Regular contributors may be invited to become maintainers with:
- Commit access
- Review privileges
- Involvement in project direction

---

## 📜 License

By contributing to CS Quest Adventures, you agree that your contributions will be licensed under the same license as the project. [Check repository for specific license]

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make CS Quest Adventures better for learners around the world. Thank you for being part of this community!

[← Back to Home](../index.qmd) | [View Teaching Guide](teaching-guide.md) | [View FAQ](faq.md)
