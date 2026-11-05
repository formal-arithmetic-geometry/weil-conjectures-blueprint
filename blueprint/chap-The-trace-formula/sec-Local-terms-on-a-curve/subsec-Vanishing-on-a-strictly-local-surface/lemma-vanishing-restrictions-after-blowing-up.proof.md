+++
kind = "proof"
of = "lemma-vanishing-restrictions-after-blowing-up"
order = 979
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-relative-dualizing-complex", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic"]
+++
After blowing up $t$, the three curves are separated along the
exceptional divisor, which then plays the role of $D_2$ in the previous
lemma.

Let $\widetilde T\to T$ be the blowup in $t$, with exceptional divisor
$E\simeq\mathbf P^1_k$, and let $D',H',C'$ be the strict transforms.
In these terms, the hypotheses on tangent cones say that $D'\cap E$ is disjoint
from both $C'\cap E$ and $H'\cap E$. We therefore apply Lemmas [lemma-cohomology-near-two-transverse-divisors] and [lemma-restriction-punctured-curve] to the surface $X=\widetilde T-D'$ with the divisors $D_1=H'\cap X$ and
$D_2=E\cap X=E-D'$. Here the divisor $E-D'$ is connected, since it is a
projective line with finitely many points removed, and $H'\cap X$ meets it
transversely in the single point $z$ corresponding to the tangent
direction of $H$. Since the blowup is an isomorphism off $E$, the source
of the map is $R\Gamma(X-E,j'_!N')$ for the pulled-back complex $N'$.

The strict transform $C'$ is proper and quasi-finite over the
strictly local curve $C$, hence finite. Its closed fibre is the
finite set of tangent directions of its branches, so $C'$ is a
finite disjoint union of strictly local curves $C'_w$, each meeting
$E$ at a single point $w$ of $E-D'$. Each restriction to $C'_w-w$ is
zero by Lemma [lemma-restriction-punctured-curve]. Since
$C'-E\simeq C-t$, the given restriction map is the direct sum of
these zero maps.
