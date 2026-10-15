+++
id = "det-sp-trace-basic"
kind = "lemma"
title = "Basic properties of the smooth trace"
uses = ["def-pur-smooth-trace", "det-sp-orientation-charts"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and $\Lambda$
admissible.

1. $\operatorname{Tr}_f(K)$ is natural in $K\in\Dctf(Y,\Lambda)$, and it is the
   counit of the adjunction $Rf_!\dashv f^*(-)(d)[2d]$ obtained by transporting
   $Rf_!\dashv f^!$ along $\gamma_f$.
2. For the projection $p_d:\mathbf A^d_Y\to Y$ and $K=\Lambda_Y$,
   $\operatorname{Tr}_{p_d}(\Lambda_Y)$ is the coefficient version of affine-space
   integration, which on each geometric fibre sends the class of the origin to
   $1$.
3. For finite étale $f$ (so $d=0$, and $f^!=f^*$ with $\gamma_f$ the identity
   of the étale adjunction), $\operatorname{Tr}_f(K)$ is summation over the fibres
   $f_*f^*K\to K$.
