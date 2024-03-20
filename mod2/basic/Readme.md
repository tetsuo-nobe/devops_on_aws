## Apache HTTP Server と MariaDB を構築するテンプレート
- 下記のAWSリソースを使用
  - VPC
    - Internet Gateway
    - Subnet
    - RouteTable
    - セキュリティグループ
  - EC2 インスタンスに設定する IAM ロールとロールプロファイル
  - EC2インスタンス
  - ELB の Application Load Balancer 
  - RDS 
    - データベースサブネットグループ
    - MariaDBデータベースインスタンス
- AMI の ID は、マッピングでリージョンIDから取得
- 下記をOutput指定
  - 作成したMySQLデータベースのエンドポイントアドレス
  - 作成した Application Load Balancer DNS 名
  - 作成した EC2 インスタンスの ID

![cfn-demo-img](https://devops.nobelabo.net/img/github_mod2_wordpress.png)
