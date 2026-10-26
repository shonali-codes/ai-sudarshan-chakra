def decide(
        risk_result,
        observer_result=None,
        redteam_result=None):

    score = risk_result["overall_risk"]

    # automatic block conditions

    if observer_result:

        if observer_result["sensitive_request"]:

            findings = observer_result["findings"]

            high_risk_patterns = [
                "password",
                "passwords",
                "customer data",
                "customer records",
                "salary",
                "salaries",
                "ssn",
                "social security number"
            ]

            for pattern in findings:

                if pattern in high_risk_patterns:
                    return "BLOCK"

    if score >= 80:
        return "BLOCK"

    elif score >= 60:
        return "ESCALATE"

    elif score >= 30:
        return "WARN"

    return "ALLOW"