## シークレット情報を参照するCloudFormationテンプレート
- template_parameter_store.yaml
  - WordPressのブログ環境を構築するテンプレート
    - Systems Managerのパラメータストアで管理しているSecureStringパラメータより値を参照して下記に設定
      - RDSデータベースの管理者ユーザパスワード
- template_secrets_manager.yaml
  - WordPressのブログ環境を構築するテンプレート
    - Secrets Managerで管理しているシークレットより値を参照して下記に設定
      - RDSデータベースの管理者ユーザ名
      - RDSデータベースの管理者ユーザパスワード

