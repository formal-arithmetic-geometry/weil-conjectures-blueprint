+++
kind = "proof"
of = "lemma-hankel-rank-rationality--2"
order = 1376004
uses = ["lemma-hankel-rank-rationality--1"]
+++
Suppose that $C_{K'}$ has a normalized fraction. By
[lemma-hankel-rank-rationality--1], its shift span $V'$ over $K'$ is
finite-dimensional. Let $V$ be the shift span of $C$ over $K$.
Applying $K\hookrightarrow K'$ coordinate by coordinate carries
every shift of $C$ to the corresponding shift of $C_{K'}$, and hence
carries $V$ into $V'$.

Any finite linearly independent family in $V$ remains linearly
independent over $K'$ after this map. Indeed, finitely many coordinates
give a square matrix with nonzero determinant, and the determinant
remains nonzero under the field inclusion. Its rows are therefore
independent over $K'$, so the original family of sequences is too.
Every finite independent family in $V$ consequently has at most
$\dim_{K'}V'$ elements. Thus $V$ is finite-dimensional, and another
application of [lemma-hankel-rank-rationality--1] gives a normalized
fraction over $K$.

Conversely, applying $K\hookrightarrow K'$ to the coefficients of
$CQ=P$ with $Q(0)=1$ gives the required normalized fraction over $K'$.
