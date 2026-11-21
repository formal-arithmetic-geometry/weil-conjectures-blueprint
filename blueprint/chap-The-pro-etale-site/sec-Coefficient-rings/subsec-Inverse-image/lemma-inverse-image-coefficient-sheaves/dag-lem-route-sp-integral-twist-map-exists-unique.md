+++
id = "dag-lem-route-sp-integral-twist-map-exists-unique"
kind = "dag-lemma"
title = "The integral transition is uniquely specified on every positive quotient twist."
name_showing = false
order = 187545
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-integral-twist-map-exists-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spIntegralTwistMap_existsUnique"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-route-sp-integers-map-exists-unique", "dag-lem-route-sp-ell-map-exists-unique", "dag-def-pur-roots-of-unity-sheaf", "dag-lem-sp-integral-level-transition-unique", "dag-def-pur-sheaf-inverse-limit", "dag-lem-sp-ell-quotient-finite-discrete"]
+++
Let $X$ be any scheme, $\ell$ a prime, and $E\subseteq F\subseteq\overline{\mathbf Q}_\ell$ finite intermediate extensions of $\mathbf Q_\ell$, with valuation rings $\mathcal O_E,\mathcal O_F$ `def-weil-l-adic-coefficient-extension`. Use the small pro-etale site and coefficient universe of [def-weil-pbc-proetale-site, def-weil-size-convention]. The coefficients $R_G=\mathcal O_{G,X}$, for $G=E,F$, are the pulled-back continuous-function condensed ring objects [sk-def-sfb-condensed-ring, sk-def-sfb-pulled-back-coefficients]. For $n\geq0$, write $B_{G,n}=\mathcal O_G/\ell^{n+1}\mathcal O_G$ with its discrete topology, and $B_{G,n,X}=p_X^*\underline{B_{G,n}}$. Let $q_{G,n}:R_G\to B_{G,n,X}$ and $r_{G,n}:B_{G,n+1,X}\to B_{G,n,X}$ be the pulled-back quotient reductions, continuous before pullback by [dag-lem-sp-ell-quotient-finite-discrete]. Let $i:R_E\to R_F$ be the unique integral coefficient map over $E_X\to F_X$ of [dag-lem-route-sp-integers-map-exists-unique], and let $j_n:B_{E,n,X}\to B_{F,n,X}$ be the unique map satisfying $j_nq_{E,n}=q_{F,n}i$ of [dag-lem-route-sp-ell-map-exists-unique]. Composition here is in the usual functional order.

Put $U_n=\mu_{\ell^{n+1},X}$, with $v_n:U_{n+1}\to U_n$, $u\mapsto u^\ell$, as in [dag-def-pur-roots-of-unity-sheaf]. In the category of internal $R_G$-modules `sk-def-sfb-module-objects`, let $T_{G,n}$ have underlying abelian sheaf $B_{G,n,X}\otimes_{\mathbf Z}U_n$ `sk-def-sfb-sheaf-tensor`, with $R_G$ acting on the first factor through $q_{G,n}$. Use the unique module transition with underlying arrow $r_{G,n}\otimes v_n$ of [dag-lem-sp-integral-level-transition-unique]. Let $L_G=\varprojlim_{n\in\mathbf N^{\mathrm{op}}}T_{G,n}$ in internal $R_G$-modules, and write $p_{G,n}:|L_G|\to B_{G,n,X}\otimes_{\mathbf Z}U_n$ for its underlying projections, where vertical bars forget the module action [def-pur-sheaf-inverse-limit, def-weil-pbc-internal-abelian-sheaf-module-equivalence]. Then there exists exactly one morphism of abelian sheaves $f:|L_E|\to|L_F|$ such that
$$
 p_{F,n}\circ f=(j_n\otimes\mathrm{id}_{U_n})\circ p_{E,n}\qquad(n\geq0).
$$
This is the assertion for the specified systems spIntegralTwistSystem and their limits spIntegralTwist. No invertibility of $\ell$ on $X$ is assumed, and the conclusion specifies an underlying abelian-sheaf morphism, with no additional linearity assertion.

(SHEAF DAG node `lem-route-sp-integral-twist-map-exists-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-l-adic-coefficient-extension`, `def-weil-size-convention`, `sk-def-sfb-condensed-ring`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-module-objects`, `sk-def-sfb-sheaf-tensor`, `def-weil-pbc-internal-abelian-sheaf-module-equivalence`.
