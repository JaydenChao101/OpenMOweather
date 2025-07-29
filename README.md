# OpenMOweather

**Status:** 🚧 開發中 (Dev)

## 專案簡介

OpenMOweather 是一個以 FastAPI 建置的中介 API 服務，用於把「澳門特別行政區政府地球物理氣象局（SMG）」公開的氣象資料轉換並提供統一、易用的 RESTful 接口。

主要目標：

1. **資料轉換**：將 SMG 原始 XML/JSON 資料，轉為結構化、標準化的回傳格式。
2. **簡易存取**：使用者只需呼叫本 API，即可獲取最新或歷史的氣象資訊，無需解析底層格式。
3. **開發擴充**：基於 FastAPI，方便未來新增認證、快取、資料庫儲存、即時推播等功能。

## 功能亮點

* 取得即時天氣狀況（預報、實況）。
* 支援歷史天氣查詢（依日期或區域）。
* 多種回傳格式：JSON。
* 可擴充 FastAPI 中介層：快取、認證、限流。

## 環境需求

* Python 3.8+
* FastAPI
* Uvicorn (ASGI server)
* aiohttp 或 requests (撈取 SMG API)
* Pydantic (資料驗證)



## 聯絡方式

如有問題或建議，請透過 GitHub Issue 提問，或聯絡作者。

---

© 2025 Jayden Chao. All rights reserved.
