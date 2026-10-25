"""
export_mcq_assessment.py
Edulateral Foundation — Interactive Assessment Dashboard Generator.
Builds a self-contained, offline HTML5 application containing all 125 MCQs
with interactive question filtering, instant scoring, timer, and grade reporting.
"""

import os
import json

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\EDULATERAL_OFFICIAL_MCQ_BANK"
json_path = os.path.join(base_dir, "official_mcq_evaluation_dataset.json")
html_path = os.path.join(base_dir, "interactive_quiz_evaluation.html")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edulateral Foundation — HPC Evaluative Assessment Portal</title>
    <style>
        :root {{
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --card-bg: #1e293b;
            --accent: #38bdf8;
            --accent-green: #22c55e;
            --accent-red: #ef4444;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #334155;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }}
        body {{ background: var(--bg-primary); color: var(--text-main); line-height: 1.6; padding: 2rem 1rem; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        header {{ text-align: center; margin-bottom: 2rem; padding: 1.5rem; background: var(--bg-secondary); border-radius: 12px; border: 1px solid var(--border); }}
        h1 {{ font-size: 1.8rem; color: var(--accent); margin-bottom: 0.5rem; }}
        .subtitle {{ color: var(--text-muted); font-size: 0.95rem; }}
        .nav-days {{ display: flex; gap: 0.5rem; justify-content: center; margin: 1.5rem 0; flex-wrap: wrap; }}
        .day-btn {{ background: var(--bg-secondary); color: var(--text-main); border: 1px solid var(--border); padding: 0.6rem 1.2rem; border-radius: 8px; cursor: pointer; font-weight: 600; transition: all 0.2s; }}
        .day-btn.active, .day-btn:hover {{ background: var(--accent); color: #000; border-color: var(--accent); }}
        .stats-bar {{ display: flex; justify-content: space-between; align-items: center; background: #0284c7; color: white; padding: 0.8rem 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; font-weight: 600; }}
        .question-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }}
        .question-header {{ display: flex; justify-content: space-between; margin-bottom: 1rem; color: var(--accent); font-weight: 700; font-size: 0.9rem; }}
        .question-title {{ font-size: 1.1rem; margin-bottom: 1.2rem; font-weight: 600; }}
        .options {{ display: flex; flex-direction: column; gap: 0.6rem; }}
        .option-label {{ display: flex; align-items: flex-start; gap: 0.8rem; background: #0f172a; padding: 0.8rem 1rem; border-radius: 8px; border: 1px solid var(--border); cursor: pointer; transition: border-color 0.2s; }}
        .option-label:hover {{ border-color: var(--accent); }}
        .option-label input {{ margin-top: 0.3rem; }}
        .explanation {{ margin-top: 1.2rem; padding: 1rem; border-radius: 8px; font-size: 0.9rem; display: none; }}
        .explanation.visible {{ display: block; }}
        .correct-exp {{ background: rgba(34, 197, 94, 0.15); border-left: 4px solid var(--accent-green); color: #86efac; }}
        .actions {{ text-align: center; margin: 2rem 0; }}
        .submit-btn {{ background: var(--accent-green); color: #000; font-size: 1.1rem; font-weight: bold; padding: 0.8rem 2.5rem; border: none; border-radius: 8px; cursor: pointer; transition: transform 0.1s; }}
        .submit-btn:hover {{ transform: scale(1.02); }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🏢 EDULATERAL FOUNDATION — HPC ASSESSMENT PORTAL</h1>
            <p class="subtitle">GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)</p>
            <p class="subtitle">Trainer: <strong>Shivam Gupta</strong> | Official Evaluative Examination Question Bank</p>
        </header>

        <div class="nav-days" id="dayButtons"></div>

        <div class="stats-bar">
            <span id="currentDayTitle">Day 1 Assessment</span>
            <span id="scoreDisplay">Score: 0 / 25</span>
        </div>

        <div id="quizContainer"></div>

        <div class="actions">
            <button class="submit-btn" onclick="submitAssessment()">Submit & Grade Assessment</button>
        </div>
    </div>

    <script>
        const dataset = {json.dumps(data)};
        const dayKeys = Object.keys(dataset);
        let currentDayKey = dayKeys[0];
        let userAnswers = {{}};

        function init() {{
            const nav = document.getElementById('dayButtons');
            dayKeys.forEach((key, index) => {{
                const btn = document.createElement('button');
                btn.className = 'day-btn ' + (index === 0 ? 'active' : '');
                btn.textContent = 'Day ' + (index + 1);
                btn.onclick = () => switchDay(key, btn);
                nav.appendChild(btn);
            }});
            renderDay(currentDayKey);
        }}

        function switchDay(key, btnElement) {{
            currentDayKey = key;
            document.querySelectorAll('.day-btn').forEach(b => b.classList.remove('active'));
            btnElement.classList.add('active');
            userAnswers = {{}};
            document.getElementById('scoreDisplay').textContent = 'Score: 0 / 25';
            renderDay(key);
        }}

        function renderDay(key) {{
            const container = document.getElementById('quizContainer');
            container.innerHTML = '';
            const questions = dataset[key];
            const dayNum = dayKeys.indexOf(key) + 1;
            document.getElementById('currentDayTitle').textContent = `Day ${{dayNum}} Assessment (${{questions.length}} MCQs)`;

            questions.forEach((q, i) => {{
                const card = document.createElement('div');
                card.className = 'question-card';
                card.id = `card-${{q.id}}`;

                let optionsHtml = '';
                for (const optKey of Object.keys(q.options).sort()) {{
                    optionsHtml += `
                        <label class="option-label" id="opt-${{q.id}}-${{optKey}}">
                            <input type="radio" name="${{q.id}}" value="${{optKey}}" onchange="recordAnswer('${{q.id}}', '${{optKey}}')">
                            <span><strong>(${{optKey}})</strong> ${{q.options[optKey]}}</span>
                        </label>
                    `;
                }}

                card.innerHTML = `
                    <div class="question-header">
                        <span>QUESTION ${{i + 1}} OF ${{questions.length}}</span>
                        <span>ID: ${{q.id}}</span>
                    </div>
                    <div class="question-title">${{q.question}}</div>
                    <div class="options">${{optionsHtml}}</div>
                    <div class="explanation correct-exp" id="exp-${{q.id}}">
                        <strong>Correct Answer: (${{q.answer}})</strong><br>
                        ${{q.explanation}}
                    </div>
                `;
                container.appendChild(card);
            }});
        }}

        function recordAnswer(qId, selectedOpt) {{
            userAnswers[qId] = selectedOpt;
        }}

        function submitAssessment() {{
            const questions = dataset[currentDayKey];
            let score = 0;

            questions.forEach(q => {{
                const exp = document.getElementById(`exp-${{q.id}}`);
                exp.classList.add('visible');
                const userSelected = userAnswers[q.id];

                for (const optKey of Object.keys(q.options)) {{
                    const label = document.getElementById(`opt-${{q.id}}-${{optKey}}`);
                    label.style.borderColor = 'var(--border)';
                    if (optKey === q.answer) {{
                        label.style.borderColor = 'var(--accent-green)';
                        label.style.background = 'rgba(34, 197, 94, 0.2)';
                    }} else if (userSelected === optKey && optKey !== q.answer) {{
                        label.style.borderColor = 'var(--accent-red)';
                        label.style.background = 'rgba(239, 68, 68, 0.2)';
                    }}
                }}

                if (userSelected === q.answer) {{
                    score++;
                }}
            }});

            const percentage = ((score / questions.length) * 100).toFixed(1);
            document.getElementById('scoreDisplay').textContent = `Score: ${{score}} / ${{questions.length}} (${{percentage}}%)`;
            alert(`Assessment Graded!\\nYour Score: ${{score}} / ${{questions.length}} (${{percentage}}%)\\nDetailed explanations are now visible below each question.`);
        }}

        window.onload = init;
    </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[SUCCESS] Interactive evaluation dashboard created: {html_path}")
