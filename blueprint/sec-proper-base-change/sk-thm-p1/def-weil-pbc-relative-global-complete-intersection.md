+++
id = "def-weil-pbc-relative-global-complete-intersection"
kind = "definition"
title = "Relative global complete intersection"
lean = ["Algebra.IsRelativeGlobalCompleteIntersectionPresentation", "Algebra.IsRelativeGlobalCompleteIntersection"]
order = 1656
+++
Let $R$ be a commutative ring, $n,c\ge0$ integers and $f_1,\dots,f_c\in R[x_1,\dots,x_n]$; let $T=R[x_1,\dots,x_n]/(f_1,\dots,f_c)$, an $R$-algebra. One says that *the presentation $T=R[x_1,\dots,x_n]/(f_1,\dots,f_c)$ is a relative global complete intersection* (over $R$) if for every prime ideal $\mathfrak p\subset R$ whose fibre ring $T\otimes_R\kappa(\mathfrak p)$ is nonzero, $c\le n$ and the Krull dimension of the topological space $\operatorname{Spec}(T\otimes_R\kappa(\mathfrak p))$ equals $n-c$. A ring map $R\to S$ is a *relative global complete intersection* if there are such $n,c,f_1,\dots,f_c$ with this presentation a relative global complete intersection and an isomorphism of $R$-algebras $T\cong S$. If $c>n$ the condition says that every fibre ring is zero.
