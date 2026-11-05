+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--7"
order = 79013
uses = ["corollary-evaluation-weakly-contractible-objects--6"]
+++
An isomorphism evaluates to a bijection by evaluation of its inverse.
Conversely, apply [corollary-evaluation-weakly-contractible-objects--6]
to the short sequences
$$
A\xrightarrow{0}A\xrightarrow{f}B,
\qquad
A\xrightarrow{f}B\xrightarrow{0}B.
$$
Bijectivity of $f(W)$ makes both evaluated sequences exact. Thus $f$
is both a monomorphism and an epimorphism, and is an isomorphism in the
abelian category of module sheaves.

For complexes, $v$ is a quasi-isomorphism if and only if its mapping
cone is acyclic. Evaluation is additive and preserves finite
biproducts, so evaluation of the cone is naturally isomorphic to the
cone of $v(W)$. Apply the acyclicity criterion of
[corollary-evaluation-weakly-contractible-objects--6] and then the cone
criterion over $\mathcal R(W)$.
