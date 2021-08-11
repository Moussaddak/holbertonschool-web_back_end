#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))  # True ok
print(a.require_auth(None, []))  # True ok
print(a.require_auth("/api/v1/status/", []))  # True  None
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))  # False ok
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))  # False ok
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))  # True None
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))  # True None
print(a.require_auth("/api/v1/status", ["/api/v1/statu*"]))  # True None
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))  # True None
