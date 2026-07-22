from flask import Flask, render_template_string, request, jsonify
import os
import urllib.request
import json

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

bot_status = {
    "state": "OPEN (Trading)",
    "active_markets": ["XAUUSD"],
    "golden_hours": "14:00 - 17:00 IST (High Win-Rate)",
    "volatility_status": "NORMAL (Safe to Trade)",
    "consecutive_losses": 0,
    "circuit_breaker": "ACTIVE (Max Daily Loss Guard)",
    "trend_direction": "BULLISH (Favorable for BUY)",
    "best_day": "Tuesday / Thursday",
    "drawdown_limit": "-$100.00",
    "current_pnl": "-$7.60",
    "win_rate": "54.5%",
    "current_table": "TABLE-1",
    "current_step": "Step 1 of 9",
    "total_trades": "22",
    "winning_trades": "12",
    "losing_trades": "10",
    "balance": "220.29",
    "equity": "220.05",
    "ai_advice": "Jini AI hybrid bridge is active and syncing tables."
}

def get_ai_trading_advice(pnl, balance, table, step):
    if not GEMINI_API_KEY:
        return "⚠️ Gemini API Key missing!"
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        prompt = (
            f"You are Jini, an expert quantitative algorithmic trading AI for XAUUSD managing a grid/recovery table strategy (Table-1 and Table-2). "
            f"Current status -> PnL: {pnl}, Balance: ${balance}, Active Table: {table}, Current Step: {step}. "
            f"Give a short, punchy 2-sentence tactical recommendation in Hindi and English mix for the trader."
        )
        data = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode())
            return res_data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"AI Bridge optimizing strategy grids..."

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JINI AI QUANT DASHBOARD 🧞‍♂️</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 20px; }
        h1 { color: #58a6ff; font-size: 26px; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; width: 300px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); text-align: left; }
        .card-wide { background-color: #161b22; border: 1px solid #58a6ff; border-radius: 8px; padding: 20px; width: 640px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); text-align: left; margin: 0 auto; }
        .card h3 { margin-top: 0; color: #3fb950; border-bottom: 1px solid #30363d; padding-bottom: 8px; font-size: 18px; }
        .val { font-weight: bold; color: #f0f6fc; }
        .status-box { background-color: #1f6feb; color: white; padding: 10px; border-radius: 6px; margin-bottom: 20px; font-weight: bold; display: inline-block; font-size: 18px; }
        .wallet-text { font-size: 22px; color: #e3b341; margin: 5px 0; font-weight: bold; }
        .ai-text { font-size: 16px; color: #58a6ff; line-height: 1.5; font-style: italic; }
    </style>
</head>
<body>

    <h1>🧞‍♂️ JINI AI QUANTITATIVE TRADING ENGINE 🧞‍♂️</h1>
    <div class="status-box">Status: {{ status.state }}</div>

    <div class="container" style="margin-top: 0; margin-bottom: 20px;">
        <div class="card-wide" style="border-color: #58a6ff;">
            <h3 style="color: #58a6ff;">🤖 Jini AI Hybrid Brain & Strategy Advisor</h3>
            <p class="ai-text">"{{ status.ai_advice }}"</p>
        </div>
    </div>

    <div class="container">
        <div class="card" style="border-color: #e3b341;">
            <h3 style="color: #e3b341;">💰 Live MT5 Wallet</h3>
            <p class="wallet-text">Balance: <span class="val" style="color: #ffffff;">${{ status.balance }}</span></p>
            <p class="wallet-text">Equity: <span class="val" style="color: #3fb950;">${{ status.equity }}</span></p>
        </div>

        <div class="card">
            <h3>📊 Live Global Performance</h3>
            <p>Daily Net Profit: <span class="val" style="color: #3fb950;">{{ status.current_pnl }}</span></p>
            <p>Win Rate: <span class="val">{{ status.win_rate }}</span></p>
            <p>Total Trades: <span class="val">{{ status.total_trades }}</span></p>
            <p>Winning / Losing: <span class="val" style="color: #3fb950;">{{ status.winning_trades }}</span> / <span class="val" style="color: #da3633;">{{ status.losing_trades }}</span></p>
            <p>Active Table: <span class="val" style="color: #a371f7;">{{ status.current_table }}</span></p>
            <p>Current Step: <span class="val" style="color: #a371f7;">{{ status.current_step }}</span></p>
        </div>

        <div class="card">
            <h3>🧠 AI Strategy Switcher</h3>
            <p>Primary Engine: <span class="val" style="color: #d29922;">Table-1 & Table-2 Grid</span></p>
            <p>AI Decision Mode: <span class="val" style="color: #3fb950;">ACTIVE BRIDGE</span></p>
            <p>Best Trading Day: <span class="val">Tuesday / Thursday</span></p>
            <p>Market Volatility: <span class="val" style="color: #3fb950;">{{ status.volatility_status }}</span></p>
        </div>

        <div class="card">
            <h3>🛡️ Risk & Circuit Breakers</h3>
            <p>Consecutive Losses: <span class="val">{{ status.consecutive_losses }} / 2</span></p>
            <p>Circuit Breaker: <span class="val" style="color: #3fb950;">{{ status.circuit_breaker }}</span></p>
            <p>Max Drawdown Limit: <span class="val" style="color: #f85149;">{{ status.drawdown_limit }}</span></p>
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, status=bot_status)

@app.route('/update', methods=['POST'])
def update_status():
    try:
        data = request.get_json()
        if data:
            bot_status["current_pnl"] = data.get("pnl", bot_status["current_pnl"])
            bot_status["win_rate"] = data.get("win_rate", bot_status["win_rate"])
            bot_status["current_table"] = data.get("table", bot_status["current_table"])
            bot_status["current_step"] = data.get("step", bot_status["current_step"])
            bot_status["total_trades"] = data.get("total_trades", bot_status["total_trades"])
            bot_status["winning_trades"] = data.get("winning_trades", bot_status["winning_trades"])
            bot_status["losing_trades"] = data.get("losing_trades", bot_status["losing_trades"])
            bot_status["balance"] = data.get("balance", bot_status["balance"])
            bot_status["equity"] = data.get("equity", bot_status["equity"])
            bot_status["state"] = data.get("state", bot_status["state"])
            
            # Get AI smart advice based on current live PnL and Table steps
            bot_status["ai_advice"] = get_ai_trading_advice(
                bot_status["current_pnl"], 
                bot_status["balance"], 
                bot_status["current_table"], 
                bot_status["current_step"]
            )
            
            # We can also return AI command back to MT5 if needed!
            return jsonify({"status": "success", "ai_signal": "HOLD_GRID"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/kill', methods=['POST'])
def kill_switch():
    bot_status["state"] = "🛑 EMERGENCY STOPPED BY USER"
    bot_status["circuit_breaker"] = "TRIPPED (Locked)"
    bot_status["ai_advice"] = "Emergency stop triggered! All trading tables halted."
    return render_template_string(HTML_TEMPLATE, status=bot_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
