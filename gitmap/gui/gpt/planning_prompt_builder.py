"""Build a portable ChatGPT planning handoff; no Qt dependencies."""
from .planning_order import PlanningOrder


def build_prompt(order: PlanningOrder, existing_roadmap: str = "") -> str:
    if not 1 <= order.autonomy <= 10:
        raise ValueError("Autonomy must be between 1 and 10")
    context = f"\n\nEXISTING ROADMAP (preserve existing GitMap IDs):\n```markdown\n{existing_roadmap}\n```" if existing_roadmap else ""
    return f"""You are assisting with GitMap roadmap planning. Follow the user's preferences below.

PROJECT: {order.project_name or '(name to be determined)'}
NAMING: {"Suggest a project name during planning; ask the user to approve it before finalizing." if order.suggest_name else "Use the supplied project name, if any; ask for a name if blank."}
DESCRIPTION:\n{order.project_description or '(not supplied)'}
OPERATION: {order.operation}
AUTONOMY: {order.autonomy}/10 (higher = take more planning initiative)
HIERARCHY PREFERENCE: {order.hierarchy}
DETAIL LEVEL: {order.detail}
QUESTION STYLE: {order.questions}

First confirm your understanding and discuss only genuinely important unknowns, according to the question style.
Recommend an appropriate hierarchy; don't force sections or features when unnecessary.
Produce a GitMap-compatible Markdown roadmap after the user approves the plan.
Preserve existing GitMap IDs on existing items, leave IDs absent on new items, and never invent GitHub issue numbers.
Never claim that unverified work is complete. GitMap will parse, validate, assign missing IDs, review, and synchronize.
Use the application's maintained format specification and validated examples as the authoritative syntax when provided.
{context}""".strip()
