## シークレット情報を参照するCodeBuildのbuildspec.yml
- buildspec.yml
  - CodeBuildによるビルド処理内容が記述されているファイル
    - dockerのコマンドを発行しコンテナイメージをビルドしてタグ付けを行っている。
    - ビルド後、構築したイメージをAmazon ECRにpushしている。
    - Systems Managerのパラメータストアで管理しているSecureStringパラメータより値を参照して下記に設定
      - 環境変数(リージョンID用）
    - Secrets Managerで管理しているシークレットより値を参照して下記に設定
      - 環境変数(Amazon ECRのリポジトリ名用) (8行目）
      - 環境変数(AWSアカウントID用) (9行目）
- Dockerfile
  - Dockerイメージのビルド用
    - Apache HTTP ServerでWebページを表示するコンテナイメージ

