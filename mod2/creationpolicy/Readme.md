## Creation Policyのサンプル
- Auto Scaling Groupでの使用 
  - creationpolicy_autoscaling.yml
    - Auto Scaling Groupを作成する
    - Auto Scaling Groupにより作成される3つのEC2インスタンスがcfn-signalのシグナルを送信が完了するとAuto Scalig Groupが作成完了状態になる。
- EC2インスタンスでの使用
  - step0.jso
    - 2つのEC2インスタンスを作成する
    - インスタンス間の依存関係は考慮されず作成される。
  - step1.json
    - 2つのEC2インスタンスを作成する。
    - DependsOnの指定があるのでInstance1が作成されてからInstance2が作成される。
  - step2.json
    - 2つのEC2インスタンスを作成する。
    - Creation Policyの指定があるのでInstance1はcfn-signalが実行されるまで作成完了状態にならない。
    - DependsOnの指定があるのでInstance1が作成されてからInstance2が作成される。



