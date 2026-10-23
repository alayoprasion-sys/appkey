from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# لێرەدا خۆت ئەو کۆدانە دادەنێیت کە دەتەوێت و ماوەی بەسەرچوونیان
licenses = {
    "DAVAN-VIP-2026": "2026-12-31",
    "TEST-KEY-123": "2026-10-25"
}

@app.route('/verify', methods=['GET'])
def verify_key():
    user_key = request.args.get('key')
    
    if not user_key or user_key not in licenses:
        return jsonify({"status": "error", "message": "❌ ئەم کۆدە هەڵەیە!"})
    
    expiry_str = licenses[user_key]
    expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")
    current_date = datetime.now()

    # پشکنینی کاتی بەسەرچوون
    if current_date > expiry_date:
        return jsonify({"status": "expired", "message": "❌ کاتی ئەم کۆدە بەسەرچووە!"})
    
    return jsonify({"status": "success", "message": "✅ کۆدەکە ڕاستە و چالاکە!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
