+++
id = "lem-sc-fixed-points-finite"
kind = "lemma"
title = "Fixed points of $p$-linear maps"
lean = ["LinearMap.Frobenius.finite_fixedPoints", "LinearMap.Frobenius.natCard_fixedPoints_le"]
order = 1431
+++
Let $k$ be a field of characteristic $p>0$, $V$ a
finite-dimensional $k$-vector space and $F:V\to V$ a
$p$-linear endomorphism ($F(\lambda v)=\lambda^pF(v)$,
$F(v+w)=F(v)+F(w)$). Then the fixed-point set
$V^F=\{v\in V:F(v)=v\}$ is a finite $\mathbf F_p$-vector space
of dimension at most $\dim_kV$.
