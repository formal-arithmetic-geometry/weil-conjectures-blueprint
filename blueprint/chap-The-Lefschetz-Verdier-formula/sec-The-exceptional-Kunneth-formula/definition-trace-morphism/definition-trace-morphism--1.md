+++
id = "definition-trace-morphism--1"
kind = "definition"
title = "Trace morphism (1)"
name_showing = false
order = 913001
aliases = ["bp-r276-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.evaluationKernel", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceMap"]
uses = ["definition-constructible-sheaves", "definition-correspondence", "definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "theorem-existence-exceptional-inverse-image", "proposition-composition-base-change-rf-shriek", "proposition-composition-open-restriction-compactifications-f"]
+++
In the setting of Lemma [lemma-external-duality-trace-morphism], let
$e_K:P_X\to R\Delta_{X*}\omega_X$ be adjoint to the evaluation
$\Delta_X^*P_X=K\otimes^{\mathbf L} \mathbb D_XK\to\omega_X$. The
*trace morphism* is the composite

$$
\mathcal H_c(K)\simeq c^!P_X\xrightarrow{c^!e_K}c^!R\Delta_{X*}\omega_X
\xrightarrow{\sim}Ri_{c*}d_c^!\omega_X
\simeq Ri_{c*}\omega_{\Fix(c)}
$$

of the second isomorphism of the lemma, $c^!e_K$, exceptional base
change for the proper map $\Delta_X$, and the composition of
exceptional inverse images $d_c^!a_X^!=a_{\Fix(c)}^!$.
