+++
id = "sk-thm-picard-coherence"
kind = "theorem"
title = "Coherence of the higher direct images"
order = 710
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.Scheme.Modules.isFinitePresentation_higherDirectImage"]
tags = ["sketch"]
+++
Let $f:X\to T$ be a proper morphism of finite presentation and $\cF$ an
$\cO_X$-module of finite presentation, flat over $T$ (the standing
assumptions of this subsubsection). Then:

- **(a)** $Rf_*\cF$ is perfect: locally on $T$ it is represented by a
bounded complex of finite free $\cO_T$-modules whose formation commutes
with every base change $T'\to T$. In particular every point of $T$ has
an open neighbourhood $U$ such that $R^qf_*\cF|_U=0$ for all $q>d_U$,
where $d_U<\infty$ bounds the dimensions of the fibres of $f$ over $U$.
- **(b)** If $T$ is locally Noetherian, $R^qf_*\cF$ is a coherent
$\cO_T$-module for all $q$; for this, flatness of $\cF$ over $T$ is not
needed.
- **(c)** If $T$ is quasi-compact, $R^qf_*\cF=0$ for all $q\gg0$.
