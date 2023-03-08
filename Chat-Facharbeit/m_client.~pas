unit m_client;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ScktComp, mmsystem;

type
  Tclient = class(TForm)
    ed_nick: TEdit;
    ed_ip: TEdit;
    bt_connect: TButton;
    bt_send: TButton;
    me_chat: TMemo;
    me_send: TMemo;
    Label1: TLabel;
    Label2: TLabel;
    ClientSocket1: TClientSocket;
    Label3: TLabel;
    ed_port: TEdit;
    CheckBox1: TCheckBox;
    procedure bt_connectClick(Sender: TObject);
    procedure ClientSocket1Read(Sender: TObject; Socket: TCustomWinSocket);
    procedure bt_sendClick(Sender: TObject);
    procedure ClientSocket1Disconnect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure ClientSocket1Connect(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure FormActivate(Sender: TObject);
    procedure ClientSocket1Error(Sender: TObject; Socket: TCustomWinSocket;
      ErrorEvent: TErrorEvent; var ErrorCode: Integer);
    procedure ClientSocket1Connecting(Sender: TObject;
      Socket: TCustomWinSocket);
    procedure ed_nickChange(Sender: TObject);
    procedure ed_portChange(Sender: TObject);
    procedure ed_ipChange(Sender: TObject);
    procedure me_sendKeyDown(Sender: TObject; var Key: Word;
      Shift: TShiftState);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
  private
    status: Integer;
    welcomemessage: String;
    procedure Delay(msecs:integer); //procedure von BaraoZemo (http://www.delphipages.com/forum/showthread.php?t=100977#3)
    { Private-Deklarationen }
  public
    { Public-Deklarationen }
  end;

var
  client: Tclient;

implementation

{$R *.dfm}

procedure Tclient.Delay(msecs:integer);
var FirstTickCount:longint;
begin
  FirstTickCount:=GetTickCount;
  repeat
  Application.ProcessMessages;
  until
  ((GetTickCount-FirstTickCount) >= Longint(msecs));
end;

procedure Tclient.FormActivate(Sender: TObject);
begin
status := 0;
  ed_nick.Enabled := TRUE;
  ed_ip.Enabled := TRUE;
  ed_port.Enabled := TRUE;
end;

procedure Tclient.bt_connectClick(Sender: TObject);
begin
if (ed_nick.Text = '') or (ed_ip.Text = '') or (ed_port.Text = '') then begin
  Application.MessageBox('Es wurde ein Feld nicht ausgefüllt!', 'Informationen fehlen', MB_ICONWARNING or MB_OK);
  if ed_nick.Text = '' then ed_nick.Color := clRed;
  if ed_ip.Text = '' then ed_ip.Color := clRed;
  if ed_port.Text = '' then ed_port.Color := clRed;
  end
  else
IF status = 0 THEN
  BEGIN
  status := 1;
  ClientSocket1.Host := ed_ip.Text;
  ClientSocket1.Port := StrToInt(ed_port.Text);
  ClientSocket1.Open;
  welcomemessage := 'User "' + ed_nick.Text + '" hat den Chat betreten.';
  END
ELSE
  BEGIN
  status := 0;
  bt_connect.Caption := 'Verbinden';
  ed_nick.Enabled := TRUE;
  ed_ip.Enabled := TRUE;
  ed_port.Enabled := TRUE;
  Delay(100);
  ClientSocket1.Close;
  END
end;

procedure Tclient.ClientSocket1Read(Sender: TObject;
  Socket: TCustomWinSocket);
var
  msg: String;
begin
  msg := Socket.ReceiveText;
  if msg <> welcomemessage then
  me_chat.Lines.Add(msg) else
end;

procedure Tclient.bt_sendClick(Sender: TObject);
var
  msg: String;
begin
  msg := me_send.Text;
  msg := ed_nick.Text + ': ' + msg;
  ClientSocket1.Socket.SendText(msg);
  me_send.Clear;
end;

procedure Tclient.ClientSocket1Connect(Sender: TObject;
  Socket: TCustomWinSocket);
var remoteaddr, remoteport, nick: String;
begin
bt_send.Enabled := TRUE;
bt_connect.Caption := 'Trennen';
nick := ed_nick.Text;
remoteaddr := Socket.RemoteAddress;
remoteport := IntToStr(Socket.RemotePort);
me_chat.Lines.Add('');
me_chat.Lines.Add('Server IP: ' + remoteaddr + ':' + remoteport);
Delay(500);
ClientSocket1.Socket.SendText(welcomemessage);
end;

procedure Tclient.ClientSocket1Disconnect(Sender: TObject;
  Socket: TCustomWinSocket);
begin
ClientSocket1.Socket.SendText('User "' + ed_nick.Text + '" hat den Chat verlassen.');
bt_send.Enabled := FALSE;
me_chat.Lines.Add('');
me_chat.Lines.Add('[' + TimeToStr(Now) + '] Verbindung getrennt');
bt_connect.Caption := 'Verbinden';
ed_nick.Enabled := TRUE;
ed_ip.Enabled := TRUE;
ed_port.Enabled := TRUE;
end;

procedure Tclient.ClientSocket1Error(Sender: TObject;
  Socket: TCustomWinSocket; ErrorEvent: TErrorEvent;
  var ErrorCode: Integer);
begin
  Application.MessageBox(PChar('Ein Fehler ist aufgetreten! Error: ' + IntToStr(ErrorCode)), PChar('Error ' + IntToStr(ErrorCode)), MB_ICONWARNING or MB_OK);
  ErrorCode := 0;
  status := 0;
  bt_connect.Caption := 'Verbinden';
  ed_nick.Enabled := TRUE;
  ed_ip.Enabled := TRUE;
  ed_port.Enabled := TRUE;
end;

procedure Tclient.ClientSocket1Connecting(Sender: TObject;
  Socket: TCustomWinSocket);
begin
  status := 1;
  ed_nick.Enabled := false;
  ed_ip.Enabled := false;
  ed_port.Enabled := false;
end;

procedure Tclient.ed_nickChange(Sender: TObject);
begin
  ed_nick.Color := clWindow;
end;

procedure Tclient.ed_portChange(Sender: TObject);
begin
  ed_port.Color := clWindow;
end;

procedure Tclient.ed_ipChange(Sender: TObject);
begin
  ed_ip.Color := clWindow;
end;

procedure Tclient.me_sendKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
if CheckBox1.State = cbChecked then
  if Key = VK_RETURN then begin bt_send.Click; Delay(10); me_send.Clear; end;
end;

procedure Tclient.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  status := 0;
  bt_connect.Caption := 'Verbinden';
  ed_nick.Enabled := TRUE;
  ed_ip.Enabled := TRUE;
  ed_port.Enabled := TRUE;
  Delay(100);
  ClientSocket1.Close;
end;

end.
