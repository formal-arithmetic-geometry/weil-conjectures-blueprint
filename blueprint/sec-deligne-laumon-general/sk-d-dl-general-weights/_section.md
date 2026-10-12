+++
id = "sk-d-dl-general-weights"
kind = "definition"
title = "Mixed upper bounds"
order = 3114
lean = ["AlgebraicGeometry.LAdicWeilSheaf.IsMixedOfWeightsAtMost", "AlgebraicGeometry.LAdicWeilComplex.IsMixedOfWeightsAtMost"]
uses = ["sk-d-dl-a1-setup"]
tags = ["sketch"]
+++
Retain $k_0=\mathbf F_q$, geometric Frobenius, and a field embedding
$\iota:\DLRQ\hookrightarrow\mathbf C$. Let $X_0$ be a $k_0$-scheme,
with the coefficient framework of Section [sec-six-functors]. A
constructible Weil sheaf $F$ on $X_0$ is *$\iota$-mixed of weights at most
$w$* if it has a finite filtration by Weil subsheaves
$0=G_0\subset G_1\subset\cdots\subset G_n=F$ whose successive quotients
$G_{i}/G_{i-1}$ are each punctually $\iota$-pure of some weight
$v_i\le w$. It is *$\iota$-mixed* if it is $\iota$-mixed of weights at
most $w$ for some $w$. A bounded constructible Weil complex $K$ is
*$\iota$-mixed of weights at most $w$* if $\mathcal H^bK$ is
$\iota$-mixed of weights at most $w+b$ for every $b\in\mathbf Z$.

Subobjects, quotients and extensions of Weil sheaves preserve the bound
"$\iota$-mixed of weights at most $w$": intersect a filtration, take its
images, or splice filtrations, respectively.
