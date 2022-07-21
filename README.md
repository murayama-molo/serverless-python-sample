# serverless-python-sample

serverless framework を通して AWS 環境上に API Gateway, Lambda(python), CloudFront, S3 を作ってみるサンプル

<img width="881" alt="スクリーンショット 2022-07-14 16 52 36" src="https://user-images.githubusercontent.com/21980958/178931198-026c516a-f0bc-4033-970d-97ff0975c2e0.png">

# Requirement

以下の環境で構築しました

## aws

```bash
$ aws --version
aws-cli/1.25.29 Python/3.8.10 Windows/10 exec-env/EC2 botocore/1.27.29
```

## chocolatey

```bash
choco -v
1.1.0
```

## node.js

```bash
$ node -v
v18.6.0
```

## npm

```bash
$ npm -v
8.13.2
```

## serverless framework

```bash
$ serverless -v
Framework Core: 3.20.0 (standalone)
Plugin: 6.2.2
SDK: 4.3.2
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
$ npm ci
```

※npm install ですと動かない場合があります

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

# Local Debug

## serverless offline を起動

```bash
$ serverless offline
```

## 確認

postman や curl 等で確認してください

```
GET http://localhost:3000/dev/api/hello?test=get
```

```
POST http://localhost:3000/dev/api/hello
Content-Type: "application/json"
{
    "test": "post"
}
```

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
