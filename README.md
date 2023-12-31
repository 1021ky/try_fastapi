# try_fastapi

書籍「動かして学ぶ！Python FastAPI開発入門」を読みながら書いたFastAPI ßWebアプリケーションの練習用リポジトリです。

## memo

### Document

fastapiはエンドポイントを定義した時点でswaggerでの定義もされる。
Mockを分けて作らなくてもエンドポイントを定義して、レスポンスをハードコーディングしてしまえば、それでMockになるな。
良い。

### response

<https://fastapi.tiangolo.com/ja/advanced/response-directly/>にかかれているようにカスタムレスポンスも作れる。
<https://fastapi.tiangolo.com/ja/advanced/custom-response/#_1>にあるように用意されているレスポンスもある。

* HTMLResponse
* PlainTextResponse
* JSONResponse
* ORJSONResponse
* UJSONResponse
* RedirectResponse
* StreamingResponse
* FileResponse

### ディレクトリ構成

<https://fastapi.tiangolo.com/tutorial/sql-databases/?h=file#file-structure>
に基本構成サンプルがある。
ただ、本書ではファイルではなくディレクトリで分けている。

エンドポイントが増えたときに、ファイルが巨大になるからとのこと

### レスポンス定義

レスポンスはclassで表現する。
レスポンスフィールドを表す属性に型ヒントを書いておくと、レスポンス構築時（？）に、型チェックが入り、実行時エラーになるようになっている。
分岐処理があって、ある処理のときは属性の型が違って、別の処理のときは属性の型が違うということはなくしやすそう。

エンドポイントの定義はルーターで行う。
ルーターでレスポンスはどのようなフィールドであるかは、レスポンスクラスを指定することで定義する。
ということはルーターを見れば、エンドポイントとルーターの定義がわかるということか。

### リクエスト

リクエストもモデルを定義する
ルーターとして定義している関数の引数の型ヒントとして、モデルを指定することで、リクエストのモデルを定義できる。

リクエストのモデルでは、DBとのORMを設定できる

###　DBとの接続

本書で使っているpymysqlでは、pythonインタプリタで接続をためせた

```shell
poetry shell
python
>>> con = pymysql.connect(user="root", host="mysql", database="demo",port=3306, passwd="developer")
>>> con.get_host_info()
'socket mysql:3306'
```

migrate_db.pyでDBのマイグレーションを行ったあと、テーブルスキーマが期待通りできているか、pythonインタプリタで確認した。

```shell
>>> with con.cursor() as cursor:
...     cursor.execute("SHOW TABLES")
...     tables = cursor.fetchall()
...     for table in tables:
...             print(table[0])
...
2
dones
tasks
```

### 非同期DB接続

ライブラリをpymysql->aiomysqlに変更するだけで、非同期になる。
ただ、poetryでpoetry add aiomysqlだけだと、aiomysqlの依存ライブラリがインストールされない。
```zsh
ValueError: the greenlet library is required to use this function. No module named 'greenlet'
```
https://github.com/python-poetry/poetry/issues/5429が関連してそうで
`sqlalchemy = {extras = ["asyncio"], version = "^2.0.23"}`とpyproject.tomに追記すると動いた。`

コードには適宜async awaitを入れるだけで動いた。


### その他気になったことメモ

#### cookie使いたい場合は？
<https://fastapi.tiangolo.com/ja/tutorial/cookie-params/>
cookie用のクラスがある。
あとは、ルーターでセット。

#### datadog apm使いたい
<https://ddtrace.readthedocs.io/en/stable/integrations.html#fastapi>

専用のモジュールがあるので、それを使える。

#### ログを使いたい

標準のloggingモジュールを使う

#### フレームワークとビジネスロジックを分けたい

<https://fastapi.tiangolo.com/ja/advanced/using-dependencies/>

