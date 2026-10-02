const API='http://localhost:8000';
export async function getLearners(){return (await fetch(API+'/api/learners')).json()}
export async function getLearner(id){return (await fetch(API+'/api/learners/'+id)).json()}
export async function analyze(id){return (await fetch(API+'/api/agent/analyze',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({learner_id:id})})).json()}
export async function review(payload){return (await fetch(API+'/api/reviews',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})).json()}
export async function audit(){return (await fetch(API+'/api/audit')).json()}
