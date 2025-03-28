from __future__ import annotations
from dotenv import load_dotenv # Keep if you use it for other non-secret env vars
import streamlit as st
import logfire
import asyncio

# Set page config - must be the first Streamlit command
st.set_page_config(
    page_title="Archon - Agent Builder",
    page_icon="🤖",
    layout="wide",
)

# Accessing the secrets
base_url = st.secrets["BASE_URL"]
openai_api_key = st.secrets["OPENAI_API_KEY"]
supabase_url = st.secrets["SUPABASE_URL"]
supabase_service_key = st.secrets["SUPABASE_SERVICE_KEY"]
reasoner_model = st.secrets["REASONER_MODEL"]
primary_model = st.secrets["PRIMARY_MODEL"]
embedding_api_key = st.secrets["EMBEDDING_API_KEY"]
embedding_base_url = st.secrets["EMBEDDING_BASE_URL"]
embedding_model = st.secrets["EMBEDDING_MODEL"]

# Accessing the secrets under the [general] section
try:
    base_url = st.secrets["general"]["BASE_URL"]
    openai_api_key = st.secrets["general"]["OPENAI_API_KEY"]
    supabase_url = st.secrets["general"]["SUPABASE_URL"]
    supabase_service_key = st.secrets["general"]["SUPABASE_SERVICE_KEY"]
    reasoner_model = st.secrets["general"]["REASONER_MODEL"]
    primary_model = st.secrets["general"]["PRIMARY_MODEL"]
    embedding_api_key = st.secrets["general"]["EMBEDDING_API_KEY"]
    embedding_base_url = st.secrets["general"]["EMBEDDING_BASE_URL"]
    embedding_model = st.secrets["general"]["EMBEDDING_MODEL"]
    # Set a flag indicating secrets were loaded successfully
    secrets_loaded = True
except KeyError as e:
    st.error(f"❌ Missing required secret in [general] section: {e}. Please check secrets configuration in Streamlit Cloud. App cannot start.")
    secrets_loaded = False # Set flag to false
    # Optionally exit if secrets are absolutely essential to even start the UI
    # st.stop()

# --- Proceed only if secrets were loaded ---
if secrets_loaded:
    # Utilities and styles
    # NOTE: get_clients() might now need to accept these secrets as arguments,
    # or be modified to not use secrets itself if they are passed from here.
    # This is why accessing secrets within get_clients is often cleaner.
    from utils.utils import get_clients
    from streamlit_pages.styles import load_css

    # Streamlit pages
    from streamlit_pages.intro import intro_tab
    from streamlit_pages.chat import chat_tab
    from streamlit_pages.environment import environment_tab
    from streamlit_pages.database import database_tab
    from streamlit_pages.documentation import documentation_tab
    from streamlit_pages.agent_service import agent_service_tab
    from streamlit_pages.mcp import mcp_tab
    from streamlit_pages.future_enhancements import future_enhancements_tab

    # Load environment variables from .env file (Optional)
    # load_dotenv()

    # Initialize clients
    # !!! IMPORTANT: Adjust get_clients if it needs these secrets passed in, e.g.:
    # openai_client, supabase = get_clients(openai_api_key=openai_api_key, supabase_url=supabase_url, ...)
    # OR modify get_clients to simply use the variables defined above (less ideal).
    # Assuming get_clients is modified or doesn't directly use secrets anymore:
    openai_client, supabase = get_clients() # Modify this call/function as needed!

    # Load custom CSS styles
    load_css()

    # Configure logfire to suppress warnings (optional)
    logfire.configure(send_to_logfire='never')

    async def main():
        # Check for tab query parameter
        query_params = st.query_params
        if "tab" in query_params:
            tab_name = query_params["tab"]
            if tab_name in ["Intro", "Chat", "Environment", "Database", "Documentation", "Agent Service", "MCP", "Future Enhancements"]:
                st.session_state.selected_tab = tab_name

    # Add sidebar navigation
    with st.sidebar:
        st.image("public/ArchonLightGrey.png", width=1000)
        
        # Navigation options with vertical buttons
        st.write("### Navigation")
        
        # Initialize session state for selected tab if not present
        if "selected_tab" not in st.session_state:
            st.session_state.selected_tab = "Intro"
        
        # Vertical navigation buttons
        intro_button = st.button("Intro", use_container_width=True, key="intro_button")
        chat_button = st.button("Chat", use_container_width=True, key="chat_button")
        env_button = st.button("Environment", use_container_width=True, key="env_button")
        db_button = st.button("Database", use_container_width=True, key="db_button")
        docs_button = st.button("Documentation", use_container_width=True, key="docs_button")
        service_button = st.button("Agent Service", use_container_width=True, key="service_button")
        mcp_button = st.button("MCP", use_container_width=True, key="mcp_button")
        future_enhancements_button = st.button("Future Enhancements", use_container_width=True, key="future_enhancements_button")
        
        # Update selected tab based on button clicks
        if intro_button:
            st.session_state.selected_tab = "Intro"
        elif chat_button:
            st.session_state.selected_tab = "Chat"
        elif mcp_button:
            st.session_state.selected_tab = "MCP"
        elif env_button:
            st.session_state.selected_tab = "Environment"
        elif service_button:
            st.session_state.selected_tab = "Agent Service"
        elif db_button:
            st.session_state.selected_tab = "Database"
        elif docs_button:
            st.session_state.selected_tab = "Documentation"
        elif future_enhancements_button:
            st.session_state.selected_tab = "Future Enhancements"
    
    # Display the selected tab
    if st.session_state.selected_tab == "Intro":
        st.title("Archon - Introduction")
        intro_tab()
    elif st.session_state.selected_tab == "Chat":
        st.title("Archon - Agent Builder")
        await chat_tab()
    elif st.session_state.selected_tab == "MCP":
        st.title("Archon - MCP Configuration")
        mcp_tab()
    elif st.session_state.selected_tab == "Environment":
        st.title("Archon - Environment Configuration")
        environment_tab()
    elif st.session_state.selected_tab == "Agent Service":
        st.title("Archon - Agent Service")
        agent_service_tab()
    elif st.session_state.selected_tab == "Database":
        st.title("Archon - Database Configuration")
        database_tab(supabase)
    elif st.session_state.selected_tab == "Documentation":
        st.title("Archon - Documentation")
        documentation_tab(supabase)
    elif st.session_state.selected_tab == "Future Enhancements":
        st.title("Archon - Future Enhancements")
        future_enhancements_tab()

if __name__ == "__main__":
    asyncio.run(main())

# --- End of file ---