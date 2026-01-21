import pytest
from pages.drag_drop_page import DragDropPage


@pytest.mark.positive
def test_drag_and_drop_positive(driver):
    """
    Positive Test Case:
    Verify draggable box is successfully dropped into target box
    """

    page = DragDropPage(driver)
    page.open_page()
    page.switch_to_demo_frame()
    page.perform_drag_and_drop()

    assert page.get_target_text() == "Dropped!", "Drag and Drop failed"


@pytest.mark.negative
def test_drag_and_drop_negative(driver):
    """
    Negative Test Case:
    Verify target text is NOT 'Dropped!' without performing drag and drop
    """

    page = DragDropPage(driver)
    page.open_page()
    page.switch_to_demo_frame()

    assert page.get_target_text() != "Dropped!", "Negative test failed"
