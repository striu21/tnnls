import fall

if not fall.is_installed("pycloudflared"):
    fall.run_pip("install pycloudflared", "pycloudflared")
