+++
id = "sk-prop-av-fixed-base-change"
kind = "proposition"
title = "Fixed points are unchanged by algebraically closed base change"
lean = ["LinearMap.Frobenius.bijective_tmul_fixedPoints"]
order = 556
uses = ["sk-def-av", "sk-prop-av-lang-steinberg"]
tags = ["sketch"]
+++
Let $k\subseteq k'$ be an extension of algebraically closed fields of
characteristic $p>0$, $V$ a finite-dimensional $k$-vector space and
$F:V\to V$ $p$-linear, with base change
$F'=F\otimes\sigma_{k'}$ on $V\otimes_kk'$. Then
$V^F\to(V\otimes_kk')^{F'}$, $v\mapsto v\otimes1$, is an isomorphism
of $\F_p$-vector spaces.
