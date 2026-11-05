+++
kind = "proof"
of = "lemma-cohomology-near-two-transverse-divisors--2"
order = 972004
uses = ["lemma-cohomology-near-two-transverse-divisors--1"]
+++
The connected regular locally noetherian scheme $D_2$ is irreducible,
and $z$ is closed in $D_2$. Put $K=M|_{D_2}$. By
[lemma-cohomology-near-two-transverse-divisors--1], all geometric stalks
of $K$ over $z$ vanish and $K|_{D_2-z}$ has locally constant cohomology.
Apply
`AlgebraicGeometry.Etale.derivedGlobalSectionsRestriction_eq_zero_of_isZero_of_isLocallyConstant`
to $K$.

To describe this last step, lift a geometric generic point to the
strict localization of $D_2$ at $\bar w$, and another to its strict
localization at a geometric point over $z$. Restriction through the
latter localization is zero, since its derived global sections are
the zero stalk at $z$. The two geometric generic points have the same
image; passing to a common algebraically closed field transfers this
vanishing between them. On the strict localization at $\bar w$, the
restriction to its geometric generic point is an isomorphism because
the cohomology sheaves are locally constant. Naturality and composition
of restriction maps therefore give the asserted zero morphism in
$D(A)$.
