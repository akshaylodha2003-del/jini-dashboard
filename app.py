from flask import Flask, render_template_string, request

app = Flask(__name__)

bot_status = {
    "state": "LIVE SIMULATION ACTIVE 🚀",
    "active_markets": ["XAUUSD", "US30", "Forex"],
    "golden_hours": "14:00 - 17:00 IST (High Win-Rate)",
    "volatility_status": "NORMAL (Safe to Trade)",
    "consecutive_losses": 0,
    "circuit_breaker": "ACTIVE (Max 9 SL Limit)",
    "trend_direction": "BULLISH (Favorable for BUY)",
    "best_day": "Tuesday / Thursday",
    "drawdown_limit": "-$200.00",
    "current_pnl": "$0.00",
    "win_rate": "0.0%",
    "current_table": "Table-1",
    "current_step": "Step 1 of 9",
    "total_net_profit": "$0.00",
    "gross_profit": "$0.00",
    "gross_loss": "-$0.00",
    "profit_factor": "0.00",
    "recovery_factor": "0.00",
    "total_trades": "0",
    "winning_trades": "0",
    "losing_trades": "0"
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JINI AI QUANT DASHBOARD 🧞‍♂️</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 20px; }
        h1 { color: #58a6ff; font-size: 24px; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; width: 320px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); text-align: left; }
        .card h3 { margin-top: 0; color: #3fb950; border-bottom: 1px solid #30363d; padding-bottom: 8px; font-size: 16px; }
        .val { font-weight: bold; color: #f0f6fc; float: right; }
        .btn-danger { background-color: #da3633; color: white; border: none; padding: 12px 20px; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; width: 100%; margin-top: 10px; }
        .status-box { background-color: #1f6feb; color: white; padding: 10px; border-radius: 6px; margin-bottom: 20px; font-weight: bold; display: inline-block; font-size: 14px; }
        p { margin: 8px 0; font-size: 14px; }
    </style>
</head>
<body>
    <h1>🧞‍♂️ JINI QUANTITATIVE TRADING ENGINE 🧞‍♂️</h1>
    <div class="status-box">Status: {{ status.state }}</div>
    <div class="container">
        <!-- 1. Live Performance & Global Report -->
        <div class="card">
            <h3>📊 Live Global Performance</h3>
            <p>Total Net Profit: <span class="val" style="color: #3fb950;">{{ status.total_net_profit }}</span></p>
            <p>Gross Profit: <span class="val">{{ status.gross_profit }}</span></p>
            <p>Gross Loss: <span class="val" style="color: #f85149;">{{ status.gross_loss }}</span></p>
            <p>Profit Factor: <span class="val">{{ status.profit_factor }}</span></p>
            <p>Recovery Factor: <span class="val">{{ status.recovery_factor }}</span></p>
            <p>Win Rate: <span class="val">{{ status.win_rate }}</span></p>
            <p>Total Trades: <span class="val">{{ status.total_trades }}</span></p>
            <p>Winning Trades: <span class="val">{{ status.winning_trades }}</span></p>
            <p>Losing Trades: <span class="val">{{ status.losing_trades }}</span></p>
            <hr style="border: 0.5px solid #30363d;">
            <p>Active Table: <span class="val">{{ status.current_table }}</span></p>
            <p>Current Step: <span class="val" style="color: #58a6ff;">{{ status.current_step }}</span></p>
        </div>

        <!-- 2. AI Pattern Analyzer -->
        <div class="card">
            <h3>🧠 AI Pattern Analyzer</h3>
            <p>Golden Hours: <span class="val" style="color: #d29922;">{{ status.golden_hours }}</span></p>
            <p>Trend Direction: <span class="val">{{ status.trend_direction }}</span></p>
            <p>Best Trading Day: <span class="val">{{ status.best_day }}</span></p>
            <p>Market Volatility: <span class="val" style="color: #3fb950;">{{ status.volatility_status }}</span></p>
        </div>

        <!-- 3. Risk & Circuit Breakers -->
        <div class="card">
            <h3>🛡️ Risk & Circuit Breakers</h3>
            <p>Consecutive Losses: <span class="val">{{ status.consecutive_losses }} / 9</span></p>
            <p>Circuit Breaker: <span class="val" style="color: #3fb950;">{{ status.circuit_breaker }}</span></p>
            <p>Max Drawdown Limit: <span class="val" style="color: #f85149;">{{ status.drawdown_limit }}</span></p>
        </div>

        <!-- 4. Emergency Controls -->
        <div class="card">
            <h3>⚡ Emergency Controls</h3>
            <p>Remote Kill Switch:</p>
            <form action="/kill" method="post">
                <button type="submit" class="btn-danger">🛑 STOP ALL TRADING</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, status=bot_status)

@app.route('/kill', methods=['POST'])
def kill_switch():
    bot_status["state"] = "🛑 EMERGENCY STOPPED BY USER"
    bot_status["circuit_breaker"] = "TRIPPED (Locked)"
    return render_template_string(HTML_TEMPLATE, status=bot_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
