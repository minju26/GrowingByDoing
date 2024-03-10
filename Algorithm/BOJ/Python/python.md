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

### 함수

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