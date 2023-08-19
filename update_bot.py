import subprocess

# Pull latest changes
subprocess.run(["git", "pull"])

# Update dependencies
subprocess.run(["pip", "install", "--upgrade", "-r", "requirements.txt"])

# Restart the bot
subprocess.run(["systemctl", "restart", "your_bot_service"])
