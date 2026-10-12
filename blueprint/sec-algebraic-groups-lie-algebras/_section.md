+++
id = "sec-algebraic-groups-lie-algebras"
kind = "section"
title = "Algebraic Groups and Lie Algebras"
order = 2797
uses = ["sec-abelian-varieties", "sec-trace-formula"]
+++
**Content.** This section supplies the group theory and linear algebra behind
the weight arguments of the purity and Deligne–Laumon sections. Over an
algebraically closed field of characteristic zero, a Lie algebra with a
faithful semisimple representation satisfies $\rad L=Z(L)$ and
$L=Z(L)+[L,L]$ [sk-p-lie]. With Cartier's theorem [sk-i-cartier] and basic
affine geometry [sk-p-geometry], this gives the group–Lie comparison
[sk-p-comparison]. For a representation of a degree datum
$\deg\colon W\to\mathbf Z$, the arithmetic and geometric monodromy groups
$G\supseteq H$ [sk-d-monodromy] then satisfy $G^\circ=Z(G^\circ)^\circ H^\circ$
[sk-p-product]. So some central $z\in Z(G)\cap HF^N$ exists [sk-p-central].
Using it, the determinant weight of a subquotient can be read off from a
central scalar [sk-p-readout]. A linear-algebra layer handles characteristic
polynomials along filtrations and the spectra of $\otimes$, $\bigwedge^s$ and
duals [sk-p-linear-spectra]. From these come the tensor and exterior-power
weight rules [sk-p-tensor], [sk-p-exterior]. Rank-one interfaces finish the
section: the factorization of rank-one characters, $(V_\ell A)^F=0$ for
abelian varieties [sk-p-tate], and the cyclotomic Frobenius.

**Key theorem.**

- Prop [sk-p-readout] (weight readout): if a positive central pair $(N,z)$
  acts on a nonzero $W$-subquotient $Q$ with finite geometric determinant by
  a scalar $c_Q$ (automatic for $Q$ simple), then
  $\dw_\lambda(Q)=\lambda(c_Q)/N$. Used in §[sec-purity-real-sheaves],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Prop [sk-p-linear-filtration] (characteristic polynomials along a
  filtration): $\det(1-Tf\mid V)=\prod_j\det(1-Tf\mid\mathrm{gr}_j)$, so
  eigenvalues on subquotients occur on $V$, and so do scalars acting on
  nonzero invariant subquotients. Used in §[sec-purity-real-sheaves],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].
- Prop [sk-p-rankone] (rank-one factorization): a rank-one character $\chi$
  of $W=P\rtimes\mathbf Z$ with finite geometric image factors as
  $\chi=\chi_{\mathrm{fin}}\cdot z^{\deg}$, where $z=\chi(\gamma)$ and
  $\chi_{\mathrm{fin}}$ has finite image $\chi(P)$. Used in
  §[sec-purity-real-sheaves].
- Prop [sk-p-cyclotomic] (cyclotomic Frobenius): on $\Zell(1)$ and
  $\Qell(1)$, arithmetic Frobenius acts as $q$ and geometric Frobenius as
  $q^{-1}$. Used in §[sec-deligne-laumon-a1], §[sec-zeta-weil].

**References.**

- Stacks Project: `00NP` (regular local rings are domains); `0B8X`, `01V5`
  (density and openness of the smooth locus over a perfect field); `00TV`
  (regularity criterion for smoothness).
- J. S. Milne, *Algebraic Groups* (2017): Corollary 1.35 and Appendix A
  (products and vanishing ideals); Theorem 3.23 (Cartier's theorem) and
  Proposition 1.37.
