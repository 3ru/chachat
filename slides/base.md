---
marp: true
theme: gaia
size: 16:9
page_number: true
paginate: true
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

<!--
_color: white
_footer: Ryu
-->

![bg brightness:0.5](photo-1598965402089-897ce52e8355.jpg)
## ChaChat


---
![bg right 60%](chat_screen.png)
## 作成したアプリ
Chachat
- チャットアプリ

- アカウント登録可能
- アイコン設定可能
- 即時チャット反映

---

![bg 50% ](firebase.png)
## バックエンド環境

---

![bg 50% ](CloudArchitecture.png)
## インフラ設計

---
![bg 100% right](authenticate.png)

## アカウント登録

Firebase Authentication

- 新規アカウント登録
- ログイン認証

---
![bg 100% right](picture_storage.png)

## アカウント登録

Firebase StorageStorage

- アイコン画像保存

---
![bg 110% right](realtime_database.png)

## アカウント登録

Firebase Realtime Database

- チャットログ保存
- アイコン画像とユーザーの紐づけ
- 一覧画面用に最後のチャットを記録

----
## 実際の動作
https://youtu.be/IMiwu558So0

----
## 総括

- 手軽にチャットが可能
- ユーザーは全て参照されるため、小さいコミュニティや組織での利用が想定される
