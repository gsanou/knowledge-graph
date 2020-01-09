1. 提取rdf_about的值
2. 查询所有的individuals
3. 进create_json函数
4. 先调query_individual_content（）
5. query_individual_content返回的结果是dataproperty的value和subindividuals
6. for value和subindividual，返回dict值
7. 把dict值写进json文件里