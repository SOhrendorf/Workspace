program p_chat;

uses
  Forms,
  m_choose in 'm_choose.pas' {Form2},
  m_client in 'm_client.pas' {client},
  m_server in 'm_server.pas' {server};

{$R *.res}

begin
  Application.Initialize;
  Application.Title := 'Delphi-Chat';
  Application.CreateForm(TForm2, Form2);
  Application.CreateForm(Tclient, client);
  Application.CreateForm(Tserver, server);
  Application.Run;
end.
