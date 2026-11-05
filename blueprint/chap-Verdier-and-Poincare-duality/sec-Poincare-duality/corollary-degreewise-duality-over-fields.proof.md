+++
kind = "proof"
of = "corollary-degreewise-duality-over-fields"
order = 861
uses = ["lemma-cohomology-modules-underlying-abelian", "proposition-proper-base-change-degree-zero", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-perfect-pairing"]
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
