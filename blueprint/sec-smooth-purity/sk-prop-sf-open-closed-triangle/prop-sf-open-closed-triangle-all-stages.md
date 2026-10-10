+++
id = "prop-sf-open-closed-triangle-all-stages"
kind = "theorem"
title = "The open–closed triangle at every coefficient stage"
order = 1851
tags = ["latex:proposition"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-complete", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-frobenius-detailed", "def-weil-integral-rational-qbar-compact-support", "def-weil-open-closed-recollement", "def-weil-rationalization-karoubi", "def-weil-weil-sheaf-complex", "fix-lem-exchanges", "lem-cbc-completed-extension-zero-comparison", "lem-cbc-open-closed-recollement", "lem-cbc-proetale-extension-zero-comparison", "lem-sf-proetale-constructible-origin", "lem-weil-pbc-comparison-pullback", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-open-closed-recollement-adjunctions", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-descent-functors", "prop-weil-pbc-direct-image-limits", "prop-weil-pbc-rational-transport", "prop-weil-pbc-roos-triangle", "prop-weil-pbc-scalar-extension", "prop-weil-pbc-site-comparison-finite-level", "thm-weil-pbc-verdier-axioms"]
+++
Let $X$ be a separated finite-type $k$-scheme, let $i:Z\hookrightarrow X$ be
a closed immersion and $j:U\hookrightarrow X$ the complementary open
immersion. Let $\Lambda$ be one of the coefficient stages
$A_{E,n},\mathcal O_E,E,\Qlb$, with the categories $D^b_c(-,\Lambda)$
([def-weil-derived-complete-integral-detailed],
[def-weil-rationalization-karoubi],
[def-weil-algebraically-closed-coefficients]), the pullbacks $i^*,j^*$ of
[def-weil-derived-pullback-tensor-hom], the direct image $i_*=Ri_*$ of
[def-weil-derived-direct-image] and the extension by zero $j_!=Rj_!$ of
[def-weil-integral-rational-qbar-compact-support]. For
$K\in D^b_c(X,\Lambda)$ the open counit and the closed unit extend to a
distinguished triangle, the open–closed recollement triangle of
[def-weil-open-closed-recollement],
$$
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\longrightarrow j_!j^*K[1].
$$
Moreover $\operatorname{Hom}(j_!j^*K[m],i_*i^*K)=0$ for all $m$; hence the
third arrow is uniquely determined by the other two and the triangle is
functorial in $K$. If $X=X_0\otimes_{k_0}k$, $Z$, $U$ come from
$k_0$-schemes, $\Lambda\in\{E,\Qlb\}$ and $K$ is a Weil complex
([def-weil-weil-sheaf-complex]), then all three arrows are
Weil-equivariant.
