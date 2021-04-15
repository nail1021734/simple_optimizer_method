# readme

請執行main.py即可得到計算結果，如要更改初始位置等參數請修改main.py內Q1,Q2,Q3 function內goldSearch、Dichotomous、cyclic或powell方法的參數

## goldSearch function

func：要最佳化的函數
a: lower bound
b: upper bound
tol: tolerance

## Dichotomous function

func：要最佳化的函數
a: lower bound
b: upper bound
ep: epilson
tol: tolerance

## cyclic funciton

func：要最佳化的函數
init_X: 初始點
x_bound_list: 每個變數的bound
tol: tolerance

## powell function

func：要最佳化的函數
init_X: 初始點
min_b: lower bound
max_b: upper bound
tol: tolerance