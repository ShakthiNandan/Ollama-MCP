import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client  # built-in SSE transport

async def main():
    url = "http://[::1]:8931/sse"  # MCP server SSE endpoint from config
    try:
        print(f"Attempting to connect to MCP server at {url}...")
        async with sse_client(url=url) as (reader, writer):
            print("SSE connection established")
            async with ClientSession(reader, writer) as session:
                print("Initializing session...")
                await session.initialize()
                print("Session initialized successfully")
                
                # List available tools
                tools = await session.list_tools()
                print("\nAvailable MCP tools:")
                for tool in tools:
                    print(f"- {tool}")
                
                # Optional: You can uncomment to test a specific tool if needed
                # if "mcp_playwright_browser_snapshot" in tools:
                #     print("\nTesting browser snapshot tool...")
                #     result = await session.call_tool("mcp_playwright_browser_snapshot", {})
                #     print(f"Snapshot result: {result}")
                
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")

if __name__ == "__main__":
    asyncio.run(main())
