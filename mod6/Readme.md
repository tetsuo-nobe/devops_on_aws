## DockerイメージをビルドしてAmazon ECRにプッシュするPipelineのソースの内容
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - dockerのコマンドを発行しコンテナイメージをビルドしてタグ付けを行っている。
    - ビルド後、構築したイメージをAmazon ECRにpushしている。
- Dockerfile
  - Dockerイメージのビルド用
    - Apache HTTP ServerでWebページを表示するコンテナイメージ

## デモ内容
- Dockerfileとbuildspec.ymlをCodeCommitにpushする。
- CodePipelineのパイプラインが実行してCodeCommitからソースを取り出す。
- CodeBuildのプロジェクトが実行され、DockerイメージがビルドされAmazon ECRにpushする。

![codebuild-docker-demo-img](https://devops.nobelabo.net/img/mod6_codebuild_docker.png)