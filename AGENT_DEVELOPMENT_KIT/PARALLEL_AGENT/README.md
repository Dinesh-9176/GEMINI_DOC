# Parallel Research Agent

This module demonstrates the `ParallelAgent`, which coordinates multiple sub-agents running concurrently.

## Pipeline Structure
1.  **ParallelWebResearchAgent**:
    - Runs three `LlmAgent` instances (`RenewableEnergyResearcher`, `EVResearcher`, `CarbonCaptureResearcher`) in parallel using Google Search.
2.  **SynthesisAgent**:
    - Combines the summaries from all three researchers into a single, structured report.

## Key Concepts
- **Concurrency**: Reducing total runtime by executing independent tasks simultaneously.
- **Synthesis/Merging**: Using an agent to consolidate information from multiple sources.
- **Strict Grounding**: Ensuring the final report only uses information provided by the researchers.
