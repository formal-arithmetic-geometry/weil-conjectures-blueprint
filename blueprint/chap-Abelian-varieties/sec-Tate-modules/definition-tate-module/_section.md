+++
id = "definition-tate-module"
kind = "definition"
title = "Tate module"
order = 1508
lean = ["AlgebraicGeometry.IsAbelianVariety.tateModule", "AlgebraicGeometry.IsAbelianVariety.rationalTateModule"]
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative"]
+++
Let $A$ be an abelian variety over $k$ and let $\ell$ be a prime
invertible in $k$. The *Tate module* of $A$ is

$$
T_\ell A=\varprojlim_n A[\ell^n](\bar k),
$$

the limit taken along the maps $[\ell]:A[\ell^{n+1}](\bar k)\to
A[\ell^n](\bar k)$, and we put $V_\ell A=T_\ell A\otimes_{\mathbf Z_\ell}\mathbf Q_\ell$.
