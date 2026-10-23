+++
id = "sk-d-relative-frob"
kind = "definition"
title = "The relative Frobenius factorization"
order = 3668
uses = ["sk-d-setup", "sk-d-weil"]
lean = ["AlgebraicGeometry.ProEtale.relativeFrobenius"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a morphism of schemes and let $\Phi_{X,m}:X\to X$,
$\Phi_{Y,m}:Y\to Y$ be endomorphisms with $\Phi_{Y,m}f=f\Phi_{X,m}$. The case of
interest is a map $f_0:X_0\to Y_0$ of
finite-type separated schemes over $\mathbf F_q$, with $f:X\to Y$ its geometric
base change and $\Phi_{X,m}$, $\Phi_{Y,m}$ the Frobenius maps. Put

$$
X'_m=Y\times_{\Phi_{Y,m},Y,f}X,
\quad p_m:X'_m\to X,\quad f'_m:X'_m\to Y,
\quad r_m=(f,\Phi_{X,m}):X\to X'_m.
$$

Then $p_mr_m=\Phi_{X,m}$ and $f'_mr_m=f$.
