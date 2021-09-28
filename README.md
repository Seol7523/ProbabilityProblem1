# ProbabilityProblem1

## Question

처음 제시된 문제

```
1부터 20까지의 숫자중 1개를 뽑아 그 숫자가 내가 베팅한 숫자이면 돈을 받는다.
이때 1부터 20까지의 숫자에 원하는 만큼 베팅할수있다고 하면 가장 효율적인 방법은 무엇인가?
```


다듬은 문제
```
1부터 20까지의 숫자에 돈을 거는 도박이 있다. 여러 숫자에 동시에 돈을 걸수있으며 한 숫자에 거는 돈은 x원으로 모두 같다고 하자.
만약 1부터 20까지의 숫자중 렌덤으로 뽑힌 숫자가 내가 베팅한 숫자중 1가지라면 y원을 상금으로 받는다.
이때 최대한 이익을 남기려면 몇개의 숫자에 베팅하는것이 옳을까?
```

## Result

Cost : 숫자 하나에 베팅할때 소비되는 비용

Profit : 숫자를 맞추었을때 받는 돈

### **Case 1. Cost:1,profit:1 일 경우**

10번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%201%2010times.png)

100번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%201%20100times.png)

1000번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%201%201000times.png)


### **Case 2. Cost:1,profit:10 일 경우**

10번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2010%2010times.png)

100번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2010%20100times.png)

1000번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2010%201000times.png)


### **Case 3. Cost:1,profit:20 일 경우**

10번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2020%2010times.png)

100번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2020%20100times.png)

1000번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2020%201000times.png)


### **Case 4. Cost:1,profit:30 일 경우**

10번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2030%2010times.png)

100번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2030%20100times.png)

1000번 시행시
![](https://github.com/Seol7523/ProbabilityProblem1/blob/main/Result/1%2030%201000times.png)


### **Summary**

모든 숫자에 베팅할때 들어가는 Cost와 Profit의 크기를 비교할때

**Cost > Profit** : 최대한 적은 숫자에 베팅하는 것이 유일하게 돈을 지키는 길

**Cost = Profit** : 큰 차이는 없어보임. 그러나 8개~12개 구간의 진폭이 큼. 이 구간을 피해서 베팅할시 돈을 잃지는 않을 확률은 매우 적음

**Cost < Profit** : 무조건 18개~20개 숫자에 베팅. 확률상 무조건 결국은 돈을 벌게됨

역시 한군데에만 돈을 걸게하는 이유가 있음






Research by S.C.H

~~*도박하지 맙시다*~~
