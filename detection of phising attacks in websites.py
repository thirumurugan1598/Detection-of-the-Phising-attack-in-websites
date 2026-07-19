from urllib.parse import urlparse
import re

def detect_phishing(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # 1. HTTPS check
    if parsed.scheme != "https":
        score += 2
        reasons.append("Website is not using HTTPS.")

    # 2. IP address instead of domain
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain):
        score += 3
        reasons.append("Uses an IP address instead of a domain name.")

    # 3. Too many subdomains
    if domain.count(".") > 3:
        score += 2
        reasons.append("Unusually large number of subdomains.")

    # 4. Suspicious keywords
    suspicious = [
        "login",
        "verify",
        "secure",
        "update",
        "account",
        "bank",
        "signin"
    ]

    for word in suspicious:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious keyword: {word}")

    # 5. Long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long.")

    print("=" * 50)
    print("Website:", url)
    print("=" * 50)

    if score >= 6:
        print("⚠️ High Risk")
    elif score >= 3:
        print("⚡ Medium Risk")
    else:
        print("✅ Low Risk")

    print("\nRisk Score:", score)

    print("\nReasons:")
    if reasons:
        for reason in reasons:
            print("-", reason)
    else:
        print("- No obvious phishing indicators detected.")

# Example
detect_phishing("hhttps://amazon.in")