# Active Context

**Current Focus:** Investigating why environment variables/credentials set via the Streamlit Community Cloud UI are not persisting across user sessions (logout/login).

**Recent Changes:**
-   Memory Bank initialized with core files (`projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `activeContext.md`, `progress.md`).

**Analysis:**
-   The application uses `st.secrets` in `streamlit_ui.py` to access secrets deployed via Streamlit Cloud. This is the correct approach for that environment.
-   For local development, the application uses `utils/utils.py` functions (`get_env_var`, `save_env_var`) to manage environment variables stored in `workbench/env_vars.json`. This mechanism provides persistence locally.
-   The UI for managing local environment variables is in `streamlit_pages/environment.py`.
-   The core issue was identified as a disconnect: `streamlit_ui.py` correctly read from `st.secrets` in the Cloud, but `utils.utils.get_env_var` (used by backend components like `get_clients` and `archon_graph.py`) did *not* check `st.secrets`, only checking a local JSON file or `os.environ`. This meant secrets set in the Cloud UI were not accessible to the backend logic.

**Resolution Attempt 2:**
-   Further modified `utils/utils.py`: The `get_env_var` function now *only* checks `st.secrets.general[var_name]` when running in a Streamlit environment. It no longer falls back to checking the root `st.secrets`. This enforces strict consistency with the access pattern used in `streamlit_ui.py`.

**Next Steps:**
1.  Ensure secrets in the Streamlit Community Cloud UI are defined under a `[general]` section (e.g., `[general]`, `OPENAI_API_KEY = "sk-..."`).
2.  Deploy the *latest* updated code to Streamlit Community Cloud.
3.  Verify that credentials set via the Cloud UI now populate correctly in the Environment tab and persist across user sessions (logout/login).

**Active Decisions:**
-   Refined the fix in `utils/utils.py` to enforce strict consistency in accessing secrets via `st.secrets.general`.
