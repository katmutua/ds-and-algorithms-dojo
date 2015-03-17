class QuickSort:

    def __init__(self, list_a):
        self.list_a = list_a

    def list_length(self):
        return len(self.list_a)

    def lower_array(self):
        if not self.list_a:
            print RuntimeError("Cannot sort an empty list")

        elif self.list_length() == 1:
            return self.list_a
        else:
            return self.list_a[:self.list_length()/2]

    def upper_array(self):
        return self.list_a[self.list_length()/2:]


quick_sort = QuickSort([2,4,5,3,1,9,4,5,10])
quick_sort.sort_values()
