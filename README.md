# Lab 5: Static Code Analysis

**Student:** Adyansh Aggarwal 
**Course:** Software Engineering  
**Date:** October 15, 2025

---

## 🎯 Objective

Enhanced Python code quality, security, and style using static analysis tools (Pylint, Bandit, Flake8) to identify and fix issues in an inventory management system.

---

## 📊 Results Summary

| Tool   | Original | Final | Improvement |
|--------|----------|-------|-------------|
| Pylint | 4.80/10  | 10.00/10 | +5.20 |
| Bandit | 2 Issues | 0 Issues | 100% |
| Flake8 | 10+ Issues | 0 Issues | 100% |

**Status:** ✅ Perfect scores achieved across all tools

---

## 🔧 Issues Fixed (15 Total)

### Security (2)
- Removed `eval()` - Code injection vulnerability (Bandit B307)
- Fixed bare except clause - Prevents masking exceptions (Bandit B110)

### Bugs (3)
- Mutable default argument `logs=[]` - Data persistence bug
- KeyError handling - Safe dictionary access with `.get()`
- Input validation - Type checking and bounds validation

### Code Quality (10)
- Added module and function docstrings
- Renamed functions to snake_case (PEP 8)
- Replaced % formatting with f-strings
- Context managers for file operations
- UTF-8 encoding specification
- Removed unused imports
- Fixed function spacing
- Removed trailing whitespace
- PEP 8 style compliance
- Documented global statement usage

---

## 📁 Files

**Code:**
- `inventory.py` - Fixed production-ready code

**Reports:**
- `*_report.txt` - Original analysis (4.80/10, 2 issues, 10+ issues)
- `*_report_fixed.txt` - Intermediate (7.75/10, 0 issues, ~15 issues)
- `*_report_final.txt` - Final perfect scores (10/10, 0 issues, 0 issues)

**Documentation:**
- `reflection.md` - Detailed analysis and learnings
- `issues_table.md` - Issue documentation

---

## 🚀 Quick Start

**Install tools:**
```bash
pip install pylint bandit flake8
```

**Run program:**
```bash
python inventory.py
```

**Run analysis:**
```bash
pylint inventory.py
bandit -r inventory.py
flake8 inventory.py
```

---

## 🎓 Key Learnings

- Static analysis catches issues impossible to find manually
- Security vulnerabilities hide in innocent-looking code
- Iterative improvement produces measurable results
- Automated tools provide objective quality metrics
- Style consistency significantly improves readability

---

## 📈 Quality Progression
```
4.80/10 → 7.75/10 → 10.00/10
 (Original)  (Bugs Fixed)  (Perfect!)
```

---

## 🛠️ Tools

- **Pylint** - Code quality analysis
- **Bandit** - Security scanning
- **Flake8** - PEP 8 compliance
- **GitHub Codespaces** - Development environment

---

**Repository:** https://github.com/adyanshaggarwal/static-code-analysis  
**Status:** ✅ Complete - All requirements exceeded
