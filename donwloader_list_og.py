#!/usr/bin/env python3
"""
Anna's Archive Downloader - ULTIMATE CLOUDFLARE BYPASS
Uses multiple advanced techniques to bypass Cloudflare detection
"""

import os
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
    import undetected_chromedriver as uc

    UNDETECTED_AVAILABLE = True
except ImportError:
    UNDETECTED_AVAILABLE = False
    print("❌ Install: pip install undetected-chromedriver")

try:
    from fake_useragent import UserAgent

    FAKE_UA_AVAILABLE = True
except ImportError:
    FAKE_UA_AVAILABLE = False
    print("❌ Install: pip install fake-useragent")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class UltimateCloudflareBypass:
    def __init__(self, download_dir="downloads", wait_time=30, proxy=None, user_data_dir=None):
        """
        Ultimate Cloudflare bypass with multiple techniques

        Args:
            proxy (str): Format "ip:port" or "user:pass@ip:port"
            user_data_dir (str): Path to existing Chrome profile
        """
        self.base_url = "https://annas-archive.org"
        self.download_dir = download_dir
        self.wait_time = wait_time
        self.proxy = proxy
        self.user_data_dir = user_data_dir

        os.makedirs(download_dir, exist_ok=True)

        # Setup with ultimate stealth
        self.driver = self._setup_ultimate_chrome()
        self.wait = WebDriverWait(self.driver, wait_time)

    def _setup_ultimate_chrome(self):
        """Setup Chrome with ULTIMATE anti-detection techniques"""
        logger.info("🚀 Setting up ULTIMATE Chrome bypass...")

        if not UNDETECTED_AVAILABLE:
            raise ImportError("undetected-chromedriver required: pip install undetected-chromedriver")

        try:
            options = uc.ChromeOptions()

            # === TECHNIQUE 1: Use existing Chrome profile ===
            if self.user_data_dir:
                logger.info(f"🔐 Using Chrome profile: {self.user_data_dir}")
                options.add_argument(f"--user-data-dir={self.user_data_dir}")
                # Use different profile to avoid conflicts
                options.add_argument("--profile-directory=AutomationProfile")

            # === TECHNIQUE 2: Advanced stealth arguments ===
            stealth_args = [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",
                "--disable-features=VizDisplayCompositor",
                "--disable-ipc-flooding-protection",
                "--disable-renderer-backgrounding",
                "--disable-backgrounding-occluded-windows",
                "--disable-field-trial-config",
                "--disable-back-forward-cache",
                "--disable-hang-monitor",
                "--disable-prompt-on-repost",
                "--disable-sync",
                "--disable-translate",
                "--hide-scrollbars",
                "--mute-audio",
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-logging",
                "--disable-gpu-logging",
                "--disable-software-rasterizer"
            ]

            for arg in stealth_args:
                options.add_argument(arg)

            # === TECHNIQUE 3: Realistic window size ===
            # Use common screen resolutions
            resolutions = [
                (1920, 1080), (1366, 768), (1536, 864), (1440, 900), (1280, 720)
            ]
            width, height = random.choice(resolutions)
            options.add_argument(f"--window-size={width},{height}")

            # === TECHNIQUE 4: Proxy configuration ===
            if self.proxy:
                options.add_argument(f'--proxy-server={self.proxy}')
                logger.info(f"🌐 Using proxy: {self.proxy}")

            # === TECHNIQUE 5: Enhanced download settings ===
            prefs = {
                "download.default_directory": os.path.abspath(self.download_dir),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True,
                "profile.default_content_settings.popups": 0,
                "profile.managed_default_content_settings.images": 2,  # Don't load images
                "profile.default_content_setting_values.notifications": 2
            }
            options.add_experimental_option("prefs", prefs)

            # === TECHNIQUE 6: Create driver with version matching ===
            logger.info("🎯 Starting Chrome with ultimate stealth...")
            driver = uc.Chrome(
                options=options,
                use_subprocess=False,
                version_main=138  # Match your Chrome version
            )

            # === TECHNIQUE 7: Post-startup stealth injection ===
            self._inject_ultimate_stealth(driver)

            # === TECHNIQUE 8: Pre-warm the browser ===
            self._prewarm_browser(driver)

            logger.info("✅ Ultimate Chrome setup complete!")
            return driver

        except Exception as e:
            logger.error(f"❌ Ultimate Chrome setup failed: {e}")
            raise

    def _inject_ultimate_stealth(self, driver):
        """Inject the most comprehensive stealth measures available"""
        try:
            logger.info("🥷 Injecting ULTIMATE stealth measures...")

            # Navigate to about:blank to inject stealth
            driver.get("about:blank")

            # Massive stealth injection
            stealth_script = """
                // === CORE WEBDRIVER REMOVAL ===
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });

                // === COMPREHENSIVE NAVIGATOR OVERRIDES ===
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [
                        {
                            name: 'Chrome PDF Plugin',
                            filename: 'internal-pdf-viewer',
                            description: 'Portable Document Format',
                            length: 1,
                            item: () => null,
                            namedItem: () => null
                        },
                        {
                            name: 'Chromium PDF Plugin',
                            filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai',
                            description: 'Portable Document Format', 
                            length: 1,
                            item: () => null,
                            namedItem: () => null
                        },
                        {
                            name: 'Microsoft Edge PDF Plugin',
                            filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai',
                            description: 'Portable Document Format',
                            length: 1,
                            item: () => null,
                            namedItem: () => null
                        }
                    ]
                });

                Object.defineProperty(navigator, 'languages', {
                    get: () => ['en-US', 'en']
                });

                Object.defineProperty(navigator, 'platform', {
                    get: () => 'Win32'
                });

                Object.defineProperty(navigator, 'hardwareConcurrency', {
                    get: () => 8
                });

                Object.defineProperty(navigator, 'deviceMemory', {
                    get: () => 8
                });

                Object.defineProperty(navigator, 'maxTouchPoints', {
                    get: () => 0
                });

                // === PERMISSIONS API OVERRIDE ===
                const originalQuery = window.navigator.permissions.query;
                window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                        Promise.resolve({ state: Notification.permission }) :
                        originalQuery(parameters)
                );

                // === CHROME RUNTIME REMOVAL ===
                if (window.chrome) {
                    Object.defineProperty(window.chrome, 'runtime', {
                        get: () => undefined
                    });

                    Object.defineProperty(window.chrome, 'app', {
                        get: () => undefined
                    });
                }

                // === SCREEN PROPERTIES ===
                Object.defineProperty(screen, 'colorDepth', {
                    get: () => 24
                });

                Object.defineProperty(screen, 'pixelDepth', {
                    get: () => 24
                });

                // === REMOVE AUTOMATION ARTIFACTS ===
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;

                // === WEBGL FINGERPRINT OVERRIDE ===
                const getParameter = WebGLRenderingContext.prototype.getParameter;
                WebGLRenderingContext.prototype.getParameter = function(parameter) {
                    if (parameter === 37445) {
                        return 'Intel Inc.';
                    }
                    if (parameter === 37446) {
                        return 'Intel(R) Iris(TM) Graphics 6100';
                    }
                    return getParameter(parameter);
                };

                // === CANVAS FINGERPRINT PROTECTION ===
                const toDataURL = HTMLCanvasElement.prototype.toDataURL;
                HTMLCanvasElement.prototype.toDataURL = function() {
                    // Add slight noise to canvas fingerprint
                    const noise = Math.random() * 0.0001;
                    return toDataURL.apply(this, arguments) + noise;
                };

                // === AUDIO CONTEXT FINGERPRINT ===
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) {
                    const getChannelData = AudioBuffer.prototype.getChannelData;
                    AudioBuffer.prototype.getChannelData = function() {
                        const data = getChannelData.apply(this, arguments);
                        // Add slight noise to audio fingerprint
                        for (let i = 0; i < data.length; i++) {
                            data[i] += Math.random() * 0.0001;
                        }
                        return data;
                    };
                }

                // === TIMEZONE CONSISTENCY ===
                Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {
                    value: function() {
                        return {
                            locale: 'en-US',
                            timeZone: 'America/New_York',
                            calendar: 'gregory',
                            numberingSystem: 'latn'
                        };
                    }
                });

                console.log('🥷 Ultimate stealth injection complete');
            """

            driver.execute_script(stealth_script)
            logger.info("✅ Ultimate stealth injection successful")

        except Exception as e:
            logger.warning(f"⚠️ Some stealth measures failed: {e}")

    def _prewarm_browser(self, driver):
        """Pre-warm browser to establish normal browsing patterns"""
        try:
            logger.info("🔥 Pre-warming browser...")

            # Visit a few normal sites first to establish browsing history
            prewarm_sites = [
                "https://www.google.com",
                "https://www.wikipedia.org"
            ]

            for site in prewarm_sites:
                try:
                    logger.info(f"🌐 Pre-warming: {site}")
                    driver.get(site)
                    time.sleep(random.uniform(2, 4))

                    # Simulate some interaction
                    self._simulate_natural_browsing(driver)

                except Exception as e:
                    logger.debug(f"Pre-warm site failed: {e}")
                    continue

            logger.info("✅ Browser pre-warming complete")

        except Exception as e:
            logger.warning(f"⚠️ Browser pre-warming failed: {e}")

    def _simulate_natural_browsing(self, driver):
        """Simulate natural browsing behavior"""
        try:
            # Random mouse movements
            for _ in range(2):
                x = random.randint(100, 800)
                y = random.randint(100, 500)
                driver.execute_script(f"""
                    var event = new MouseEvent('mousemove', {{
                        clientX: {x},
                        clientY: {y},
                        bubbles: true
                    }});
                    document.dispatchEvent(event);
                """)
                time.sleep(random.uniform(0.1, 0.3))

            # Random scroll
            scroll_amount = random.randint(100, 300)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.5, 1.0))

        except Exception as e:
            logger.debug(f"Natural browsing simulation failed: {e}")

    def test_ultimate_bypass(self):
        """Test the ultimate bypass against Anna's Archive"""
        try:
            logger.info("🧪 Testing ULTIMATE bypass...")

            # Navigate to Anna's Archive
            self.driver.get(self.base_url)

            # Extended wait for page load
            time.sleep(10)

            # Simulate extensive human behavior
            self._simulate_comprehensive_human_behavior()

            # Check for detection
            page_source = self.driver.page_source.lower()

            detection_indicators = [
                "verify you are human",
                "checking your browser",
                "security check",
                "cloudflare",
                "challenge-form",
                "robot"
            ]

            detected = [indicator for indicator in detection_indicators if indicator in page_source]

            if detected:
                logger.warning(f"🤖 STILL DETECTED: {detected}")

                # Take screenshot
                self.driver.save_screenshot("ultimate_bypass_test.png")
                logger.info("📸 Screenshot: ultimate_bypass_test.png")

                # Try to handle the challenge
                logger.info("🔧 Attempting challenge resolution...")
                if self._handle_advanced_challenge():
                    logger.info("✅ Challenge resolved!")
                    return True
                else:
                    logger.warning("❌ Challenge resolution failed")
                    return False
            else:
                logger.info("🎉 ULTIMATE BYPASS SUCCESSFUL!")
                logger.info(f"📄 Page title: {self.driver.title}")

                # Test search functionality
                try:
                    search_box = self.driver.find_element(By.CSS_SELECTOR,
                                                          "input[type='search'], input[name='q']")
                    logger.info("🔍 Search functionality confirmed!")
                    return True
                except:
                    logger.info("✅ No detection, but search not found")
                    return True

        except Exception as e:
            logger.error(f"❌ Ultimate bypass test failed: {e}")
            return False

    def _simulate_comprehensive_human_behavior(self):
        """Simulate the most comprehensive human behavior"""
        try:
            logger.info("🤖 Simulating comprehensive human behavior...")

            # Extended observation period
            observation_time = random.uniform(5, 8)
            logger.info(f"👀 Observing page for {observation_time:.1f}s...")
            time.sleep(observation_time)

            # Multiple realistic mouse paths
            for i in range(8):
                # Create curved mouse paths
                start_x = random.randint(100, 400)
                start_y = random.randint(100, 300)
                end_x = random.randint(500, 1000)
                end_y = random.randint(300, 600)

                steps = random.randint(15, 25)
                for step in range(steps):
                    progress = step / steps

                    # Bezier curve for natural movement
                    control_x = (start_x + end_x) / 2 + random.randint(-100, 100)
                    control_y = (start_y + end_y) / 2 + random.randint(-50, 50)

                    x = start_x + progress * (end_x - start_x) + progress * (1 - progress) * (control_x - start_x)
                    y = start_y + progress * (end_y - start_y) + progress * (1 - progress) * (control_y - start_y)

                    self.driver.execute_script(f"""
                        var event = new MouseEvent('mousemove', {{
                            clientX: {x},
                            clientY: {y},
                            bubbles: true,
                            view: window
                        }});
                        document.dispatchEvent(event);
                    """)
                    time.sleep(random.uniform(0.01, 0.03))

                time.sleep(random.uniform(0.5, 1.2))

            # Natural reading pauses
            time.sleep(random.uniform(3, 6))

            # Realistic scrolling patterns
            for _ in range(5):
                scroll_amount = random.randint(50, 200)
                direction = random.choice([1, -1])
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount * direction});")
                time.sleep(random.uniform(0.8, 2.0))

            # Focus interactions
            try:
                elements = self.driver.find_elements(By.TAG_NAME, "div")[:5]
                for element in elements:
                    try:
                        self.driver.execute_script("arguments[0].focus();", element)
                        time.sleep(random.uniform(0.2, 0.5))
                    except:
                        continue
            except:
                pass

            logger.info("✅ Comprehensive behavior simulation complete")

        except Exception as e:
            logger.debug(f"Behavior simulation error: {e}")

    def _handle_advanced_challenge(self):
        """Handle Cloudflare challenges with advanced techniques"""
        try:
            logger.info("🔧 Handling advanced challenge...")

            # Look for verification elements
            selectors = [
                "input[type='checkbox']",
                ".cf-turnstile input",
                ".challenge-form input",
                "button[type='submit']"
            ]

            element = None
            for selector in selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for elem in elements:
                        if elem.is_displayed():
                            element = elem
                            break
                    if element:
                        break
                except:
                    continue

            if element:
                logger.info("✅ Found challenge element")

                # Ultra-realistic interaction
                self.driver.execute_script("""
                    arguments[0].scrollIntoView({
                        behavior: 'smooth',
                        block: 'center'
                    });
                """, element)

                time.sleep(random.uniform(2, 4))

                # Advanced mouse approach
                element_rect = self.driver.execute_script("""
                    var rect = arguments[0].getBoundingClientRect();
                    return {x: rect.left + rect.width/2, y: rect.top + rect.height/2};
                """, element)

                # Curved approach to element
                start_x, start_y = 300, 300
                target_x, target_y = element_rect['x'], element_rect['y']

                steps = random.randint(20, 30)
                for step in range(steps):
                    progress = step / steps
                    curve_factor = 0.3 * progress * (1 - progress)

                    x = start_x + progress * (target_x - start_x) + curve_factor * random.randint(-50, 50)
                    y = start_y + progress * (target_y - start_y) + curve_factor * random.randint(-50, 50)

                    self.driver.execute_script(f"""
                        var event = new MouseEvent('mousemove', {{
                            clientX: {x},
                            clientY: {y},
                            bubbles: true
                        }});
                        document.dispatchEvent(event);
                    """)
                    time.sleep(random.uniform(0.02, 0.05))

                # Hover and click with realistic timing
                time.sleep(random.uniform(0.5, 1.0))

                try:
                    element.click()
                    logger.info("✅ Challenge element clicked")
                except:
                    self.driver.execute_script("arguments[0].click();", element)
                    logger.info("✅ Challenge element clicked (JS)")

                # Wait for completion
                return self._wait_for_challenge_completion()

            else:
                logger.info("ℹ️ No interactive challenge elements found")
                return self._wait_for_challenge_completion()

        except Exception as e:
            logger.error(f"❌ Advanced challenge handling failed: {e}")
            return False

    def _wait_for_challenge_completion(self):
        """Wait for challenge completion with continued behavior"""
        try:
            logger.info("⏳ Waiting for challenge completion...")

            max_wait = 90
            initial_url = self.driver.current_url

            for i in range(max_wait):
                time.sleep(1)

                # Continue realistic behavior during wait
                if i % 8 == 0:
                    x = random.randint(200, 800)
                    y = random.randint(200, 500)
                    self.driver.execute_script(f"""
                        var event = new MouseEvent('mousemove', {{
                            clientX: {x},
                            clientY: {y},
                            bubbles: true
                        }});
                        document.dispatchEvent(event);
                    """)

                # Check for completion
                current_url = self.driver.current_url
                page_text = self.driver.page_source.lower()

                challenge_indicators = [
                    "verify you are human",
                    "checking your browser",
                    "security check"
                ]

                still_challenging = any(indicator in page_text for indicator in challenge_indicators)

                if not still_challenging or current_url != initial_url:
                    logger.info("✅ Challenge completed!")
                    time.sleep(random.uniform(2, 4))
                    return True

                if i % 30 == 0 and i > 0:
                    logger.info(f"⏳ Still waiting... ({i}/{max_wait})")

            logger.warning("⚠️ Challenge completion timeout")
            return False

        except Exception as e:
            logger.error(f"❌ Challenge completion error: {e}")
            return False

    def close(self):
        """Close browser"""
        if hasattr(self, 'driver'):
            self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Test the ultimate bypass
