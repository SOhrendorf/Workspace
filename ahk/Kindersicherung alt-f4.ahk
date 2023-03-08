!f4::
MsgBox, Boese nein, tu es nicht!
return

^!f4::
InputBox, Benutzereingabe, Sicherheitsabfrage, Möchten sie wirklich runterfahren.
if (Benutzereingabe = "ja")
{
MsgBox, naja, hier gehts nicht :P
}
