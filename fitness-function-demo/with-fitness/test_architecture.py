import ast
from pathlib import Path

def test_no_direct_import_of_inventory_service():
    violations = []
    code = Path("order_service.py").read_text()
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module and "inventory" in node.module:
                violations.append(f"Line {node.lineno}: imports {node.module}")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if "inventory" in alias.name:
                    violations.append(f"Line {node.lineno}: imports {alias.name}")
    assert not violations, f"Fitness function failed: direct inventory import found"
