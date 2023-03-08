int(42.5)           # 42
float(-1)           # -1.0
str(0.5)            # "0.5"
bool(0.001)         # True, weil nur bei 0 der Wert False herauskommt.
str("False")        # "False"
int(False)          # 0, weil der Wahrheitswert False dem Integer-Wert 0 entspricht.
float("10")         # 10.0
bool('0')           # True, weil nur der leere String als Boolean False ergibt.
int("False")        # Nicht möglich, weil "False" kein Integer ist.
float("True")       # Nicht möglich, weil "True" kein Integer ist.