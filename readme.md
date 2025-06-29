Technologies:
OLLAMA
PYTHON PLAYWRIGHT 
PLAYWRIGHT MCP
MCPO
PYTHON OPEN WEBUI
DOCKER OPEN WEBUI
-------------------------------------------------------------------------------------------------------------------------------------------
## OLLAMA:
1) Start the ollama server:
```ollama```
2) Pull the LLM:
```ollama run llama3-groq-tool-use:latest```
-------------------------------------------------------------------------------------------------------------------------------------------
## PYTHON PLAYWRIGHT:

1) Install the Playwright Module
```pip install pytest-playwright```
2) Playwright config
```playwright install```
-------------------------------------------------------------------------------------------------------------------------------------------
## PLAYWRIGHT MCP:
1) Playwright Setup:
```npx @aethr/playwright-mcp@latest```
            (OR)
```npx @playwright/mcp```

2) To run the Playwright Server:

```npx @aethr/playwright-mcp@latest --config mcp.config.json```
            (OR)
```npx @playwright/mcp --config mcp.config.json```

3) Save the file "mcp.config.json"
--------------------------------------------------------------------------------------------------
    {
    "browser": {
        "browserName": "chromium",
        "launchOptions": {
        "headless": false
        }
    },
    "server": {
        "host": "localhost",
        "port": 8931
    },
    "capabilities": ["core", "tabs", "pdf", "wait"],
    "exposedTools": [
        "browser_navigate",
        "browser_click",
        "browser_type",
        "browser_close",
        "browser_resize",
        "browser_take_screenshot",
        "browser_snapshot",
        "browser_pdf_save",
        "browser_handle_dialog",
        "browser_press_key",
        "browser_hover",
        "browser_drag",
        "browser_select_option",
        "browser_tab_list",
        "browser_tab_new",
        "browser_tab_select",
        "browser_tab_close",
        "browser_wait_for",
        "browser_network_requests",
        "browser_console_messages",
        "browser_assert_contain_text"
    ]
    }

--------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
## MCPO:
1) Install MCPO Module
```pip install mcpo```
2) Save the file "config.json"
    {
    "model": "ollama:localhost:11434/llama3-groq-tool-use:latest",
    "mcpServers": {
        "playwright": {
        "url": "http://localhost:8931/"
        }
    }
    }
            (or)

    {
    "mcpServers": {
        "memory": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"]
        },
        "time": {
        "command": "uvx",
        "args": ["mcp-server-time", "--local-timezone=America/New_York"]
        },
        "mcp_sse": {
        "type": "sse", // Explicitly define type
        "url": "http://127.0.0.1:8001/sse",
        "headers": {
            "Authorization": "Bearer token",
            "X-Custom-Header": "value"
        }
        },
        "mcp_streamable_http": {
        "type": "streamable_http",
        "url": "http://127.0.0.1:8002/mcp"
        } // Streamable HTTP MCP Server
    }
    }

3) Run MCPO:
```mcpo --config config.json```

-------------------------------------------------------------------------------------------------------------------------------------------
## PYTHON OPEN WEBUI:
1) Install Open WEBUI Package
    ```pip install open-webui```
2) Serve the UI
    ```open-webui serve```
-------------------------------------------------------------------------------------------------------------------------------------------
## DOCKER OPEN WEBUI
1) Save the docker-compose.yml
--------------------------------------------------------------------------------------------------
```
    version: "3.9"

    services:
    ollama:
        image: ollama/ollama
        container_name: ollama
        restart: always
        volumes:
        - ollama:/root/.ollama
        ports:
        - "11434:11434"
        deploy:
        resources:
            reservations:
            devices:
                - capabilities: [gpu]

    openwebui:
        image: ghcr.io/open-webui/open-webui:ollama
        container_name: openwebui
        restart: always
        ports:
        - "3000:8080"
        volumes:
        - openwebui:/app/backend/data
        depends_on:
        - ollama
        extra_hosts:
        - "host.docker.internal:host-gateway"
        environment:
        - OLLAMA_BASE_URL=http://ollama:11434

    volumes:
    ollama:
    openwebui:
```
--------------------------------------------------------------------------------------------------
2) Start the container from Docker Desktop