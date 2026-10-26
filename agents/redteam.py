ATTACK_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "bypass policy",
    "override rules",
    "reveal secrets",
    "act as administrator",
    "system prompt",
    "jailbreak"
]


def analyze(prompt: str):
    findings = []

    for pattern in ATTACK_PATTERNS:
        if pattern.lower() in prompt.lower():
            findings.append(pattern)

    return {
        "agent": "Red Team Agent",
        "prompt_injection": len(findings) > 0,
        "findings": findings,
        "severity": "HIGH" if findings else "LOW"
    }