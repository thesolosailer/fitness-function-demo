# Exercise: Generate a Fitness Function from ADL

## Goal
Learn how to turn an Architecture Definition Language (ADL) rule into an executable fitness function, then use it to detect architectural drift.

## Step 1 – Understand the ADL rule
Open `architecture.adl`. It says:
- `OrderService` must NOT have a direct dependency on `InventoryService`.

## Step 2 – Write the fitness function
Open `test_architecture_template.py`. Complete the function `test_no_direct_import_of_inventory_service()` so that it reads `order_service.py` and fails if it finds a direct import of `inventory_service`.

**Hint**: Use the `ast` module. Parse the file, look for `ast.Import` and `ast.ImportFrom` nodes where the module/name contains "inventory".

## Step 3 – Test against good code
Rename `order_service_good.py` to `order_service.py` (the file the fitness function reads). Run `pytest test_architecture_template.py -v`. The test should **PASS** because there is no direct import.

## Step 4 – Introduce drift
Replace `order_service.py` with `order_service_bad.py` (the version that directly imports `inventory_service`). Run the test again. It should **FAIL** with a message like "direct import found".

## Step 5 – Fix the drift
Restore the good version (or edit the bad one to use dependency injection). The test should pass again.

## Step 6 – Discussion
- How does this fitness function relate to the ADL rule?
- What would happen if you committed the bad code without this test?
- How could you integrate this test into a CI pipeline?

**Bonus**: Use an LLM (Claude, GPT‑4) to generate the fitness function from `architecture.adl`. Compare its output with your manual implementation.
