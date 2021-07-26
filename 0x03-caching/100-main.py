#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
# Current cache:
# A: Hello      0
# B: World      0
# C: Holberton  0
# D: School     0
print(my_cache.get("B"))
# World
my_cache.put("E", "Battery")
# DISCARD: A
my_cache.print_cache()
# Current cache:
# B: World      1
# C: Holberton  0
# D: School     0
# E: Battery    0
my_cache.put("C", "Street")
my_cache.print_cache()
# Current cache:
# B: World      1
# C: Street     1
# D: School     0
# E: Battery    0
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
# None
# World
# Street
my_cache.put("F", "Mission")
# DISCARD: D
my_cache.print_cache()
# Current cache:
# B: World      2
# C: Street     2
# E: Battery    0
# F: Mission    0
my_cache.put("G", "San Francisco")
# DISCARD: E
my_cache.print_cache()
# Current cache:
# B: World          2
# C: Street         2
# F: Mission        0
# G: San Francisco  0
my_cache.put("H", "H")
# DISCARD: F
my_cache.print_cache()
# Current cache:
# B: World          2
# C: Street         2
# G: San Francisco  0
# H: H              0
my_cache.put("I", "I")
# DISCARD: G
my_cache.print_cache()
# Current cache:
# B: World      2
# C: Street     2
# H: H          0
# I: I          0
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
# I
# H
# I
# H
# I
# H
# Current cache:
# B: World      2
# C: Street     2
# H: H          3
# I: I          3
my_cache.put("J", "J")
# DISCARD: B
my_cache.print_cache()
# Current cache:
# C: Street     2
# H: H          3
# I: I          3
# J: J          0
my_cache.put("K", "K")
# DISCARD: J
my_cache.print_cache()
# Current cache:
# C: Street     2
# H: H          3
# I: I          3
# K: K          0
my_cache.put("L", "L")
# DISCARD: K
my_cache.print_cache()
# Current cache:
# C: Street     2
# H: H          3
# I: I          3
# L: L          0
my_cache.put("M", "M")
# DISCARD: L
my_cache.print_cache()
# Current cache:
# C: Street     2
# H: H          3
# I: I          3
# M: M          0





















