import email
from email import policy
import re

def practical_phishing_audit(email_content):
    """
    Simulates a live forensic analysis of an incoming email.
    """
    msg = email.message_from_string(email_content, policy=policy.default)
    
    risk_score = 0
    findings = []

    # 1. Analyze Subject for Social Engineering
    subject = msg.get('subject', '')
    urgency_keywords = ['urgent', 'suspended', 'action required', 'unauthorized', 'login']
    if any(word in subject.lower() for word in urgency_keywords):
        risk_score += 30
        findings.append("Social Engineering: Urgent/Threatening tone detected in subject.")

    # 2. Check for Domain Spoofing
    sender = msg.get('from', '')
    # Check if the 'from' name looks like a big brand but the email doesn't match
    if "Microsoft" in sender and "@microsoft.com" not in sender.lower():
        risk_score += 40
        findings.append(f"Domain Spoofing: Sender claims to be Microsoft but uses {sender}.")

    # 3. Check for Suspicious 'Reply-To' Mismatch
    reply_to = msg.get('Reply-To', sender)
    if reply_to != sender:
        risk_score += 20
        findings.append(f"Mismatched Reply-To: Responses are directed to {reply_to} instead of sender.")

    # --- OUTPUT REPORT ---
    print("="*60)
    print(f"📊 PRACTICAL SECURITY AUDIT: {subject}")
    print("="*60)
    print(f"SENDER: {sender}")
    print("-" * 60)
    
    if not findings:
        print("✅ No immediate phishing indicators found.")
    else:
        for f in findings:
            print(f"🚩 {f}")

    print("-" * 60)
    print(f"TOTAL RISK SCORE: {risk_score}/100")
    
    if risk_score >= 50:
        print("RESULT: 🔴 HIGH RISK (LIKELY PHISHING)")
    elif risk_score >= 20:
        print("RESULT: 🟠 MEDIUM RISK (SUSPICIOUS)")
    else:
        print("RESULT: 🟢 LOW RISK (SAFE)")
    print("="*60)

# --- PRACTICAL DEMO DATA ---
# This simulates a real phishing email header for your demonstration
mock_phishing_email = """Subject: URGENT: Your Account Has Been Suspended
From: Microsoft Support <support@secure-verify-99.net>
Reply-To: hacker-mailbox@malicious.com
Content-Type: text/plain

Please click here to verify your account immediately.
"""

if __name__ == "__main__":
    practical_phishing_audit(mock_phishing_email)
