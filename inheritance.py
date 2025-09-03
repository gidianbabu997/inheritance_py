
# # # class babu():
# # #     print(a+b)
# # # babu(2,3)    
# # # single inheritance its is knowns as the inheritance from parent ot child 
# # class parent():
# #     def output(self):
# #         print("iam the parent")
# # class child(parent):
# #     def output1(self):
# #         print("iam the child")
# # a=child()
# # a.output1()   
# # a.output()    

# #multi level inheritance  its means p1 to p2 to child inheritance the property
# class garndfather():
#     def output(self):
#         print("iam the grandfather")
# class father(garndfather):
#     def output1(self):
#         print("iam the parent")
# class child(father):
#     def output2(self):
#         print("iam the child")
# a=child()
# a.output1() 
# a.output2()  
# a.output() 


# #mutli level inheritance its is know as mutliple parents and single child then it called as mutli level inheritance
# class father():
#     def output(self):
#         print("iam the father")
# class mother():
#     def output1(self):
#         print("iam the mother")
# class child(father,mother):
#     def output2(self):
#         print("iam the child")
# a=child()
# a.output1() 
# a.output2()  
# a.output() 

# heirachial inheritance
class parent():
    def output(self):
        print("iam the parent")
class child1(parent):
    def output1(self):
        print("iam the child1")
class child2(parent):
    def output2(self):
        print("iam the child2")
a=child1()
a.output1()
a=child2()
# a.output1() 
a.output2()  
a.output() 








