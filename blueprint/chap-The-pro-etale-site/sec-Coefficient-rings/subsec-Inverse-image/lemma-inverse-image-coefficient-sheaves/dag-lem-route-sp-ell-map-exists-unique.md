+++
id = "dag-lem-route-sp-ell-map-exists-unique"
kind = "dag-lemma"
title = "The induced quotient inclusion is characterized by the two integral reductions."
name_showing = false
order = 187542
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-ell-map-exists-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spEllMap_existsUnique"]
uses = ["dag-lem-sp-ell-quotient-finite-discrete", "dag-lem-route-sp-integers-map-exists-unique"]
+++
Let $\ell$ be a prime, let $E\subseteq F\subseteq\overline{\mathbf Q}_\ell$ be finite extensions of $\mathbf Q_\ell$, with the restricted absolute values and integer rings $\mathcal O_E,\mathcal O_F$ of `def-sfb-padic-integers-condensed-ring`, and let $X$ be any scheme. For $G=E,F$ and $n\geq0$, put $B_{G,n}=\mathcal O_G/\ell^{n+1}\mathcal O_G$, with the discrete topology, and let $q_{G,n}:\mathcal O_G\to B_{G,n}$ be reduction, a continuous ring homomorphism ([dag-lem-sp-ell-quotient-finite-discrete]), with condensation $\underline{q_{G,n}}$ of `def-sfb-continuous-map-condensed-ring-map`. Write $\underline T(S)=C(S,T)$ for the underlying abelian sheaf of the condensed ring of `def-sfb-continuous-map-condensed-ring`, and put $T_X=p_X^*\underline T$ using `sk-def-sfb-pullback-from-point`. Let $r_{G,n}=p_X^*\underline{q_{G,n}}:\mathcal O_{G,X}\to B_{G,n,X}$ be the coefficient map of `def-sfb-coefficient-map`. Let $\iota_{E,F}:\underline E\to\underline F$ be the field inclusion of `def-sfb-qlbar-subextension-map` and $\kappa_G:\underline{\mathcal O}_G\to\underline G$ the integer inclusion of `def-sfb-integers-to-subfield-point`. Let $i_{E,F,X}:\mathcal O_{E,X}\to\mathcal O_{F,X}$ be the unique morphism of ring objects with $(\kappa_F)_X\circ i_{E,F,X}=(\iota_{E,F})_X\circ(\kappa_E)_X$, given by [dag-lem-route-sp-integers-map-exists-unique]. Then there exists exactly one morphism of abelian sheaves
$$\phi:B_{E,n,X}\longrightarrow B_{F,n,X}$$
satisfying
$$\phi\circ r_{E,n}=r_{F,n}\circ i_{E,F,X}.$$
The uniqueness is among all abelian-sheaf morphisms, without requiring them to preserve the ring structures.

(SHEAF DAG node `lem-route-sp-ell-map-exists-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-padic-integers-condensed-ring`, `def-sfb-continuous-map-condensed-ring`, `def-sfb-continuous-map-condensed-ring-map`, `sk-def-sfb-pullback-from-point`, `def-sfb-coefficient-map`, `def-sfb-qlbar-subextension-map`, `def-sfb-integers-to-subfield-point`.
