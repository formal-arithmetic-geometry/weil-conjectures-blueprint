+++
kind = "proof"
of = "lemma-frobenius-fixed-scheme--2"
order = 959007
uses = ["lemma-frobenius-fixed-scheme--1"]
+++
Under the bijection in [lemma-frobenius-fixed-scheme--1], the fixed points
lie over points of $X_0$ with finite residue field of degree dividing $m$.
There are finitely many such points, since $X_0$ is of finite type, and
over each there are finitely many embeddings of the residue field into
$\mathbf F_{q^m}$. This is the finiteness argument in
`Scheme.Hom.finite_fixedFieldPoints`, transported by
`IsModelFrobenius.fixedPointEquiv`.

For finite $I$, identify $\coprod_{i\in I}\Spec k$ with
$\Spec(\prod_{i\in I}k)$. Its structure morphism comes from the diagonal
map $k\to\prod_{i\in I}k$, which is finite as a map of rings. Apply this
to $I=I_m$ and use the equalizer description in
[lemma-frobenius-fixed-scheme--1].
