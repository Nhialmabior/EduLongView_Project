# Lightweight acceptance checklist for the prototype.
# Run the API and verify:
# 1. GET /api/learners returns synthetic cohort.
# 2. GET /api/learners/LRN-0042 returns history.
# 3. POST /api/agent/analyze identifies evidence-backed patterns.
# 4. POST /api/reviews with rejected does not update profiles.
# 5. Approved review records an approval before profile write.
