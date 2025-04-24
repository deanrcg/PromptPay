# Step 1: Basic Python app to estimate ChatGPT prompt cost

import openai
import tiktoken
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = "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"

# Constants for GPT-4 Turbo pricing (as of 2024)
COST_PER_1K_INPUT_TOKENS = 0.01
COST_PER_1K_OUTPUT_TOKENS = 0.03

# HTML UI for simple interaction
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ChatGPT Prompt Estimator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
        }
        .container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        #costEstimate {
            background-color: #fff;
            padding: 15px;
            border-radius: 4px;
            margin-top: 10px;
        }
        .cost-item {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ChatGPT Prompt Cost Estimator</h1>
        <div>
            <label for="prompt">Enter your prompt:</label><br>
            <textarea id="prompt" rows="6" oninput="updateCost(this.value)"></textarea>
        </div>
        <div id="costEstimate">
            <div class="cost-item">Input Tokens: <span id="inputTokens">0</span></div>
            <div class="cost-item">Estimated Cost: $<span id="totalCost">0.000</span></div>
        </div>
    </div>

    <script>
        async function updateCost(text) {
            const response = await fetch('/estimate_tokens', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({text: text})
            });
            
            const data = await response.json();
            document.getElementById('inputTokens').textContent = data.input_tokens;
            document.getElementById('totalCost').textContent = data.total_cost.toFixed(5);
        }
    </script>
</body>
</html>
"""

def count_tokens(text, model="gpt-4"):
    tokenizer = tiktoken.encoding_for_model(model)
    return len(tokenizer.encode(text))

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/estimate_tokens", methods=["POST"])
def estimate_tokens():
    text = request.json.get("text", "")
    input_tokens = count_tokens(text)
    
    # Cost calculation
    input_cost = (input_tokens / 1000) * COST_PER_1K_INPUT_TOKENS
    # Assuming average output tokens for estimation
    estimated_output_tokens = min(input_tokens * 1.5, 100)  # Rough estimate, capped at 100 tokens
    output_cost = (estimated_output_tokens / 1000) * COST_PER_1K_OUTPUT_TOKENS
    total_cost = input_cost + output_cost
    
    return jsonify({
        "input_tokens": input_tokens,
        "total_cost": total_cost
    })

if __name__ == "__main__":
    app.run(debug=True) 