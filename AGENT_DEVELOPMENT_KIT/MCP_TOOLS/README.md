# MCP Tools (Filesystem)

This module demonstrates integrating the standard Model Context Protocol (MCP) filesystem server.

## Features
- **MCP Stdio Protocol**: Connects to an external MCP server via standard input/output.
- **`npx` Deployment**: Automatically installs and runs the `@modelcontextprotocol/server-filesystem` using `npx`.

## Example
`agent.py` configures a `filesystem_assistant_agent` that can list, read, and manage files in a target folder using the MCP server.

> [!IMPORTANT]
> The `TARGET_FOLDER_PATH` must be an absolute path that the `npx` process can access.
