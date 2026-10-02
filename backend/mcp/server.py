from mcp.server.fastmcp import FastMCP
from .tools.learner import get_learner_history
from .tools.evidence import get_evidence
from .tools.summary import draft_teacher_summary

mcp=FastMCP("EduLongView")

@mcp.tool()
def learner_history(learner_id:str): return get_learner_history(learner_id)

@mcp.tool()
def evidence(learner_id:str, subject:str|None=None, term:str|None=None): return get_evidence(learner_id,subject,term)

@mcp.tool()
def teacher_summary(patterns:list, gaps:list): return draft_teacher_summary(patterns,gaps)

@mcp.tool()
def profile_update_notice(): return {"message":"Profile updates are only performed through the API after recorded human approval."}

if __name__=="__main__": mcp.run()
