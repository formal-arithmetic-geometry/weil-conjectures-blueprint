+++
id = "lem-weil-pbc-finitely-generated-field-complete-intersection-model"
kind = "lemma"
title = "A finitely generated field is the fraction field of a quotient of a polynomial ring by a regular sequence, with n - c = trdeg"
uses = ["def-weil-field"]
lean = ["FieldTheory.exists_completeIntersection_fractionField_model"]
order = 1900
+++
Let $k$ be a field [def-weil-field] and $K/k$ a field extension which is finitely generated: $K=k(b_1,\dots,b_m)$ for finitely many $b_1,\dots,b_m\in K$. Let $x_1,\dots,x_d\in K$ ($d\ge0$) be a finite transcendence basis of $K/k$. Then there are integers $n\ge c\ge0$ with $n-c=d$, polynomials $f_1,\dots,f_c\in k[X_1,\dots,X_n]$ which form a regular sequence in the ring $k[X_1,\dots,X_n]$, and a homomorphism of $k$-algebras $\iota:A\to K$, where $A=k[X_1,\dots,X_n]/(f_1,\dots,f_c)$, such that (a) $\iota$ is injective, and (b) every element of $K$ equals $\iota(a)\,\iota(s)^{-1}$ for some $a,s\in A$ with $s\neq0$. In particular $A$ is an integral domain, and $\iota$ induces an isomorphism of $k$-algebras $S^{-1}A\xrightarrow{\sim}K$, $a/s\mapsto\iota(a)\iota(s)^{-1}$, where $S=A\setminus\{0\}$ and $S^{-1}A$ is the ring of fractions of $A$ with respect to $S$.
