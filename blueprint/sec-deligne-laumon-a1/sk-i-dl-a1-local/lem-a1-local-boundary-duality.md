+++
id = "lem-a1-local-boundary-duality"
kind = "lemma"
title = "Local boundary duality"
order = 3031
uses = ["def-weil-exceptional-inverse-image", "def-weil-open-closed-recollement", "def-wf-tate-twist", "fix-cor-verdier-exchange", "lem-cbc-open-closed-recollement", "lem-fix-weil-operations", "lem-pod-cohomology-of-dual-over-field", "prop-pur-rational-purity-trace-coherence", "prop-sf-closed-immersion-unit", "prop-sf-closed-unit-all-stages", "prop-sf-localization-all-stages", "prop-sf-open-closed-triangle-all-stages", "prop-weil-open-closed-recollement-adjunctions", "rem-dl-a1-conventions", "thm-coef-qbar-verdier", "thm-pur-rational-and-qbar-purity"]
lean = ["AlgebraicGeometry.exists_linearEquiv_dual_stalk_higherDirectImage"]
+++
In the conventions of [rem-dl-a1-conventions], let
$j:U_0\hookrightarrow C_0$ be a dense open immersion of smooth
curves over $k_0$, let $i:Z_0\hookrightarrow C_0$ be the closed
complement with its reduced structure, and let $F$ be a lisse
$\Qlb$-Weil sheaf on $U_0$, with dual $F^\vee$; write
$A(F)=i^*Rj_*F$ on $Z$. Then, for every missing closed point $s\in Z_0$,
with geometric point $\bar s$, local geometric Frobenius $F_s$ and
$q_s=\#k(s)$, there is a perfect $F_s$-equivariant pairing

$$
(j_*F^\vee)_{\bar s}\otimes(R^1j_*F)_{\bar s}
\longrightarrow\Qlb(-1),
$$

that is, a linear isomorphism
$e:(j_*F^\vee)_{\bar s}\xrightarrow{\sim}(R^1j_*F)_{\bar s}^\vee$ with
$e(F_sa)(F_sb)=q_s\,e(a)(b)$ for all $a,b$; equivalently an isomorphism
$(R^1j_*F)_{\bar s}^\vee\simeq(j_*F^\vee)_{\bar s}(1)$. Here
$j_*$ is the ordinary direct image.
