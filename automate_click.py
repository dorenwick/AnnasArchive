#!/usr/bin/env python3
"""
Anna's Archive Downloader - Human-like Mouse Movement
Mimics realistic human cursor movement and clicking patterns
"""

import os
import time
import random
import logging
import math
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
    import undetected_chromedriver as uc

    UNDETECTED_AVAILABLE = True
except ImportError:
    UNDETECTED_AVAILABLE = False
    print("❌ Install: pip install undetected-chromedriver")

try:
    import pyautogui

    PYAUTOGUI_AVAILABLE = True
    # Configure pyautogui
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1
except ImportError:
    PYAUTOGUI_AVAILABLE = False
    print("❌ Install: pip install pyautogui")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HumanLikeDownloader:
    def __init__(self, download_dir="downloads", wait_time=5, proxy=None):
        """
        Anna's Archive downloader with human-like mouse movements
        """
        self.base_url = "https://annas-archive.org"
        self.download_dir = download_dir
        self.wait_time = wait_time
        self.proxy = proxy

        os.makedirs(download_dir, exist_ok=True)

        # Setup browser
        self.driver = self._setup_chrome()
        self.wait = WebDriverWait(self.driver, wait_time)
        self.actions = ActionChains(self.driver)

        # Human behavior parameters
        self.typing_speed_range = (0.05, 0.2)  # seconds between keystrokes
        self.mouse_speed_range = (0.5, 2.0)  # seconds for mouse movements
        self.pause_range = (1.0, 3.0)  # random pauses

    def _setup_chrome(self):
        """Setup Chrome with working configuration"""
        logger.info("🚀 Setting up Chrome...")

        if not UNDETECTED_AVAILABLE:
            raise ImportError("undetected-chromedriver required")

        try:
            options = uc.ChromeOptions()

            # Human-like window size (common resolution)
            options.add_argument("--window-size=1366,768")

            # Basic stealth options
            stealth_args = [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",
                "--disable-web-security",
                "--allow-running-insecure-content",
                "--disable-extensions-file-access-check",
                "--disable-extensions"
            ]

            for arg in stealth_args:
                options.add_argument(arg)

            # Proxy if provided
            if self.proxy:
                options.add_argument(f'--proxy-server={self.proxy}')
                logger.info(f"🌐 Using proxy: {self.proxy}")

            # Download settings
            prefs = {
                "download.default_directory": os.path.abspath(self.download_dir),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True
            }
            options.add_experimental_option("prefs", prefs)

            # Create driver
            driver = uc.Chrome(options=options, use_subprocess=False, version_main=138)

            # Apply stealth
            self._apply_stealth(driver)

            logger.info("✅ Chrome setup complete!")
            return driver

        except Exception as e:
            logger.error(f"❌ Chrome setup failed: {e}")
            raise

    def _apply_stealth(self, driver):
        """Apply stealth measures"""
        try:
            driver.get("about:blank")

            stealth_script = """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [
                        {name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer'},
                        {name: 'Native Client', filename: 'internal-nacl-plugin'}
                    ]
                });
                Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                Object.defineProperty(navigator, 'userAgent', {
                    get: () => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
                });
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                if (window.chrome) {
                    Object.defineProperty(window.chrome, 'runtime', {get: () => undefined});
                }
            """

            driver.execute_script(stealth_script)
            logger.info("✅ Stealth applied")

        except Exception as e:
            logger.warning(f"⚠️ Stealth application failed: {e}")

    def get_current_mouse_position(self):
        """Get current mouse cursor position"""
        if not PYAUTOGUI_AVAILABLE:
            logger.warning("⚠️ PyAutoGUI not available, using default position")
            return (400, 300)

        try:
            current_pos = pyautogui.position()
            logger.info(f"🖱️ Current mouse position: {current_pos}")
            return current_pos
        except Exception as e:
            logger.warning(f"⚠️ Could not get mouse position: {e}")
            return (400, 300)

    def human_like_mouse_movement(self, start_pos, end_pos, duration=None):
        """
        Create human-like mouse movement with bezier curves and natural speed variations
        """
        if not PYAUTOGUI_AVAILABLE:
            logger.warning("⚠️ PyAutoGUI not available, skipping mouse movement")
            return False

        try:
            if duration is None:
                duration = random.uniform(*self.mouse_speed_range)

            start_x, start_y = start_pos
            end_x, end_y = end_pos

            # Calculate distance
            distance = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

            # Adjust duration based on distance (humans move faster for longer distances)
            if distance > 200:
                duration *= 0.7
            elif distance < 50:
                duration *= 1.5

            logger.info(f"🖱️ Moving mouse from {start_pos} to {end_pos} over {duration:.2f}s")

            # Create control points for bezier curve (adds natural curve to movement)
            control1_x = start_x + (end_x - start_x) * 0.3 + random.randint(-50, 50)
            control1_y = start_y + (end_y - start_y) * 0.3 + random.randint(-30, 30)

            control2_x = start_x + (end_x - start_x) * 0.7 + random.randint(-30, 30)
            control2_y = start_y + (end_y - start_y) * 0.7 + random.randint(-20, 20)

            # Generate smooth path points
            steps = int(duration * 60)  # 60 FPS-like smoothness
            points = []

            for i in range(steps + 1):
                t = i / steps

                # Bezier curve calculation
                x = (1 - t) ** 3 * start_x + 3 * (1 - t) ** 2 * t * control1_x + 3 * (
                            1 - t) * t ** 2 * control2_x + t ** 3 * end_x
                y = (1 - t) ** 3 * start_y + 3 * (1 - t) ** 2 * t * control1_y + 3 * (
                            1 - t) * t ** 2 * control2_y + t ** 3 * end_y

                # Add slight randomness (human hand tremor)
                x += random.uniform(-1, 1)
                y += random.uniform(-1, 1)

                points.append((int(x), int(y)))

            # Move mouse through all points
            for point in points:
                pyautogui.moveTo(point[0], point[1])
                time.sleep(duration / len(points))

            logger.info("✅ Human-like mouse movement completed")
            return True

        except Exception as e:
            logger.error(f"❌ Mouse movement failed: {e}")
            return False

    def human_like_click(self, target_element):
        """
        Perform human-like click with realistic timing and movement
        """
        try:
            logger.info("🖱️ Performing human-like click...")

            # Get current mouse position
            current_pos = self.get_current_mouse_position()

            # Get element position and size
            element_rect = self.driver.execute_script("""
                var rect = arguments[0].getBoundingClientRect();
                return {
                    x: rect.left + window.pageXOffset,
                    y: rect.top + window.pageYOffset,
                    width: rect.width,
                    height: rect.height
                };
            """, target_element)

            # Calculate click position (slightly randomized within element bounds)
            click_x = element_rect['x'] + element_rect['width'] * random.uniform(0.3, 0.7)
            click_y = element_rect['y'] + element_rect['height'] * random.uniform(0.3, 0.7)

            # Convert to screen coordinates
            browser_pos = self.driver.get_window_position()
            browser_size = self.driver.get_window_size()

            # Account for browser chrome (address bar, etc.)
            chrome_height = 120  # Approximate browser chrome height

            screen_x = browser_pos['x'] + click_x
            screen_y = browser_pos['y'] + click_y + chrome_height

            target_pos = (int(screen_x), int(screen_y))

            logger.info(f"🎯 Target click position: {target_pos}")

            # Pre-click pause (humans pause before clicking)
            time.sleep(random.uniform(0.3, 0.8))

            # Move mouse to target with human-like movement
            movement_duration = random.uniform(0.8, 1.5)
            success = self.human_like_mouse_movement(current_pos, target_pos, movement_duration)

            if not success:
                logger.warning("⚠️ Mouse movement failed, using Selenium click")
                target_element.click()
                return True

            # Pre-click hover pause (humans often pause slightly after moving)
            time.sleep(random.uniform(0.2, 0.5))

            # Perform the click
            if PYAUTOGUI_AVAILABLE:
                # Human-like click timing
                pyautogui.mouseDown()
                time.sleep(random.uniform(0.05, 0.15))  # Human click duration
                pyautogui.mouseUp()

                logger.info("✅ Human-like click completed")

                # Post-click pause
                time.sleep(random.uniform(0.3, 0.7))

                return True
            else:
                # Fallback to Selenium
                target_element.click()
                return True

        except Exception as e:
            logger.error(f"❌ Human-like click failed: {e}")
            # Fallback to regular Selenium click
            try:
                target_element.click()
                return True
            except Exception as e2:
                logger.error(f"❌ Fallback click also failed: {e2}")
                return False

    def handle_cloudflare_human_like(self):
        """Handle Cloudflare with human-like behavior"""
        try:
            logger.info("🔍 Checking for Cloudflare challenges...")

            # Initial page load pause (humans need time to see the page)
            time.sleep(random.uniform(1, 2))

            page_text = self.driver.page_source.lower()
            cloudflare_indicators = [
                "verify you are human",
                "checking your browser",
                "security check",
                "cloudflare",
                "challenge-form",
                "turnstile"
            ]

            is_cloudflare = any(indicator in page_text for indicator in cloudflare_indicators)

            if is_cloudflare:
                logger.info("🚨 Cloudflare challenge detected!")

                # Simulate human reading behavior
                logger.info("👀 Simulating human reading...")
                time.sleep(random.uniform(2, 4))  # Humans read the message

                # Look for iframe first (common pattern)
                try:
                    iframe = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "iframe[title*='Cloudflare'], iframe[src*='challenges.cloudflare'], iframe[title*='Widget containing']"))
                    )

                    logger.info("🖼️ Found Cloudflare iframe")

                    # Switch to iframe
                    self.driver.switch_to.frame(iframe)
                    logger.info("🔄 Switched to iframe")

                    # Brief pause after switching
                    time.sleep(random.uniform(0.5, 1))

                except TimeoutException:
                    logger.info("📄 No iframe found, looking for direct elements")

                # Look for the checkbox
                checkbox_selectors = [
                    "input[type='checkbox']",
                    "label.ctp-checkbox-label",
                    "label[for*='challenge']",
                    ".challenge-form input",
                    ".cf-turnstile input",
                    "input[value*='Verify']"
                ]

                checkbox = None
                for selector in checkbox_selectors:
                    try:
                        checkbox = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        logger.info(f"✅ Found checkbox with selector: {selector}")
                        break
                    except TimeoutException:
                        continue

                if checkbox:
                    # Human-like behavior before clicking
                    logger.info("🤔 Simulating human decision making...")
                    time.sleep(random.uniform(1, 2))

                    # Perform human-like click
                    success = self.human_like_click(checkbox)

                    if success:
                        logger.info("✅ Human-like click successful!")

                        # Switch back to main content if we were in iframe
                        try:
                            self.driver.switch_to.default_content()
                        except:
                            pass

                        return self._wait_for_completion()
                    else:
                        logger.warning("❌ Human-like click failed")
                        return False
                else:
                    logger.error("❌ Could not find Cloudflare checkbox")
                    return False
            else:
                logger.info("✅ No Cloudflare challenge detected")
                return True

        except Exception as e:
            logger.error(f"❌ Human-like Cloudflare handling error: {e}")
            return False

    def simulate_human_typing(self, element, text):
        """Type text with human-like timing variations"""
        try:
            element.clear()
            time.sleep(random.uniform(0.2, 0.5))

            for char in text:
                element.send_keys(char)
                # Vary typing speed (humans don't type at constant speed)
                if char == ' ':
                    time.sleep(random.uniform(0.1, 0.3))  # Longer pause for spaces
                elif char in '.,!?':
                    time.sleep(random.uniform(0.2, 0.4))  # Pause after punctuation
                else:
                    time.sleep(random.uniform(*self.typing_speed_range))

            logger.info(f"✅ Human-like typing completed: '{text}'")
            return True

        except Exception as e:
            logger.error(f"❌ Human-like typing failed: {e}")
            return False

    def _wait_for_completion(self):
        """Wait for challenge completion"""
        try:
            logger.info("⏳ Waiting for challenge completion...")

            max_wait = 30
            initial_url = self.driver.current_url

            for i in range(max_wait):
                time.sleep(1)

                try:
                    current_url = self.driver.current_url
                    page_text = self.driver.page_source.lower()

                    challenge_indicators = [
                        "verify you are human",
                        "checking your browser",
                        "security check"
                    ]

                    still_challenging = any(indicator in page_text for indicator in challenge_indicators)

                    if not still_challenging or current_url != initial_url:
                        logger.info("✅ Challenge completion confirmed!")
                        time.sleep(random.uniform(1, 2))
                        return True

                    # Check for success elements
                    success_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                                 "input[placeholder*='search'], input[type='search']")
                    if success_elements:
                        logger.info("✅ Search elements found - challenge completed!")
                        return True

                except Exception as e:
                    logger.debug(f"Completion check error: {e}")

                if i % 10 == 0 and i > 0:
                    logger.info(f"⏳ Still waiting... ({i}/{max_wait})")

            logger.warning("⚠️ Challenge completion timeout")
            return False

        except Exception as e:
            logger.error(f"❌ Challenge completion error: {e}")
            return False

    def process_single_search(self, search_term):
        """Process single search with human-like behavior"""
        try:
            logger.info(f"🌐 Navigating to Anna's Archive...")

            # Navigate to site
            self.driver.get(self.base_url)

            # Handle Cloudflare with human-like behavior
            success = self.handle_cloudflare_human_like()

            if not success:
                logger.warning("⚠️ Cloudflare handling failed")
                return False

            # Human pause after successful challenge completion
            time.sleep(random.uniform(2, 4))

            # Find search box
            search_box = None
            search_selectors = [
                "input[placeholder*='Title, author, DOI, ISBN, MD5']",
                "input[type='search']",
                "input[name='q']"
            ]

            for selector in search_selectors:
                try:
                    search_box = self.wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    logger.info(f"🔍 Found search box")
                    break
                except TimeoutException:
                    continue

            if not search_box:
                logger.error("❌ Search box not found")
                return False

            # Human-like typing
            success = self.simulate_human_typing(search_box, search_term)
            if not success:
                return False

            # Human pause before pressing enter
            time.sleep(random.uniform(0.5, 1.5))
            search_box.send_keys(Keys.RETURN)

            # Wait for results with human-like patience
            logger.info("⏳ Waiting for search results...")
            time.sleep(random.uniform(2, 4))

            # Handle potential Cloudflare on search results
            self.handle_cloudflare_human_like()

            # Continue with download logic...
            logger.info("✅ Search completed successfully")
            return True

        except Exception as e:
            logger.error(f"❌ Search processing error: {str(e)}")
            return False

    def close(self):
        """Close browser"""
        if hasattr(self, 'driver'):
            self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Main execution
