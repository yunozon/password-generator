import secrets

def generate_urlsafe_token():
    """URL安全なトークンを生成します"""
    return secrets.token_urlsafe(32)

if __name__ == "__main__":
    urlsafe_token = generate_urlsafe_token()
    print("Generated URL-safe token:", urlsafe_token)