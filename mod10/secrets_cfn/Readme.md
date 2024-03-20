## シークレット情報を参照するCloudFormationテンプレート
- webapp_template_parameter_store.yaml
  - Apache HTTP Server と MariaDB を構築するテンプレート
    - Systems Manager のパラメータストアで管理しているパラメータより値を参照して下記に設定
      - RDS データベースの管理者ユーザ名 (String)
      - RDS データベースの管理者ユーザパスワード (**SecureString**)
- webapp_template_secrets_manager.yaml
  - Apache HTTP Server と MariaDB を構築するテンプレート
    - Secrets Manager で管理しているシークレットより値を参照して下記に設定
      - RDS データベースの管理者ユーザ名
      - RDS データベースの管理者ユーザパスワード

