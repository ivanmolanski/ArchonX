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

**New Issue Encountered (Post-Deployment Attempt):**
-   Deployment failed with `OSError: [Errno 28] inotify watch limit reached`. This indicates the Streamlit Cloud environment ran out of resources to monitor file changes, likely due to the large number of files in the `iterations/` directory.

**Resolution Attempt 3 (inotify fix):**
-   Modified `.streamlit/config.toml` to add `server.folderWatchBlacklist = ["iterations"]`. This instructs Streamlit to ignore the `iterations` directory for file watching, aiming to prevent the `inotify` limit error.

**Next Steps:**
1.  Deploy the *latest* updated code (including the `.streamlit/config.toml` change) to Streamlit Community Cloud.
2.  Verify that the application starts successfully without the `inotify` error.
3.  Verify that credentials set via the Cloud UI (under `[general]`) now populate correctly in the Environment tab and persist across user sessions (logout/login).

**Active Decisions:**
-   Addressed the `inotify` limit error by blacklisting the `iterations` directory in Streamlit's config.
-   Keeping the previous fix in `utils/utils.py` to enforce consistent secret access via `st.secrets.general`.
