from gymtime.scrape.fetch import fetch_c2c_html


def test_fetch_c2c_html():
    html = fetch_c2c_html()
    assert "<!DOCTYPE html>" in html
