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
