+++
id = "def-weil-pbc-associated-graded-ring"
kind = "definition"
title = "Associated graded ring of an ideal"
lean = ["Ideal.associatedGraded", "Ideal.associatedGradedCommRing", "Ideal.associatedGradedRingHom", "Ideal.associatedGradedAlgebra"]
order = 1606
+++
Let $A$ be a commutative ring and $J\subseteq A$ an ideal; $J^0=A$ and $J^{k+1}=J^kJ$. For $n\ge0$ let $G_n=J^n/J^{n+1}$, the quotient of the $A$-module $J^n$ by its submodule $J^{n+1}$, whose elements are the classes $a\bmod J^{n+1}$, $a\in J^n$; so $G_0=A/J$ as an abelian group. The *associated graded ring* of $A$ with respect to $J$ is the abelian group $\operatorname{gr}_J(A)=\bigoplus_{n\ge0}G_n$, with canonical inclusions $\iota_n:G_n\to\operatorname{gr}_J(A)$; an element $\xi=(\xi_n)_n$ is the finite sum $\sum_n\iota_n(\xi_n)$, and $\xi_n$ is its *homogeneous component of degree $n$*. Its multiplication is $(\xi\eta)_k=\sum_{n+m=k}\mu_{n,m}(\xi_n,\eta_m)$, where $\mu_{n,m}:G_n\times G_m\to G_{n+m}$ is the biadditive map $(a\bmod J^{n+1},\,b\bmod J^{m+1})\mapsto ab\bmod J^{n+m+1}$ ($a\in J^n$, $b\in J^m$). With this multiplication and unit $1\bmod J$ in degree $0$, $\operatorname{gr}_J(A)$ is a commutative ring, and $\iota_0:A/J\to\operatorname{gr}_J(A)$ is an injective ring homomorphism; $\operatorname{gr}_J(A)$ is regarded as an $A/J$-algebra through $\iota_0$, so that $(a\bmod J)\cdot(x\bmod J^{n+1})=ax\bmod J^{n+1}$ for $a\in A$, $x\in J^n$.
