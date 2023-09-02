# try_fastapi

FastAPIを使ったWebアプリケーションの練習用リポジトリです。

## memo

fastapiはエンドポイントを定義した時点でswaggerでの定義もされる。
Mockを分けて作らなくてもエンドポイントを定義して、レスポンスをハードコーディングしてしまえば、それでMockになるな。
良い。

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
