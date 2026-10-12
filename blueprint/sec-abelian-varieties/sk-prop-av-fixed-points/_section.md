+++
id = "sk-prop-av-fixed-points"
kind = "proposition"
title = "Fixed points of $p$-linear maps are finite"
lean = ["LinearMap.Frobenius.finite_fixedPoints", "LinearMap.Frobenius.natCard_fixedPoints_le"]
order = 568
uses = ["sk-def-av"]
tags = ["sketch"]
+++
Let $k$ be a field of characteristic $p>0$, $V$ a finite-dimensional
$k$-vector space and $F:V\to V$ a $p$-linear endomorphism
($F(\lambda v)=\lambda^pF(v)$, $F(v+w)=F(v)+F(w)$). Then
$V^F=\{v:F(v)=v\}$ is a finite $\F_p$-vector space of dimension
$\le\dim_kV$.
