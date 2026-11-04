+++
id = "lemma-vanishing-local-term-zero-stalk"
kind = "lemma"
title = "Vanishing of the local term at a zero stalk"
order = 983
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.sectionsWithSupportRestriction_eq_zero", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_supportedRestriction_frobeniusGraph_eq_zero", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_zero_of_smooth"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-proper-direct-image-unbounded-complexes", "definition-verdier-dual-evaluation", "definition-correspondence", "definition-frobenius-correspondences-their-operators"]
+++
In the setting of Lemma [lemma-local-term-restriction-map], let $y$ be a
fixed point of $\Phi_X^m$, and suppose $K_{\bar y}=0$. Then

$$
\rho:R\Gamma_\Gamma(T,P)\longrightarrow R\Gamma_y(\Delta,\delta^*P)
$$

is zero in $D(A)$. Consequently $\operatorname{LT}_y(\psi)=0$ for every
morphism $\psi:(\Phi_X^m)^*K\to K$.
