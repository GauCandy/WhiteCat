## Mục Lục

- [Tổng Hợp Tài Liệu (VN)](#tổng-hợp-tài-liệu-vn)
  - [language.js — i18n](#languagejs--trình-nạp-locale-và-trợ-lý-i18n)
  - [prefix.js — Prefix](#prefixjs--khung-lệnh-dựa-trên-prefix)
  - [slash.js — Slash](#slashjs--trình-nạp-và-xử-lý-slash-command)
  - [time.js — Scheduler](#timejs--bộ-lập-lịch-công-việc)
- [Event — Khung xử lý theo sự kiện](#event--khung-xử-lý-theo-sự-kiện)
- [Điều Khoản Sử Dụng (Terms Gate)](#điều-khoản-sử-dụng-terms-gate)
- [CatBox — Biến dùng chung](#catbox--biến-dùng-chung)
- [Ví (Wallet) và Log giao dịch](#ví-wallet-và-log-giao-dịch)
- [Database Driver](#database-driver)
- [Thay đổi CSDL liên quan](#thay-đổi-csdl-liên-quan)

## Tổng Hợp Tài Liệu (VN)

Tài liệu này tập hợp và dịch sang tiếng Việt các nội dung trong thư mục `docs`: `language.md`, `prefix.md`, `slash.md`, và `time.md`.

---

### language.js — Trình nạp locale và trợ lý i18n

- Tổng quan: Nạp các tệp locale, hợp nhất nội dung, và cung cấp các hàm trợ giúp để tra cứu/định dạng chuỗi với cơ chế dự phòng an toàn.

**Bố cục thư mục**
- `src/language/*.yml|yaml`: tên tệp (ví dụ `en.yml`) trở thành mã ngôn ngữ.
- Thư mục con theo ngôn ngữ: `src/language/<lang>/*.yml` được nhóm theo tên tệp và hợp nhất vào ngôn ngữ đó.
- Dự phòng JSON: nếu không có package `yaml`, bộ phân tích sẽ thử định dạng JSON.

**API**
- `initLanguage({ dir, defaultLang, watch })`
  - `dir`: thư mục gốc (mặc định `src/language`).
  - `defaultLang`: ngôn ngữ mặc định ban đầu (có thể lấy từ biến môi trường `DEFAULT_LANG`), mặc định `en`.
  - `watch`: khi `true`, theo dõi thư mục và tự tải lại khi có thay đổi.
  - Trả về `{ t, tg, has, getAvailableLanguages, setDefaultLang }`.
- `t(lang, pathOrGroup, maybeKey?, vars?)`
  - Tra cứu khóa lồng nhau. Ví dụ: `t('vi', 'errors.not_found')` hoặc `t('vi', 'errors', 'not_found')`.
  - Placeholder: `{name}` hoặc `{{user.id}}` sẽ được thay bằng giá trị trong `vars`.
  - Dự phòng: nếu thiếu khóa trong `lang`, sẽ thử ở ngôn ngữ mặc định; nếu vẫn thiếu, trả về chính đường dẫn khóa.
- `tg(lang, group, key, vars?)`: alias rõ ràng cho `t` theo cặp nhóm + khóa.
- `has(lang, groupOrPath, key?)`: kiểm tra tồn tại (boolean).
- `getAvailableLanguages()`: trả về danh sách mã ngôn ngữ đã nạp.
- `setDefaultLang(lang)`: đổi ngôn ngữ mặc định khi đang chạy.

**Quy tắc hợp nhất**
- Tệp cấp cao nhất cho một ngôn ngữ sẽ được nạp trước, sau đó là các nhóm theo tệp trong thư mục con của ngôn ngữ đó; tất cả được deep-merge.
- Đối tượng merge đệ quy; mảng/giá trị nguyên thủy sẽ ghi đè.

**Theo dõi (watching)**
- Khi `watch: true`, dùng `fs.watch` ở thư mục gốc và từng thư mục theo ngôn ngữ; khi có thay đổi, nạp lại toàn bộ locales.

**Hành vi dự phòng**
- `resolveLang`: nếu `lang` yêu cầu tồn tại thì dùng, ngược lại dùng `defaultLang` (mặc định `en`).
- `t()` sẽ fallback sang ngôn ngữ mặc định nếu khóa thiếu ở ngôn ngữ được yêu cầu.

**Lỗi & Nhật ký**
- Lỗi phân tích YAML được log kèm đường dẫn tệp và thông báo lỗi.
- Nếu package `yaml` không cài, sẽ log cảnh báo một lần và chấp nhận JSON.

---

### prefix.js — Khung lệnh dựa trên prefix

- Tổng quan: Nạp lệnh dựa trên prefix, xác định prefix theo guild, cung cấp context phong phú, xử lý quyền và lỗi.

**Nạp lệnh**
- Quét đệ quy thư mục `src/command/prefix`.
- Bỏ qua tệp/thư mục bắt đầu bằng `_`.
- Hỗ trợ module xuất ra:
  - Một object `{ name, aliases?, description?, run(ctx) }`
  - Một mảng các object dạng trên
  - Một hàm `module.exports = async (ctx) => {}` (tự đặt tên theo tên tệp)

**Xác định prefix**
- Các prefix hiệu lực cho mỗi tin nhắn:
  - Từ `src/config.json: app.prefix` (hoặc ENV `PREFIX`, mặc định `!`).
  - Ghi đè theo guild từ DB `guilds.prefix` (có cache). Cả hai được xét; cái khớp đầu tiên sẽ dùng.
- Hàm trợ giúp:
  - `updateGuildPrefix(guildId, newPrefix)`: lưu vào DB và cache.
  - `getGuildPrefixById(guildId)`: lấy từ DB (có cache).

**Xác định ngôn ngữ (Guild)**
- Trong guild, `ctx.language` lấy từ `guilds.language` trong DB nếu có; nếu không thì `message.guild.preferredLocale`.
- Ở DM, lệnh prefix không chạy; `language` là `null`.
- Có sẵn các trợ lý từ language.js: `t, tg, has, setDefaultLang`.

**Context (`ctx`) truyền vào lệnh**
- `client`, `message`, `args`, `content`, `command`
- `prefix`, `allPrefixes`
- `env`, `db` (adapter kết nối DB dạng pool)
- `ownerIds` (từ `config.json.app.ownerIds`)
- `language`, `t`, `tg`, `has`, `setDefaultLang`
- Trợ lý guild: `setGuildPrefix`, `getGuildPrefix`, `getGuildPrefixById`
- Trợ lý ngôn ngữ: `setGuildLanguage`, `getGuildLanguage`, `refreshGuildLanguage`

**Kiểm tra quyền (Guild)**
- Trước khi chạy lệnh, kiểm tra bot có: `ViewChannel`, `SendMessages`, `SendMessagesInThreads` trong kênh.
- Nếu thiếu, bỏ qua lệnh một cách im lặng (tránh spam). Khi `debug.prefix=true`, sẽ log cảnh báo.

**Xử lý lỗi**
- Ẩn các lỗi phía người dùng khi `debug.prefix` không bật:
  - Missing Permissions (50013), Unknown Message (10008), Cannot DM (50007), Unknown Channel (10003), Missing Access (50001)
- Với lỗi khác: ghi log và thử phản hồi bằng thông báo lỗi chung.

**Debug**
- Điều khiển qua `src/config.json: debug.prefix`.

---

### slash.js — Trình nạp và xử lý Slash Command

- Tổng quan: Nạp động slash commands, cung cấp hàm đồng bộ, tiêm context, và xử lý quyền cũng như lỗi hiển thị tạm thời (ephemeral).

**Nạp lệnh**
- Quét đệ quy `src/command/slash` (bỏ qua tên bắt đầu bằng `_`).
- Các định dạng module hỗ trợ:
  - Object `{ data: { name, description, options?, contexts?, integrationTypes?, dmPermission? }, run(ctx) }`
  - Hoặc `{ name, description, options?, run }` (được chuẩn hóa về `data`).
  - Mảng các module ở trên.

**Hàm đồng bộ**
- `syncGuildCommands(client, guildId)`: đặt bộ lệnh cho một guild.
- `syncGlobalCommands(client)`: đặt lệnh ở cấp ứng dụng (có thể mất vài phút để đồng bộ).

**Context (`ctx`) truyền vào**
- `client`, `interaction`, `env`, `db` (pool DB)
- `ownerIds` (từ `config.json.app.ownerIds`)
- `language`:
  - Ngữ cảnh DM/cài đặt cho người dùng (context 1 hoặc 2, hoặc không ở trong guild): dùng `interaction.locale` (ngôn ngữ người dùng)
  - Trong guild: lấy `guilds.language` từ DB nếu có; nếu không thì `interaction.guildLocale`/`guild.preferredLocale`
- Trợ lý i18n từ language.js: `t`, `tg`, `has`, `setDefaultLang`

**Kiểm tra quyền (Guild)**
- Trước khi chạy, kiểm tra bot có: `ViewChannel`, `SendMessages`, `SendMessagesInThreads` trong kênh.
- Nếu thiếu: trả lời cảnh báo ephemeral một lần (`flags: 64`) rồi thoát.

**Xử lý lỗi**
- Ẩn các lỗi phía người dùng khi `debug.slash` không bật.
- Thiếu quyền (50013): trả lời cảnh báo ephemeral.
- Lỗi khác ở chế độ debug: trả lời lỗi chung ở dạng ephemeral.

**Ephemeral và Flags**
- Dùng `flags: 64` để trả lời ephemeral. `4096` dùng để ẩn thông báo ping (không ẩn nội dung).
- Mẫu xử lý hoàn toàn ephemeral: `deferReply({ flags: 64 })` → `editReply()` → có thể `followUp({ flags: 64 })`.

**Cài đặt theo ngữ cảnh (User-install / Contexts)**
- `data.contexts` và `data.integrationTypes` quyết định nơi lệnh xuất hiện.
- Ví dụ chỉ cho cài đặt người dùng trong kênh riêng tư: `contexts: [2]`, `integrationTypes: [1]`.

**Debug**
- Điều khiển qua `src/config.json: debug.slash`.

---

### time.js — Bộ lập lịch công việc

- Tổng quan: Nạp các module theo thời gian và lập lịch chạy công việc theo chu kỳ cố định, thời điểm trong ngày, hoặc tại một ngày/giờ cụ thể.

**Nạp module**
- Tìm trong `src/module/time` các tệp `.js` (bỏ qua tệp bắt đầu bằng `_`).
- Mỗi tệp có thể export:
  - Một hàm `(ctx) => {}` chạy khi lịch kích hoạt, hoặc
  - Một object có `run(ctx)` hoặc `onTick(ctx)`, kèm theo các trường lập lịch.

**Trường lập lịch**
- `every` / `interval`: chạy định kỳ.
  - Số = mili-giây.
  - Chuỗi rút gọn: `'second'|'minute'|'hour'` (căn mốc), hoặc `'5s'|'10m'|'2h'|'250ms'`.
  - Object: `{ hours, minutes, seconds, ms }`.
  - `immediate: true` để chạy một lần ngay trước khi bắt đầu chu kỳ.
- `at`: mảng thời điểm trong ngày, `'HH:mm'` hoặc `'HH:mm:ss'`. Chạy hằng ngày vào các thời điểm đó.
- `date` / `atDate`: lên lịch chạy một lần tại `Date` hoặc timestamp. Với khoảng trễ dài (> 24 ngày) sẽ có bộ kiểm tra hằng ngày để cài lại timeout.
- `enabled`: nếu `false` thì bỏ qua job.

**Căn mốc (alignment)**
- Với `'second'|'minute'|'hour'`, lần chạy đầu tiên căn mốc tới ranh giới kế tiếp rồi lặp theo chu kỳ cố định.

**Context (`ctx`) cung cấp cho job**
- `client` (Discord client), `env` (process env), `now: () => new Date()`
- `db` (adapter pool DB) nếu có.

**Điều khiển khi chạy**
- `initTimeJobs(client, extra?)`: nạp module và lên lịch công việc, mỗi process chỉ khởi tạo một lần.
- `stopTimeJobs()`: xóa tất cả timer/interval và đánh dấu scheduler đã dừng.

**Nhật ký & lỗi**
- Mỗi handle được log kèm lần chạy kế tiếp.
- Ngoại lệ trong job được bắt và log; scheduler vẫn tiếp tục hoạt động.


---

## Event — Khung xử lý theo sự kiện

- Nạp module từ `src/module/event` (đệ quy, bỏ `_*.js`).
- Mỗi module: `{ on: 'messageCreate'|'interactionCreate'|..., once?, enabled?, priority?, filter?, run(ctx) }`.
- Context chung: `client`, `env`, `db`, `ownerIds`, i18n (`t/tg/has/setDefaultLang`), `wallet` helpers, `language` gợi ý theo payload.
- Ví dụ có sẵn: `message_logger.js` (in log mọi tin nhắn), `broadcast_all_channels.js` (demo broadcast) và `accept_term.js` (xử lý nút đồng ý điều khoản).

---

## Điều Khoản Sử Dụng (Terms Gate)

- Bảng `users` có cột `term` (0/1, mặc định 0) và `join_at` (thời điểm chấp nhận).
- Khi chạy lệnh prefix/slash, nếu `term=0` bot sẽ gửi embed + nút (ảnh theo ngôn ngữ từ `src/image/terms/`).
- Nút có `custom_id`: `accept-terms:<userId>:<epochSecs>`. Event `accept_term.js` ghi nhận và cập nhật DB (UPSERT) để `term=1`, `join_at` từ epoch.
- i18n cho tiêu đề/mô tả/nút: group `terms` trong `src/language/en*.yml`, `src/language/vi.yml`.

---

## CatBox — Biến dùng chung

- File: `src/cache/cat_box.js`
- Cấu trúc:
  - `app`: cấu hình, `prefix`, `ownerIds`, `startedAt`.
  - `flags.debug`: `{ prefix, slash }` và có thể mở rộng.
  - `guild[gid]`: cache `prefix`, `language`.
  - `user[uid]`: cache `term` (đã chấp nhận điều khoản hay chưa).
- Mục tiêu: chia sẻ cache giữa prefix/slash/event/time, giảm truy vấn lặp.

---

## Ví (Wallet) và Log giao dịch

- Bảng:
  - `user_wallet(user_id PK, wcoin BIGINT)` — FK → `users(user_id)` ON DELETE CASCADE.
  - `guild_wallet(guild_id PK, wcoin BIGINT)` — FK → `guilds(guild_id)` ON DELETE CASCADE.
  - `log_wallet` — lưu giao dịch: `from_user?`, `to_user?`, `to_guild?`, `currency`, `amount`, `status` (`pending|success|failed`), `message`, timestamps.
- Helpers dùng chung ở `ctx.wallet` (đã được tiêm vào prefix/slash/event/time):
  - `getUserBalance(userId, currency='wcoin')`
  - `getGuildBalance(guildId, currency='wcoin')`
  - `creditUser(userId, amount, currency='wcoin', note?)`
  - `creditGuild(guildId, amount, currency='wcoin', note?)`
  - `debitUser(userId, amount, currency='wcoin', note?)` (có kiểm tra đủ tiền)
  - `debitGuild(guildId, amount, currency='wcoin', note?)` (có kiểm tra đủ tiền)
  - `transfer({type:'user'|'guild', id}, {type:'user'|'guild', id}, amount, currency='wcoin', note?)`
- Thiết kế ưu tiên an toàn cạnh tranh: mọi phép cộng/trừ chạy trong TRANSACTION, tính toán tại DB bằng `UPDATE ... SET col = col ± ?` và kiểm tra đủ số dư via `AND col >= ?`.

---



## Database Driver
- Driver: dự án dùng lớp Driver database có thể hoán đổi giữa MariaDB (mặc định) và MySQL (mysql2).
- Cấu hình: thiết lập biến môi trường `DB_CLIENT` = `mariadb` | `mysql2` trong `.env`.
- Chuẩn sử dụng: mọi nơi trong code chỉ dùng API thống nhất `pool.query(sql, params)` và `pool.getConnection()`/`release()` (không gọi trực tiếp phương thức riêng của từng driver).
- Số lớn: với mysql2 bật `supportBigNumbers` + `bigNumberStrings`; với mariadb giữ `bigIntAsNumber=false` để trả về chuỗi, tránh mất chính xác.
- Đóng kết nối: dùng `pool.end()` (wrapper đã cung cấp `closePool()`), không gọi API driver thô để tránh nhầm lẫn.

---

## Thay đổi CSDL liên quan

- `guilds.language` cho phép `NULL`, không default.
- Thêm bảng `users(term TINYINT(1) DEFAULT 0, join_at TIMESTAMP NULL)`.
- Thêm `user_wallet`, `guild_wallet`, `log_wallet` như mô tả ở trên.
