+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-stalk-formula"
uses = ["def-pc-separably-closed"]
+++
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
