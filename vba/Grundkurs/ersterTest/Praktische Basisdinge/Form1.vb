Imports System.Windows.Forms
Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim result As Integer
        result = MessageBox.Show("Ich bin ganz Wichtig ;)", "Meine Gedanken", MessageBoxButtons.OKCancel)
        If result = DialogResult.Cancel Then
            Me.BackColor = Color.Red
        End If
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        OpenFileDialog1.ShowDialog()
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        SaveFileDialog1.ShowDialog()
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        ColorDialog1.ShowDialog()
    End Sub

    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        Dim Datei As String
        If OpenFileDialog2.ShowDialog = Windows.Forms.DialogResult.OK Then
            Datei = OpenFileDialog2.FileName
            RichTextBox1.LoadFile(Datei, RichTextBoxStreamType.PlainText)
        End If

        RichTextBox1.Modified = False
        Text = Datei
    End Sub
End Class
