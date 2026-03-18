# Teaching Guide

## Using CS Quest Adventures in Your Classroom

CS Quest Adventures provides a complete, interactive platform for teaching computer science concepts through three distinct learning tracks. This guide helps educators effectively integrate the platform into their curriculum.

---

## 🎯 Platform Overview for Educators

### Three Independent Tracks
- **Python Track:** 19 lessons covering programming fundamentals
- **Rust Track:** 19 lessons teaching systems programming concepts
- **Pygame Track:** 7 game development projects

### Key Educational Features
- ✅ **No installation required** — Students code in browser
- ✅ **Self-paced learning** — Students progress at their own speed
- ✅ **Medieval quest theme** — Gamification increases engagement
- ✅ **Built-in challenges** — Assessment opportunities in every lesson
- ✅ **Multiple learning modes** — In-page coding, JupyterLite, local development

---

## 📚 Curriculum Integration

### As Primary Curriculum

**Full-Semester Course (Python Track)**
- **Duration:** 12-16 weeks
- **Time:** 3-4 hours per week
- **Coverage:** All 19 Python quests
- **Assessment:** Built-in challenges + final projects
- **Format:** 
  - Week 1-2: Intro + Variables & Data Types
  - Week 3-4: Control Flow (Conditionals & Loops)
  - Week 5-8: Data Structures (Lists, Dictionaries)
  - Week 9-12: Functions & Algorithms
  - Week 13-16: OOP, Recursion, Complexity

**Game Development Course (Pygame Track)**
- **Duration:** 8-10 weeks
- **Prerequisites:** Python fundamentals
- **Coverage:** All 7 Pygame projects
- **Format:**
  - Week 1: Intro + Quest 1 (Maze)
  - Week 2-3: Quests 2-3 (Physics & Collision)
  - Week 4-5: Quests 4-5 (Game Mechanics)
  - Week 6-8: Quests 6-7 (Advanced Projects)
  - Week 9-10: Original game project

### As Supplementary Material

**Flipped Classroom Model:**
- Assign quests as homework
- Use class time for discussion and challenges
- Review solutions together
- Extend with group projects

**Lab Component:**
- Use quests as guided lab exercises
- Students complete during lab sessions
- Instructor available for help
- Submit challenge solutions

**Independent Study:**
- Students work through tracks independently
- Check in weekly for progress
- Final project demonstrates mastery

---

## 📊 Suggested Lesson Plans

### Python Track — Lesson Plan Template

**Quest Structure (90 minutes):**
1. **Introduction (10 min)**
   - Review previous concepts
   - Introduce today's topic
   - Show real-world applications

2. **Concept Exploration (20 min)**
   - Work through quest content together
   - Run example code as class
   - Discuss concept boxes

3. **Guided Practice (30 min)**
   - Students work through quest exercises
   - Code along with instructor
   - Ask questions as they arise

4. **Independent Challenges (25 min)**
   - Students attempt challenge boxes
   - Work independently or in pairs
   - Instructor circulates to help

5. **Wrap-Up & Discussion (5 min)**
   - Review key concepts
   - Preview next quest
   - Assign homework

### Example: Quest 1 (Variables)

**Learning Objectives:**
- Define and create variables
- Understand data types (int, float, string)
- Perform basic operations
- Use print() for output

**Pre-Class:**
- None (first lesson)

**In-Class Activities:**
1. Demo: Create variables in browser code cell
2. Exercise: Students create 5 variables with different types
3. Challenge: Create a "student profile" using variables
4. Discussion: Where are variables used in real programs?

**Assessment:**
- Complete challenge boxes
- Submit "student profile" program
- Quick quiz on variable naming rules

**Homework:**
- Quest 2: Data Types
- Read concept boxes before next class

---

## 🎯 Assessment Strategies

### Formative Assessment

**During Quests:**
- Challenge box completion (embedded in each lesson)
- Code execution results (instant feedback)
- Concept understanding checks

**Weekly:**
- Short coding exercises
- Peer code review
- Progress check-ins

### Summative Assessment

