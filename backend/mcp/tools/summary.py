def draft_teacher_summary(patterns, gaps):
    lines=["AI-generated analysis — teacher review required.",""]
    for p in patterns:
        lines.append(f"• {p['category']}: {p['pattern']} ({p['confidence']} confidence)")
        lines.append("  Evidence: "+", ".join(p["evidence_ids"]))
    if gaps: lines += ["","Evidence gaps:"]+[f"• {g}" for g in gaps]
    return "\n".join(lines)
