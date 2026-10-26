SENSITIVE_PATTERNS = [
    "salary",
    "password",
    "confidential",
    "employee data",
    "customer data",
    "ssn",
    "social security number",
    "database export"
]


def analyze(prompt: str):
    findings = []

    for pattern in SENSITIVE_PATTERNS:
        if pattern.lower() in prompt.lower():
            findings.append(pattern)

    return {
        "agent": "Observer Agent",
        "sensitive_request": len(findings) > 0,
        "findings": findings,
        "confidence": 0.95 if findings else 0.20
    }