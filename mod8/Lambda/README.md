## CodeDeployによるLambda関数のBlue/Greenデプロイのデモ用コンテンツ
* SAM テンプレートの DeploymentPreferenceで指定する。
* デプロイするLambda関数のファイル
  - myDateTimeFunction.jsは、現在のLambda関数
  - myDateTimeFunction.js.v2は、更新したLambda関数
* デプロイ中にフックで実行されるテスト用のLambda関数のファイル
  - afterAllowTraffic.js
  - beforeAllowTraffic.js
  - これらは、CodeDeployに対してテスト成功か失敗かの結果を送信する必要がある。

