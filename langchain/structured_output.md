Use **TypedDict** if
- You only need type hints (basic structure enforcement)
- You don't need validation (e.g checking numbers are positive)
- You trust LLM to return correct data

Use **Pydantic** if
- You need data validation
- You need default values if LLM misses them
- You want automatic type conversion

Use **Json Schema** if
- You don't want to import extra python Libraries
- You need data validation but don't need python objects
- You want to define structure in a standard Json format


## When to Use What?

| Feature                  | TypedDict | Pydantic | JSON Schema |
|--------------------------|:---------:|:--------:|:-----------:|
| ✅ Basic structure        | ✓         | ✓        | ✓           |
| ✅ Type enforcement       | ✓         | ✓        | ✓           |
| ✅ Data validation        | ✗         | ✓        | ✓           |
| ✅ Default values         | ✗         | ✓        | ✗           |
| ✅ Automatic conversion   | ✗         | ✓        | ✗           |
| ✅ Cross-language compatibility | ✗   | ✗        | ✓           |
