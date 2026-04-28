import ast
from pathlib import Path

def test_no_direct_import_of_inventory_service():
    """Fitness function: order_service.py must not directly import inventory_service"""
    # Read the order_service.py file
    source_file = Path("order_service_good.py")
    with open(source_file, 'r') as f:
        code = f.read()
    
    # Parse the code into an AST
    tree = ast.parse(code)
    
    # Walk the tree and check for direct imports of inventory_service
    for node in ast.walk(tree):
        # Check for 'import inventory_service' statements
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "inventory_service":
                    raise AssertionError(f"VIOLATION: Direct import of inventory_service found in {source_file}")
        
        # Check for 'from inventory_service import ...' statements
        if isinstance(node, ast.ImportFrom):
            if node.module == "inventory_service":
                raise AssertionError(f"VIOLATION: Direct import from inventory_service found in {source_file}")
    
    print(f"PASS: {source_file} does not directly import inventory_service")


if __name__ == "__main__":
    test_no_direct_import_of_inventory_service()
