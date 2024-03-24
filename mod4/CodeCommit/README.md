# AWS CodeCommit の基本操作 (git-remote-codecommit を使用）

## AWS の認証情報が設定され、Git クライアント、Python3 および pip 9.0.3 以降が使用できる Linux 環境を前提とする

* 参考:[git-remote-codecommit を使用した HTTPS 接続のセットアップ手順](https://docs.aws.amazon.com/ja_jp/codecommit/latest/userguide/setting-up-git-remote-codecommit.html)

### リポジトリ名を環境変数に設定

```
REPO_NAME=demo-repo
```

### AWS IAM の ID（認証情報をもっていること） を確認

```
aws sts get-caller-identity
```

### AWS CodeCommit リポジトリの作成

```
aws codecommit create-repository --repository-name ${REPO_NAME} 
```

### git-remote-codecommit のインストール

```
pip install git-remote-codecommit
```

### HTTP GRCでgit clone

```
git clone codecommit://${REPO_NAME}   ${REPO_NAME} 
```

### ローカルリポジトリへ移動

```
cd ${REPO_NAME}/
```

### ブランチをmainに変更

```
git checkout -b main
```

### ファイルを作成

```
touch demo.txt
echo "Hello" > demo.txt
```

### ステータスを確認

```
git status
```

### 変更をステージングに追加

```
git add .
```

### コミット

```
git commit -m "add file"
```

### プッシュ

```
git push -u origin main
```

### 現在のブランチを確認

```
git branch
```

### ブランチを作成して、切り替える (ローカルにブランチができる）

```
git checkout -b  branchA
git branch
```

### ファイルを編集

```
echo "World" >> demo.txt
```

### 現在のブランチや修正ファイル名の確認

```
git status
```

### 変更をステージングに追加

```
git add .
```

### コミット

```
git commit -m 'modify file'
```

#### プッシュ

```
git push origin branchA
```
