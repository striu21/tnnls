import sus

if not sus.is_installed("pycloudflared"):
    sus.run_pip("install pycloudflared", "pycloudflared")
