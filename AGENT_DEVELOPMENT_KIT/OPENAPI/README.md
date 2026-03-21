# OpenAPI Pet Store Agent

This is a full-featured example of an agent using an OpenAPI specification to interact with a REST API.

## Features
- **Dynamic Tool Generation**: Uses `OpenAPIToolset` to parse an OpenAPI spec (JSON) and generate tools.
- **Pet Store Mock**: Interacts with a mock Pet Store API hosted on `httpbin.org`.
- **Session Management**: Demonstrates `InMemorySessionService` and `Runner` for persistent agent interactions.

## Key Concepts
- **Operation Mapping**: Mapping API endpoints (GET /pets, POST /pets) to agent tools.
- **Async Execution**: Using `runner.run_async` for real-time interaction logs.
