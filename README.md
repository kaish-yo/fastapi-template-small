# FastAPI template for simple REST APIs

## Introduction

小規模な開発を想定してなるべく全体像がわかりやすいように最小限の機能を実装している。
そのため、以下のような機能が必要な場合は別途改変が必要であることに留意すること。

- ローカルでの DB 構築(SQLite など)とそれに伴う docker-compose による複数コンテナのビルド
  - 最初から開発環境のサーバーに マネージド DB を立てて直接テストすることが多いので不要と考え割愛
- CICD Pipeline との統合
  - 特定のサービスに依存するため割愛
- テストコード
  - テンプレ化が難しいので割愛するが、[StepCI](https://docs.stepci.com/integration/fastapi.html)による実装例を今後追加するかもしれない。

## Get Started

### Install pre-commit

1. pre-commit によるチェックを有効化するため、以下のコマンドによりローカル PC に pre-commit をインストールする

```bash
pip install pre-commit
```

2. ターミナルを再起動し、以下コマンドを実行する

```bash
pre-commit install
```

#### 注意

Black Formatter のみ自動修正が行われないため、エラーが出た場合は以下コマンドを実行した上で再度 add でステージング、そして commit をする必要がある点に注意する。

```bash
black app
```

### Build in local environment

1. `.env`を`.env.example`を参考に作成し、組み込む環境変数を定義する
2. [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を VSCode にインストールし、`Ctrl+Shift+P` でメニューを開いて`Dev Containers: Reopen in Container`を実行する
3. 開発環境のコンテナが立ち上がる
