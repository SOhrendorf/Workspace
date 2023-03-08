Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Label1.Text = "Ich war hier, Mfg"
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Me.BackColor = Color.Red
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Me.BackColor = Color.Blue
    End Sub

    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        Label2.BackColor = Color.Yellow
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        Label2.BackColor = Color.Green
    End Sub

    Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
        'Label3.Text = TextBox1.Text * TextBox2.Text
        Dim a As Integer
        Dim b As Integer
        Dim c
        a = TextBox1.Text
        b = TextBox2.Text
        If a Or b > 0 Then
            c = a * b
        Else
            c = "Fehler!"
        End If
        c = a * b
        Label3.Text = c
    End Sub

    Private Sub Loopen()
        Dim a
        a = 10
        'Variante 1
        Do Until a > 10
            ' hier die Anweisung 
        Loop

        'Variante 2
        For a = 0 To 3
            ' Anweisungen hier
            System.Threading.Thread.Sleep(200) 'Pause
            Application.DoEvents()              'Oberfläche neu zeichne / aktuliesieren
        Next

    End Sub

    Private Sub Convertieren()
        Dim z1 As Byte
        Dim z2 As Short
        z2 = 256
        z1 = CByte(z2) ' keine Sprennung der Daten möglich
    End Sub
End Class