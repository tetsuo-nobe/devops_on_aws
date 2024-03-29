## AWS CDKv2のデモ
### CDKv2を使用し、Lambda関数と統合したAPI GatewayのREST APIを作成する


1. Cloud9のターミナルを開きます。

2. デモ用のフォルダを作成して移動します。

```
mkdir aws-cdkv2-demo
cd  aws-cdkv2-demo
```

3. CDKのバージョンを確認します。

```
cdk --version
```

4. CDKのリソースを作成します。デモではTypeScriptを使用します。

```
cdk init app --language typescript
```

5. デプロイするPythonのLambda関数を作成します。このデモでは、srcディレクトリにindex.pyとして作成します。

```
(このフォルダのindex.pyの内容を参照してください。)
```

6. lib/aws-cdkv2-demo-stack.tsを編集して、Lambda関数とAPI GatewayのAPIをデプロイするコードを追記します。

```
(このフォルダのaws-cdkv2-demo-stack.tsの内容を参照してください。)
```

7. CDKのコードがどのような CloudFormation のテンプレートに変換されるか確認します。

```
cdk synth
```


8. CDKを使ってスタックを作成します。
(初回の場合は、先にcdk bootstrap を実行して CDKに必要なリソース群を作成します。)

```
cdk deploy
```

9. 作成したスタックを削除する場合は下記を実行します。

```
cdk destroy
```




