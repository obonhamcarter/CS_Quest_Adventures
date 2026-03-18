# Frequently Asked Questions (FAQ)

## General Questions

### What is CS Quest Adventures?
CS Quest Adventures is an interactive, web-based platform for learning computer science through three distinct tracks: Python, Rust, and Pygame game development. All content is gamified with a medieval quest theme.

### Do I need to install anything?
**No!** Python code runs directly in your browser using Pyodide and JupyterLite. Rust examples link to the Rust Playground. However, for Pygame projects, you'll need to download and run them locally.

### Is it really free?
Yes! CS Quest Adventures is completely free and open source. No hidden fees, no subscriptions, no accounts required to access content.

### What devices are supported?
The site works on any modern device with a web browser (desktop, laptop, tablet, or phone). For the best experience with interactive coding, we recommend a laptop or desktop.

---

## Getting Started

### Which track should I start with?
- **Complete beginner?** Start with Python — it's the most beginner-friendly
- **Already know basics?** Try Rust for systems programming or Pygame for game dev
- **Want to make games?** Pygame track, but Python fundamentals help first
- **Interested in performance?** Rust track teaches memory safety and systems concepts

### Do I need prior programming experience?
**Python track:** No prior experience needed — starts from absolute basics  
**Rust track:** Some programming knowledge helpful but not required  
**Pygame track:** Python fundamentals recommended (complete Python track first)

### How long does each track take?
- **Python Track:** 15-30 hours (19 quests)
- **Rust Track:** 20-40 hours (19 quests)
- **Pygame Track:** 10-20 hours (7 game projects)

Time varies based on prior experience and how deep you explore each concept.

### Can I do multiple tracks at once?
Yes! Tracks are independent. Many learners do Python and Rust in parallel since they cover similar concepts in different languages.

---

## Technical Questions

### What is Pyodide?
Pyodide is a Python runtime that runs in your web browser using WebAssembly. It allows you to execute Python code without a server or local installation.

### What is JupyterLite?
JupyterLite is a full Jupyter environment that runs entirely in your browser. It includes a Python runtime, file manager, and notebook interface — all without server infrastructure.

### Can I save my work?
- **In-browser code:** Changes aren't saved automatically (copy code you want to keep)
- **JupyterLite:** Saves notebooks to browser local storage (use File → Download to keep permanently)
- **Downloaded notebooks:** Save to your computer permanently

### What Python version is used?
Pyodide currently uses Python 3.11. For local installations, we recommend Python 3.9 or higher.

### Which Rust version is used?
The Rust Playground uses the latest stable Rust version (currently 1.70+). For local installations, rustup installs the latest stable version.

### Can I use external Python packages?
In Pyodide, you can install packages that are available in the Pyodide repository using:
```python
import micropip
await micropip.install('package-name')
```
Not all PyPI packages work in Pyodide. Popular ones like NumPy, Pandas, and Matplotlib are supported.

---

## Content Questions

### Are the Python and Rust tracks similar?
Yes! They cover parallel concepts:
- Both have 19 quests
- Similar progression: variables → data types → functions → algorithms → classes
- Same medieval quest theme
- Learn the same fundamental concepts in different languages

### Can I skip quests?
Yes, quests are designed to be modular. However, later quests assume knowledge from earlier ones, especially in sequences like loops → lists → functions.

### Are solutions provided?
Yes! Most challenges include expandable solution boxes. Try solving yourself first, then check the solution.

### Can I suggest new content?
Absolutely! We welcome contributions. See our [README](../README.md) and [ADDING_NEW_TRACKS guide](ADDING_NEW_TRACKS.md) for how to contribute.

---

## Pygame Questions

### Why can't Pygame run in the browser?
Pygame requires system-level graphics and audio APIs that aren't accessible through WebAssembly. You'll need to download and run projects locally.

### How do I run Pygame projects?
```bash
# Install Pygame
pip install pygame

# Download a project
# Navigate to project folder
cd tracks/pygame/projects/Day_01

# Run it
python main.py
```

### What platforms does Pygame support?
Pygame works on Windows, macOS, and Linux. It requires Python 3.7+ and graphics support.

### Can I share my Pygame creations?
Yes! You can:
- Share the Python source code
- Create executable files using PyInstaller
- Upload to GitHub and share the repository
- Create videos/screenshots of your games

---

## Troubleshooting

### Code cells won't run
- **Refresh the page** — sometimes Pyodide needs to reload
- **Check browser compatibility** — use Chrome, Firefox, Safari, or Edge
- **Disable ad blockers** — they sometimes interfere with WebAssembly
- **Clear browser cache** — old cached files might cause issues

