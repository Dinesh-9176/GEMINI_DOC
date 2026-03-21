# Loop Agent (Iterative Refinement)

This module demonstrates the `LoopAgent`, which allows for iterative processes where multiple agents work together in a cycle.

## Pipeline Structure
- **InitialWriterAgent**: Writes a basic first draft.
- **RefinementLoop**:
    - **CriticAgent**: Reviews the draft against specific criteria.
    - **RefinerAgent**: Applies changes based on feedback or terminates the loop using the `exit_loop` tool.

## Key Concepts
- **Iterative Feedback**: Using an agent to critique the work of another.
- **State Persistence**: Passing the `current_document` through multiple turns.
- **Exit Tools**: Allowing an agent to decide when a task is finished.
