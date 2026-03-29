#!/bin/bash
set -e

echo "=== Docker Network Isolation Test ==="
echo ""

echo "[1] DNS Resolution Test"
echo "------------------------"
if getent ahosts openrouter.ai > /dev/null 2>&1; then
    echo "[OK] openrouter.ai resolves:"
    getent ahosts openrouter.ai | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort -u
else
    echo "[FAIL] Cannot resolve openrouter.ai"
    exit 1
fi
echo ""

echo "[2] TCP Connection Test (Python)"
echo "------------------------"
OPENROUTER_IP=$(getent ahosts openrouter.ai | awk '{print $1}' | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -1)
echo "Testing TCP connection to $OPENROUTER_IP:443..."
python3 -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect(('$OPENROUTER_IP', 443))
    print('[OK] TCP connection to openrouter.ai:443 succeeded')
except Exception as e:
    print(f'[FAIL] Cannot connect to openrouter.ai:443: {e}')
    exit(1)
finally:
    s.close()
"
echo ""

echo "[3] HTTPS Request Test (curl)"
echo "------------------------"
echo "Testing HTTPS request to openrouter.ai..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "https://openrouter.ai/api/v1" 2>&1 || echo "000")
if [ "$HTTP_CODE" != "000" ]; then
    echo "[OK] Received HTTP response code: $HTTP_CODE"
else
    echo "[FAIL] Could not reach openrouter.ai via HTTPS"
    exit 1
fi
echo ""

echo "[4] Python httpx Test"
echo "------------------------"
echo "Testing with Python httpx library..."
python3 -c "
import httpx
try:
    response = httpx.get('https://openrouter.ai/api/v1', timeout=15)
    print(f'[OK] httpx received status: {response.status_code}')
except Exception as e:
    print(f'[FAIL] httpx error: {e}')
    exit(1)
"
echo ""

echo "[5] OpenRouter API Test (openai/gpt-4.1-nano)"
echo "------------------------"
echo "Making real API request to openrouter.ai with openai/gpt-4.1-nano..."
python3 -c "
import os
import httpx

api_key = os.environ.get('OPENAI_API_KEY', '')
if not api_key:
    print('[FAIL] OPENAI_API_KEY not set')
    exit(1)

response = httpx.post(
    'https://openrouter.ai/api/v1/chat/completions',
    headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    },
    json={
        'model': 'openai/gpt-4.1-nano',
        'messages': [{'role': 'user', 'content': 'Say \"hello world\" in exactly 2 words'}],
        'max_tokens': 20,
    },
    timeout=30,
)

if response.status_code == 200:
    data = response.json()
    content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
    print(f'[OK] API request succeeded')
    print(f'     Response: {content}')
else:
    print(f'[FAIL] API request failed with status: {response.status_code}')
    print(f'     Response: {response.text[:200]}')
    exit(1)
"
echo ""

echo "=== All Tests Passed ==="