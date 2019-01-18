class Amazon:
    def __init__(self, driver):
        self.driver = driver

    def _get_cart_item(self, book):
        print("Get cart item: {0}".format(book))
        book_found = False
        # find all items in cart and iterate to find one with name <book>.
        # Xpath is used to get first level children from element
        all_books = self.driver.find_element_by_class_name("sc-list-body").find_elements_by_xpath("./*")
        for bookFromCart in all_books:
            if book in bookFromCart.find_element_by_class_name("sc-product-title").text:
                book_found = True
                return bookFromCart
        if not book_found:
            raise Exception("Book not found")

    def go_to(self, link):
        print("Go to: {0}".format(link))
        self.driver.get(link)

    def sign_in(self, username, password):
        print("Sign in with username, password: {0}, {1}".format(username, password))
        dropDown = self.driver.find_element_by_id("nav-link-accountList").click()
        email = self.driver.find_element_by_id("ap_email").send_keys(username)
        password = self.driver.find_element_by_id("ap_password").send_keys(password)
        singIn = self.driver.find_element_by_id("signInSubmit").click()
        # missing check to see if sign in is succeeded
        print("User signed in")

    def add_to_cart_paperback(self, books):
        print("Debug: select paperback")
        if isinstance(books, str):
            books = [books]
        for book in books:
            # insert search value
            txtSearch = self.driver.find_element_by_id("twotabsearchtextbox")
            txtSearch.send_keys(book)
            # invoke search button
            btnSearch= self.driver.find_element_by_class_name("nav-search-submit").find_element_by_tag_name("input")
            btnSearch.click()
            # click on book that is searched. Missing exception handling when book is not found
            foundBook = self.driver.find_element_by_class_name("a-text-normal")
            foundBook.click()
            # click on paperback
            self._click_paperback()
            # click on add to chart
            addToChart = self.driver.find_element_by_id("add-to-cart-button")
            addToChart.click()
            print("Book: {0} added to chart.".format(book))

    def _click_paperback(self):
        # paperback element is not the same element for all books that are added. if exception happen, try second way
        try:
            self.driver.find_element_by_id("mediaTab_heading_1").click()
        except:
            findPaperback = self.driver.find_element_by_class_name("swatchElement").find_elements_by_tag_name("span")
            for paperback in findPaperback:
                if paperback.text == "Paperback":
                    paperback.click()
                    break

    def save_for_later(self, book):
        print("Set book: {0} to 'save for later'".format(book))
        book = self._get_cart_item(book)
        book.find_element_by_class_name("sc-action-save-for-later").click()
        print("Book 'saved for later'")

    def delete_from_cart(self, book):
        print("Delete book: {0} from cart".format(book))
        book = self._get_cart_item(book)
        book.find_element_by_class_name("sc-action-delete").click()

    def gift(self, book):
        print("Set book: {0} as gift".format(book))
        book = self._get_cart_item(book)
        # check checkbox for gift
        checkbox = book.find_element_by_class_name("sc-gift-option").find_element_by_tag_name("input")
        checkbox.click()
        print("Book is now gift")

    def change_quantity(self, book_name, quantity):
        print("Change quantity of book: {0} to value: {1}".format(book_name, quantity))
        # Missing check if quantity value is allowed
        if not isinstance(quantity, str):
            quantity = str(quantity)
        book = self._get_cart_item(book_name)
        # expand quantity
        quantity_dropdown = book.find_element_by_class_name("a-dropdown-container")
        quantity_dropdown.click()
        # select desired quantity
        qantity_values = self.driver.find_element_by_class_name("a-popover-wrapper").find_elements_by_tag_name("a")
        for q in qantity_values:
            if quantity in q.text:
                q.click()

    def open_cart(self):
        print("Open cart")
        self.driver.find_element_by_id("nav-cart").click()
        print("Cart opened")
