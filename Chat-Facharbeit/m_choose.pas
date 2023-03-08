unit m_choose;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm2 = class(TForm)
    Label1: TLabel;
    Button1: TButton;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure FormCloseQuery(Sender: TObject; var CanClose: Boolean);
  private
    opened : Boolean;
    { Private-Deklarationen }
  public
    { Public-Deklarationen }
  end;

var
  Form2: TForm2;

implementation

uses m_client, m_server;

{$R *.dfm}

procedure TForm2.Button1Click(Sender: TObject);
begin
client.Show;
opened := true;
end;

procedure TForm2.Button2Click(Sender: TObject);
begin
server.Show;
opened := true;
end;

procedure TForm2.FormCloseQuery(Sender: TObject; var CanClose: Boolean);
begin
if opened then begin
  CanClose := false;
  if Application.MessageBox('Es könnten noch Fenster geöffnet sein. Jetzt beenden?', 'Wirklich beenden?', MB_ICONWARNING or MB_YESNO) = IDYES then Application.Terminate;
end;
end;

end.
