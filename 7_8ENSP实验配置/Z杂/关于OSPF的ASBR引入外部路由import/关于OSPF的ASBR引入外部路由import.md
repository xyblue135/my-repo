![image-20247254338948.png|425](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/Z%E6%9D%82/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/image-20247254338948.png)
```
import-route static cost 10 #修改默认外部路由开销1为10
```
外乡人，优先级比较低，150
![image-20247254455882.png|375](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/Z%E6%9D%82/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/image-20247254455882.png)
查看5类LSA
![image-20247254710243.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/Z%E6%9D%82/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/image-20247254710243.png)
![image-20247254731778.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/Z%E6%9D%82/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/image-20247254731778.png)
# 修改开销度量值
![image-2024725925944.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/Z%E6%9D%82/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/%E5%85%B3%E4%BA%8EOSPF%E7%9A%84ASBR%E5%BC%95%E5%85%A5%E5%A4%96%E9%83%A8%E8%B7%AF%E7%94%B1import/image-2024725925944.png)
1. **计算方式**:

    - **E1 (Metric-Type-1)**: 外部路径成本 + 内部路径成本
    - **E2 (Metric-Type-2)**: 只有外部路径成本
2. **泛洪范围**:
    
    - **E1 (Metric-Type-1)**: 在整个AS内泛洪
    - **E2 (Metric-Type-2)**: 同样在整个AS内泛洪，但其度量值计算不同
3. **对内部路径的影响**:
    
    - **E1 (Metric-Type-1)**: 考虑内部路径的成本，因此可能会选择更长但带宽更高的路径。
    - **E2 (Metric-Type-2)**: 不考虑内部路径的成本，可能会导致选择最短但不一定是最优的路径。