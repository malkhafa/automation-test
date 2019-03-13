def wait_for_url(url, driver):
    while driver.current_url == url:
        print("        Working on it")
    print("done")
def loop_until_found(xpath, driver):
    while True:
        x = find_displayed_element(driver.find_elements_by_xpath(xpath))
        if x != 1:
            return x
def find_displayed_element(elements):
    for element in elements:
        if element.is_displayed():
            return element
    return 1
