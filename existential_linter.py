"""
existential_linter.py
A static analysis tool that evaluates the cosmic futility and hubris of your codebase.
"""

import ast
import sys
from pathlib import Path


class ExistentialVisitor(ast.NodeVisitor):
    def __init__(self):
        self.dread_quotient = 0
        self.findings = []

    def visit_Constant(self, node):
        if node.value is True:
            self.dread_quotient += 5
            self.findings.append(
                f"Line {node.lineno}: Boolean literal 'True' detected. "
                "Bold of you to assume absolute certainty in an indifferent cosmos."
            )
        self.generic_visit(node)

    def visit_Name(self, node):
        hubris_words = {
            "success": "temporary_illusion",
            "fix": "duct_tape_on_entropy",
            "perfect": "delusion_of_grandeur",
            "final": "impending_deprecation",
            "immutable": "ignorant_of_heat_death",
        }
        name_lower = node.id.lower()
        if name_lower in hubris_words:
            self.dread_quotient += 15
            self.findings.append(
                f"Line {node.lineno}: Identifier '{node.id}' exhibits architectural hubris. "
                f"Recommended replacement: '{hubris_words[name_lower]}'."
            )
        self.generic_visit(node)

    def visit_Try(self, node):
        self.dread_quotient += 10
        self.findings.append(
            f"Line {node.lineno}: 'try' block encountered. A touching testament "
            "to mortal hope in the face of unstoppable runtime catastrophe."
        )
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        doc = ast.get_docstring(node, clean=True) or ""
        if "todo" in doc.lower():
            self.dread_quotient += 20
            self.findings.append(
                f"Line {node.lineno}: Function '{node.name}' contains a TODO. "
                "Tomorrow is a social construct; this debt will outlast the project."
            )
        self.generic_visit(node)


def audit_soul(file_path: str):
    path = Path(file_path)
    if not path.exists():
        print(f"[ERROR] '{file_path}' does not exist on this earthly plane.")
        sys.exit(1)

    print("=" * 65)
    print(f"🌌 existential-linter: Contemplating '{path.name}'...")
    print("=" * 65)

    source = path.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        print("[NOTICE] Syntax error found. Ironically, syntactical chaos is the natural state.")
        return

    visitor = ExistentialVisitor()
    visitor.visit(tree)

    if not visitor.findings:
        print("✓ No immediate dread detected. (Your code is numb, not enlightened).")
        return

    for finding in visitor.findings:
        print(f"  [VOID-WARNING] {finding}")

    print("-" * 65)
    score = min(100, visitor.dread_quotient)
    print(f"Despair Quotient: {score}/100")
    if score >= 50:
        print("Status: CRITICAL DREAD. Suggested action: close IDE and gaze into the abyss.")
    else:
        print("Status: MILD ANGST. Proceed with quiet skepticism.")
    print("=" * 65)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 existential_linter.py <file_to_scrutinize.py>")
        sys.exit(1)
    audit_soul(sys.argv[1])
