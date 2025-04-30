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
[GASのURL](https://script.google.com/macros/s/AKfycbyrOZp_sYfIgeXkgeehN7fznOMVg2NOo-y3XIOUfIzJScoGcqFLGz39HDchPxYg00Bs/exec)

やりたいこと
1. GASにPOSTでJSONを送りつけて、GAS側でエラーがあったらメール送信する。
2. outputを送ってもjsonに反映されないので、それを修正する