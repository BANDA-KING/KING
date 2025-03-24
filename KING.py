import os, sys
try:
    __import__("KING").email_verification_system()
except Exception as e:
    exit(str(e))
