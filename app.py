from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# 🤖 AI & Risk Management System State (Default Values)
bot_status = {
    "state": "WAITING FOR MT5 DATA...",
    "active_markets": ["XAUUSD"],
    "golden_hours": "14:00 - 17:00 IST (High Win-Rate)",
    "volatility_status": "NORMAL (Safe to Trade)",
    "consecutive_losses": 0,
    "circuit_breaker": "ACTIVE (Max Daily Loss Guard)",
    "trend_direction": "AUTO (Momentum Based)",
    "best_day": "Tuesday / Thursday",
    "drawdown_limit": "-$100.00",
    "current_pnl": "$0.00",
    "win_rate": "0.0%",
    "current_table": "Table-1",
    "current_step": "Step 1 of 9",
    "total_trades": "0",
    "winning_trades": "0",
    "losing_trades": "0",
    "balance": "0.00",
    "equity": "0.00"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JINI AI QUANT DASHBOARD 🧞‍♂️</title>
    <meta http-equiv="refresh" content="3"> <!-- हर 3 सेकंड में ऑटो रिफ्रेश होगा -->
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 20px; }
        h1 { color: #58a6ff; font-size: 26px; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; width: 300px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); text-align: left; }
        .card h3 { margin-top: 0; color: #3fb950; border-bottom: 1px solid #30363d; padding-bottom: 8px; font-size: 18px; }
        .val { font-weight: bold; color: #f0f6fc; }
        .btn-danger { background-color: #da3633; color: white; border: none; padding: 12px 20px; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; width: 100%; margin-top: 10px; }
        .btn-danger:hover { background-color: #f85149; }
        .status-box { background-color: #1f6feb; color: white; padding: 10px; border-radius: 6px; margin-bottom: 20px; font-weight: bold; display: inline-block; font-size: 18px; }
        .wallet-text { font-size: 22px; color: #e3b341; margin: 5px 0; font-weight: bold; }
    </style>
</head>
<body>

    <h1>🧞‍♂️ JINI AI QUANTITATIVE TRADING ENGINE 🧞‍♂️</h1>
    <div class="status-box">Status: {{ status.state }}</div>

    <div class="container">
        <!-- 0. Live MT5 Wallet (NEW) -->
        <div class="card" style="border-color: #e3b341;">
            <h3 style="color: #e3b341;">💰 Live MT5 Wallet</h3>
            <p class="wallet-text">Balance: <span class="val" style="color: #ffffff;">${{ status.balance }}</span></p>
            <p class="wallet-text">Equity: <span class="val" style="color: #3fb950;">${{ status.equity }}</span></p>
        </div>

        <!-- 1. Live PnL & Performance -->
        <div class="card">
            <h3>📊 Live Global Performance</h3>
            <p>Daily Net Profit: <span class="val" style="color: #3fb950;">{{ status.current_pnl }}</span></p>
            <p>Win Rate: <span class="val">{{ status.win_rate }}</span></p>
            <p>Total Trades: <span class="val">{{ status.total_trades }}</span></p>
            <p>Winning / Losing: <span class="val" style="color: #3fb950;">{{ status.winning_trades }}</span> / <span class="val" style="color: #da3633;">{{ status.losing_trades }}</span></p>
            <p>Active Table: <span class="val" style="color: #a371f7;">{{ status.current_table }}</span></p>
            <p>Current Step: <span class="val" style="color: #a371f7;">{{ status.current_step }}</span></p>
        </div>

        <!-- 2. AI Machine Learning Intelligence -->
        <div class="card">
            <h3>🧠 AI Pattern Analyzer</h3>
            <p>Golden Hours: <span class="val" style="color: #d29922;">{{ status.golden_hours }}</span></p>
            <p>Trend Direction: <span class="val">{{ status.trend_direction }}</span></p>
            <p>Best Trading Day: <span class="val">{{ status.best_day }}</span></p>
            <p>Market Volatility: <span class="val" style="color: #3fb950;">{{ status.volatility_status }}</span></p>
        </div>

        <!-- 3. Risk Management & Circuit Breakers -->
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

# 🌐 WEBHOOK: MT5 SE LIVE DATA LENE KE LIYE
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
            return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/kill', methods=['POST'])
def kill_switch():
    bot_status["state"] = "🛑 EMERGENCY STOPPED BY USER"
    bot_status["circuit_breaker"] = "TRIPPED (Locked)"
    return render_template_string(HTML_TEMPLATE, status=bot_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
