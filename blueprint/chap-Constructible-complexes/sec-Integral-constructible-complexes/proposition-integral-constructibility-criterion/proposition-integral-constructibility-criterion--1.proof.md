+++
kind = "proof"
of = "proposition-integral-constructibility-criterion--1"
order = 246002
uses = ["lemma-integral-models", "lemma-comparison-completed-coefficients", "proposition-extension-zero-restriction-closed-subscheme"]
+++
First identify the two presentations of the continuous integral
coefficient sheaf by their canonical isomorphism. Restriction of scalars
along this isomorphism is an exact equivalence, so it preserves and
reflects boundedness and the finite constant local models of each
cohomology sheaf.

Apply [lemma-integral-models](2) in this presentation. It identifies
bounded constructibility with adic constructibility after restriction
to the constant sheaf $\mathcal O_E$. We compare the two clauses of
adic constructibility with the conditions in the statement.
The coefficient limit of [lemma-comparison-completed-coefficients]
and the normalized quotient maps identify the canonical Roos
augmentation with the completion unit after restriction of scalars.
Thus its invertibility is exactly derived completeness of $K$.
At the first quotient, the constant and continuous residue coefficient
sheaves agree. The resulting exact equivalences identify the actual
derived reduction $K_1$, its constructible cohomology, and its relative
derived tensor products. They therefore preserve and reflect the
finite Tor condition. On the constant-coefficient side that condition
also gives boundedness, by tensoring with the coefficient sheaf itself.
Combining these comparisons proves the displayed equivalence.

For the equality of subcategories, take
$K\in\Dbc(X,\mathcal O_E)$ and choose $a\leq b$ outside which its
cohomology vanishes. A finitely presented module over the DVR
$\mathcal O_E$ has a finite free resolution in degrees $-1,0$.
Flat extension to the continuous coefficient sheaf and exact inverse
image give Tor amplitude $[-1,0]$ for each finite constant local model.
Vanishing of tensor cohomology can be checked on the pro-étale cover
exhibiting the model. A finite open and closed refinement of a
constructible stratification, together with the localization sequence
of [proposition-extension-zero-restriction-closed-subscheme], gives
the same interval for each constructible cohomology sheaf $H^q(K)$.
The bounded truncation triangles then give Tor amplitude $[a-1,b]$
for $K$: each $H^q(K)[-q]$ has amplitude $[q-1,q]$, contained in this
common interval. Hence $K\in\Dctf(X,\mathcal O_E)$. The reverse
inclusion holds by definition.
