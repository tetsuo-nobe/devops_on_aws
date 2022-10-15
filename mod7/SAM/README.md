## AWS SAMのデモ
### SAMを使用し、Lambda関数と統合したAPI GatewayのREST APIを作成する


1. Cloud9 のターミナルを開きます。

1. デモ用のフォルダを作成して移動します。

        
        mkdir aws-sam-demo
        cd  aws-sam-demo
        

1. SAM のバージョンを確認します。

        
        sam --version
        

1. SAM のリソースを作成します。デモでは Python の Lambda 関数を作成します。

        
        sam init --runtime python3.7
        

1. テンプレートを選択します。このデモでは、1のAWS Quick Start Templatesを選択します。

        
        Which template source would you like to use?
                1 - AWS Quick Start Templates
                2 - Custom Template Location
        Choice: 1
        

1. アプリケーションのテンプレートを選択します。このデモでは、1 の Hello World Example を選択します。

        
        Choose an AWS Quick Start application template
                1 - Hello World Example
                2 - Infrastructure event management
                3 - Multi-step workflow
        Template: 1
        

1. AWS X-Ray によるトレース取得の有効化または無効化を指定します。このデモでは、そのまま Enter キーを押下して N (無効化)を選択します。

        
        Based on your selections, the only Package type available is Zip.
        We will proceed to selecting the Package type as Zip.

        Based on your selections, the only dependency manager available is pip.
        We will proceed copying the template using pip.

        Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: 
        

1. プロジェクト名を指定します。このデモでは aws-sam-demo-app を入力します。

        
        Project name [sam-app]:aws-sam-demo-app
        


1. 下記の内容を確認・編集します。

        - SAM テンプレート

        - aws-sam-demo/aws-sam-demo-app/template.yaml 
        - 上記ファイルにHelloWorldFunctionのプロパティに下記を追記して関数名を明示的に指定します。
        -  FunctionName: HelloWorldFunction-SAM

        - デプロイするLambda関数

        - aws-sam-demo/aws-sam-demo-app/hello_world/app.py
        - デフォルトで {message: hello world}というJSONを返します。必要に応じて変更します。　


1. SAM でサーバーレスアプリケーションを構築してテストやデプロイする前準備を行います。

        
        cd aws-sam-demo-app
        sam build
        

1. SAM を使用しローカルでテストします。(Docker が必要です。)

        
        sam local invoke 
        


    - [その他のローカルテスト用のコマンド](#その他のローカルテスト用のコマンド) 
    - この後、デプロイを実施します。
    - sam deploy --guidedを使わない場合は下の12番のタスクを実行します。 
        <br />
    - [sam deploy --guidedを使う場合はこちら](#デプロイをシンプルにするために) 
        
 
1. デプロイパッケージを格納するためのS3バケットを作成します。(既存のものでもOK)

        
        aws s3 mb s3://tnobe-sam-demo
        

1. デプロイパッケージをS3に格納します。

        
        sam package --output-template-file packaged.yaml --s3-bucket tnobe-sam-demo
        

1. デプロイを実行します。

        
        sam deploy --template-file packaged.yaml --stack-name aws-sam-demo-app --capabilities CAPABILITY_IAM
        

    - 以上でデプロイは完了です！

1. SAMで作成したスタックを削除するには、`sam delete` を実行します。

        
        sam delete
        
 <br />
 <br />
 <br />

## デプロイをシンプルにするために 
 
sam deploy --guidedを使うと、sam deployのパラメータをファイルに保存し、以後、容易にデプロイできます。

        
        sam deploy --guided
        

以後、対話的に進めていくと、指定した内容がsam deploy実行時に必要パラメータとしてファイル（デフォルト:samconfig.toml）保存され、その後デプロイが実行されます。

        
        Configuring SAM deploy
        ======================

                Looking for config file [samconfig.toml] :  Not found

                Setting default arguments for 'sam deploy'
                =========================================
                Stack Name [sam-app]: aws-sam-demo-app
                AWS Region [ap-northeast-1]: 
                #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
                Confirm changes before deploy [y/N]: 
                #SAM needs permission to be able to create roles to connect to the resources in your template
                Allow SAM CLI IAM role creation [Y/n]: 
                #Preserves the state of previously provisioned resources when an operation fails
                Disable rollback [y/N]: 
                HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
                Save arguments to configuration file [Y/n]: 
                SAM configuration file [samconfig.toml]: 
                SAM configuration environment [default]: 

                Looking for resources needed for deployment:
                Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-31392rxojqwi
                A different default S3 bucket can be set in samconfig.toml
        (以下略)
        

1回目のデプロイが完了後、2回目のsam deployを実施する時は、ファイル（デフォルト:samconfig.toml）が存在する場合は、そこから必要なパラメータが取得されるので、下記のように簡単なコマンドでデプロイできます。

        
        sam deploy 
        

 <br />
 <br />
 <br />

## その他のローカルテスト用のコマンド 

Lambda関数
        
        sam local start-lambda
        

        
        aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt
        

API Gateway
        
        sam local start-api
        

        
        curl http://127.0.0.1:3000/hello
        




