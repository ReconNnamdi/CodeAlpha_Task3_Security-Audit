# CodeAlpha Task 3 - Security Audit

## Objective
Audit a Python login system for vulnerabilities using Bandit, then remediate and verify the fixes.

## Vulnerabilities Found
1. **SQL Injection (B608)**: Query built using string concatenation.
2. **Hardcoded Password (B105)**: Password stored in plain text.

## Security Fixes Applied
- Used parameterized queries `?` to prevent SQL Injection
- Hashed passwords with `hashlib.sha256()`
- Added input validation
- Removed hardcoded credentials

## How to Run
1. Run `python secure_login.py`
2. Test login: `admin` / `123456`
3. Run `bandit -r secure_login.py` to verify - Result: No issues identified

## Evidence
Screenshots of vulnerable scan, secure code running, and clean bandit scan are included.

**Internship:** CodeAlpha
