+++
id = "sec-algebraic-groups-lie-algebras"
kind = "section"
title = "Algebraic Groups and Lie Algebras"
order = 3687
uses = ["sec-curve-estimates", "sec-nagata-compactification", "sec-picard-framework", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-purity", "sec-trace-formula", "sk-thm-br"]
+++
**Content.** This section supplies the group theory and linear algebra behind
the weight arguments of the purity and Deligne–Laumon sections. It follows
the appendix on algebraic groups and Lie algebras in characteristic zero,
then the section on monodromy and determinant weights.

Over an algebraically closed field of characteristic zero, every algebraic
group is smooth and reduced [sk-i-cartier]. Its identity component is an
open normal subgroup of finite index, images of homomorphisms are closed,
and a closed subgroup with the full Lie algebra of a connected group is
everything [sk-p-geometry]. A connected group and its Lie algebra have the
same stable subspaces, and the center of the Lie algebra is the Lie algebra
of the center [sk-p-comparison]. Lie's eigenvector theorem
[sk-lem-walg-lie-eigenvector], Engel's theorem [sk-lem-walg-engel],
Cartan's trace criterion [sk-lem-walg-trace-criterion] and the Killing
form [sk-lem-walg-killing] give $\rad\mathfrak l=Z(\mathfrak l)$ and
$\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l]$ for a Lie algebra
with a faithful semisimple representation [sk-p-lie].

For a Weil group $W=P\rtimes\langle s\rangle$, semisimplicity passes to
normal subgroups [sk-i-restriction]. Characteristic polynomials
factor along filtrations, with the spectra of duals, tensor products and
exterior powers [sk-p-linear-filtration], and tensor and exterior powers of
filtered representations are filtered by the constructions on the
composition factors [sk-r-linear-library]. For a semisimple representation
the monodromy groups $G\supseteq H$ satisfy
$G^\circ=Z(G^\circ)^\circ H^\circ$ [sk-p-product], which gives a central
element $z=hF^N$ of positive degree [sk-p-central]. The determinant weight
[sk-d-weights] of a subquotient on which $z$ acts by a scalar is read off
from that scalar [sk-p-readout]. This yields the determinant weights of the
simple factors of tensor products [sk-p-tensor] and exterior powers
[sk-p-exterior], also for representations that are not semisimple
[sk-rem-walg-nonsemisimple].

**Key theorem.**

- Lemma [sk-p-readout] (weight readout): if the central element $z=hF^N$
  acts on a nonzero subquotient $Q$ with finite geometric determinant by a
  scalar $c_Q$ (automatic for $Q$ simple), then
  $\dw_\iota(Q)=\lambda_\iota(c_Q)/N$.
- Propositions [sk-p-tensor], [sk-p-exterior]: the determinant weights of
  the simple factors of $V\otimes V'$ are the sums
  $\dw_\iota(A_a)+\dw_\iota(B_b)$, and those of $\bigwedge^rV$ are the sums
  $\sum_an_a\dw_\iota(A_a)$ with $0\le n_a\le\dim A_a$, $\sum_an_a=r$.
- Lemma [sk-p-linear-filtration] (filtrations and spectra):
  $\det(1-Tu\mid V)=\prod_a\det(1-Tu\mid\operatorname{gr}_aV)$, so
  eigenvalues on subquotients occur on $V$.

**References.**

- Stacks Project: `035Z` (products of reduced schemes over a perfect
  field); `056V` (dense smooth open subscheme); `00NP` (regular local rings
  are domains); `054K` (Chevalley's theorem); `02VL` (descent of
  smoothness).
- J. S. Milne, *Algebraic Groups* (2017): Theorem 3.23 (Cartier's theorem)
  and Proposition 1.37.
