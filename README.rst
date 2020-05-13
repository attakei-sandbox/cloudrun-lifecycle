==================
cloudrun-lifecycle
==================

Cloud Runのコンテナがいつまで生きているかが気になって調べてみるためのセット

使い方
======

* ``docker build`` する
* ``docker push`` する
* ``SLACK_WEBHOOK_URL`` にSlackのIncoming WebhookのURLを設定して、Cloud Runのサービスを起動する
* **Start container** というポストが来るのを見届ける
* **Shutdown container** というポストが来るのを待つ

実験中のメモ
============

* 1回目

  * On start: 2020-05-13 15:25 JST
  * Shutdown: ???
