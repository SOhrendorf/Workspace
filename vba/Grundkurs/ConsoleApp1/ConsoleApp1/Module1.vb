Imports System.Console
Module Module1

    Sub Main()
        Ausgabe()
        Ausgabe("Simon")
        Ausgabe("acht", 8)
        WriteLine(gibWasZurueck())
        errorHandling()
        ReadLine()
    End Sub
    Sub Ausgabe()
        WriteLine("Ich bin ein statischer Text")
        ReadLine()
    End Sub

    Sub Ausgabe(a As String, Optional i As Integer = 42)
        WriteLine(a)
        WriteLine(i)
        ReadLine()
    End Sub

    Sub Namenspace_Imports()
        Dim name

        WriteLine("Geben sie Ihren Namen ein")
        name = ReadLine()
        WriteLine("Hallo {0}", name)
        ReadLine()
    End Sub

    Function gibWasZurueck() As Integer
        Return 3 'verlässt die Funktion
    End Function

    Sub errorHandling()
        Dim a
        Dim b
        a = "Müller"
        b = "Meier"
        Try
            WriteLine(a / b)
        Catch Ausnahme As Exception
            WriteLine("Achtung Feler beim dividiren! ")
        End Try

    End Sub
End Module
