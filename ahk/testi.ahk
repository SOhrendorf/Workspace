^j::
MsgBox, Wow!
MsgBox, Das sind
Run, notepad.exe
WinActivate, Unbenannt - Editor
WinWaitActive, Unbenannt - Editor
Send, 7 Zeilen{!}{Enter}
SendInput, innerhalb des STRG{+}J-Hotkeys.
return