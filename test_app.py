import pytest
from app import app, passwords


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------------------------------------------------------------------------
# passwords data structure
# ---------------------------------------------------------------------------

class TestPasswords:
    def test_passwords_is_dict(self):
        assert isinstance(passwords, dict)

    def test_expected_keys_present(self):
        for key in ("level1", "level2", "level4", "level5", "level6", "level9"):
            assert key in passwords, f"{key} missing from passwords"

    def test_level3_not_in_passwords(self):
        """level3 is commented out in the source."""
        assert "level3" not in passwords

    def test_password_values_are_strings(self):
        for key, value in passwords.items():
            assert isinstance(value, str), f"passwords[{key!r}] is not a string"

    def test_specific_password_values(self):
        assert passwords["level1"] == "JIGGER"
        assert passwords["level2"] == "3:33"
        assert passwords["level4"] == "WTC"
        assert passwords["level5"] == "Walter White"
        assert passwords["level9"] == "Grape"


# ---------------------------------------------------------------------------
# index route  /
# ---------------------------------------------------------------------------

class TestIndexRoute:
    def test_index_redirects(self, client):
        response = client.get("/")
        assert response.status_code == 302

    def test_index_redirects_to_level1(self, client):
        response = client.get("/", follow_redirects=False)
        assert "/level1" in response.headers["Location"]

    def test_index_follow_redirects(self, client):
        response = client.get("/", follow_redirects=True)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# level1 route  /level1
# ---------------------------------------------------------------------------

class TestLevel1Route:
    def test_level1_get_returns_200(self, client):
        response = client.get("/level1")
        assert response.status_code == 200

    def test_level1_get_renders_template(self, client):
        response = client.get("/level1")
        assert b"Level 1" in response.data or b"level1" in response.data.lower()

    def test_level1_get_contains_game_container(self, client):
        response = client.get("/level1")
        assert b"game-container" in response.data

    def test_level1_get_contains_plane_image(self, client):
        response = client.get("/level1")
        assert b"plane.png" in response.data

    def test_level1_get_contains_tower_images(self, client):
        response = client.get("/level1")
        assert b"tower1.jpg" in response.data
        assert b"tower2.jpg" in response.data

    def test_level1_post_redirects(self, client):
        response = client.post("/level1")
        assert response.status_code == 302

    def test_level1_post_redirects_to_level2(self, client):
        response = client.post("/level1", follow_redirects=False)
        assert "/level2_69" in response.headers["Location"]

    def test_level1_post_follow_redirects(self, client):
        response = client.post("/level1", follow_redirects=True)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# level2 route  /level2_69
# ---------------------------------------------------------------------------

class TestLevel2Route:
    def test_level2_get_returns_200(self, client):
        response = client.get("/level2_69")
        assert response.status_code == 200

    def test_level2_get_renders_template(self, client):
        response = client.get("/level2_69")
        assert b"Riddle" in response.data

    def test_level2_get_contains_input_area(self, client):
        response = client.get("/level2_69")
        assert b"answer-input" in response.data

    def test_level2_get_contains_submit_button(self, client):
        response = client.get("/level2_69")
        assert b"SUBMIT ANSWER" in response.data

    def test_level2_get_contains_final_form(self, client):
        response = client.get("/level2_69")
        assert b"final-form" in response.data

    def test_level2_post_redirects(self, client):
        response = client.post("/level2_69")
        assert response.status_code == 302

    def test_level2_post_redirects_to_level3(self, client):
        response = client.post("/level2_69", follow_redirects=False)
        assert "/level3_nig" in response.headers["Location"]

    def test_level2_post_follow_redirects(self, client):
        response = client.post("/level2_69", follow_redirects=True)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# level3 route  /level3_nig
# ---------------------------------------------------------------------------

