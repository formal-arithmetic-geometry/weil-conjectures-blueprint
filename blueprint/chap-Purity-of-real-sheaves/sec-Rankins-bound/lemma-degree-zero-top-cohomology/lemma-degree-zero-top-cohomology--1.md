+++
id = "lemma-degree-zero-top-cohomology--1"
kind = "lemma"
title = "Global sections and geometric invariants"
name_showing = false
order = 1150001
aliases = ["bp-r353-1"]
lean = ["AlgebraicGeometry.WeilGroup.exists_globalSections_linearEquiv_invariants"]
uses = ["definition-lisse-sheaves", "definition-weil-structure", "definition-weil-representation"]
+++
Let $U_0/\Fq$ be a curve, let $\ell\ne\operatorname{char}\Fq$, and let
$\mathcal F$ be a lisse $\overline{\mathbf Q}_\ell$-Weil sheaf. Choose a
geometric base point, a lisse monodromy equivalence at that point, and
compatible Weil monodromy data. Write $(V,\rho)$ for the resulting
Weil fundamental representation. If $\gamma\in W(U_0)$ has degree one,
restriction to the base point gives a linear isomorphism

$$
f:\Gamma(U,\mathcal F)\xrightarrow{\sim}V^{\pi_1(U)},\qquad
f(Fs)=\rho(\gamma)f(s).
$$

Thus the isomorphism respects the geometric Frobenius.
