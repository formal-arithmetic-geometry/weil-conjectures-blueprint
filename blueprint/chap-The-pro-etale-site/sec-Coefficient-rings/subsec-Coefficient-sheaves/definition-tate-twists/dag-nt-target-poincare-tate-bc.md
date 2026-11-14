+++
id = "dag-nt-target-poincare-tate-bc"
kind = "dag-lemma"
title = "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tateTwistDerived"
name_showing = false
order = 184546
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "nt-target-poincare-tate-bc"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tateTwistDerived"]
+++
Let $\ell$ be a prime and let $X$ be a scheme on which $\ell$ is invertible. Let $d,n\in\mathbf Z$. Write $B=\mathrm{Profinite.padicAlgClRingObj}(\ell)$ for the finite-subextension-valued condensed ring $\underline{\overline{\mathbf Q}}_\ell$ `sk-def-sfb-qlbar-condensed`, and $B_X=p_X^*B$ for its coefficient ring on $X_{\mathrm{proet}}$. Use exactly the internal-module Tate construction $B_X(d)$ of [dag-def-pur-condensed-tate-twists], and let $\mathrm{tateTwistDerived}(X,\ell,d)=B_X(d)[0]$. Then
$$\mathrm{tateTwistDerived}(X,\ell,d)[n]\in D^b_c(X)[[B]],$$
where bounded constructibility is exactly the upstream predicate boundedConstructible, i.e. `def-sfb-bounded-constructible-complexes` (the definition recorded for the blueprint unit `sk-def-sfb-bounded-constructible`) in the ordinary unbounded derived category of internal $B_X$-modules: cohomology is zero outside a finite interval, and every cohomology module is constructible in the sense of `def-sfb-constructible-module`, namely there is one finite stratification of $X$ by immersions $g_a\colon X_a\to X$ such that each $g_a^*$ of the module is locally finitely presented over $g_a^*B_X$. No quasi-compactness, Noetherianity, finite-type or finite-field hypothesis on $X$ is assumed. The invertibility hypothesis repairs the unrestricted upstream lemma; it is the hypothesis of the blueprint Tate-twist setting.

(SHEAF DAG node `nt-target-poincare-tate-bc`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pur-condensed-tate-twists`, `sk-def-sfb-qlbar-condensed`, `sk-def-sfb-bounded-constructible`, `def-sfb-bounded-constructible-complexes`, `def-sfb-constructible-module`.
