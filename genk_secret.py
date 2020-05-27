import secrets

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
print(f"L_SECRET_KEY = {''.join(secrets.choice(chars) for i in range(50))}")
print(f"P_SECRET_KEY = {''.join(secrets.choice(chars) for i in range(50))}")