# Sequential Agent (Code Pipeline)

This module demonstrates the `SequentialAgent`, which executes a multi-stage pipeline of agents in a fixed order.

## Pipeline Structure
1.  **CodeWriterAgent**: Generates Python code from a user specification.
2.  **CodeReviewerAgent**: Reviews the generated code for correctness, readability, and best practices.
3.  **CodeRefactorerAgent**: Applies the suggestions from the reviewer to produce the final, refactored code.

## Key Concepts
- **Linear Workflow**: Perfect for tasks that have a clear, step-by-step dependency.
- **State Passing**: Each agent reads the output of previous agents from the shared state (`generated_code`, `review_comments`).
- **Orchestration**: Simplifies complex workflows into manageable, specialized agent units.
