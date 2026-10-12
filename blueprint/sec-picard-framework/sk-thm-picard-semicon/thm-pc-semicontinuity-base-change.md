+++
id = "thm-pc-semicontinuity-base-change"
kind = "theorem"
title = "Semicontinuity and base change"
order = 682
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "def-pc-perfect-complex", "lem-pc-flat-complex-derived-pullback", "lem-pc-rf-perfect-base-change"]
lean = ["AlgebraicGeometry.Scheme.Modules.upperSemicontinuous_hFiber", "AlgebraicGeometry.Scheme.Modules.exists_isFiniteLocallyFreeOfRank_higherDirectImage_of_isLocallyConstant"]
+++
Let $f:X\to T$ be a proper morphism of finite presentation and let
$\mathcal F$ be an $\mathcal O_X$-module of finite presentation, flat
over $T$. For $t\in T$ write $X_t=X\times_T\operatorname{Spec}\kappa(t)$
and let $\mathcal F_t$ be the pullback of $\mathcal F$ to $X_t$. Fix an
integer $q$.

1. For every $t\in T$ the space $H^q(X_t,\mathcal F_t)$ is finite
   dimensional over $\kappa(t)$, and there is a canonical base-change map
   $$
   \varphi^q(t):\;R^qf_*\mathcal F\otimes_{\mathcal O_T}\kappa(t)
   \longrightarrow H^q(X_t,\mathcal F_t).
   $$
2. The function
   $\beta^q(t)=\dim_{\kappa(t)}H^q(X_t,\mathcal F_t)$ is upper
   semicontinuous on $T$.
3. If $T$ is reduced and $\beta^q$ is locally constant on $T$, then
   $R^qf_*\mathcal F$ is a finite locally free $\mathcal O_T$-module, of
   rank $\beta^q(t)$ on a neighbourhood of each $t\in T$ (in particular
   it is flat over $T$), and $\varphi^q(t)$ is an isomorphism
   for every $t\in T$.

The reducedness hypothesis in (3) cannot be omitted: over a
non-reduced base, $T$ may even be a single point (so that $\beta^q$ is
trivially constant) while $R^qf_*\mathcal F$ is not flat.
