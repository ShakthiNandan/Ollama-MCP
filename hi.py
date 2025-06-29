import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client  # <-- built-in SSE transport

async def main():
    url = "http://localhost:8931/sse"  # your MCP server SSE endpoint
    async with sse_client(url=url) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools:", tools)
            # Optionally call a tool:
            # resp = await session.call_tool("tool_name", arguments={...})
            # print(resp)

asyncio.run(main())
