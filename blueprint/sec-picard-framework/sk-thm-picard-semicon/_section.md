+++
id = "sk-thm-picard-semicon"
kind = "theorem"
title = "Semicontinuity and base change"
order = 711
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.Modules.upperSemicontinuous_hFiber"]
tags = ["sketch"]
+++
Let $f:X\to T$ be a proper morphism of finite presentation and $\cF$ an
$\cO_X$-module of finite presentation, flat over $T$. For every integer
$q$ the function
$t\mapsto\dim_{\kappa(t)}H^q(X_t,\cF_t)$ is upper semicontinuous on
$T$, and there are canonical base-change maps
$R^qf_*\cF\otimes\kappa(t)\to H^q(X_t,\cF_t)$. If moreover $T$ is
*reduced* and this function is locally constant, then $R^qf_*\cF$ is
finite locally free (in particular flat) and the base-change maps in
degree $q$ are isomorphisms.
