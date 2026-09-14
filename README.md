# 🚀 DevOps Internship — Day 01

> **Foundation First. Automate Later.**

**Day 01** marks the beginning of my DevOps internship learning journey.

The first day was focused on building a practical foundation in **DevOps fundamentals, Linux, Ubuntu, Bash, Git, and GitHub**. The goal was not only to learn commands, but to understand how these tools fit into a real development and DevOps workflow.

---

## 🧭 Learning Journey

```text
┌───────────────────────┐
│    DevOps Concepts    │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│    Linux / Ubuntu     │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│     Bash Commands     │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│         Git           │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│       GitHub          │
└───────────┬───────────┘
            ↓
      Docker → CI/CD → Cloud
```

---

# 📌 Day 01 Overview

| Category             | Details                     |
| -------------------- | --------------------------- |
| 🐧 OS                | Ubuntu Linux                |
| 💻 Shell             | Bash                        |
| 🔧 Version Control   | Git                         |
| ☁️ Remote Repository | GitHub                      |
| 🎯 Primary Focus     | Linux + Git Fundamentals    |
| 🧪 Learning Approach | Learn → Practice → Document |
| 📅 Internship Stage  | Day 01                      |

---

# 🎯 Objectives

The main objectives for Day 01 were:

* Understand the fundamentals of DevOps
* Understand why Linux is widely used in DevOps
* Become comfortable working with the Ubuntu terminal
* Understand Linux paths and filesystem hierarchy
* Create and manage files and directories from the command line
* Understand the basic Git version-control workflow
* Understand how Git tracks project changes
* Connect a local Git repository with GitHub
* Build a foundation for Docker and CI/CD

---

# 🧠 01 — DevOps Fundamentals

## What is DevOps?

DevOps is a combination of **development practices, operational practices, automation, collaboration, and continuous improvement** designed to make software delivery faster, reliable, and repeatable.

A simplified software delivery flow:

```text
Plan
  ↓
Code
  ↓
Build
  ↓
Test
  ↓
Release
  ↓
Deploy
  ↓
Operate
  ↓
Monitor
  ↺
```

### Key concepts introduced

* Collaboration
* Automation
* Continuous Integration
* Continuous Delivery
* Infrastructure
* Monitoring
* Feedback
* Continuous improvement

### Core idea

> **DevOps is not just a collection of tools. It is a way of building and delivering software efficiently through collaboration and automation.**

---

# 🐧 02 — Linux & Ubuntu

Linux is an important part of modern DevOps environments because many servers, cloud workloads, containers, and development environments run on Linux.

During Day 01, I worked with **Ubuntu** and the **Bash terminal**.

### Areas explored

* Linux command line
* Current working directory
* Absolute and relative paths
* Files and directories
* Directory navigation
* File creation
* File copying
* File movement
* File deletion
* Linux filesystem hierarchy

---

# ⌨️ 03 — Linux Command Practice

## 📍 Navigation Commands

| Command | Purpose                               |
| ------- | ------------------------------------- |
| `pwd`   | Display the current working directory |
| `ls`    | List files and directories            |
| `cd`    | Change the current directory          |

Example:

```bash
pwd
ls
cd devops-internship
```

---

## 📁 File & Directory Commands

| Command | Purpose            |
| ------- | ------------------ |
| `mkdir` | Create a directory |
| `touch` | Create a file      |

Example:

```bash
mkdir day-01
cd day-01
touch README.md
```

---

## 🔄 File Management Commands

| Command | Purpose                     |
| ------- | --------------------------- |
| `cp`    | Copy files or directories   |
| `mv`    | Move or rename files        |
| `rm`    | Remove files or directories |

Example:

```bash
cp README.md backup.md
mv backup.md notes.md
rm notes.md
```

---

# 🌳 04 — Linux Filesystem

Linux uses a hierarchical filesystem that begins at the root directory:

```text
/
├── home/
│   └── user/
├── etc/
├── var/
├── usr/
├── tmp/
├── bin/
└── root/
```

### Important directories

| Directory | Purpose                                |
| --------- | -------------------------------------- |
| `/`       | Root of the filesystem                 |
| `/home`   | User home directories                  |
| `/etc`    | System configuration files             |
| `/var`    | Variable data such as logs             |
| `/usr`    | User applications and system resources |
| `/tmp`    | Temporary files                        |
| `/bin`    | Essential command binaries             |
| `/root`   | Root user's home directory             |

Understanding filesystem structure is important when working with **servers, applications, logs, configuration files, and deployment environments**.

---

# 🔀 05 — Git Fundamentals

Git is a **distributed version control system** that allows developers to track changes, create versions, collaborate, and safely manage source code.

Instead of manually keeping multiple copies of a project:

```text
project-final
project-final-v2
project-final-new
project-final-latest
```

Git maintains a structured history of changes.

---

# 🔄 Git Workflow

The basic Git workflow learned during Day 01:

```text
             ┌─────────────────┐
             │ Working         │
             │ Directory       │
             └────────┬────────┘
                      ↓
             ┌─────────────────┐
             │ Staging Area    │
             └────────┬────────┘
                      ↓
             ┌─────────────────┐
             │ Local Repository│
             │    Commit       │
             └────────┬────────┘
                      ↓
             ┌─────────────────┐
             │     GitHub      │
             │ Remote Repo     │
             └─────────────────┘
```

