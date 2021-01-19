## アプリケーションのソースの内容
### 下記のフォルダやファイル群がCodeCommitに格納されている前提です。
- srcフォルダ
  - SpringBootアプリケーションのソース用フォルダ
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - Mavenのコマンドを発行しSpringBootアプリケーションのビルドとパッケージを行っている。
    - 成果物として、ビルドされたSpringBootアプリケーションのJARファイルを指定している。
- pom.xml
  - Mavenに必要な設定ファイル

## デモ内容
- CodeBuildを使用し、シンプルなSpringBootアプリケーションをビルドする。
- ソースはCodeCommitで管理し、ビルドツールは、Apache Mavenを使用する。
- ビルドした成果物(Artifact)は、S3バケットに格納する。

![codebuild-demo-img](https://devops.nobelabo.net/img/mod4_codebuild.png)