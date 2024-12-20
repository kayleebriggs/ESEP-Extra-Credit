# ESEP-Extra-Credit
In-Memory Database with Transaction Support

## Overview
This project implements an in-memory key-value database with transaction support. It supports operations such as `begin_transaction`, `put`, `get`, `commit`, and `rollback`.

## Features
1. **Key-Value Store**: Keys are strings, and values are integers.
2. **Transactions**: Changes are isolated until committed, ensuring data integrity.
3. **Error Handling**: Operations outside of transactions throw exceptions.

## Instructions to Run
1. Clone the repository.
2. Ensure Python 3.7+ is installed.
3. Run the script:
   ```bash
   python main.py

## Suggestions
- While it would make the assignment less free, I think providing a test suite would make this more direct so that students can know what their precise output should be. This would make things for graders easier as well. 
- If you dont want to limit the language for this assignment, you could require that students make their own tests and submit a screenshot of the output. 
- More explicit instructions about expected behavior in edge cases. 
- The assignment doesn't outline anything about how the code will actually be graded, it might be more interesting if I were expected to take in some user input, which I would have to then verify is in the correct format and implement it.
