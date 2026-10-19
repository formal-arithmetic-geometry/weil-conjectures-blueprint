+++
id = "prop-sf-open-closed-triangle-all-stages"
kind = "theorem"
title = "The open–closed triangle for every admissible coefficient ring"
lean = ["AlgebraicGeometry.WeilComplex.exists_distTriang_openClosed"]
order = 2195
tags = ["latex:proposition"]
uses = ["sk-def-sf-setting", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-bounded-constructible", "sk-def-sf-operations", "sk-prop-sf-open-closed-triangle", "sk-thm-existence", "sk-lem-integral-models", "sk-def-sf-weil-complexes", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-frobenius-detailed", "def-weil-open-closed-recollement", "def-weil-weil-sheaf-complex", "fix-lem-exchanges", "lem-cbc-open-closed-recollement", "lem-cbc-proetale-extension-zero-comparison", "lem-sf-proetale-constructible-origin", "lem-weil-pbc-comparison-pullback", "prop-weil-open-closed-recollement-adjunctions", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-site-comparison-finite-level"]
+++
Let $X$ be a separated finite-type $k$-scheme, let $i:Z\hookrightarrow X$ be
a closed immersion and $j:U\hookrightarrow X$ the complementary open
immersion. Let $\Lambda$ be one of the coefficient rings
$A_{E,n},\mathcal O_E,E,\Qlb$, regarded as condensed rings, with the categories
$D^b_c(-,\Lambda)\subseteq D(-_{\mathrm{proét}},\Lambda)$ of [sk-def-sf-setting].
Use the pullbacks $i^*,j^*$ of $\Lambda$-modules, the direct image $i_*=Ri_*$
and the extension by zero $j_!$ ([sk-def-sf-operations]). For
$K\in D^b_c(X,\Lambda)$ the open counit and the closed unit extend to a
distinguished triangle in $D(X_{\mathrm{proét}},\Lambda)$, the open–closed
recollement triangle of [def-weil-open-closed-recollement],
$$
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\longrightarrow j_!j^*K[1],
$$
all of whose vertices lie in $D^b_c(X,\Lambda)$.
Moreover $\operatorname{Hom}(j_!j^*K[m],i_*i^*K)=0$ for all $m$; hence the
third arrow is uniquely determined by the other two and the triangle is
functorial in $K$. If $X=X_0\otimes_{k_0}k$, $Z$, $U$ come from
$k_0$-schemes, $\Lambda\in\{E,\Qlb\}$ and $K$ is a Weil complex
([sk-def-sf-weil-complexes], [def-weil-weil-sheaf-complex]), then all three
arrows are Weil-equivariant.
