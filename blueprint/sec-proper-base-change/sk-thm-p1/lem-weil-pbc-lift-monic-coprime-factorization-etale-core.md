+++
id = "lem-weil-pbc-lift-monic-coprime-factorization-etale-core"
kind = "lemma"
title = "Core étale lifting with one reduction"
lean = ["Polynomial.exists_etale_lift_monic_coprime_factorization_core"]
order = 1875
+++
Let $A$ be a commutative ring, $I\subseteq A$ an ideal, $f\in A[X]$ a monic polynomial, and $g_0,h_0\in(A/I)[X]$ monic and coprime (i.e. $ag_0+bh_0=1$ for some $a,b\in(A/I)[X]$) with $\bar f=g_0h_0$, where $\bar f$ is the image of $f$ in $(A/I)[X]$. Then there exist a ring map $\varphi:A\to A'$ such that $\operatorname{Spec}A'\to\operatorname{Spec}A$ is etale and the induced map $\alpha:A/I\to A'/IA'$ is bijective, and monic polynomials $g',h'\in A'[X]$ with $\varphi(f)=g'h'$ and such that the image of $g'$ in $(A'/IA')[X]$ is $\alpha(g_0)$ (coefficientwise).
