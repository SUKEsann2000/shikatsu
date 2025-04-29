ラズパイの死活管理用です。<br>
Pythonです。

必要なライブラリ
1. pings
2. subprocess
3. ntplib
4. time
5. requests
6. json
7. speedtest-cli
8. sys
<br>
[GASのURL](https://script.google.com/macros/s/AKfycbwx00CUM7ilZTcNirO_AzdaswySKmqq9vTBNkSngsr5MaFk24YK-Wn4I64jkE655MML/exec)

やりたいこと
1. speedtest-cliを使って速度計測をする
2. GASにPOSTでJSONを送りつけて、GAS側でエラーがあったらメール送信する。
3. JSONにはstatusのboolも入れる