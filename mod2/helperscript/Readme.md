## ヘルパースクリプトのサンプル
### （東京リージョンでデフォルトのVPCを使用する前提）
- Helper-Script-Test-cfn-init.yaml
  - cfn-initのサンプル
- Helper-Script-Test-cfn-signal.yaml
  - cfn-signalのサンプル
  - signalが10秒以内に受け取る設定にして敢えてスタック作成を失敗させている
- Helper-Script-Test-cfn-hup.yaml
  - cfn-hupのサンプル
  - 上記でスタックを作成後、下記でメタデータを更新する
    - Helper-Script-Test-cfn-hup-update.yaml

