const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  await page.goto('file:///Users/vasylkolos/Downloads/Oleksandr Halushkaeweb/auto/index.html', { waitUntil: 'load' });
  
  const attrCount = await page.evaluate(() => document.querySelectorAll('[data-modal]').length);
  console.log('Modal triggers found:', attrCount);
  
  await page.click('h4:has-text("Reifenwechsel")');
  await page.waitForTimeout(500);
  const isVisible = await page.isVisible('.ag-modal-overlay.active');
  console.log('Modal visible after click:', isVisible);
  await browser.close();
})();