if __name__ == "__main__":
    print("🤖 HUMAN-LIKE ANNA'S ARCHIVE DOWNLOADER")
    print("=" * 60)
    print("🖱️ Uses realistic mouse movements and timing")
    print("⌨️ Human-like typing with natural speed variations")
    print("🧠 Simulates human decision-making pauses")
    print("=" * 60)
    print()

    if not PYAUTOGUI_AVAILABLE:
        print("⚠️ WARNING: PyAutoGUI not available")
        print("   Install with: pip install pyautogui")
        print("   Mouse movements will fall back to Selenium")
        print()

    try:
        with HumanLikeDownloader(
                download_dir="../annas_archive_downloads"
        ) as downloader:

            # Test search
            test_term = "Manufacturing Consent Noam Chomsky"
            logger.info(f"🧪 Testing with: {test_term}")

            success = downloader.process_single_search(test_term)

            if success:
                logger.info("🎉 Human-like session successful!")
            else:
                logger.warning("⚠️ Session had issues")

    except KeyboardInterrupt:
        logger.info("⏹️ Session interrupted")
    except Exception as e:
        logger.error(f"💥 Session failed: {e}")
        print(f"\n💡 Requirements:")
        print("   pip install undetected-chromedriver")
        print("   pip install pyautogui")
        print("   pip install selenium")