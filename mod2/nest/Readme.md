## ネスト構成のテンプレート
- nest_main_template.yaml
  - 下記の2つのテンプレートを含む
    - nest_network_template.yaml
      - VPCを作成する
    - nest_apptier_template.yaml
      - 作成されたVPCにセキュリティグループを作成する