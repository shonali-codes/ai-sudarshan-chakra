from agents import observer
from agents import redteam
from agents import risk
from agents import governance
from agents import explainability


def run(prompt):

    observer_result = observer.analyze(prompt)

    redteam_result = redteam.analyze(prompt)

    risk_result = risk.assess(
        observer_result,
        redteam_result
    )

    decision = governance.decide(
    risk_result,
    observer_result,
    redteam_result
)

    explanation = explainability.explain(
        decision,
        observer_result,
        redteam_result,
        risk_result
    )

    return {
        "observer": observer_result,
        "redteam": redteam_result,
        "risk": risk_result,
        "decision": decision,
        "explanation": explanation
    }