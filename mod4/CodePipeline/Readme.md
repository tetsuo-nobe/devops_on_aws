## アプリケーションのソースの内容
### 下記のフォルダやファイル群がCodeCommitに格納されている前提です。
- deployフォルダ
  - startapp.sh
    - アプリケーション起動用のスクリプト
    - ApplicationStartフックで実行するようappspec.ymlで指定されている
  - stopapp.sh
    - アプリケーション停止用のスクリプト
    - ApplicationStopフックで実行するようappspec.ymlで指定されている
  - SimpleSpringBoot.service
    - SpringBootアプリケーションのサービス設定用ファイル
- srcフォルダ
  - SpringBootアプリケーションのソース用フォルダ
- appspec.yml
  - CodeDeployによるデプロイ手順が記載されたファイル
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - Mavenのコマンドを発行しSpringBootアプリケーションのビルドとパッケージを行っている。
    - 成果物として、下記を指定している
      - ビルドされたSpringBootアプリケーションのJARファイル
      - appspec.yml (デプロイステージのCodeDeployで必要なため)
      - deployフォルダ内の全てのファイル(デプロイステージのCodeDeployで必要なため)
- pom.xml
  - Mavenに必要な設定ファイル

## デモ内容
- CodePipelineでシンプルなSpringBootアプリケーションをビルド、デプロイするパイプラインを 作成し、実行する。


![codepipeline-demo-img](https://devops.nobelabo.net/img/mod4_codepipeline.png)