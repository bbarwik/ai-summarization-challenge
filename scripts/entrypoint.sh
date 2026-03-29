#!/bin/bash
set -e

if [ "$(id -u)" -ne 0 ]; then
    echo "[!] This script must be run as root"
    exit 1
fi

echo "[*] Applying network isolation rules..."

echo "[*] Resolving openrouter.ai IPs..."
OPENROUTER_IPS=$(getent ahosts openrouter.ai | awk '{print $1}' | sort -u | grep -E '^[0-9]+\.[0-9]+\.[0-9]+')
if [ -z "$OPENROUTER_IPS" ]; then
    echo "[!] Failed to resolve openrouter.ai"
    exit 1
fi
echo "[*] openrouter.ai IPs: $OPENROUTER_IPS"

echo "[*] Clearing existing OUTPUT rules..."
iptables -F OUTPUT

echo "[*] Adding DROP policy for OUTPUT..."
iptables -P OUTPUT DROP

echo "[*] Allowing established/related connections..."
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

echo "[*] Allowing loopback..."
iptables -A OUTPUT -o lo -j ACCEPT

echo "[*] Allowing DNS (for resolution)..."
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT

echo "[*] Allowing Google DNS (8.8.8.8)..."
iptables -A OUTPUT -d 8.8.8.8 -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -d 8.8.8.8 -p tcp --dport 53 -j ACCEPT

echo "[*] Allowing openrouter.ai on port 443..."
for IP in $OPENROUTER_IPS; do
    echo "[*] Allowing $IP:443..."
    iptables -A OUTPUT -d "$IP" -p tcp --dport 443 -j ACCEPT
done

echo "[*] Network isolation applied."
echo "[*] Starting pipeline as appuser..."

HOME=/home/appuser exec su -m appuser -c "CORE_MODEL=$CORE_MODEL $*"