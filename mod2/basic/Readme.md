## WordPressブログ環境を構築するテンプレート
- 下記のAWSリソースを使用
  - VPC
    - Internet Gateway
    - Subnet
    - RouteTable
    - セキュリティグループ
  - EC2インスタンス 
  - RDS 
    - データベースサブネットグループ
    - MySQLデータベースインスタンス
- キーペア名はパラメータで指定
- AMIのIDは、マッピングでリージョンIDから取得
- 下記をOutput指定
  - 作成したMySQLデータベースのエンドポイントアドレス
  - 作成したEC2インスタンスのパブリックDNSアドレス

![cfn-demo-img](https://devops.nobelabo.net/img/github_mod2_wordpress.png)
