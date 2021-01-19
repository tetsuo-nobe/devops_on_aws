## アプリケーションのリビジョン・ファイルの内容
### 下記のファイル群がzipファイルにまとめられ、S3バケットに格納されている前提です。
- SimpleSpringBoot-0.1.0.jar
  - SpringBootアプリケーションのファイル
- SimpleSpringBoot.service
  - SpringBootアプリケーションのサービス設定用ファイル
- appspec.yml
  - CodeDeployによるデプロイ手順が記載されたファイル
- startapp.sh
  - アプリケーション起動用のスクリプト
  - ApplicationStartフックで実行するようappspec.ymlで指定されている
- stopapp.sh
  - アプリケーション停止用のスクリプト
  - ApplicationStopフックで実行するようappspec.ymlで指定されている

![codedeploy-demo-img](https://devops.nobelabo.net/img/demo-codedeploy.png)