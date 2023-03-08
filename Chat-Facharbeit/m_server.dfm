object server: Tserver
  Left = 270
  Top = 121
  Width = 340
  Height = 606
  AutoSize = True
  BorderIcons = [biSystemMenu, biMinimize]
  Caption = 'Server Interface'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnActivate = FormActivate
  OnCloseQuery = FormCloseQuery
  PixelsPerInch = 96
  TextHeight = 13
  object Label2: TLabel
    Left = 33
    Top = 0
    Width = 19
    Height = 13
    Caption = 'Port'
  end
  object Label3: TLabel
    Left = 1
    Top = 32
    Width = 57
    Height = 13
    Caption = 'Servername'
  end
  object mem_stat: TMemo
    Left = 0
    Top = 136
    Width = 324
    Height = 432
    TabStop = False
    ReadOnly = True
    ScrollBars = ssVertical
    TabOrder = 5
  end
  object Edit2: TEdit
    Left = 64
    Top = 0
    Width = 121
    Height = 21
    TabOrder = 0
    Text = '7777'
    OnChange = Edit2Change
  end
  object Edit3: TEdit
    Left = 64
    Top = 32
    Width = 121
    Height = 21
    TabOrder = 1
    OnChange = Edit3Change
  end
  object Button1: TButton
    Left = 64
    Top = 56
    Width = 121
    Height = 25
    Caption = 'Server starten'
    TabOrder = 2
    OnClick = Button1Click
  end
  object Edit1: TEdit
    Left = 0
    Top = 104
    Width = 257
    Height = 21
    TabOrder = 3
    OnChange = Edit1Change
  end
  object bt_send: TButton
    Left = 264
    Top = 104
    Width = 49
    Height = 25
    Caption = 'Senden'
    TabOrder = 4
    OnClick = bt_sendClick
  end
  object ServerSocket1: TServerSocket
    Active = False
    Port = 4567
    ServerType = stNonBlocking
    OnClientConnect = ServerSocket1ClientConnect
    OnClientRead = ServerSocket1ClientRead
    OnClientError = ServerSocket1ClientError
    Left = 32
    Top = 48
  end
end
