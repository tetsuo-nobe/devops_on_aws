## シークレット情報を参照するCloudFormationテンプレート
- webapp_template_parameter_store.yaml
  - Apache HTTP Server と MariaDB を構築するテンプレート
    - Systems Managerのパラメータストアで管理しているSecureStringパラメータより値を参照して下記に設定
      - RDSデータベースの管理者ユーザ名
      - RDSデータベースの管理者ユーザパスワード
- webapp_template_secrets_manager.yaml
  - Apache HTTP Server と MariaDB を構築するテンプレート
    - Secrets Managerで管理しているシークレットより値を参照して下記に設定
      - RDSデータベースの管理者ユーザ名
      - RDSデータベースの管理者ユーザパスワード

