+++
id = "sec-algebraic-groups-lie-algebras"
kind = "section"
title = "Algebraic Groups and Lie Algebras"
order = 3878
+++
**Content.** This section supplies the group theory and linear algebra behind
the weight arguments of the purity and Deligne–Laumon sections. It follows
the appendix on algebraic groups and Lie algebras in characteristic zero.

Over an algebraically closed field of characteristic zero, every algebraic
group is smooth and reduced [sk-i-cartier]. Its identity component is an
open normal subgroup of finite index, images of homomorphisms are closed,
and for a connected matrix group a closed subgroup with the full Lie algebra
is everything [sk-p-geometry]. A connected group and its Lie algebra have the
same stable subspaces, and for a matrix group the center of the Lie algebra is
the Lie algebra of the center [sk-p-comparison]. Lie's eigenvector theorem
[sk-lem-walg-lie-eigenvector], Engel's theorem [sk-lem-walg-engel],
Cartan's trace criterion [sk-lem-walg-trace-criterion] and the Killing
form [sk-lem-walg-killing] give $\rad\mathfrak l=Z(\mathfrak l)$ and
$\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l]$ for a Lie algebra
with a faithful semisimple representation [sk-p-lie].

The section of the tex on monodromy and determinant weights, which applies
these facts to the monodromy groups of a lisse Weil sheaf on a curve, sits in
the section on purity of real sheaves, after the determinant weights of
lisse Weil sheaves. The lemma on filtrations and spectra (`walg:filtration-spectra`) sits there
too, after the definition of weights, as in the tex.

**Key theorem.**

- Proposition [sk-p-lie]: a Lie algebra $\mathfrak l$ with a faithful
  semisimple representation satisfies $\rad\mathfrak l=Z(\mathfrak l)$
  and $\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l]$.

**References.**

- Stacks Project: `035Z` (products of reduced schemes over a perfect
  field); `056V` (dense smooth open subscheme); `00NP` (regular local rings
  are domains); `054K` (Chevalley's theorem); `02VL` (descent of
  smoothness).
- J. S. Milne, *Algebraic Groups* (2017): Theorem 3.23 (Cartier's theorem)
  and Proposition 1.37.
