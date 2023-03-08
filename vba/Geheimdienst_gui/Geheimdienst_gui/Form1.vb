Public Class form1

    Public file As String

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        If OpenFileDialog1.ShowDialog() = Windows.Forms.DialogResult.OK Then
            file = My.Computer.FileSystem.GetParentPath(OpenFileDialog1.FileName)
            Label1.Text = file
        End If
    End Sub

    Public Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim python_file As String = file & "\otp.py"
        My.Computer.FileSystem.DeleteFile(python_file)
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Dim source As String = "C:\workspace\python\otp.py"
        Dim python_file As String = file & "\otp.py"
        Dim script As String = "otp.py"

        FileCopy(source, python_file)

        System.Threading.Thread.Sleep(3000)

        'Dim psi = New ProcessStartInfo("C:\Windows\System32\cmd.exe", "python " & python_file)
        'Dim proc = Process.Start(psi)
        'proc.WaitForExit()

        Process.Start("cmd", "/k cd " & file & "&" & "python " & script)

    End Sub
End Class
