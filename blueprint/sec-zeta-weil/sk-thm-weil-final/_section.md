+++
id = "sk-thm-weil-final"
kind = "theorem"
title = "The Weil conjectures for smooth proper schemes"
order = 4144
uses = ["sk-cor-tf-point-counting", "sk-thm-intfactors", "sk-cor-tf-functional-equation", "sk-cor-trace"]
lean = ["AlgebraicGeometry.Scheme.weil_conjectures"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$.
With $P_i$ and $b_i$ as in [sk-thm-intfactors]:

1. $Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$ is rational;
   each $P_i$ has integer coefficients and constant coefficient one.
1. Each reciprocal root $\alpha$ of $P_i$ satisfies
   $|\tau(\alpha)|=q^{i/2}$ for every complex embedding $\tau$.
1. $b_i=b_{2d-i}$, and these numbers are independent of $\ell$.
   If $X_0$ is geometrically connected, then
   $P_0=1-T$, $P_{2d}=1-q^dT$, and $b_0=b_{2d}=1$.
1. Put $\chi=\sum_i(-1)^ib_i$. Then $d\chi$ is even and there
   is $\varepsilon\in\{1,-1\}$ such that

$$
Z\!\left(X_0,\frac1{q^dT}\right)
 =\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
 \quad\hbox{in }\mathbf Q(T).
$$

*Complement.* The map $\alpha\mapsto q^d/\alpha$ carries the reciprocal roots
of $P_i$ bijectively, with multiplicities, onto those of $P_{2d-i}$.