**Midterm Project Ideas:**
- **Python:** Create a text-based adventure game
- **Rust:** Build a command-line tool
- **Pygame:** Modify and extend Quest 1-3

**Final Project Ideas:**
- **Python:** Data analysis project with visualization
- **Rust:** Systems utility (file processor, network tool)
- **Pygame:** Original game combining concepts from all 7 quests

**Portfolio-Based:**
- Students compile their best work
- Include modified quests + original project
- Write reflection on learning journey

---

## 📝 Tracking Student Progress

### Manual Tracking

**Option 1: Submission-Based**
- Students download notebooks with solutions
- Submit via LMS (Canvas, Blackboard, etc.)
- Instructor reviews and grades

**Option 2: Self-Reporting**
- Weekly progress reports
- Students screenshot challenge completions
- Honor system with spot checks

**Option 3: Git-Based**
- Students fork repository
- Complete work in their fork
- Submit via pull request or link

### Automated Tracking (Requires Custom Development)

The platform doesn't have built-in progress tracking, but you can add:
- Fork the repository
- Add analytics integration
- Implement user accounts
- Track quest completion via JavaScript

---

## 👥 Classroom Management Tips

### For In-Person Classes

**Computer Lab Setup:**
- Ensure all computers have modern browsers
- Test Pyodide loads on school network
- Have offline backup (downloaded notebooks)
- Bookmark the site on all machines

**Pair Programming:**
- Assign pairs for quest work
- Rotate pairs every 2-3 quests
- Navigator/driver roles
- Encourages collaboration

**Help Desk System:**
- Use sticky notes for help requests (red=stuck, green=done)
- Create help queue on whiteboard
- Student helpers answer easy questions

### For Online/Remote Classes

**Synchronous Sessions:**
- Share screen while going through quests
- Use breakout rooms for pair programming
- Live coding demonstrations
- Virtual help desk (raise hand feature)

**Asynchronous:**
- Record walkthroughs of complex quests
- Discussion forum for questions
- Office hours for live help
- Weekly progress videos

---

## 🆘 Handling Common Student Issues

### "The code won't run in my browser"

**Troubleshooting:**
1. Check browser (Chrome, Firefox, Safari, Edge)
2. Refresh page (Ctrl+Shift+R or Cmd+Shift+R)
3. Try incognito/private mode
4. Check internet connection (for initial Pyodide load)
5. Try different browser

**Backup Solution:**
- Download notebook version
- Install Jupyter locally
- Use Google Colab

### "I don't understand the concept"

**Teaching Strategies:**
1. Re-read concept boxes together
2. Draw diagrams/visuals
3. Use physical analogies
4. Look at previous quest examples
5. Peer explanation (teach each other)

### "The challenge is too hard"

**Scaffolding:**
1. Break into smaller steps
2. Provide pseudocode outline
3. Show similar example
4. Pair with stronger student
5. Reveal solution hints gradually

### "I finished early, now what?"

**Extension Activities:**
1. Attempt bonus challenges
2. Modify code with new features
3. Help classmates
4. Start next quest
5. Create original variation

---

## 🎮 Using the Pygame Track

### Prerequisites
Ensure students complete Python fundamentals first:
- Variables & data types
- Functions
- Loops
- Lists/dictionaries

### Setup for Pygame (Required)
Since Pygame can't run in browser:

**Option 1: Lab Computers**
- Pre-install Python + Pygame
- Download all project files
- Create shared folder for student work

**Option 2: Student Laptops**
- Provide setup guide ([setup.qmd](../setup.qmd))
- Schedule "setup day" to help everyone install
- Test installations before starting quest

**Option 3: Cloud IDEs**
- GitHub Codespaces (free tier)
- Replit (Pro account recommended)
- GitPod

### Teaching Pygame Quests

**Quest Structure:**
1. **Play first** — Show completed game
2. **Read tutorial** — Work through quest page together
3. **Code sections** — Build game step-by-step
4. **Test frequently** — Run after each feature
5. **Modify & extend** — Add custom features

**Common Challenges:**
- Window not showing: Check `pygame.display.flip()`
- Colors wrong: RGB values (0-255)
- Movement too fast: Adjust velocity or FPS
- Collision not working: Check rectangles overlap logic

