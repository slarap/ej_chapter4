from ex5_class_terminal import Terminal, Mobile
t1 = Terminal("666112233")
t2 = Terminal("666744459") 
t3 = Terminal("632128919")
t4 = Terminal("664135818")
print(t1)
print(t2)
t1.call(t2, 420)
t1.call(t3, 210)
print(t1)
print(t2)
print(t3)
print(t4)

m1 = Mobile("666112233", "rat")
m2 = Mobile("666744459", "monkey")
m3 = Mobile("632128919", "elephant")
print(m1)
print(m2)
m1.call(m2, 210)
m1.call(m3, 320)
m2.call(m3, 450)
print(m1)
print(m2)
print(m3)



