# FastAPI template for simple REST APIs

## Introduction

小規模な開発を想定してなるべく全体像がわかりやすいように最小限の機能を実装している。
そのため、以下のような機能が必要な場合は別途改変が必要であることに留意すること。

- ローカルでの DB 構築(SQLite など)とそれに伴う docker-compose による複数コンテナのビルド
  - 個人的に最初から開発環境のサーバーに マネージド DB を立てて直接テストすることが多いので不要と考え割愛
- CICD Pipeline との統合
  - 特定のサービスに依存するため割愛
- テストコード
  - テンプレ化が難しいので割愛

## Get Started

1. pre-commit によるチェックを有効化する場合は、以下のコマンドによりローカル PC に pre-commit をインストールする

```bash
pip install pre-commit
```

1. ターミナルを再起動し、以下コマンドを実行する

```bash
pre-commit install
```
