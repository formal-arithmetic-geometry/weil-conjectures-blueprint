+++
kind = "proof"
of = "corollary-degreewise-duality-over-fields"
order = 861
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "proposition-exact-products", "proposition-milnor-sequence", "corollary-continuity-cohomology", "definition-tate-twists", "lemma-reduction-derived-nakayama", "lemma-integral-models", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "theorem-results-from-etale-theory", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-exceptional-inverse-image", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients", "definition-sp-scalar-extension", "theorem-sp-qbar", "definition-trace-map", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "theorem-verdier-biduality", "definition-perfect-pairing", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
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
Here both spaces are finite-dimensional by Lemma [lemma-perfect-complexes-geometric-point]. Finally, the second pairing is
the first one with the second factor and the value line twisted by
$(-d)$, so it is perfect as well.
