import re

def test_pincode_logic():
    with open(r'c:\Users\moham\Downloads\blackroots website\assets\theme.js', 'r', encoding='utf-8') as f:
        js = f.read()

    with open(r'c:\Users\moham\Downloads\blackroots website\index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Check 1: HomePincodeResult is hidden by default in HTML
    assert 'id="HomePincodeResult" class="hidden' in html, "FAIL: HomePincodeResult must be hidden by default!"
    print("[PASS] HomePincodeResult is hidden by default in HTML markup.")

    # Check 2: ResultPincodeNum has NO hardcoded text in initial HTML
    assert '<span id="ResultPincodeNum" class="text-white font-black text-base underline decoration-amber-400"></span>' in html, "FAIL: ResultPincodeNum must be empty in initial HTML!"
    print("[PASS] ResultPincodeNum is clean and empty in initial HTML markup.")

    # Check 3: window.executePincodeCheck is present in theme.js
    assert 'window.executePincodeCheck' in js, "FAIL: window.executePincodeCheck missing in theme.js"
    print("[PASS] window.executePincodeCheck present in theme.js.")

    # Check 4: Inline HTML event attributes present
    assert 'oninput="window.executePincodeCheck(false)"' in html, "FAIL: oninput missing in index.html"
    assert 'onclick="window.executePincodeCheck(true)"' in html, "FAIL: onclick missing in index.html"
    print("[PASS] Native inline HTML event handlers (oninput & onclick) present in index.html.")

    print("=== AUTOMATED PINCODE VERIFICATION TEST PASSED 100% ===")

if __name__ == '__main__':
    test_pincode_logic()
