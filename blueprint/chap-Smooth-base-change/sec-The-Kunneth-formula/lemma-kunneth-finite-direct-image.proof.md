+++
kind = "proof"
of = "lemma-kunneth-finite-direct-image"
order = 713
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "lemma-degree-zero-calculation", "lemma-reduction-curve-over-normal-base", "lemma-base-change-along-product-projection", "definition-kunneth-map", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Both sides are additive in $Q$, so we may assume $Q=\pi_*A_{T'}$. Set

$$
v=\operatorname{id}_Y\times\pi,\qquad
w=\operatorname{id}_X\times\pi,\qquad
h'=f\times\operatorname{id}_{T'}.
$$

Direct image along a finite morphism is exact and commutes with pullback, and by the
projection formula we have

$$
Rf_*M\boxtimes\pi_*A_{T'}
\simeq v_*p_{Y,T'}^*Rf_*M,
\qquad
M\boxtimes\pi_*A_{T'}\simeq w_*p_{X,T'}^*M.
$$

Since $hw=vh'$, the comparison between these two expressions is
$v_*$ of the base change map of
Lemma [lemma-base-change-along-product-projection] for $h'$, hence it
is an isomorphism.
Moreover, this comparison is $\kappa_{M,Q}$, because under the adjunction
$h^*\dashv Rh_*$ and the adjunctions for the finite maps, both correspond to
the counit $\varepsilon_f\otimes^{\mathbf L}1$ that defines $\kappa_{M,Q}$.
