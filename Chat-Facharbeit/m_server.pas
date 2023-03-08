unit m_server;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ScktComp, StdCtrls;

type
  Tserver = class(TForm)
    ServerSocket1: TServerSocket;
    mem_stat: TMemo;
    Label2: TLabel;
    Edit2: TEdit;
    Edit3: TEdit;
    Label3: TLabel;
    Button1: TButton;
    Edit1: TEdit;
    bt_send: TButton;
    procedure ServerSocket1ClientRead(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure Button1Click(Sender: TObject);
    procedure Edit2Change(Sender: TObject);
    procedure ServerSocket1ClientConnect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure Edit1Change(Sender: TObject);
    procedure FormActivate(Sender: TObject);
    procedure FormCloseQuery(Sender: TObject; var CanClose: Boolean);
    procedure bt_sendClick(Sender: TObject);
    procedure Edit3Change(Sender: TObject);
    procedure ServerSocket1ClientError(Sender: TObject;
      Socket: TCustomWinSocket; ErrorEvent: TErrorEvent;
      var ErrorCode: Integer);
    
  private
  running : Boolean;
  procedure Delay(msecs:integer); //procedure von BaraoZemo (http://www.delphipages.com/forum/showthread.php?t=100977#3)
    { Private-Deklarationen }
  public
    { Public-Deklarationen }
  end;

var
  server: Tserver;

implementation

{$R *.dfm}

procedure Tserver.Delay(msecs:integer);
var FirstTickCount:longint;
begin
  FirstTickCount:=GetTickCount;
  repeat
  Application.ProcessMessages;
  until
  ((GetTickCount-FirstTickCount) >= Longint(msecs));
end;

procedure Tserver.ServerSocket1ClientRead(Sender: TObject;
  Socket: TCustomWinSocket);
var
  msg: String;
  i: Integer;

  zeilennr: integer;
begin
msg := '[' + TimeToStr(Now) + '] ' + Socket.ReceiveText;
  mem_stat.Lines.Add(msg);
  for i := 0 to ServerSocket1.Socket.ActiveConnections-1 do
    ServerSocket1.Socket.Connections[i].SendText(msg)
end;

procedure Tserver.Button1Click(Sender: TObject);
begin
if (Edit2.Text = '') or (Edit3.Text = '') then begin
  Application.MessageBox('Es wurde ein Feld nicht ausgefüllt!', 'Informationen fehlen', MB_ICONWARNING or MB_OK);
  if Edit2.Text = '' then Edit2.Color := clRed;
  if Edit3.Text = '' then Edit3.Color := clRed;
  end
  else begin
ServerSocket1.Port := StrToInt(Edit2.Text);
ServerSocket1.Active := not ServerSocket1.Active;
if ServerSocket1.Active then
begin
  running := true;
  Button1.Caption := 'Server stoppen';
  mem_stat.Lines.Add('Server gestartet');
  Edit2.Enabled := false;
  Edit3.Enabled := false;
  bt_send.Enabled := true;
end
else
begin
  running := false;
  Button1.Caption := 'Server starten';
  mem_stat.Lines.Add('Server gestoppt');
  Edit2.Enabled := true;
  Edit3.Enabled := true;
  bt_send.Enabled := false;
end;
end;
end;

procedure Tserver.Edit2Change(Sender: TObject);
begin
  Edit2.Color := clWindow;
end;

procedure Tserver.ServerSocket1ClientConnect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
Socket.SendText('Servername: ' + Edit3.Text);
end;

procedure Tserver.Edit1Change(Sender: TObject);
begin
if ServerSocket1.Socket.ActiveConnections <> 0 then bt_send.Enabled := true
  else bt_send.Enabled := false;
end;

procedure Tserver.FormActivate(Sender: TObject);
begin
bt_send.Enabled := false;
end;

procedure Tserver.FormCloseQuery(Sender: TObject; var CanClose: Boolean);
begin
if running then begin
  CanClose := false;
  if Application.MessageBox('Server ist nicht gestoppt! Jetzt stoppen?', 'Server nicht gestoppt', MB_ICONWARNING or MB_YESNO) = IDYES then begin
    Button1.Caption := 'Server starten';
    mem_stat.Lines.Add('Server gestoppt');
    Edit2.Enabled := true;
    Edit3.Enabled := true;
    ServerSocket1.Active := false;
    running := false;
    CanClose := true;
    Server.Close;
    end;
  end;
end;


procedure Tserver.bt_sendClick(Sender: TObject);
var i : Integer;
begin
  for i := 0 to ServerSocket1.Socket.ActiveConnections-1 do
    ServerSocket1.Socket.Connections[i].SendText('[' + TimeToStr(Now) + '] server: ' + Edit1.Text);
  mem_stat.Lines.Add('[' + TimeToStr(Now) + '] server: ' + Edit1.Text);
  Edit1.Clear
end;

procedure Tserver.Edit3Change(Sender: TObject);
begin
  Edit3.Color := clWindow;
end;

procedure Tserver.ServerSocket1ClientError(Sender: TObject;
  Socket: TCustomWinSocket; ErrorEvent: TErrorEvent;
  var ErrorCode: Integer);
begin
mem_stat.Lines.Add('Error: ' + IntToStr(ErrorCode));
ErrorCode := 0;
end;

end.
