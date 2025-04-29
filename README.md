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
GASのURL
https://script.google.com/macros/s/AKfycbxZHkVs90SrvtuSG8x4Z0KYg0m_k37HQkYwlKW9HKpnli8rSGwD1F8RIl9yjwf4HqAZ/exec

やりたいこと
1. speedtest-cliを使って速度計測をする
2. GASにPOSTでJSONを送りつけて、GAS側でエラーがあったらメール送信する。
3. JSONにはstatusのboolも入れる