# Tech Context

**Programming Language:** Python 3.11+

**Core Libraries/Frameworks:**
-   **Streamlit:** UI framework for the web application.
-   **LangGraph:** Orchestration of the agentic workflow.
-   **Pydantic AI:** Core library for defining and running AI agents, leveraging Pydantic models.
-   **OpenAI Python SDK:** Interacting with OpenAI compatible APIs (including OpenAI, Ollama, OpenRouter).
-   **Anthropic Python SDK:** Interacting with Anthropic APIs (used via Pydantic AI's `AnthropicModel`).
-   **Supabase Python SDK:** Interacting with the Supabase database for documentation retrieval.
-   **python-dotenv:** Loading environment variables from `.env` files (primarily for local setup, less relevant for Streamlit Cloud).

**Development Setup:**
-   Requires Python 3.11+.
-   Dependencies are managed via `requirements.txt`.
-   A virtual environment (`venv`) is recommended.
-   Local environment variables can be managed using the UI (`streamlit_pages/environment.py`) which saves to `workbench/env_vars.json`, or potentially via a `.env` file (though the JSON method seems preferred).

**Technical Constraints:**
-   Relies on external LLM APIs (OpenAI, Anthropic, etc.) or locally running models (Ollama). Requires valid API keys and network access.
-   Supabase is used for documentation vector storage; requires Supabase URL and service key.
-   Streamlit's execution model: The script reruns on interaction, requiring careful state management using `st.session_state`.
-   Secrets management differs between local development (`workbench/env_vars.json`) and Streamlit Cloud deployment (`st.secrets`).

**Key Dependencies & Integrations:**
-   **LLM Providers:** OpenAI, Anthropic, OpenRouter, Ollama. Configuration managed via `streamlit_pages/environment.py`.
-   **Vector Database:** Supabase (pgvector extension) for storing and querying documentation embeddings.
-   **IDE Integration (MCP):** Configuration provided for Windsurf, Cursor, Cline/Roo Code, Claude Code via `streamlit_pages/mcp.py`.

**Code Structure:**
-   `streamlit_ui.py`: Main application entry point, sets up UI layout and navigation.
-   `streamlit_pages/`: Modules for each UI tab/page.
-   `archon/`: Core logic for the agentic workflow (LangGraph graph, Pydantic AI coder, refiner agents, tools).
-   `utils/`: Utility functions (client initialization, environment variable management, logging).
-   `workbench/`: Directory for generated files (scope.md, logs.txt, env_vars.json). Should likely be in `.gitignore`.
-   `mcp/`: Code related to the MCP server (`mcp_server.py`).
-   `public/`: Static assets (images).
-   `Dockerfile`: For building the Docker image.
-   `run_docker.py`: Script to manage Docker containers.
-   `requirements.txt`: Python dependencies.