---

## 🏆 Engagement Strategies

### Gamification Ideas

**Quest Completion Badges:**
- Create physical or digital badges
- Award for completing each track
- Special badges for extensions/creativity

**Leaderboard:**
- Track quest completion
- Speed challenges (optional)
- Most creative modifications

**Quest Tournaments:**
- Pygame game tournament (students play each other's games)
- Code golf challenges (shortest code)
- Optimization challenges (fastest algorithm)

### Real-World Connections

**Guest Speakers:**
- Local software developers
- Game developers
- Systems programmers (Rust)

**Field Trips:**
- Game development studio
- Tech company
- Hackathon events

**Project Showcases:**
- End-of-term demo day
- Parents invited
- Display best games/projects

---

## 📚 Additional Resources for Educators

### Professional Development
- Complete all quests yourself first
- Explore modification possibilities
- Join educator communities:
  - CS Teachers subreddit
  - Computer Science Teachers Association (CSTA)

### Supplementary Materials
- [Python Official Docs](https://docs.python.org/)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Real Python Tutorials](https://realpython.com/)

### Creating Custom Content
See [ADDING_NEW_TRACKS.md](ADDING_NEW_TRACKS.md) to create:
- School-specific tracks
- Custom challenges
- Local interest topics

---

## 📞 Support for Educators

### Getting Help
- **Email:** obonhamcarter@allegheny.edu
- **GitHub Issues:** Report bugs or request features
- **FAQ:** [sitedocs/faq.md](faq.md)

### Sharing Your Experience
We'd love to hear how you use CS Quest Adventures:
- Share lesson plans
- Contribute improvements
- Report what works/doesn't work
- Suggest new features

---

## 📄 Sample Syllabus

### CS 101: Introduction to Programming (Python Track)

**Course Description:**
Introduction to computer science through the Python programming language using the CS Quest Adventures platform. Students complete 19 interactive programming quests covering fundamental concepts.

**Prerequisites:** None

**Learning Outcomes:**
- Write Python programs using variables, functions, and control structures
- Analyze and debug code
- Apply algorithmic thinking to problem-solving
- Understand object-oriented programming concepts

**Grading:**
- Quest Challenges: 40%
- Midterm Project: 20%
- Final Project: 25%
- Participation: 15%

**Schedule:**
- Weeks 1-2: Quests 1-2 (Variables, Data Types)
- Weeks 3-4: Quests 3-4 (Conditionals, Loops)
- Weeks 5-6: Quests 5-6 (Lists, Functions)
- Week 7: Midterm Project
- Weeks 8-9: Quests 7-8 (Dictionaries, Fibonacci)
- Weeks 10-11: Quests 9-11 (Sorting, Number Game, Recursion)
- Weeks 12-13: Quests 12-15 (Complexity, Functions Deep-Dive)
- Weeks 14-15: Quests 16-19 (Advanced Topics)
- Week 16: Final Project Presentations

**Required Materials:**
- Computer with internet access
- Browser (Chrome, Firefox, Safari, or Edge)
- [Optional] Python installation for local development

---

## ✅ Quick Start Checklist for Educators

### Before First Class
- [ ] Complete Python Quest 1 yourself
- [ ] Test site on school computers/network
- [ ] Prepare backup plan (offline notebooks)
- [ ] Decide on assessment strategy
- [ ] Create grading rubric for challenges
- [ ] Set up submission system (LMS, email, etc.)

### First Day of Class
- [ ] Demonstrate browser-based coding
- [ ] Walk through first quest together
- [ ] Explain medieval quest theme
- [ ] Show JupyterLite environment
- [ ] Explain assessment/grading
- [ ] Assign Quest 1 as homework

### Ongoing
- [ ] Check student progress weekly
- [ ] Answer questions in office hours
- [ ] Grade challenge submissions
- [ ] Provide feedback on code
- [ ] Adjust pacing as needed

---

[← Back to Home](../index.qmd) | [View FAQ](faq.md) | [View Contributing Guide](contributing.md)
