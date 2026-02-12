![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/publish.yml/badge.svg)
![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/tests.yml/badge.svg)
![GitHub Workflow Status](https://github.com/metaboatrace/models/actions/workflows/lint.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/metaboatrace/models.svg)
![PyPI version](https://img.shields.io/pypi/v/metaboatrace.models.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python version](https://img.shields.io/badge/python-3.13-blue.svg)
![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

## 概要

ボートレース関連の開発で用いるモデルのパッケージ  
※ 機械学習におけるモデルではなく、クリーンアーキテクチャでのエンティティ層に相当するモジュールの集積

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

このリポジトリは [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) を採用している。

- `main` ブランチを唯一の常設ブランチとする
- 作業はトピックブランチで行い、PR を経て `main` にマージする
- リリースは Git タグで管理する
