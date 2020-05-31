from enum import Enum

class State(Enum):
    VULNERABLE = 0
    INTRUDED = 1
    EXFILTRATED = 2
    SECURE = 3

M = 3 # number of computers
I =  0 # Intruded computers
J = 0 # Exfiltrated Intruded computers

BETA_I = 2 # Mean time to intrude in days

LAMBDA_J = lambda j: 4 + 2 * j # Mean time to comprise J intruded computers in days
MU_J = lambda j: 2 * j # Mean time for finishing data exfiltration on j Intruded computers in days

FIXING_RATE = 2 #days
DAMAGING_RATE = 10 # days
REPAIRING_RATE = 2 # days

ENTRY_WIDTH_UI = 10

