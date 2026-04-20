# 🎣 Task 2: Phishing Detection & Awareness Report

**Prepared by:** [HOGLAH MAWONDO]  
**Internship Track:** Cyber Security (Future Interns)  
**Task ID:** FUTURE_CS_02  

---

## 1. Executive Summary
This project demonstrates the methodology for identifying and analyzing phishing attempts. By evaluating three distinct email samples, I have identified key "Red Flags" used by adversaries, such as **punycode domains**, **sender spoofing**, and **social engineering** tactics. This report serves as a baseline for organizational security awareness.

---

## 2. Technical Analysis & Findings


| Email Sample | Classification | Technical Red Flags Observed | Risk Level |
| :--- | :--- | :--- | :--- |
| **Sample 01: O365 Alert** | 🔴 Phishing | Punycode domain (`micr0soft.com`), Hidden URL redirecting to a credential harvester. | **CRITICAL** |
| **Sample 02: HR Internal** | 🟢 Safe | Validated DKIM/SPF signatures, internal IP origin, expected payroll communication. | **LOW** |
| **Sample 03: DHL Tracking** | 🟠 Suspicious | Display Name Spoofing; 'From' address does not match DHL domain. No active payload detected. | **MEDIUM** |

---

## 3. 🔍 Deep Dive: Phishing Indicators
In my analysis of **Sample 01**, the following indicators were flagged:
1.  **Sender Deception:** The "From" field showed `Microsoft Security`, but the actual header revealed `support@secure-login-392.top`.
2.  **Social Engineering:** Used an "Urgent Account Suspension" theme to bypass the user's critical thinking.
3.  **URL Masking:** The "Verify Now" button link was masked using a URL shortener (`bit.ly/xxxx`) to hide the final malicious destination.

---

## 4. 🐍 Automation: Email Header Analyzer
I developed a Python-based utility to automate the extraction of metadata from `.eml` files. This script checks for high-risk keywords and extracts the `Return-Path` to verify sender authenticity.

### Script Capabilities:
*   **Metadata Extraction:** Pulls Subject, From, and Return-Path.
*   **Heuristic Analysis:** Scans for high-pressure keywords (e.g., *Urgent*, *Suspended*).
*   **Security Validation:** Compares the 'From' field against the 'Return-Path'.

*(Note: The full source code is available in `header_analyzer.py` in this repository.)*

---

## 5. ✅ Prevention & Awareness Guidelines
To protect the organization, users should follow the **"S.T.O.P"** framework:
*   **S**crutinize the Sender: Check the actual email address, not just the name.
*   **T**hink Before Clicking: Hover over links to verify the destination URL.
*   **O**bserve the Tone: Be wary of extreme urgency or threats of account closure.
*   **P**ause and Report: If it looks suspicious, use the "Report Phishing" button immediately.
