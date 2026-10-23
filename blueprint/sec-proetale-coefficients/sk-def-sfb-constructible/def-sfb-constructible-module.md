+++
id = "def-sfb-constructible-module"
kind = "definition"
title = "Constructible modules on the pro-étale site"
order = 1242
uses = ["def-sfb-locally-finitely-presented", "def-constructible-stratification"]
lean = ["AlgebraicGeometry.ProEtale.IsConstructibleModuleObject"]
+++
In the situation of [def-sfb-locally-finitely-presented], an $\mathcal R$-module $M$ is
*constructible* if there is a stratification of $X$ [def-constructible-stratification],
with strata given by immersions $g_a\colon X_a\to X$, such that, for every $a$, the
$g_a^*\mathcal R$-module $\operatorname{mapMod}(g_a^*)(M)$ is locally finitely presented
over $g_a^*\mathcal R$ [def-sfb-locally-finitely-presented].
