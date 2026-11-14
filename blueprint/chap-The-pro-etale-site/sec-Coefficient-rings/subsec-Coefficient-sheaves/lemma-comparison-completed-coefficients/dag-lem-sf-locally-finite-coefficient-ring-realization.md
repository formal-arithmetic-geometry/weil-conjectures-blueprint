+++
id = "dag-lem-sf-locally-finite-coefficient-ring-realization"
kind = "dag-lemma"
title = "Locally finite continuous-function realization of condensed coefficients"
name_showing = false
order = 178502
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--2"
dag_id = "lem-sf-locally-finite-coefficient-ring-realization"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.locallyFiniteCoefficientRing_realization"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $\ell$ be prime and $\Omega=\overline{\mathbf Q}_\ell$ with its extended $\ell$-adic norm topology. Let $C$ be the commutative condensed ring whose sections on a profinite set $S$ are the continuous maps $S\to\Omega$ with image in one finite intermediate extension of $\mathbf Q_\ell$, with pointwise operations `sk-def-sfb-qlbar-condensed`. For any scheme $T$, let $p_T^*C$ be its coefficient inverse image on the small pro-etale site [sk-def-sfb-pulled-back-coefficients, def-weil-pbc-proetale-site], in the universes of `def-weil-size-convention`. Let $B_T$ be the auxiliary continuous-function ring sheaf defined as follows: on $V\to T$ its sections are continuous functions $|V|\to\Omega$ such that each point has an open neighbourhood on which the image spans a finite-dimensional $\mathbf Q_\ell$-subspace, with precomposition restrictions and pointwise operations. There is a canonical isomorphism of sheaves of commutative rings
$$\theta_T:p_T^*C\xrightarrow{\sim}B_T.$$
For a finite intermediate field $E\subset\Omega$, write $C(-,E)=\underline E$ for the condensed ring of continuous $E$-valued functions `sk-def-sfb-condensed-ring`; the composite $p_T^*C(-,E)\to p_T^*C\xrightarrow{\theta_T}B_T$ of $\theta_T$ with the pullback of the inclusion is, under the canonical continuous-function realization $p_T^*C(-,E)\cong(V\mapsto C(|V|,E))$ `lem-weil-pbc-continuous-coefficient-realizations`, postcomposition of functions with $E\hookrightarrow\Omega$. For every scheme morphism $h:T'\to T$, the square of ring-sheaf maps $\eta_h:p_T^*C\to h_*p_{T'}^*C$ (the coefficient map of [dag-sk-def-sfb-coefficient-morphisms], mate of the canonical pullback comparison) and $B_T\to h_*B_{T'}$ commutes with $\theta_T$ and $h_*\theta_{T'}$; the bottom map is precomposition of functions. No Noetherianity or separatedness hypothesis on $T$ is required. On a geometric fibre in `def-weil-weil-sheaf-complex`, the coefficient ring for strict Weil pairs is $p_T^*C$; this result realizes that ring only. It does not identify a derived category of Weil sheaves with the category of strict pairs.

(SHEAF DAG node `lem-sf-locally-finite-coefficient-ring-realization`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--2]. DAG kind: statement. Placed through `sk-prop-sfb-qlbar-colimit-x` (ancestor-1). DAG status: split. Statement dependencies not drawn: `sk-def-sfb-qlbar-condensed`, `sk-def-sfb-pulled-back-coefficients`, `def-weil-size-convention`, `def-weil-weil-sheaf-complex`, `sk-def-sfb-condensed-ring`, `lem-weil-pbc-continuous-coefficient-realizations`, `sk-def-sfb-coefficient-morphisms`.
