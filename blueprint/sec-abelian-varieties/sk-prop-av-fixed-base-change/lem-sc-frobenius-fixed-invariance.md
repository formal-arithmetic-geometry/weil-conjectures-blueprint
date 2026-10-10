+++
id = "lem-sc-frobenius-fixed-invariance"
kind = "lemma"
title = "Fixed points under algebraically closed base change"
lean = ["LinearMap.Frobenius.bijective_tmul_fixedPoints"]
order = 568
uses = ["lem-sc-lang-steinberg"]
+++
Let $k\subseteq k'$ be an extension of algebraically closed
fields of characteristic $p>0$, $V$ a finite-dimensional
$k$-vector space, and $F:V\to V$ a $p$-linear endomorphism
($F(\lambda v)=\lambda^pF(v)$, $F(v+w)=F(v)+F(w)$). Write
$V^F=\{v\in V:F(v)=v\}$ and let
$F':=F\otimes\sigma_{k'}:V\otimes_kk'\to V\otimes_kk'$ be the
base-changed $p$-linear map, where $\sigma_{k'}(x)=x^p$ is the
Frobenius of $k'$. Then the natural map

$$
V^F\longrightarrow(V\otimes_kk')^{F'},\qquad v\longmapsto v\otimes1,
$$

is an isomorphism of $\mathbf F_p$-vector spaces.
