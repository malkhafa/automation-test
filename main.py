from wrapper import *

choptions = ["--no-sandbox", "--disable-gpu", "--window-size=1420,1080"]
brswer = Brwser(choptions)
def login():
    brswer.go_to("https://qa-portfolio-vanguard.cicada.digital.ge.com/")
    print(" Login")
    brswer.go_sleep(10)
    brswer.send_text("502799960", "//*[@id='username']")
    brswer.send_text("Aut0m@ti0n", "//*[@id='password']")
    brswer.send_click('//*[@id="submitFrm"]',"",15,'Submit username and password to Login')


def verify_elements():
# Verify cards on the Product Onboarding view:

    #Products Onboarded
    card1 = brswer.check_exists_by_xpath("//adoption-view//div[2]/div//card[1]")
    #PRODUCTS READY TO ONBOARD
    card2 = brswer.check_exists_by_xpath("//adoption-view//div[2]/div//card[2]")
    #ONBOARDED OF RTO
    card3 = brswer.check_exists_by_xpath("//adoption-view//div[2]/div//card[3]")
    print("Products Onboarded, PRODUCTS READY TO ONBOARD, ONBOARDED OF RTO Cards exist")

# Verify Info-Icons exist on Products Onboarded cards
    tooltip1 = brswer.check_exists_by_xpath("//card[1]/mat-card/mat-card-content/div[2]/px-icon")
    tooltip2 = brswer.check_exists_by_xpath("//card[2]/mat-card/mat-card-content/div[2]/px-icon")
    tooltip3 = brswer.check_exists_by_xpath("//card[3]/mat-card/mat-card-content/div[2]/px-icon")
    print("(: Info-Icons(tooltips) exist on Products Onboarded cards :)")

# Verify column-headers exist on the table (secure-pipeline-data-table)
    column1 = brswer.check_exists_by_xpath("//mat-table/mat-header-row/mat-header-cell[1]")
    column2 = brswer.check_exists_by_xpath("//mat-table/mat-header-row/mat-header-cell[2]")
    column3 = brswer.check_exists_by_xpath("//mat-table/mat-header-row/mat-header-cell[3]")
    column3 = brswer.check_exists_by_xpath("//mat-table/mat-header-row/mat-header-cell[4]")
    print("column-headers exist on the table (business level)")

# Verify percent Onboard display:
    percent_onboard = brswer.check_exists_by_xpath("//mat-table/mat-row[1]/mat-cell[4]/px-percent-circle")
    print("%Percent Onboard displayed!")

def get_no_of_products():
# Get the total numbers of products on the cards
    #Onboarded
    no_products_onboarded= int(brswer.text('//adoption-view//div/card[1]/mat-card/mat-card-content/span') or '0')
    print("Number of products Onboarded is:", no_products_onboarded)
    #Ready To Onboard
    no_products_readyToOnboard= int(brswer.text('//adoption-view//div/card[2]/mat-card/mat-card-content/span') or '0')
    print("Number of products Ready To Onboard is:", no_products_readyToOnboard)
    #Onboarded
    no_products_onboarded_Of_RTO= int(brswer.text('//adoption-view//div/card[3]/mat-card/mat-card-content/span').split('%')[0] or '0')
    print("Percentage of products ONBOARDED OF RTO:", no_products_onboarded_Of_RTO)

def nav_product_level():
    brswer.send_click('//adoption-view//mat-table/mat-row[1]/mat-cell[1]','','','Clicking on the first business on the table to navigate to product level')
    brswer.go_sleep(3)
    #Verify all table headers exists
    product = brswer.check_exists_by_xpath("//mat-header-row/mat-header-cell[1]")
    Onb_class = brswer.check_exists_by_xpath("//mat-header-row/mat-header-cell[2]")
    Onb_status = brswer.check_exists_by_xpath("//mat-header-row/mat-header-cell[3]")
    Onb_time = brswer.check_exists_by_xpath("//mat-header-row/mat-header-cell[4]")
    print("column-headers exist on the table (products level)")

    #Verify Cards exists on the products level
    prod_onboarded = brswer.check_exists_by_xpath("//product-view//card[1]")
    prod_rto = brswer.check_exists_by_xpath("//product-view//card[2]")
    onboarded_of_rto = brswer.check_exists_by_xpath("//product-view//card[3]")
    average_onboarding_time = brswer.check_exists_by_xpath("//product-view//card[4]")
    print("All Cards exist on the table (products level)")








login()
verify_elements()
get_no_of_products()
nav_product_level()
