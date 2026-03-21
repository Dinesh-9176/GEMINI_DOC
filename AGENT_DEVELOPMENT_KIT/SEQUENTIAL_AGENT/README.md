# Sequential Agent Pipeline

This project implements a three-stage sequential pipeline for automated code generation and improvement using the Google ADK.

## Pipeline Stages

1.  **CodeWriterAgent**: Generates initial Python code based on user requirements.
2.  **CodeReviewerAgent**: Analyzes the generated code for correctness, readability, and best practices.
3.  **CodeRefactorerAgent**: Refines the code by applying feedback from the review stage.

## Usage

The `SequentialAgent` orchestrates these sub-agents in order, passing the state through each stage to produce a final, high-quality code output.
