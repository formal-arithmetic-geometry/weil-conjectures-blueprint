+++
id = "lemma-weil-pbc-finite-stalk-formula"
kind = "lemma"
title = "Geometric stalk formula for finite direct image"
order = 997
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Etale.stalkRestrict"]
uses = ["def-kun-separably-closed", "def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-fibre", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-fin-finite-splitting", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be a finite morphism of schemes, let $\mathcal A$ be a
Grothendieck abelian coefficient category for which presheaves on small etale
sites can be sheafified (for instance abelian groups), and let
$\bar y:\operatorname{Spec}\Omega\to Y$ be a geometric point with $\Omega$
algebraically closed. For an $\mathcal A$-valued etale sheaf $G$ on $X$ and a
geometric point $\bar x$ of the geometric fibre of $f$ over $\bar y$, the
*restriction of stalks* $(f_*G)_{\bar y}\to G_{\bar x}$ sends the germ of a
section of $G$ over $U\times_YX$, for a pointed etale neighbourhood $U$ of
$\bar y$, to its germ at the pointed etale neighbourhood $U\times_YX$ of
$\bar x$. These maps together give an isomorphism

$$
 (f_*G)_{\bar y}\xrightarrow{\sim}
 \prod_{\bar x\in|X_{\bar y}|}G_{\bar x},
$$

natural in $G$, where the product runs over the finite geometric fibre of $f$
over $\bar y$. For a finite set, this product is also the direct sum.

## Proof

After base change to the strict henselization at $\bar y$, the finite scheme
$X_{\bar y}$ is the spectrum of a finite algebra over a strictly henselian
local ring, hence a finite disjoint union of strictly henselian local schemes
indexed by the geometric points $\bar x$. Sections over a disjoint union are
the corresponding product of stalks, as computed by the stalk description of
the geometric-stalk convention and the definition of the direct image; for a
finite index set this product is the direct sum.

Alternatively, one can avoid the strict henselisation and work with the category of
*split neighbourhoods* of $\bar y$ (pointed etale neighbourhoods $(U,\bar u)$ together
with a decomposition of $X\times_YU$ into pairwise disjoint clopen pieces indexed by the
geometric points $\bar x$ over $\bar y$, the $\bar x$-th piece containing $(\bar x,\bar u)$). These
are cofinal among all pointed etale neighbourhoods: by [lem-fin-finite-splitting]
applied to $f$ there is a split neighbourhood $(Y',\bar y')$, and for any pointed etale
neighbourhood $(U,\bar u)$ the base change of its decomposition to $U\times_YY'$ is again one
(Stacks 00UJ applied to an affine chart). The $\bar x$-th pieces are cofinal among the pointed
etale neighbourhoods of $\bar x$ (an etale-local section lemma for finite algebras with a unique
point), and the sheaf $G$ sends the disjoint clopen cover to a product; finite products commute
with the filtered colimit since the coefficients satisfy AB5. Hence
$(f_*G)_{\bar y}=\varinjlim_{(U,\bar u)}G(X\times_YU)\cong\prod_{\bar x}G_{\bar x}$, the
$\bar x$-th component being the restriction of stalks, and the isomorphism is natural in $G$
because every map involved is.
