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

## node.js

windows の場合
https://otona-life.com/2022/02/09/103500/

## serverless framework

windows の場合
https://zenn.dev/mid480/articles/serverless-framework-used-by-windows-

## serverless-python-requirements

## hosting

```bash
$ npm install serverless-s3-sync
```

## lambda

pip インストールが必要な AWS Lambda の Python スクリプトを Serverless Framework で間単位デプロイできるプラグイン

```bash
$ serverless plugin install -n serverless-python-requirements
```

# Test

## lambda

```bash
$ python -m unittest discover
```

# Usage

## 自分のローカル PC の証明書を設定(AWS IAM)

## deploy

### hosting

```bash
$ serverless deploy --aws-profile ${自分の設定したプロファイル名}
```

### lambda

```bash
$ serverless deploy --aws-profile ${自分の設定したプロファイル名}
```

### デプロイできていることを確認

# Remove

お掃除
作ったリソースを全部削除

```bash
$ serverless remove --aws-profile ${自分の設定したプロファイル名}
```
