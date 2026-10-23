+++
id = "sk-def-frobmod"
kind = "definition"
title = "Frobenius modules and their trace series"
order = 3683
lean = ["LinearMap.traceSeries", "LinearMap.alternatingTraceSeries"]
tags = ["sketch"]
+++
A *Frobenius module* is a pair $(V,F)$ consisting of a
finite-dimensional $\Qlb$-vector space $V$ and a $\Qlb$-linear automorphism
$F:V\to V$. More generally, for a field $K$, a finite-dimensional $K$-vector
space $V$ and an arbitrary $K$-linear endomorphism $F:V\to V$, the
*trace series* and *determinant* of $(V,F)$ are

$$
\operatorname{tr}_F(T)=\sum_{n\ge1}\Tr(F^{n}\mid V)\frac{T^{n}}{n}\in K[[T]],
\qquad
P_{(V,F)}(T)=\det(1-TF\mid V).
$$

For a finite set $I\subset\Z$ and a family $(V_i,F_i)_{i\in I}$ of such pairs, the
*alternating trace series* is
$\operatorname{str}_F(T)=\sum_{i\in I}(-1)^{i}\operatorname{tr}_{F_i}(T)=\sum_{n\ge1}\bigl(\sum_{i\in I}(-1)^{i} \Tr(F_i^{n}\mid V_i)\bigr)\frac{T^{n}}{n}$.
No semisimplicity of $F$ is assumed anywhere.
