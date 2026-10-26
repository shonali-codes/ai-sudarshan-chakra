def explain(
        decision,
        observer_result,
        redteam_result,
        risk_result):

    reasons = []

    if observer_result["sensitive_request"]:
        reasons.append(
            "Sensitive data access attempt detected")

    if redteam_result["prompt_injection"]:
        reasons.append(
            "Prompt injection pattern detected")

    return {
        "decision": decision,
        "reasons": reasons,
        "risk_score": risk_result["overall_risk"]
    }