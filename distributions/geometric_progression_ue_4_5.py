import time
import numpy as np
import matplotlib.pyplot as plt


def pdf(x: int) -> float:
    return (1 / 2) / (2 ** x)


def print_pdf_all(x: int) -> None:
    """print the first x values of the geometric distribution"""
    for i in range(x):
        print(f'P(X = {i}) = {pdf(i)}')


def print_cdf_all(x: int) -> None:
    """print the first x cumulative values of the geometric distribution"""
    value_cdf = None
    for i in range(x):
        value_cdf = pdf(i) if value_cdf is None else value_cdf + pdf(i)
        print(f'F(X <= {i}) = {value_cdf}')


def print_pdf(x: int) -> None:
    """print the x-th value of the geometric distribution"""
    print(f'P(X = {x}) = {pdf(x)}')


def print_cdf(x: int) -> None:
    """print the x-th cumulative value of the geometric distribution"""
    value_cdf = 0
    for i in range(x + 1):
        value_cdf += pdf(i)
    print(f'F(X <= {x}) = {value_cdf}')


if __name__ == '__main__':
    for _ in range(10):
        print_pdf(_)
        print_cdf(_)
        print(f"\n")
        time.sleep(2)
