+++
kind = "proof"
of = "corollary-degreewise-duality-over-fields"
order = 854
uses = ["proposition-etale-implications", "lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "corollary-open-direct-image-over-field", "lemma-perfect-complexes-geometric-point", "theorem-nagata-s-compactification-theorem", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We take cohomology of the isomorphism (10.8);
over a field this loses nothing, because linear duality is exact.
More precisely, a bounded complex with finite-dimensional cohomology is
isomorphic in the derived category to the sum of its shifted cohomology spaces, so that
$H^{-i}(R\!\operatorname{Hom}_\Lambda(P,\Lambda))=\Hom_\Lambda(H^i(P),
\Lambda)$. Because of the shift $[2d]$, the source of
(10.8) has $H^{2d-i}(X,K^\vee(d))$ in
degree $-i$, and taking $H^{-i}$ we
get $H^{2d-i}(X,K^\vee(d))\simeq\Hom_\Lambda(H^i_c(X,K),\Lambda)$.
Since this isomorphism is induced by the pairing in degrees $(i,2d-i)$, it
says exactly that the first pairing is perfect.
Lemma [lemma-perfect-complexes-geometric-point] shows that both spaces
are finite-dimensional. The second pairing is
the first one with the second factor and the value line twisted by
$(-d)$, so it is perfect as well.
