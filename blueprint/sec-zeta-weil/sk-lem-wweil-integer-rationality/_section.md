+++
id = "sk-lem-wweil-integer-rationality"
kind = "lemma"
title = "The integral reduced fraction"
lean = ["PowerSeries.existsUnique_isNormalizedIntegralFraction"]
order = 4115
uses = ["sk-prop-criterion", "sk-cor-tf-point-counting"]
tags = ["sketch"]
+++
If $C(T)\in1+T\mathbf Z[[T]]$ is rational over $\mathbf Q$, then
there are unique coprime $A,B\in\mathbf Z[T]$ such that

$$
 C(T)=A(T)/B(T),\qquad A(0)=B(0)=1.
$$

*The zeta function.* By [sk-cor-tf-point-counting],
$Z(X_0,T)\in\mathbf Q(T)\cap(1+T\mathbf Z[[T]])$ for every
separated $X_0$ of finite type over $\mathbf F_q$. (Alternatively,
rationality over $\mathbf Q$ follows from the cohomological expression
over $\mathbf Q_\ell$ by [sk-prop-criterion].) Hence the lemma
applies, and we call the resulting fraction $A/B$ the *normalized integral
reduced fraction* of the zeta function.

*Complement.* The same holds for every $X_0$ of finite type over
$\mathbf F_q$, separated or not: there are $A,B\in\mathbf Z[T]$ with
$B(0)=1$ and $B(T)Z(X_0,T)=A(T)$, and
$Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}$.
