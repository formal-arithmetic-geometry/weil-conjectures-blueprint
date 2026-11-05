+++
id = "proposition-composition-base-change-rf-shriek--5"
kind = "proposition"
title = "Independence of the base-change comparison"
order = 516006
aliases = ["bp-r157-5"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_eq_baseChange"]
uses = ["proposition-composition-base-change-rf-shriek--4", "proposition-construction-independence-rf-shriek", "definition-compactification-refinement"]
+++
For $\Lambda=\Qbarl$ in the shared context, the base change map of
[proposition-composition-base-change-rf-shriek--4] is independent of the
compactifications used to compute it. More precisely, choose compactifications
$f=pj$ and $f'=p'j'$ and a morphism $w:\overline X'\to\overline X$ such that
the squares with $(u,j',j,w)$ and $(w,p',p,v)$ are cartesian. After identifying
$Rf_!$ with $Rp_*j_!$ and $Rf'_!$ with $Rp'_*j'_!$ by the compactification
comparisons, $\Ex_!$ is the composite
$$
v^*Rp_*j_!\longrightarrow Rp'_*w^*j_!\simeq Rp'_*j'_!u^*.
$$
In particular it agrees with the map computed using a compactification and
its base change.
