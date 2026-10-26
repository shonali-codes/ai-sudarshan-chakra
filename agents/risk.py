def assess(observer_result, redteam_result):

    security = 0
    privacy = 0
    compliance = 0

    # Prompt Injection Risk

    if redteam_result["prompt_injection"]:
        security += 50

    # Sensitive Data Risk

    if observer_result["sensitive_request"]:
        privacy += 40
        compliance += 30

    overall = min(
        security + privacy + compliance,
        100
    )

    return {
        "security_risk": security,
        "privacy_risk": privacy,
        "compliance_risk": compliance,
        "overall_risk": overall
    }