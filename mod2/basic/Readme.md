## Apache HTTP Server と MariaDB を構築するテンプレート
- 下記のAWSリソースを使用
  - VPC
    - Internet Gateway
    - Subnet
    - RouteTable
    - セキュリティグループ
    - NAT Gateway
  - EC2 インスタンスに設定する IAM ロールとロールプロファイル
  - EC2インスタンス
      - Apache HTTP Server をインストールしカスタムの index.html を構成      
  - ELB の Application Load Balancer 
  - RDS 
    - データベースサブネットグループ
    - MariaDBデータベースインスタンス
- AMI の ID は、マッピングでリージョンIDから取得
- 下記をOutput指定
  - 作成したMySQLデータベースのエンドポイントアドレス
  - 作成した Application Load Balancer DNS 名
  - 作成した EC2 インスタンスの ID

![cfn-demo-img](https://devops.nobelabo.net/img/demo-template.png)
