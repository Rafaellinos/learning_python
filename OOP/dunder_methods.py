class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {
            'name': 'yoyo',
            'that': False
        }
    # modifing dunder method str()

    #ALL dunder methods
    def __str__(self):
        """
            usually return the object in string format
        """
        return f"{self.color}"

    def __len__(self):
        """
            usually return the lenght of the object, like a list
        """
        return 5
    
    def __del__(self):
        """
            del variable deletes a variable content
        """
        return ('deleted!')

    def __getitem__(self, i):
        """
            this method is reponsible for get the dict item => dict_example['key']
        """
        return self.dict[i]

    def __call__(self):
        """
            same as calling a method by using parenteses object()
        """
        return "YESS?"
    


action_figure = Toy('red', 0)
print(action_figure.__str__()) # same output as print(str(action_figure)) 
print(len(action_figure))

# output without modified __str__ method : <__main__.Toy object at 0x7f9d48457490>
# output with modified __str__ : red

print(action_figure()) # method __call__ overwrited
print(action_figure['name']) # method getitem overwrited / action_figure.dict['name']
del action_figure # Delete the variable, can cause some bugs