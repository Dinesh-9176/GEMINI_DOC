# Custom MCP Tools

This advanced example demonstrates bridging ADK tools and the Model Context Protocol (MCP).

## Architecture
1.  **ADK Tool**: A standard ADK tool like `load_web_page` is instantiated.
2.  **MCP Server**: A custom MCP server (`my_adk_mcp_server.py`) wraps the ADK tool and exposes it via the MCP Stdio protocol.
3.  **ADK Agent**: An ADK agent (`agent.py`) connects to this custom MCP server using `StdioConnectionParams`.

## Usage
This pattern allows you to share ADK tools with any MCP-compliant client or use external MCP-wrapped tools within ADK.
