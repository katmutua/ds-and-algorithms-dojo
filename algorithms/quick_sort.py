class QuickSort:

    def __init__(self, list_a):
        self.list_a = list_a

    def sort_values(self):
        return 'nothing yet'

    def pivot_element(self):
        return self.list_a[self.list_length() - 1]

    def list_length(self):
        return len(self.list_a)

    def lower_array(self):
        if not self.list_a:
            print RuntimeError("Cannot sort an empty list")

        elif self.list_length() == 1:
            return self.list_a
        else:
            lower_list = [i for i in self.list_a if i<= self.pivot_element()]
            return lower_list

    def upper_array(self):
        upper_list = [i for i in self.list_a if i not in self.lower_array()]
        return upper_list


quick_sort = QuickSort([2,4,5,3,1,9,4,5,10])
quick_sort.sort_values()
