+++
id = "cor-zl-rfshriek-sheaf"
kind = "theorem"
title = "Cohomology-sheaf form of the direct-image theorem"
order = 4321
lean = ["AlgebraicGeometry.hasDirectImageWeightBound_over_finiteField"]
uses = ["def-weil-complex-weights", "def-weil-weil-sheaf-complex", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "lem-zl-finite-pushforward", "lem-zl-quasi-finite", "lem-zl-morphism-open-closed-reduction", "lem-zl-open-closed-weight", "lem-zl-shriek-composition", "thm-zl-relative-line-step", "sk-lem-coefficient-heart", "thm-zl-relative-noether"]
+++
Let $f:X_0\to Y_0$ be a separated finite-type morphism of
$k_0$-schemes, with $Y_0$ separated of finite type over $k_0$. If a
constructible $\Qlb$-Weil sheaf $\mathcal F$ on $X_0$
([sk-lem-coefficient-heart], [def-weil-weil-sheaf-complex]) is $\iota$-mixed of
weights at most $w$, then
$R^if_!\mathcal F$ is $\iota$-mixed of weights at most $w+i$ for
every $i$.
