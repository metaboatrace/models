![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/publish.yml/badge.svg)
![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/tests.yml/badge.svg)
![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/lint.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/metaboatrace/models.svg)
![PyPI version](https://img.shields.io/pypi/v/metaboatrace.models.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python version](https://img.shields.io/badge/python-3.13-blue.svg)
![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

## 概要

ボートレースのドメインで用いる共有データ型（pydantic モデル・Enum・値オブジェクト）のパッケージ  
※ 機械学習におけるモデルではなく、pydantic データモデルの意

DDD でいう **Shared Kernel（共有カーネル）** に相当し、複数のサービス（crawlers / ml 等）が共有するドメインの語彙・データ構造・軽量なバリデーション（値域チェック等）を提供する。

本パッケージの責務はデータ構造と値の構造的妥当性までであり、ビジネスルールは含まない。ビジネスルールは各サービス側のドメイン層が持つ。また、本パッケージへの依存は必須ではない（例: voting は共有カーネルへの結合を避け、`metaboatrace.contracts` の Published Language 経由で連携する設計を採る）。

## インストール

```bash
$ pip install metaboatrace.models
```

## 開発環境構築

```bash
uv sync
source .venv/bin/activate
```

※ `uv` が事前にインストールされていること

## ブランチ戦略

[GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) を採用している。
