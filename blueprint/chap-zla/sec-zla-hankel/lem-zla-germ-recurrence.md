+++
id = "lem-zla-germ-recurrence"
kind = "lemma"
title = "A rational germ supplies a recurrence"
order = 1000
uses = ["def-zla-eventual-recurrence", "def-zla-rational-germ"]
+++
Let $f(T)=\sum_{n\geq0}a_nT^n$ be the Taylor series of the normalized rational
germ $A(T)/B(T)$, where $B(T)=1+c_1T+\cdots+c_dT^d$. Then

$$
a_n+c_1a_{n-1}+\cdots+c_da_{n-d}=0
$$

whenever $n>\deg A$ and $n\geq d$. In particular $(c_1,\ldots,c_d;\deg A+1)$
is an eventual recurrence of order $d$ for $a$.

## Proof

Read off the coefficient of $T^n$ in the identity $B(T)f(T)=A(T)$: the
left-hand side contributes $\sum_{k=0}^{d}c_ka_{n-k}$ with $c_0=1$, and the
right-hand side contributes $0$ once $n>\deg A$.
