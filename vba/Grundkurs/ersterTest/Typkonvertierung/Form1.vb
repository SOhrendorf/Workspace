Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Label1.Text = CInt(TextBox1.Text) + CInt(TextBox2.Text) 'Text in Zahl verwandeln; trotzdem nicht mit Text rechen
    End Sub
End Class
