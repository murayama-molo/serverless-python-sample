# serverless-python-sample

serverless framework を通して AWS 環境上に API Gateway, Lambda(python), CloudFront, S3 を作ってみるサンプル

# Requirement

以下の環境で構築しました

## node.js

```bash
$ node --version
v14.18.0
```

## serverless framework

```bash
$ serverless --version
Framework Core: 2.53.1 (standalone)
Plugin: 5.4.3
SDK: 4.2.6
Components: 3.14.2
```

# Installation

## chocolatey

パッケージマネージャー

### chocolatey をインストール

https://chocolatey.org/install#individual

例:

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## AWS CLI

### AWS CLI をインストール

https://docs.aws.amazon.com/ja_jp/cli/v1/userguide/install-windows.html#install-msi-on-windows

### IAM の設定

```bash
$ aws configure
AWS Access Key ID [None]: YOUR_ACCESS_KEY_ID
AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
Default region name [None]: ap-northeast-1
Default output format [None]: json
```

## serverless framework

```bash
$ choco install serverless
```

## node.js

```bash
$ choco install nodejs
```

## npm install

node.js 関連パッケージをインストール

```bash
$ npm install
```

まだ使ってない

````
## serverless-python-requirements

pip インストールが必要な AWS Lambda の Python スクリプトを Serverless Framework で間単位デプロイできるプラグイン

```bash
$ serverless plugin install -n serverless-python-requirements
````

````

# Test

## lambda

```bash
$ python -m unittest discover
````

# deploy

```bash
$ serverless deploy
```

※aws の認証情報をプロファイルで分けている場合は

```bash
$ serverless deploy --aws-profile ${自分の設定したプロファイル名}
```

# Check

Cloud Fron の URL をブラウザで実行

# Remove

お掃除
作ったリソースを全部削除

```bash
$ serverless remove
```

※aws の認証情報をプロファイルで分けている場合は

```bash
$ serverless remove --aws-profile ${自分の設定したプロファイル名}
```
