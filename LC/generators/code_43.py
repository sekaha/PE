class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # So I think this just wants me to convert via "paper multiplication"
        # Can make a table
        # Every product goes to (carry, new_num)
        # Need to implement row addition

        # These could be swapped for a table of precomputed values with no integer
        # manipulation whatsoever so I'm counting i
        sums, prods = {}, {}

        for n1 in range(10):
            for n2 in range(n1, 10):
                # sum
                s_carry = str((n1 + n2) // 10)
                s_digit = str((n1 + n2) % 10)
                sums[(str(n1), str(n2))] = (s_carry, s_digit)

                # prod
                p_carry = str((n1 * n2) // 10)
                p_digit = str((n1 * n2) % 10)
                prods[(str(n1), str(n2))] = (p_carry, p_digit)

        def add(num1, num2):
            # base cases
            if num1 == "0":
                return num2

            if num2 == "0":
                return num1

            res = ""
            carry = "0"

            if len(num1) > len(num2):
                num1, num2 = num2, num1

            for i in range(1, len(num1) + 1):
                n1, n2 = min(num1[-i], num2[-i]), max(num1[-i], num2[-i])
                new_carry, digit = sums[(n1, n2)]
                res = add(carry, digit) + res
                carry = new_carry

            # handle remainder
            for i in range(len(num1) + 1, len(num2) + 1):
                digit = num2[-i]
                res = add(carry, digit) + res
                carry = "0"

            if carry == "1":
                res = "1" + res

            return res

        # Long divison algorithm implementation
        res = "0"

        for offset, bot_dig in enumerate(reversed(num2)):
            row = "0" * offset
            carry = "0"

            # process row
            for top_dig in reversed(num1):
                new_carry, digit = prods[(min(top_dig, bot_dig), max(top_dig, bot_dig))]
                new_sum = add(digit, carry)

                if len(new_sum) == 2:
                    new_carry = add(new_carry, new_sum[-2])
                    new_sum = new_sum[-1]

                row = new_sum + row
                carry = new_carry

            if carry != "0":
                row = carry + row

            print(
                "b",
                row,
                res,
                "=",
                add(row, res),
                add(row, res) == str(int(row) + int(res)),
            )
            res = add(row, res)

        return res


S = Solution()
S.multiply()
