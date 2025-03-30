# Progress

**Current Status:** The application is deployed on Streamlit Community Cloud. The core agent generation functionality is implemented using LangGraph and Pydantic AI. UI provides tabs for chat, environment configuration, database interaction, documentation, MCP setup, etc.

**What Works:**
-   Core agent generation workflow (`archon/archon_graph.py`).
-   Streamlit UI for interaction and configuration (`streamlit_ui.py`, `streamlit_pages/`).
-   Integration with various LLM providers (OpenAI, Anthropic, Ollama, OpenRouter).
-   Supabase integration for documentation retrieval.
-   Local environment variable management via `workbench/env_vars.json` and the Environment tab UI.
-   MCP configuration generation for different IDEs.
-   Docker deployment setup.

**What's Left to Build / Improve:**
-   Resolve the primary issue: Lack of credential persistence across sessions when deployed on Streamlit Community Cloud using `st.secrets`.
-   Potentially enhance error handling and user feedback during agent generation.
-   Further testing of the agent refinement capabilities.
-   Explore features listed in `streamlit_pages/future_enhancements.py`.

**Known Issues:**
-   **[Critical]** Credentials/secrets set via the Streamlit Community Cloud UI are reportedly not persisting across user logout/login cycles. This seems specific to the Streamlit Cloud environment's handling of `st.secrets` persistence.
-   The `workbench/` directory, containing potentially sensitive `env_vars.json`, logs, and generated scope, should be added to `.gitignore` if not already present.

**Blockers:**
-   The credential persistence issue on Streamlit Cloud is the main blocker, as it impacts usability in the deployed environment. Resolution likely requires investigating Streamlit Cloud platform behavior or seeking support from Streamlit.
