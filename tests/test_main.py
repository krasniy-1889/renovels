from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_main_url():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()[0]["id"] == 0


def test_upload_pdf_file():
    with open("src/tests/files/file.pdf", "wb") as file_pdf:
        res = client.post(
            "/file", files={"file_pdf": ("file_pdf", file_pdf, "application/pdf")}
        )
        assert res.status_code == 201
