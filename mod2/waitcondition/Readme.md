## WaitConditionのサンプル
- Auto Scaling Groupでの使用 
  - WaitCondition_AutoScaling.yml
    - Auto Scaling Groupを作成する
    - Auto Scaling Groupにより作成される3つのEC2インスタンスがcfn-signalのシグナルを送信が完了するとWaitConditionが作成完了状態になる。
- EC2インスタンスでの使用
  - WaitCondition_EC2.json
    - EC2インスタンスがcfn-signalのシグナルを送信が完了するとWaitConditionが作成完了状態になる。
    - (JSON版)
  - WaitCondition_EC2.yaml
    - EC2インスタンスがcfn-signalのシグナルを送信が完了するとWaitConditionが作成完了状態になる。
    - (YAML版)