class TestLevel3Route:
    def test_level3_get_returns_200(self, client):
        response = client.get("/level3_nig")
        assert response.status_code == 200

    def test_level3_get_renders_template(self, client):
        response = client.get("/level3_nig")
        assert b"LEVEL 3" in response.data

    def test_level3_get_contains_doors(self, client):
        response = client.get("/level3_nig")
        assert b"door-container" in response.data

    def test_level3_get_contains_five_doors(self, client):
        response = client.get("/level3_nig")
        assert response.data.count(b'class="door"') == 5

    def test_level3_get_contains_overlay(self, client):
        response = client.get("/level3_nig")
        assert b'id="overlay"' in response.data

    def test_level3_get_contains_video_element(self, client):
        response = client.get("/level3_nig")
        assert b"content-video" in response.data

    def test_level3_post_redirects(self, client):
        response = client.post("/level3_nig")
        assert response.status_code == 302

    def test_level3_post_redirects_to_level4(self, client):
        response = client.post("/level3_nig", follow_redirects=False)
        assert "/level4" in response.headers["Location"]

    def test_level3_post_follow_redirects(self, client):
        response = client.post("/level3_nig", follow_redirects=True)
        assert response.status_code == 200


# ---------------------------------------------------------------------------
# level4 route  /level4
# ---------------------------------------------------------------------------

class TestLevel4Route:
    def test_level4_get_returns_200(self, client):
        response = client.get("/level4")
        assert response.status_code == 200

    def test_level4_contains_congrats(self, client):
        response = client.get("/level4")
        assert b"Congrats" in response.data

    def test_level4_contains_season2_complete(self, client):
        response = client.get("/level4")
        assert b"season 2 complete" in response.data

    def test_level4_is_html(self, client):
        response = client.get("/level4")
        assert b"<h1>" in response.data


# ---------------------------------------------------------------------------
# invalid routes
# ---------------------------------------------------------------------------

class TestInvalidRoutes:
    def test_nonexistent_route_returns_404(self, client):
        response = client.get("/does-not-exist")
        assert response.status_code == 404

    def test_level4_post_not_allowed(self, client):
        response = client.post("/level4")
        assert response.status_code == 405


# ---------------------------------------------------------------------------
# full game flow (integration)
# ---------------------------------------------------------------------------

class TestGameFlow:
    def test_full_game_progression(self, client):
        """Walk through the entire game from index to level4."""
        # Start at index -> redirects to level1
        r = client.get("/", follow_redirects=True)
        assert r.status_code == 200

        # Beat level1 (POST) -> redirects to level2
        r = client.post("/level1", follow_redirects=True)
        assert r.status_code == 200
        assert b"Riddle" in r.data

        # Beat level2 (POST) -> redirects to level3
        r = client.post("/level2_69", follow_redirects=True)
        assert r.status_code == 200
        assert b"LEVEL 3" in r.data

        # Beat level3 (POST) -> redirects to level4
        r = client.post("/level3_nig", follow_redirects=True)
        assert r.status_code == 200
        assert b"Congrats" in r.data

    def test_levels_are_accessible_independently(self, client):
        """Each level endpoint works without requiring prior levels."""
        for path in ("/level1", "/level2_69", "/level3_nig", "/level4"):
            r = client.get(path)
            assert r.status_code == 200, f"GET {path} returned {r.status_code}"


# ---------------------------------------------------------------------------
# app configuration
# ---------------------------------------------------------------------------

class TestAppConfig:
    def test_app_name(self):
        assert app.name == "app"

    def test_app_has_expected_routes(self):
        rules = [rule.rule for rule in app.url_map.iter_rules()]
        assert "/" in rules
        assert "/level1" in rules
        assert "/level2_69" in rules
        assert "/level3_nig" in rules
        assert "/level4" in rules

    def test_level1_accepts_get_and_post(self):
        for rule in app.url_map.iter_rules():
            if rule.rule == "/level1":
                assert "GET" in rule.methods
                assert "POST" in rule.methods

    def test_level4_only_accepts_get(self):
        for rule in app.url_map.iter_rules():
            if rule.rule == "/level4":
                assert "GET" in rule.methods
                assert "POST" not in rule.methods