### What happens?

**Working Directory**

Files are created or modified here.

↓

**Staging Area**

Changes are selected for the next commit.

↓

**Commit**

Git creates a permanent snapshot of the staged changes.

↓

**GitHub**

The local repository can be pushed to a remote GitHub repository for backup and collaboration.

---

# 🛠️ 06 — Git Commands Practiced

### Initialize a repository

```bash
git init
```

Creates a new Git repository.

### Check repository status

```bash
git status
```

Shows modified, staged, and untracked files.

### Stage changes

```bash
git add .
```

Stages the current changes.

### Create a commit

```bash
git commit -m "Initial commit"
```

Creates a snapshot of the staged changes.

### Check branches

```bash
git branch
```

Displays the available local branches.

### Check remote repositories

```bash
git remote -v
```

Displays configured remote repository URLs.

### Push changes

```bash
git push
```

Uploads local commits to the remote repository.

---

# 🌐 07 — Git + GitHub Workflow

The practical workflow followed was:

```text
Create Project
      ↓
Initialize Git
      ↓
Create / Modify Files
      ↓
git status
      ↓
git add
      ↓
git commit
      ↓
Connect GitHub
      ↓
git push
```

This helped me understand the difference between:

**Git → Version control system**

**GitHub → Remote platform for hosting and collaboration**

---

# 🧪 08 — Hands-On Practice

During the practical session, I worked directly inside the Ubuntu terminal.

### File management practice

```bash
mkdir devops-practice
cd devops-practice

touch file1.txt
touch file2.txt

mkdir backup

cp file1.txt backup/
mv file2.txt backup/

ls
```

### Git practice

```bash
git init

git status

git add .

git commit -m "Initial commit"

git branch

git remote -v

git push
```

This connected the Linux command-line workflow with Git version control and GitHub.

---

# 💡 09 — Key Concepts Learned

### 🐧 Linux

Linux provides a powerful command-line environment widely used for servers, cloud infrastructure, containers, and DevOps tooling.

### 💻 Bash

Bash allows developers and engineers to interact with Linux efficiently through commands and scripts.

### 🔧 Git

Git tracks changes and maintains the history of a project.

### ☁️ GitHub

GitHub provides remote repository hosting and collaboration capabilities around Git.

### 🚀 DevOps

DevOps combines people, processes, practices, and automation to improve the software delivery lifecycle.

---

# 🧩 10 — What I Understood Today

Before Day 01:

```text
Code
 ↓
????
 ↓
Deployment
```

After Day 01:

```text
Developer
    ↓
Linux Environment
    ↓
Git Version Control
    ↓
GitHub Repository
    ↓
Build & Test
    ↓
CI/CD
    ↓
Deployment
```

This gave me a clearer understanding of how **Linux and Git become the foundation for later DevOps automation**.

---

# 📊 11 — Day 01 Progress

### DevOps

* [x] DevOps fundamentals
* [x] DevOps lifecycle introduction
* [x] Automation concept
* [x] CI/CD introduction

### Linux

* [x] Ubuntu environment
* [x] Bash terminal
* [x] Linux filesystem
* [x] Paths
* [x] File management
* [x] Directory management

### Git & GitHub

* [x] Git initialization
* [x] Git status
* [x] Staging
* [x] Commits
* [x] Branches
* [x] Remote repositories
* [x] GitHub push workflow

---

# 🏆 Day 01 Outcome

By completing Day 01, I established the basic workflow required for the upcoming DevOps stages:

```text
             FOUNDATION
                 │
        ┌────────┴────────┐
        ↓                 ↓
      Linux              Git
        │                 │
        └────────┬────────┘
                 ↓
              GitHub
                 ↓
             Automation
                 ↓
              Docker
                 ↓
               CI/CD
                 ↓
               Cloud
```

> **The goal of Day 01 was not to master DevOps, but to build the foundation required to learn it properly.**

---

# 🔮 Next — Day 02

The next stage of the internship will move deeper into **Git and development workflows**, including:

* Git branching
* Branch management
* Merging
* Pull Requests
* Git collaboration workflow
* `.gitignore`
* Merge conflicts
* GitHub repository management

Eventually, this foundation will lead into:

```text
Git
 ↓
GitHub
 ↓
Docker
 ↓
CI/CD
 ↓
Jenkins
 ↓
Cloud
 ↓
Infrastructure
 ↓
Production
```

---

# 📚 Day 01 Learning Log

| Metric              | Status      |
| ------------------- | ----------- |
| DevOps Fundamentals | ✅ Completed |
| Ubuntu              | ✅ Completed |
| Linux Filesystem    | ✅ Completed |
| Linux Commands      | ✅ Practiced |
| Git Fundamentals    | ✅ Completed |
| GitHub Workflow     | ✅ Practiced |
| Documentation       | ✅ Completed |

---

## 👨‍💻 DevOps Internship Journey

### `DAY 01 — LINUX + GIT FOUNDATIONS`

**Learn → Practice → Understand → Document → Automate**

> *Strong foundations create reliable systems.*
