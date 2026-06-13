import requests

headers = {
    "Cookie": "[cookiehat]",
    "User-Agent": "Mozilla/5.0"
}

org_id = "7bda4b04-8149-415c-8538-b6a81cb016a4"

endpoints = [
    "members", "users", "people", "admins", "owners",
    "workspaces", "teams", "projects",
    "api-keys", "tokens", "secrets",
    "audit-log", "activity", "events", "logs",
    "webhooks", "integrations", "connections",
    "limits", "rate-limits", "quotas",
    "analytics", "reports", "exports", "insights",
    "conversations", "chats", "messages", "threads",
    "files", "documents", "uploads",
    "domains", "verified-domains",
    "sso", "saml", "scim",
    "security", "privacy",
    "backups", "snapshots",
]

for ep in endpoints:
    try:
        r = requests.get(
            f"https://claude.ai/api/organizations/{org_id}/{ep}",
            headers=headers
        )
        if r.status_code not in [404]:
            print(f"[{r.status_code}] /api/organizations/{{org}}/{ep}")
            if r.status_code in [200, 403, 405]:
                print(f"  → {r.text[:200]}")
    except Exception as e:
        print(f"[ERR] {ep}: {e}")
