# System Patterns

**Core Architecture:** Model-View-Controller (MVC) adapted for Streamlit.
-   **Model:** LangGraph agentic workflow (`archon/archon_graph.py`), Supabase client (`utils/utils.py`), LLM clients (`archon/archon_graph.py`, `utils/utils.py`).
-   **View:** Streamlit UI components defined in `streamlit_ui.py` and individual page modules within `streamlit_pages/`.
-   **Controller:** Streamlit callback logic within UI components, interacting with the agentic workflow and utility functions.

**Key Technical Decisions:**
-   **Agent Framework:** LangGraph for defining the agentic workflow, providing flexibility and state management.
-   **Code Generation:** Pydantic AI for defining agent structures and leveraging LLMs for code generation.
-   **UI Framework:** Streamlit for rapid development of the web interface.
-   **Configuration Management:**
    -   Streamlit Secrets: Used for deployment on Streamlit Community Cloud. Secrets are accessed via `st.secrets`.
    -   Local JSON File (`workbench/env_vars.json`): Used for local development and persistence across sessions. Managed via `utils/utils.py` functions (`get_env_var`, `save_env_var`). Profiles allow managing multiple configurations.
-   **Database:** Supabase for storing and retrieving documentation pages relevant to Pydantic AI.
-   **Deployment:** Dockerfile provided for containerized deployment, Streamlit Community Cloud integration.

**Design Patterns:**
-   **Agentic Workflow:** Using LangGraph to orchestrate multiple LLM calls and tool interactions in a stateful manner.
-   **Dependency Injection:** Clients (Supabase, LLM) are initialized centrally (`utils/utils.py`) and passed to relevant components/tabs.
-   **Modular UI:** Streamlit pages are separated into individual Python modules (`streamlit_pages/`) for better organization.
-   **Configuration Profiles:** Allowing users to switch between different sets of environment variables (e.g., for different LLM providers) using `workbench/env_vars.json`.

**Component Relationships:**
```mermaid
graph TD
    UI[Streamlit UI (streamlit_ui.py)] --> Pages[streamlit_pages/*]
    Pages --> Utils[utils/utils.py]
    Pages --> ArchonGraph[archon/archon_graph.py]

    ArchonGraph --> LLMProviders[LLM Providers (OpenAI, Anthropic, etc.)]
    ArchonGraph --> PydanticAICoder[archon/pydantic_ai_coder.py]
    ArchonGraph --> Refiners[archon/refiner_agents/*]
    ArchonGraph --> AgentTools[archon/agent_tools.py]
    ArchonGraph --> Utils

    Utils --> Supabase[Supabase Client]
    Utils --> EmbeddingClient[Embedding Client]
    Utils --> EnvVarsJSON[workbench/env_vars.json]

    AgentTools --> Supabase
    PydanticAICoder --> Supabase
    PydanticAICoder --> EmbeddingClient
    Refiners --> Supabase
    Refiners --> EmbeddingClient

    UI --> StSecrets[st.secrets (Streamlit Cloud)]
```

**Environment Variable Handling:**
-   `utils/utils.py` contains `get_env_var` and `save_env_var` to manage variables stored in `workbench/env_vars.json`.
-   `get_env_var` prioritizes the JSON file, falling back to system environment variables.
-   `streamlit_ui.py` attempts to load secrets using `st.secrets` (primarily for Streamlit Cloud deployment).
-   `archon/archon_graph.py` uses `get_env_var` to load necessary configurations like API keys and model names.
-   `streamlit_pages/environment.py` provides the UI for managing profiles and variables stored in `workbench/env_vars.json`.
