# Product Context

**Problem:** Building AI agents often involves repetitive boilerplate code and understanding complex library specifics (like Pydantic AI). This slows down prototyping and development.

**Solution:** Archon provides a user-friendly interface where developers can describe the agent they need in natural language. Archon then leverages LLMs and its knowledge of Pydantic AI to generate the corresponding Python code, significantly reducing development time and effort.

**How it Works:**
1.  **User Input:** The user describes the desired agent via a chat interface.
2.  **Agentic Workflow:** A LangGraph-based workflow processes the request:
    *   **Scope Definition:** A reasoner LLM defines the scope, required components, and relevant documentation.
    *   **Coding:** A primary LLM generates the Pydantic AI agent code based on the scope and user input/feedback.
    *   **Refinement (Optional):** Specialized agents can refine the prompt, tools, or agent definition based on user feedback.
3.  **Output:** The generated agent code is presented to the user.
4.  **Configuration:** Users can manage API keys, model selections, and database connections through dedicated UI tabs.

**User Experience Goals:**
-   **Simplicity:** Easy-to-understand interface requiring minimal setup.
-   **Speed:** Rapid generation of functional agent code.
-   **Flexibility:** Support for multiple LLM providers and configurations.
-   **Transparency:** Clear feedback during the agent generation process.
-   **Persistence:** Reliable storage of environment configurations.
