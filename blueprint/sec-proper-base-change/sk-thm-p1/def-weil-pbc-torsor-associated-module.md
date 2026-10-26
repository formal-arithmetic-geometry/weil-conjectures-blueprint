+++
id = "def-weil-pbc-torsor-associated-module"
kind = "definition"
title = "Associated module functor of equivariant locally constant sections"
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.GaloisCover.associatedModuleFunctor", "AlgebraicGeometry.Scheme.GaloisCover.equivariantModulePresheafFunctor", "AlgebraicGeometry.Scheme.GaloisCover.equivariantModulePresheaf"]
order = 1643
+++
Let $V$ be a scheme [def-weil-pbc-scheme-conventions], $\ell\in\mathbb N$, $P$ a finite group and $c:Y\to V$ a Galois cover with group $P$ in the torsor form of [def-sbc-normal-dominant-galois]. Put $k=\mathbb Z/\ell\mathbb Z$. For a $k$-linear representation $(N,\rho_N)$ of $P$ and an etale object $W\to V$ [def-weil-pbc-etale-site], let $\mathcal T^{\mathrm{pre}}_c(N)(W)$ be the $k$-module of locally constant functions $s:W\times_V Y\to N$ satisfying $s(g y)=\rho_N(g)s(y)$ for $g\in P$. Restriction is precomposition with the induced map of fibre products, and $P$-equivariant $k$-linear maps $N\to N'$ act pointwise. The *associated module functor* $T_c$ sends $N$ to the sheafification of the presheaf of $k$-modules $W\mapsto\mathcal T^{\mathrm{pre}}_c(N)(W)$, a sheaf of $k$-modules on $V_{\Et}$ [def-weil-pbc-etale-sheaves].