### JupyterLite won't load
- **Wait a few moments** — first load downloads several MB
- **Check internet connection** — needed for initial load
- **Try incognito mode** — rules out extension conflicts
- **Check browser storage** — ensure local storage isn't full

### Pygame installation fails
```bash
# Try upgrading pip first
pip install --upgrade pip

# Then install Pygame
pip install pygame

# On Linux, you might need:
sudo apt-get install python3-pygame
```

### "Module not found" error in Pyodide
The package might not be available in Pyodide. Check the [Pyodide package list](https://pyodide.org/en/stable/usage/packages-in-pyodide.html).

### Rust code won't compile in Playground
- **Check syntax** — Rust is strict about types and lifetimes
- **Read error messages carefully** — Rust errors are very detailed
- **Try the stable version** — some features require nightly build

---

## Learning Support

### I'm stuck on a challenge. What should I do?
1. **Read the concept boxes again** — they contain key information
2. **Check the tip boxes** — hints are often there
3. **Look at previous examples** — similar patterns might apply
4. **Check the solution box** — it's okay to peek and learn
5. **Try searching online** — error messages often have solutions
6. **Ask for help** — see contact information below

### How can I get help?
- **Check this FAQ** — common answers here
- **Review quest content** — concept boxes explain each topic
- **Email:** obonhamcarter@allegheny.edu
- **GitHub Issues:** Open an issue in the repository

### Are there any communities or forums?
Currently, support is through email and GitHub issues. We're working on building a learning community!

---

## For Educators

### Can I use this in my classroom?
Yes! CS Quest Adventures is free and open source. Use it as you wish — as a primary curriculum, supplement, or independent study material.

### Can I modify the content?
Yes! The entire site is open source. Fork the repository, modify content, add your own quests. See [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md) for guidance.

### Can I track student progress?
The basic site doesn't include progress tracking or accounts. You could:
- Ask students to download and submit notebooks
- Use JupyterLite notebooks and have students export completion
- Fork and add your own tracking system

### Can I host this on my own server?
Yes! The site is built with Quarto and generates static HTML. Host anywhere:
- Your school's web server
- GitHub Pages
- Netlify
- Any static hosting service

See [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md) and [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md).

### Is there a teacher's guide?
Not yet, but we'd love contributions! Each quest includes learning objectives, concepts, and solutions. The modular structure makes it easy to adapt to your needs.

---

## Contributing

### How can I contribute?
- **Report bugs** — open GitHub issues
- **Suggest improvements** — open GitHub issues with enhancement tag
- **Add content** — submit pull requests
- **Create new tracks** — follow [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md)
- **Improve documentation** — fix typos, clarify explanations

### I want to add a new language track (e.g., JavaScript, Java, C++)
Perfect! See our comprehensive guide: [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md)

The modular architecture makes adding new tracks straightforward:
1. Create `tracks/language-name/` folder
2. Add lessons
3. Update `_quarto.yml` with new sidebar
4. Follow the template structure

### How do I submit changes?
1. Fork the repository on GitHub
2. Make your changes
3. Test locally (`quarto render`)
4. Submit a pull request
5. Describe your changes clearly

### What types of contributions are welcome?
- New quest content
- Bug fixes
- Improved explanations
- Additional examples
- New challenges
- Better styling
- Accessibility improvements
- Documentation updates
- New language tracks
- Better error messages

---

## Licensing & Legal

### What license is this under?
CS Quest Adventures is open source. Check the repository for specific license details.

### Can I use this commercially?
Check the repository license. Generally, educational use (free or paid) is fine. Attribution is appreciated!

### Do I need to credit CS Quest Adventures?
Attribution is appreciated but check the repository license for specific requirements.

---

## Future Plans

### Will more tracks be added?
Yes! The architecture is designed for easy expansion. Potential future tracks:
- JavaScript/TypeScript
- Java
- C/C++
- Go
- Web Development
- Data Science
- Machine Learning
- More game development frameworks

### Will there be accounts/progress tracking?
Possibly in the future! For now, the site is intentionally simple and account-free to minimize barriers to learning.

### Will there be mobile apps?
The web interface works on mobile devices. Native apps aren't currently planned but could be added by contributors.

### Will there be certificates?
Not currently, but this could be added. The focus is on learning, not credentials.

---

## Contact & Support

### General Questions
Email: obonhamcarter@allegheny.edu

### Bug Reports
Open an issue on GitHub: [GitHub Issues]

### Feature Requests
Open an issue on GitHub with the "enhancement" tag

### Contributing
See [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md) and the repository README

---

## Still Have Questions?

Can't find your answer here? 

- **Email:** obonhamcarter@allegheny.edu
- **GitHub Issues:** Open an issue in the repository
- **Check Documentation:** Browse [sitedocs/](.) folder for detailed guides

[← Back to Home](../index.qmd)
