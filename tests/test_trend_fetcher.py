import pytest

def test_trend_data_structure():
    """
    Asserts that the trend data structure matches the API contract 
    defined in specs/technical.md.
    """
    # This represents the data we EXPECT the skill to return
    mock_trend_output = {
        "trends": [
            {
                "topic": "Autonomous Agents",
                "relevance_score": 0.98,
                "source_url": "https://mcp.news/trends/1"
            }
        ]
    }
    
    # Validation Logic
    assert "trends" in mock_trend_output
    for trend in mock_trend_output["trends"]:
        assert isinstance(trend["topic"], str)
        assert isinstance(trend["relevance_score"], float)
        assert trend["relevance_score"] >= 0.0 and trend["relevance_score"] <= 1.0
        assert trend["source_url"].startswith("http")

def test_trend_analyzer_interface_failure():
    """
    This test is designed to FAIL. 
    It tries to call the actual skill which doesn't exist yet.
    """
    from skills.skill_trend_analyzer import trend_analyzer
    
    # This will raise an ImportError because we haven't written the code!
    result = trend_analyzer.fetch_trends(persona_id="tech_influencer", sources=[])
    assert result is not None