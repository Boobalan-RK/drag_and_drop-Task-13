from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DragDropPage:
    """
    Page Object for jQuery Drag and Drop demo
    """

    URL = "https://jqueryui.com/droppable/"

    IFRAME = "//iframe"
    SOURCE_BOX = "//div[@id='draggable']"
    TARGET_BOX = "//div[@id='droppable']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)

    def open_page(self):
        """Open drag and drop page"""
        self.driver.get(self.URL)

    def switch_to_demo_frame(self):
        """Switch to iframe containing drag-drop demo"""
        frame = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.IFRAME))
        )
        self.driver.switch_to.frame(frame)

    def perform_drag_and_drop(self):
        """Perform drag and drop action"""
        source = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.SOURCE_BOX))
        )
        target = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.TARGET_BOX))
        )

        self.actions.drag_and_drop(source, target).perform()

    def get_target_text(self):
        """Get text of target box after action"""
        return self.driver.find_element(By.XPATH, self.TARGET_BOX).text
