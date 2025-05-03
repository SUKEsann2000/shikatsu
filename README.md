ラズパイの死活管理用です。<br>
Pythonです。

必要なライブラリ
1. ping3
2. subprocess
3. ntplib
4. datetime
5. requests
6. json
7. speedtest-cli
8. sys
<br>
[GASのURL](https://script.google.com/macros/s/AKfycbwOcOPF78kSNj8LVa5J2zSOPqBcavKT4Gz0Vsfo65d_vgk6Puq8ImJ-6axjpjHAvxTb/exec)

やりたいこと
1. GASにPOSTでJSONを送りつけて、GAS側でエラーがあったらメール送信する。
2. ポートが空いてるか確認する（外側に）
3. pingのsukesann2000.duckdns.orgが通じるか