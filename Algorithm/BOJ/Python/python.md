# Python 입출력 및 함수 정리

### 입출력

```python
input("prompt msg")
```
- 매개변수로 prompt message를 받아, 입력 받기 전에 prompt message를 출력해야 한다.
- prompt message를 받지 않은 경우에도 속도 지연에 영향을 미친다.

```python
sys.stdin.readline()
```
- 문자열 타입으로 입력받는다.
- 정수/실수/리스트 등으로 사용하는 경우에는 따로 처리를 해줘야 한다.
- 개행문자 "\n"을 같이 입력받기 때문에 문자열 처리가 필요하다. (rstrip(), strip())

```python
print(*list)
```
- "a, b, c"와 같이 리스트의 원소들만 출력된다.
- print(list)의 경우 "[a, b, c]"가 출력된다.
### 함수와 표현

```python
split(sep, maxSplit)
```
- maxSplit 횟수 만큼 sep 구분자를 기준으로 문자열을 구분하여 list로 반환한다.
- sep 기본값은 none(띄어쓰기, 엔터)
- maxSplit 기본값은 -1(자를 수 있을 때 까지 문자열 전체를 자름)

```python
list.count(x)
```
- 리스트 내장함수, 매개변수 x가 리스트 내에 몇개가 있는지 반환한다.

```python
list.sort()
```
- 리스트 자체를 정렬하여 **원본 리스트가 변경**된다.

```python
newList = sorted(list)
```
- 기존의 list가 정렬된 새로운 newList가 반환되며 **원본 리스트가 변경되지 않**는다.

```python
items = [(a, b), (c, d), (e, f)]

# 튜플의 두번째 원소를 기준으로 오름차순 정렬
items.sort(key = lambda item: item[1])

# 튜플의 두번째 원소가 같다면 첫번째 원소를 기준으로 오름차순 정렬
items.sort(key = lambda item: (item[1], item[0]))

# 내림차순 정렬
items.sort(key = lambda item: item, reverse=True)

# 튜플의 두번째 원소를 기준으로 **내림차순** 정렬
items.sort(key = lambda item: item[1], resverse=True)
```
- lambda 표현식을 사용한 정렬

```pyton
enumerate(객체, start=0)
for i, value in enumerate(list)
```
- 주로 `for`문과 함께 사용되며, 순서가 있는 자료형(**list, tuple, set, dictionary, string**)에 대하여 **index와 value를 함께 반환**한다. 
- 중복되는 value가 있는 경우나 시간 시간복잡도 측면에서 `index(value)` 보다 용이함