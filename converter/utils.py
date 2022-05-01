class Converter:
    bellow_twenty = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    bellow_hundred = [
        "",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    def integer_to_english(self, num):
        if num == 0:
            return "zero"
        return self.helper(num)

    def helper(self, num):
        num_in_english = ""
        if num < 20:
            num_in_english = self.bellow_twenty[num]
        elif num < 100:
            num_in_english = (
                self.bellow_hundred[num // 10] + " " + self.helper(num % 10)
            )
        elif num < 1000:
            num_in_english = (
                self.helper(num // 100) + " " + "hundred" + " " + self.helper(num % 100)
            )
        elif num < 1000_000:
            num_in_english = (
                self.helper(num // 1000)
                + " "
                + "thousand"
                + " "
                + self.helper(num % 1000)
            )
        elif num < 1000_000_000:
            num_in_english = (
                self.helper(num // 1000_000)
                + " "
                + "million"
                + " "
                + self.helper(num % 1000_000)
            )
        elif num < 1000_000_000_000:
            num_in_english = (
                self.helper(num // 1000_000_000)
                + " "
                + "billion"
                + " "
                + self.helper(num % 1000_000_000)
            )
        elif num >= 1000_000_000_000:
            num_in_english = (
                "Sorry... Cannot convert a number greater than 999999999999"
            )
        return num_in_english.strip()
