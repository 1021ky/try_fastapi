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
