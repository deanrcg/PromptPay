# PromptPay

A real-time cost estimator for ChatGPT prompts. This tool helps you estimate the cost of your prompts before sending them to the OpenAI API.

## Features

- Real-time token counting
- Live cost estimation as you type
- Support for GPT-4 pricing
- Clean and intuitive user interface
- No need to submit forms - updates instantly

## Setup

1. Clone the repository:
```bash
git clone https://github.com/deanrcg/PromptPay.git
cd PromptPay
```

2. Install the required packages:
```bash
pip install flask openai tiktoken
```

3. Update the API key:
Open `promptpay.py` and replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

4. Run the application:
```bash
python promptpay.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. Type or paste your prompt in the text area
2. The cost estimation will update automatically as you type
3. View the number of input tokens and estimated cost in real-time

## Pricing

The application uses the following pricing (as of 2024):
- Input tokens: $0.01 per 1K tokens
- Output tokens: $0.03 per 1K tokens

## Technologies Used

- Python
- Flask
- OpenAI API
- tiktoken
- HTML/CSS/JavaScript

## License

MIT License

## Contributing

Feel free to submit issues and enhancement requests! 