1. 进main（）函数
2. 添加一个super类
3. 打开json文件
4. 进datas_process（）函数
	1） 如果datas是list类别，就调递归
	2） 如果datas是dict类别，先创建individual，然后再创建individual和individual的objectproperty
	3） for 这个datas
		<1> 如果datas的value是dict的话，add_class, add_objectproperty，然后递归
		<2> 如果datas的value是list的话，add_class, add_objectproperty，然后递归
		<3> 如果datas的value是str或者是true或false的话，add_dataproperty，add_data_value
		<4> 如果datas的value是int的话，add_dataproperty,add_data_value
		<5> 如果datas的value是float的话，add_dataproperty，add_data_value
	4） 如果datas是 str或者list类 pass

5. 每次调add_XXX(), 都直接存储到rdf文件