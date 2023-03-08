^!c::
clipboard :=""
send {f4}
sleep, 1000
send ^a
send ^c
Clipwait, 2
Run, C:\Windows\system32\cmd.exe
sleep, 800
send cd %clipboard%
send {enter}
;msgbox % clipboard - war zum debuggen
return