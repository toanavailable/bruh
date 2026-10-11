# github-actions-lab

Project Python nhỏ để thực hành bài "GitHub Actions": tự động chạy test, kiểm tra code và bảo vệ nhánh `main`.

## Cấu trúc

| Đường dẫn | Nội dung |
| --- | --- |
| `calculator/` | Code chính (`mean`, `normalize`, `load_csv`) |
| `tests/` | Test bằng pytest, gồm cả test dữ liệu `data/sample.csv` |
| `requirements.txt` | Package cần để chạy code |
| `requirements_tests.txt` | Package chỉ cần khi chạy test |
| `.github/workflows/tests.yaml` | Chạy test trên 3 hệ điều hành x 3 phiên bản Python, có cache pip và coverage |
| `.github/workflows/codecheck.yaml` | `ruff check`, `ruff format --check`, `mypy` |
| `rulesets/main-protection.json` | Ruleset bảo vệ nhánh mặc định, dùng để import trên GitHub |

## Chạy cục bộ

```bash
python -m venv .venv
.venv\Scripts\activate            # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt -r requirements_tests.txt
coverage run -m pytest -v
coverage report
```

## Các bước phải làm trên GitHub

1. **Push (bài 5).** Tạo một repository trống trên GitHub rồi chạy:

   ```bash
   git remote add origin https://github.com/<user>/github-actions-lab.git
   git push -u origin main
   ```

   Mở tab **Actions** để xem lịch sử chạy; commit sẽ có dấu tích xanh khi test qua.

2. **Cache (bài 7).** Sau lần chạy đầu, vào **Actions -> Caches** để thấy cache pip. So sánh thời gian bước "Install dependencies" giữa lần chạy đầu và lần chạy sau.

3. **Codecov (bài 8).** Đăng nhập <https://codecov.io> bằng GitHub, thêm repository, sao chép token rồi tạo secret `CODECOV_TOKEN` tại **Settings -> Secrets and variables -> Actions**. Báo cáo `coverage.xml` cũng được lưu thành artifact `coverage-report` của mỗi lần chạy.

4. **Ruleset (bài 9).** Vào **Settings -> Rules -> Rulesets -> New ruleset -> Import a ruleset** và chọn `rulesets/main-protection.json`. Ruleset này yêu cầu:
   - phải merge qua pull request, có ít nhất 1 người approve;
   - mọi conversation phải được resolve;
   - hai status check `tests-passed` và `codecheck` phải qua;
   - Repository admin được phép bypass.

   Hai status check chỉ xuất hiện để chọn sau khi workflow đã chạy ít nhất một lần, nên hãy push trước rồi mới import.

5. **Dữ liệu với DVC (bài 10).** Hiện `data/sample.csv` được commit thẳng vào git. Khi chuyển sang DVC + Google Drive:
   - lấy nội dung file `default.json` trong `%LOCALAPPDATA%\pydrive2fs\<gdrive_client_id>\` (sinh ra sau lần `dvc push` đầu tiên);
   - tạo secret `GDRIVE_CREDENTIALS_DATA` chứa nội dung đó (coi như mật khẩu, không commit);
   - bỏ comment hai bước `setup-dvc` và `dvc pull` trong `tests.yaml`.
