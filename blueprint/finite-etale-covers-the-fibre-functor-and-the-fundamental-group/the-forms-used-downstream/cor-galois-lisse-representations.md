+++
id = "cor-galois-lisse-representations"
kind = "theorem"
title = "Lisse sheaves and continuous representations"
order = 3036
lean = ["AlgebraicGeometry.lisseEquivContinuousRep"]
tags = ["latex:corollary"]
uses = ["thm-galois-fundamental", "thm-galois-lc-etale", "def-galois-fibre-functor"]
+++
Let $Y$ be connected with geometric point $\bar y$, and let $\Lambda$ be a
finite ring. Then evaluation at $\bar y$ is an equivalence between locally
constant sheaves of finite $\Lambda$-modules on $Y_{\Et}$ and continuous
$\Lambda$-linear representations of $\pi_1(Y,\bar y)$ on finite
$\Lambda$-modules. For $\Lambda=\overline{\mathbf Q}_\ell$ the same holds
for lisse $\overline{\mathbf Q}_\ell$-sheaves with finite stalks, by the
coefficient conventions for constructible complexes.

## Proof

Here $\pi_1=\pi_1(Y,\bar y)=\operatorname{Aut}(F_{\bar y})$ is the group of
[def-galois-fibre-functor]. A locally constant sheaf of finite
$\Lambda$-modules is, by [thm-galois-lc-etale] applied to the underlying
sheaf of sets together with the module structure, a finite etale cover with
a $\Lambda$-linear action of its automorphism group; by
[thm-galois-fundamental] such objects correspond to finite continuous
$\pi_1$-sets with $\Lambda$-linear action, i.e. to continuous
representations on finite $\Lambda$-modules. The
$\overline{\mathbf Q}_\ell$-statement follows by writing a lisse sheaf with
finite stalks as a filtered colimit of finite-level ones over the
coefficient stages.

Unresolved dependencies: def:weil-pbc-constructible-complexes
