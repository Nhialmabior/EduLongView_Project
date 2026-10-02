# MCP

Our Python MCP server is in `backend/mcp/server.py`.

Tools:
- learner_history
- evidence
- teacher_summary
- profile_update_notice

The profile write is intentionally enforced by the application review layer so an unapproved agent cannot mutate learner profiles.

External MCP integration: add a verified external MCP server before final competition submission. Do not claim an external server is integrated unless it has been tested and documented.
