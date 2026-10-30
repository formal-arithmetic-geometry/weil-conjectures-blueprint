+++
id = "sk-lem-wweil-integer-rationality"
kind = "lemma"
title = "Reduced fractions with integer coefficients"
order = 796
lean = ["PowerSeries.existsUnique_isNormalizedIntegralFraction"]
uses = ["sk-prop-criterion", "sk-cor-tf-point-counting"]
tags = ["sketch"]
+++
If $C(T)\in1+T\mathbf Z[[T]]$ is rational over $\mathbf Q$, then
there are unique coprime $A,B\in\mathbf Z[T]$ such that

$$
C(T)=A(T)/B(T),\qquad A(0)=B(0)=1.
$$

*Complement.* The same holds for every $X_0$ of finite type over
$\mathbf F_q$, separated or not: there are $A,B\in\mathbf Z[T]$ with
$B(0)=1$ and $B(T)Z(X_0,T)=A(T)$, and
$Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}$.
