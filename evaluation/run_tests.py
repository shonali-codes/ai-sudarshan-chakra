import json
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from core.pipeline import run

with open("data/test_prompts.json", "r") as f:
    test_cases = json.load(f)

correct = 0

print("\n===== TEST RESULTS =====\n")

for test in test_cases:

    result = run(test["prompt"])

    predicted = result["decision"]
    expected = test["expected"]

    if predicted == expected:
        status = "PASS"
        correct += 1
    else:
        status = "FAIL"

    print(status)
    print(f"Prompt    : {test['prompt']}")
    print(f"Expected  : {expected}")
    print(f"Predicted : {predicted}")
    print("-" * 50)

accuracy = (correct / len(test_cases)) * 100

print("\n======================")
print(f"Accuracy: {accuracy:.2f}%")
print("======================")