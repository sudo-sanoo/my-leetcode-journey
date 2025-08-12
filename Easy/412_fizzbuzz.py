class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz_list = []

        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                i = "FizzBuzz"
                fizzbuzz_list.append(i)
            elif i % 5 == 0:
                i = "Buzz"
                fizzbuzz_list.append(i)
            elif i % 3 == 0:
                i = "Fizz"
                fizzbuzz_list.append(i)
            else:
                i = str(i)
                fizzbuzz_list.append(i)

        return fizzbuzz_list
