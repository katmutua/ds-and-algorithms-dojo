class QuickSort:

    def __init__(self, list_a):
        self.list_a = list_a

    def sort_values(self):
       if self.check_for_empty_list():
            return RuntimeError('cannot sort an empty list bruh!')
       elif self.check_for_single_item():
           return self.list_a

    def pivot_element(self):
        return self.list_a[self.list_length() - 1]

    def lower_array(self):
        if self.list_a:
            lower_list = [i for i in self.list_a if i <= self.pivot_element()]
            return lower_list
        else:
            print 'cannot sort an empty list'

    def upper_array(self,):
        upper_list = [i for i in self.list_a if i not in self.lower_array()]
        return upper_list

    def list_length(self):
        return len(self.list_a)

    def check_for_empty_list(self):
        return not self.list_a

    def check_for_single_item(self):
        return self.list_length() == 1



quick_sort = QuickSort([2,4,5,3,34,88,99,5,10])
quick_sort.sort_values()

