+++
id = "dag-lem-sp-integral-level-transition-unique"
kind = "dag-lemma"
title = "The transition maps of the finite-level integral twists are O_E-linear and unique"
name_showing = false
order = 187550
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-sp-integral-level-transition-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spIntegralLevelTransition_existsUnique"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-pur-roots-of-unity-sheaf"]
+++
Let $\ell$ be a prime, $X$ a scheme with small pro-étale site [dag-def-weil-pbc-proetale-site], $E\subseteq\overline{\mathbf Q}_\ell$ a finite extension of $\mathbf Q_\ell$ with ring of integers $\mathcal O_E$ `def-weil-l-adic-coefficient-extension`, and $n\ge0$. For $m\ge1$ let $B_m=\mathcal O_E/\ell^m$ and let $T_m$ be the free $B_{m,X}$-module object on the sheaf $\mu_{\ell^m}$ of $\ell^m$-th roots of unity [dag-def-pur-roots-of-unity-sheaf], regarded as an $\mathcal O_{E,X}$-module `sk-def-sfb-module-objects` by restriction of scalars along the reduction $\mathcal O_{E,X}\to B_{m,X}$ of pulled-back coefficients `sk-def-sfb-pulled-back-coefficients`. Here $\mathcal O_E$ carries its valuation topology `def-sfb-coefficient-extension-integers-topology` and $B_m$ the discrete topology, $\underline{\mathcal O_E}$ and $\underline{B_m}$ are the continuous-map condensed rings `def-sfb-continuous-map-condensed-ring`, $\mathcal O_{E,X}$ and $B_{m,X}$ are their pullbacks, and the reductions $\mathcal O_{E,X}\to B_{m,X}$ and $B_{n+2,X}\to B_{n+1,X}$ are the pullbacks of the maps $\underline{\mathcal O_E}\to\underline{B_m}$ and $\underline{B_{n+2}}\to\underline{B_{n+1}}$ given on each profinite set by composing continuous maps with the quotient ring homomorphisms. Then there is exactly one morphism of $\mathcal O_{E,X}$-modules $T_{n+2}\to T_{n+1}$ whose underlying morphism of abelian sheaves is the tensor product of the reduction $B_{n+2,X}\to B_{n+1,X}$ with the power map $\mu_{\ell^{n+2}}\to\mu_{\ell^{n+1}}$, $\zeta\mapsto\zeta^\ell$. Here the free module object means $T_m=B_{m,X}\otimes_{\mathbf Z}\mu_{\ell^m}$, with the sheaf tensor product of `sk-def-sfb-sheaf-tensor` and action by multiplication on the first factor; restriction of scalars is the action obtained by precomposing that factor with the reduction map, as in `sk-def-sfb-change-of-scalars` (1).

(SHEAF DAG node `lem-sp-integral-level-transition-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-l-adic-coefficient-extension`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-sheaf-tensor`, `sk-def-sfb-change-of-scalars`, `def-sfb-coefficient-extension-integers-topology`, `def-sfb-continuous-map-condensed-ring`.
