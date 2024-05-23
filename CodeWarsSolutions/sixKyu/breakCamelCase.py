def solution(s):
    return ''.join(f' {ch}' if ch.isupper() else ch for ch in s)