if __name__ == "__main__":
    print("🚀 ULTIMATE CLOUDFLARE BYPASS TEST")
    print("=" * 50)
    print("Using advanced techniques:")
    print("✓ Chrome profile stealth")
    print("✓ Advanced fingerprint masking")
    print("✓ Comprehensive behavior simulation")
    print("✓ Multi-layer detection evasion")
    print()

    # === CONFIGURATION ===
    # Get your Chrome profile path:
    # Windows: C:/Users/USERNAME/AppData/Local/Google/Chrome/User Data
    # Mac: /Users/USERNAME/Library/Application Support/Google/Chrome
    # Linux: /home/USERNAME/.config/google-chrome

    CHROME_PROFILE = None  # Set to your Chrome profile path
    PROXY = None  # Set to "ip:port" for residential proxy

    print("💡 RECOMMENDED ENHANCEMENTS:")
    if not CHROME_PROFILE:
        print("❌ Chrome Profile: Not configured")
        print("   └─ Add your Chrome profile path for maximum stealth")
    else:
        print(f"✅ Chrome Profile: {CHROME_PROFILE}")

    if not PROXY:
        print("❌ Residential Proxy: Not configured")
        print("   └─ Add residential proxy for IP-based evasion")
    else:
        print(f"✅ Residential Proxy: {PROXY}")

    print()

    try:
        with UltimateCloudflareBypass(
        ) as bypass:

            success = bypass.test_ultimate_bypass()

            if success:
                print("\n🎉 ULTIMATE BYPASS SUCCESSFUL!")
                print("✅ Anna's Archive accessible")
                print("✅ Ready for downloading")
            else:
                print("\n⚠️ BYPASS PARTIALLY SUCCESSFUL")
                print("Challenge detected but may be resolvable")

            input("\n⏸️ Press Enter to close browser...")

    except Exception as e:
        print(f"\n💥 Ultimate bypass failed: {e}")
        print("\n🛠️ NEXT STEPS:")
        print("1. 🏠 Configure Chrome profile path")
        print("2. 🌐 Get residential proxy service")
        print("3. 🔄 Update Chrome to latest version")
        print("4. 🧹 Clear all Chrome data and restart")