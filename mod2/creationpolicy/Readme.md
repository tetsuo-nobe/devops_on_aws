## Creation Policyのサンプル
- step0.json
  - 2つのEC2インスタンスを作成する
  - インスタンス間の依存関係は考慮されず作成される。
- step1.json
  - 2つのEC2インスタンスを作成する。
  - DependsOnの指定があるのでInstance1が作成されてからInstance2が作成される。
- step2.json
  - 2つのEC2インスタンスを作成する。
  - Creation Policyの指定があるのでInstance1はcfn-signalが実行されるまで作成完了状態にならない。
    - DependsOnの指定があるのでInstance1が作成されてからInstance2が作成される。



