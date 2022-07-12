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
$ serverless plugin install -n serverless-s3-deploy
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

https://serverless-python-sample-bucket.s3.ap-northeast-1.amazonaws.com/index.html

# Note

注意点などがあれば書く

# Author

作成情報を列挙する

- 作成者
- 所属
- E-mail

# License

ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる
