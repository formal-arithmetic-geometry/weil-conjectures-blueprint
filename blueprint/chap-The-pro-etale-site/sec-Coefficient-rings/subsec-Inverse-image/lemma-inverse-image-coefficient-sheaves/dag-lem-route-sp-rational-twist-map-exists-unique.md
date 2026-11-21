+++
id = "dag-lem-route-sp-rational-twist-map-exists-unique"
kind = "dag-lemma"
title = "Localization gives the unique rational transition with the prescribed tensor formula."
name_showing = false
order = 187547
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-rational-twist-map-exists-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spRationalTwistMap_existsUnique"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-sheaf-inverse-limit", "dag-lem-route-sp-integers-map-exists-unique", "dag-lem-route-sp-ell-map-exists-unique", "dag-lem-route-sp-integral-twist-map-exists-unique", "dag-lem-sp-integral-level-transition-unique"]
+++
Fix a prime $\ell$, an algebraic closure $\Omega=\overline{\mathbf Q}_\ell$, an arbitrary scheme $X$, and finite intermediate fields $\mathbf Q_\ell\subseteq E\subseteq F\subseteq\Omega$ (equality allowed). Work in $\mathcal C=\operatorname{Sh}(X_{\mathrm{proet}},\mathbf{Ab})$ on the small site [dag-def-weil-pbc-proetale-site], with the sheafified tensor $\otimes=\otimes_{\mathbf Z}$ `sk-def-sfb-sheaf-tensor`. For $G=E,F$, write $A_G=p_X^*\underline{\mathcal O_G}$ and $K_G=p_X^*\underline G$, with their canonical inclusion $i_G:A_G\to K_G$, using the continuous-function condensed rings and their pulled-back ring objects [sk-def-sfb-condensed-ring, sk-def-sfb-pulled-back-coefficients]. For $n\geq1$ put $B_{G,n}=p_X^*\underline{\mathcal O_G/\ell^n\mathcal O_G}$, with discrete quotient topology, and let $r_{G,n}:A_G\to B_{G,n}$ be reduction. Put
$$T_{G,n}=B_{G,n}\otimes\mu_{\ell^n,X},\qquad M_G=\varprojlim_{n\geq1}T_{G,n}.$$
Here the roots and their power transitions are those of [dag-def-pur-roots-of-unity-sheaf]; $T_{G,n}$ is an $A_G$-module with action on its first factor through $r_{G,n}$, the tower transition is the $A_G$-module map with underlying arrow quotient reduction tensored with $z\mapsto z^\ell$ [dag-lem-sp-integral-level-transition-unique], the limit is taken in internal $A_G$-modules, and its action and underlying projections $p_{G,n}$ are coordinatewise [def-weil-pbc-internal-abelian-sheaf-module-equivalence, def-pur-sheaf-inverse-limit]. Thus $M_G$ is the actual integral twist, with the natural-number index $n-1$ of `spIntegralTwistLevel` corresponding to exponent $n$.

Let $d:K_E\to K_F$ be the pulled-back field inclusion and $j:A_E\to A_F$ the ring inclusion characterized by $i_Fj=di_E$ [dag-lem-route-sp-integers-map-exists-unique]. Let $a_n:B_{E,n}\to B_{F,n}$ be the quotient transition characterized by $a_nr_{E,n}=r_{F,n}j$ [dag-lem-route-sp-ell-map-exists-unique]. Let $u:M_E\to M_F$ be the integral transition characterized by
$$p_{F,n}u=(a_n\otimes1_{\mu_{\ell^n,X}})p_{E,n}\quad(n\geq1)$$
[dag-lem-route-sp-integral-twist-map-exists-unique]. Define $Q_G=K_G\otimes_{A_G}M_G$ by extension of scalars `def-sfb-modobj-extension`, with its defining balancing-coequalizer projection $q_G:K_G\otimes M_G\to Q_G$. Then there is exactly one morphism of abelian sheaves $f:Q_E\to Q_F$ such that
$$f\circ q_E=q_F\circ(d\otimes u).$$
This is the underlying-morphism assertion of `AlgebraicGeometry.ProEtale.spRationalTwistMap_existsUnique`: $Q_G$ is `spRationalTwist X ℓ G` and $q_G$ is `Mod.extendπ`. No invertibility of $\ell$ on $X$, local freeness, or additional linearity hypothesis on $f$ is imposed.

(SHEAF DAG node `lem-route-sp-rational-twist-map-exists-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `sk-def-sfb-sheaf-tensor`, `sk-def-sfb-condensed-ring`, `sk-def-sfb-pulled-back-coefficients`, `def-sfb-modobj-extension`, `def-weil-pbc-internal-abelian-sheaf-module-equivalence`.
