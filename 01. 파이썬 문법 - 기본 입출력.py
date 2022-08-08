#!/usr/bin/env python
# coding: utf-8

# # 실전에서 유용한 표준 라이브러리
# 
# itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공. 특히 순열과 조합 라이브러리 코테에서 자주 사용됨.
# 
# heapq: 힙(Heap) 자료구조를 제공함.
# 
# bisect: 이진 탐색(Binary Search) 기능을 제공함.
# 
# collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함함.
# 
# math: 필수적인 수학적 기능 제공.

# # 기본 입출력

# 모든 프로그램은 적절한 (약속된) 입출력 양식 갖고 있음.
# 
# 프로그램 동작은 첫 단계는 데이터를 입력 받거나 생성하는 것.

# ### 자주 사용되는 표준 입력 방법
# input() 함수는 한 줄의 문자열을 입력 받는 함수.
# 
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용.

# In[41]:


# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data, n)


# In[73]:


# 데이터의 개수 입력
n = input()
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(str, input().split()))

print(data, n)


# In[91]:


# 데이터의 개수 입력
n = input()
# 각 데이터를 ','을 기준으로 구분하여 입력
data = list(map(str, input().split(',')))

print(data, n)

# ','를 입력하지 않아서 구분되지 않음


# In[65]:


a, b = input().split()

print(a)


# In[66]:


a, b = input().split()

print(a + b)


# In[52]:


a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
 
print(a + b)


# ### 빠르게 입력 받기
# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있음.
# 
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용함.
# 
#  단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용함.
#  
# ** 한 두줄 입력받는 문제와 다르게, 반복문으로 여러 줄 입력 받아야 할 때 필요! input() 사용시 시간 초과 될 수 있음!

# In[67]:


import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)


# ### 자주 사용되는 표준 출력 방법
# 파이썬에서 기본 출력은 print() 함수를 이용합니다.
# 
# -> 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있습니다.
#     
# print()는 기본적으로 출력 이후에 줄 바꿈을 수행합니다.
# 
# -> 줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있습니다.
# 

# In[19]:


# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end = " ")
print(8, end = " ")

# 출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.")


# ### f-string 예제
# 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f'를 붙여 사용합니다.
# 
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있습니다.

# In[22]:


answer = 7
print(f"정답은 {answer}입니다.")


# ### 함수와 람다 표현식
# 
# 내장 함수: 파이썬이 기본적으로 제공하는 함수
# 
# 사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수
# 
# global 키워드를 변수로 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됨.

# In[79]:


a = 10

def func():
    a += 1
    print(a)
    
func()


# In[80]:


a = 10

def func():
    global a
    a += 1
    print(a)
    
func()


# In[82]:


array = [1,2,3,4,5]

def func():
    array.append(6)
    print(array)
    
func()


# In[84]:


array = [1,2,3,4,5]

def func():
    global array
    array.append(6)
    print(array)
    
func()


# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음.

# In[85]:


def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)


# 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있음.
# 
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징!

# In[86]:


def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))


# In[87]:


array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


# In[92]:


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))


# In[ ]:





# In[ ]:





# In[ ]:




