# Tài liệu Bot Discord

Đây là một bot Discord toàn diện với các tính năng về kinh tế, giải trí, quản lý server, tiện ích, tính năng cao cấp và bảo mật. Dưới đây là tổng quan có tổ chức về các mô-đun và chức năng của bot.

## Mục lục
1. [Kinh tế & Giải trí](#kinh-tế--giải-trí)
   - [Tiền tệ 💰](#tiền-tệ)
   - [Nhà cửa 🏠](#nhà-cửa)
   - [Nuôi thú cưng & Trang trại 🌱🐶🐱](#nuôi-thú-cưng--trang-trại)
   - [Săn thú 🎯](#săn-thú)
   - [Nhiệm vụ 🗺️](#nhiệm-vụ)
   - [Cấp độ & Thống kê 📊](#cấp-độ--thống-kê)
   - [Kết hôn 💍](#kết-hôn)
   - [Tarot 🔮](#tarot)
   - [Trò chơi chữ 🔤](#trò-chơi-chữ)
   - [Trò chơi Casino 🎰🎲](#trò-chơi-casino)
   - [Xổ số 🎟️](#xổ-số)
   - [Hồ sơ 👤](#hồ-sơ)
   - [Tín dụng 💳](#tín-dụng)
   - [Hành động & Biểu cảm 😄](#hành-động--biểu-cảm)
2. [Quản lý Server](#quản-lý-server)
   - [Giveaway 🎉](#giveaway)
   - [Embed & Tự động trả lời 👋](#embed--tự-động-trả-lời)
   - [Kênh thoại tạm thời 🔊](#kênh-thoại-tạm-thời)
   - [Điều hành ⚖️](#điều-hành)
   - [Vai trò & Hạng 🎭](#vai-trò--hạng)
   - [Nhật ký & Thống kê 📜](#nhật-ký--thống-kê)
   - [Tiền tố 🔧](#tiền-tố)
3. [Tiện ích 🔧](#tiện-ích)
4. [Cao cấp (VIP) 🌟](#cao-cấp-vip)
5. [Bảo mật 🚨](#bảo-mật)
   - [Chống Raid](#chống-raid)
   - [Danh tiếng](#danh-tiếng)

---

## Kinh tế & Giải trí

### Tiền tệ 💰
- **Cửa hàng**: Mua vật phẩm (nội thất, phụ kiện thú cưng), ảnh đại diện và nền (VIP/thường).
- **Quản lý số dư**:
  - Lệnh: `credits` (xem số dư).
  - Chuyển credits (xác thực quyền, ghi log giao dịch).
- **Lịch sử giao dịch**: Lưu trong cơ sở dữ liệu, hiển thị phân trang.
- **Tích hợp**: Nhà cửa, Tín dụng, Hồ sơ, Casino, Nhiệm vụ, Kết hôn, Xổ số.

### Nhà cửa 🏠
- **Trang trí**:
  - Giao diện kéo-thả để tùy chỉnh nội thất.
  - Danh mục embed để mua vật phẩm.
- **Tích hợp**: Tiền tệ (mua bằng credits), Hồ sơ (hiển thị nhà).

### Nuôi thú cưng & Trang trại 🌱🐶🐱
- **Chăm sóc thú cưng**:
  - Cho ăn, tắm (dựa trên bộ đếm thời gian).
  - Thăng cấp và tiến hóa (XP, sức khỏe, giai đoạn tiến hóa).
  - Tùy chỉnh phụ kiện thú cưng (mua/tùy chỉnh).
- **Trang trại**:
  - Tự động thu hoạch cây trồng, cá, hoặc động vật (cron job).
  - Tưới nước, chữa bệnh qua mini-game.
  - Bán sản phẩm lấy credits với giá thị trường động.
- **Tích hợp**: Tiền tệ (mua/bán), Săn thú (nguyên liệu), Cấp độ (XP từ chăm sóc).

### Săn thú 🎯
- **Logic săn**: Săn động vật (hiếm/thường) với cơ chế RNG.
- **Phần thưởng**: Credits và XP.
- **Biến thể**: Tìm bánh, nước hoặc nguyên liệu.
- **Tích hợp**: Thú cưng (động vật săn được làm thú cưng), Nhiệm vụ (nhiệm vụ liên quan săn), Tiền tệ.

### Nhiệm vụ 🗺️
- **Loại nhiệm vụ**: Hàng ngày, hàng tuần, thử thách theo cấp độ.
- **Phần thưởng**: Credits, vật phẩm, thưởng chuỗi.
- **Tích hợp**: Cấp độ (XP), Tiền tệ (credits), Săn thú (nhiệm vụ liên quan).

### Cấp độ & Thống kê 📊
- **Theo dõi XP/Cấp độ**: Tương tự Lurkr, với hệ số tăng từ boost.
- **Cụ thể theo server**: Cơ sở dữ liệu theo ID server.
- **Bảng xếp hạng**: Top hoạt động văn bản/voice (ngày/tuần/tháng).
- **Lệnh**: `rank` (cá nhân), `top` (bảng xếp hạng), `setxp`, `setlevel` (admin).
- **Tích hợp**: Hồ sơ (hiển thị cấp độ), Tiền tệ (thưởng mốc cấp), Điều hành (tự động cấp vai trò).

### Kết hôn 💍
- **Tính năng**: Mua nhẫn, tùy chỉnh lời hứa (embed lễ cưới), tải lên/tùy chỉnh ảnh kết hôn (giống meme).
- **Thưởng hàng ngày**: Tăng điểm hàng ngày (mô hình owo).
- **Tích hợp**: Tiền tệ (mua nhẫn), Hồ sơ (trạng thái kết hôn), Hành động (biểu cảm cặp đôi).

### Tarot 🔮
- **Xem bài tarot**: Rút bài ngẫu nhiên (3-5 lá) dựa trên RNG.
- **Dự báo ngẫu nhiên**: Văn bản vui nhộn, giới hạn hàng ngày.
- **Tích hợp**: Tiền tệ (mua lượt xem cao cấp), Hồ sơ (lưu lịch sử).

### Trò chơi chữ 🔤
- **Nối chữ**: Ghép từ, tính điểm theo độ dài.
- **Đếm số**: Đếm tuần tự, chống spam.
- **Đuổi hình bắt chữ**: Dựa trên hình ảnh, API ngẫu nhiên.
- **Ghép câu**: Câu đố, thưởng XP.
- **Tích hợp**: Cấp độ (XP từ chiến thắng), Giveaway (phần thưởng từ trò chơi).

### Trò chơi Casino 🎰🎲
- **Trò chơi phức tạp**: Blackjack (đa người chơi), lật xu, tài xỉu, máy xèng (chủ đề).
- **Trò chơi đơn giản**: Kéo búa bao, cờ caro, đoán số, bầu cua, đua thú (embed hoạt hình).
- **Hộp ngẫu nhiên**: Lootbox, cấp bậc hiếm/thần thoại.
- **Tích hợp**: Tiền tệ (cược/thưởng), Cấp độ (XP từ chơi), Chống Raid (giám sát lạm dụng).

### Xổ số 🎟️
- **Xổ số**: RNG công bằng, rút thăm hàng tuần.
- **Giao diện**: Embed danh sách vé.
- **Tích hợp**: Tiền tệ (mua vé), Giveaway (phần thưởng).

### Hồ sơ 👤
- **Tùy chỉnh**: Ảnh đại diện, nền, khung (VIP/thường).
- **Lệnh**: `profile` (xem), `title` (thay đổi).
- **Giao diện**: Embed đẹp, sử dụng cache.
- **Tích hợp**: Cấp độ (XP/cấp), Tiền tệ (mua tùy chỉnh), Kết hôn (trạng thái), Danh tiếng (rep).

### Tín dụng 💳
- **Nạp tiền**: Chuyển tiền thật thành credits, tỷ lệ quy đổi.
- **Mua vật phẩm VIP**: Ảnh đại diện, nền.
- **Tích hợp**: Tiền tệ (chuyển đổi), Cao cấp (mở khóa VIP), Hồ sơ (vật phẩm VIP).

### Hành động & Biểu cảm 😄
- **Hành động tương tác**: Ôm, vuốt, nhắm đến người dùng.
- **Liệt kê emoji server**: Lọc/tìm kiếm biểu cảm.
- **Tích hợp**: Hồ sơ (biểu cảm trong tiểu sử), Điều hành (ghi log lạm dụng).

---

## Quản lý Server

### Giveaway 🎉
- **Flash giveaway**: Rút thăm nhanh.
- **Giveaway thường**: Tham gia qua phản ứng.
- **Vai trò bắt buộc**: Lọc người tham gia.
- **Tùy chỉnh admin**: Phần thưởng, thời gian.
- **Tích hợp**: Tiền tệ (phần thưởng credits), Embed (thông báo).

### Embed & Tự động trả lời 👋
- **Chào mừng**: Embed chào mừng, tự động gán vai trò.
- **Tạm biệt**: Ghi log rời server.
- **Thông báo boost**: Tin nhắn cảm ơn.
- **Tùy chỉnh embed**: Màu sắc, hình ảnh.
- **Tích hợp**: Nhật ký (ghi sự kiện), Chống Raid (tắt chào mừng khi raid).

### Kênh thoại tạm thời 🔊
- **Quản lý phòng thoại**: Cho phép, bitrate, chiếm quyền, cấm, đá, giới hạn, khóa.
- **Di chuyển người dùng**: `voicemove` (kiểm tra quyền).
- **Tích hợp**: Điều hành (đá, di chuyển), Nhật ký (sự kiện thoại).

### Điều hành ⚖️
- **Cấm/Đá**: `ban`, `unban`, `kick`, `vkick` (lý do, thông báo DM).
- **Tắt tiếng/Bật tiếng**: Tắt tiếng văn bản/thoại, bật tiếng, timeout/untimeout (tự động gỡ).
- **Tắt âm/Bật âm**: Trạng thái thoại, xử lý kết nối lại.
- **Cảnh cáo**: `warn`, `warn_remove`, `warnings` (đếm tăng dần).
- **Xóa tin nhắn**: `clear` (xóa hàng loạt, lọc người dùng/bot).
- **Khóa/Mở kênh**: `lock`, `unlock` (ghi đè quyền).
- **Chế độ chậm**: Đặt thời gian, theo kênh.
- **Di chuyển người dùng**: `move` (ID/đề cập kênh).
- **Lý do**: Cập nhật lý do cho trường hợp điều hành.
- **Tích hợp**: Nhật ký (modlogs, case), Chống Raid (tự động cấm), Vai trò (kiểm tra thứ bậc).

### Vai trò & Hạng 🎭
- **Quản lý vai trò**: Thêm, xóa, nhiều vai trò, `roleinfo` (hàng loạt ≤10).
- **Hạng tự chọn**: `addrank`, `delrank`, `rank`, `ranks` (tự gán).
- **Đổi màu vai trò**: `color`, `colors` (hex/danh sách, cache).
- **Đổi biệt danh**: `setname` (ghi log điều hành).
- **Tích hợp**: Cấp độ (tự động gán vai trò), Điều hành (vai trò tắt tiếng), Hồ sơ (hiển thị vai trò).

### Nhật ký & Thống kê 📜
- **Nhật ký điều hành**: `case`, `modlogs`, `moderations` (lọc theo loại/thời gian).
- **Thống kê mod**: `modstats` (số lượng case, thời gian trung bình).
- **Thông tin server**: `serverinfo`, `membercount` (trực tuyến/ngoại tuyến).
- **Nhật ký mời**: `inviteinfo` (số lần sử dụng/hết hạn).
- **Điểm số**: CRUD điểm, tăng/giảm/đặt lại (theo server).
- **Tích hợp**: Điều hành (cập nhật lý do), Tiện ích (thống kê, thời gian hoạt động).

### Tiền tố 🔧
- **Xem/thay đổi tiền tố**: `prefix` (thông báo trực tiếp).
- **Lưu trong DB theo ID server**: Hỗ trợ rollback.
- **Tích hợp**: Tất cả hệ thống (kích hoạt lệnh).

---

## Tiện ích 🔧
- **Máy tính**: Đánh giá biểu thức toán học, thực thi an toàn.
- **Thông tin server**: `serverinfo`, `membercount` (biểu tượng thu nhỏ).
- **Thông tin mời**: `inviteinfo` (người mời/số lần sử dụng).
- **Nhắc nhở**: `remindme` (lên lịch DM, hỗ trợ lặp lại).
- **Màu ngẫu nhiên**: `randomcolor` (tạo hex, xem trước).
- **Rút gọn URL**: `short` (API bit.ly, xác thực).
- **Trò chơi nhỏ**:
  - Tung xúc xắc: `roll` (đa xúc xắc, 3d6).
  - Tung đồng xu: `flip` (kết quả emoji).
  - Oẳn tù tì: `rps` (đấu với bot).
  - Bình chọn: `poll` (phản ứng/nút, thời gian thực).
- **Thông tin người dùng**:
  - `user/whois`: Tên người dùng, ID, ngày tham gia.
  - `avatar`: Hình đại diện đầy đủ, gif động.
- **API vui**:
  - Ảnh động vật: `cat`, `dog`, `pug` (thử lại nếu lỗi).
  - Câu đùa bố: `dadjoke` (dự phòng cục bộ).
  - Kho GitHub: `github` (sao/fork).
  - Bài hát iTunes: `itunes` (liên kết xem trước).
  - Pokémon: `pokemon` (thống kê/kỹ năng).
  - Vũ trụ: `space` (tọa độ ISS, embed bản đồ).
- **Điểm nổi bật**: Cảnh báo từ khóa.
  - Lưu từ khóa: Lưu trữ DB.
  - Thông báo: Kênh/DM, thoát regex.
- **Thống kê**: Thống kê bot (số server, người dùng, ID shard).
- **Thời gian hoạt động**: `uptime` (dạng dễ đọc, ngày/giờ).
- **Tích hợp**: Hồ sơ (ảnh đại diện), Điều hành (ping để gỡ lỗi), Cấp độ (XP từ trò chơi).

---

## Cao cấp (VIP) 🌟
- **Quản lý VIP**: `vip info`, `vip move`, `vip restart` (kiểm tra cấp bậc).
- **Bảng trắng danh sách**: `vip whitelist` (thông báo DM).
- **Tùy chỉnh bot**: `vip avatar`, `vip username`, `vip status` (xử lý giới hạn tốc độ).
- **Chuyển quyền**: `vip transfer` (OAuth, nhật ký kiểm tra).
- **Tích hợp**: Tín dụng (nạp VIP), Tất cả hệ thống (mở khóa tính năng).

---

## Bảo mật 🚨

### Chống Raid
- **Phát hiện**: Tuổi tài khoản, số lượng tham gia, khung thời gian.
- **Xử lý**: Tắt tiếng, cấm, tắt thông báo chào mừng.
- **Ghi log**: Bắt đầu/kết thúc raid.
- **Tích hợp**: Điều hành (tự động cấm), Embed (tắt chào mừng), Nhật ký (sự kiện raid).

### Danh tiếng
- **Trao điểm danh tiếng**: 1 lần/24h, giao dịch độc lập.
- **Cache & thời gian**: Redis, ngăn chặn spam.
- **Tích hợp**: Hồ sơ (hiển thị danh tiếng), Cấp độ (tùy chọn chuyển danh tiếng thành XP).