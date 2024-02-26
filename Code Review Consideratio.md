###Code Reviewer Checklist:

When commiting code make sure you write clear, concise and descriptive commit messages. <br>
Your reviewer should always be able to tell what the code is supposed to do from the commit message. <br>

Make sure you make changes to the code in your branch before commiting changes. <br>

Make sure you consider these coding standards and guidelines when reviewing pull requests. When you finish your review provide constructive feedback if necessary. <br>

1. **Readability:**
   - Code is well-formatted.
   - Variable and function names are descriptive and follow naming conventions.
   - Adequate comments are present for complex sections or where clarification is needed.

2. **Functionality:**
   - Code meets the specified requirements and adheres to the design.
   - Edge cases and potential error scenarios are considered and handled appropriately.
   - No dead code or unused variables/methods.

3. **Modularity:**
   - Code is organized into logical and modular components or functions.
   - Functions are not overly long or complex.

### Code Structure:
4. **Imports and Dependencies:**
   - All required libraries/modules are imported.
   - Unused imports are removed.

5. **File Structure:**
   - Files are organized logically.
   - No unnecessary files or duplicated functionality.

6. **Error Handling:**
   - Appropriate error handling mechanisms are in place.
   - Error messages are clear and informative.

### Performance:
7. **Time and Space Complexity:**
   - Code is optimized for time and space complexity where necessary/possible.

### Testing:
8. **Unit Tests:**
   - Unit tests cover critical parts of the code.
   - Tests are meaningful and cover various scenarios.

9. **Integration Tests:**
    - Integration tests verify interactions between components.

### Documentation:
10. **Code Comments:**
    - Sufficient inline comments explain complex or non-intuitive sections.
    - Comments are up-to-date with the code changes.

11. **Documentation Files:**
    - README or documentation files are updated to reflect changes.
    - API documentation is accurate and complete.

### Best Practices:
12. **Code Duplication:**
    - Check for duplicated code and suggest refactoring if needed.
