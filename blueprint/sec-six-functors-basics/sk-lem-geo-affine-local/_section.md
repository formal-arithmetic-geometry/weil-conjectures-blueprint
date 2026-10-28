+++
id = "sk-lem-geo-affine-local"
kind = "lemma"
title = "Affine space and étale localization"
order = 2621
uses = ["sk-prop-sf-existence"]
tags = ["sketch"]
+++
Let $S$ be of finite type over the base field $k$.

1. For the projection $p_d:\mathbf A^d_S\to S$, the right adjoint $p_d^!$ of
   $Rp_{d!}:D_{\mathrm{class}}((\mathbf A^d_S)_{\mathrm{proét}},\Lambda)\to D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$
   is $p_d^*(d)[2d]$, with unit and counit compatible with base change.
2. Let $f:X\to S$ be separated of finite type (with $f^!$ the right adjoint of
   $Rf_!$ of [sk-prop-sf-existence]), let
   $N\in D_{\mathrm{class}}(S_{\mathrm{proét}},\Lambda)$, and let $u:U\to X$ be
   separated, étale and of finite type. There is a canonical identification

   $$
   u^*f^!N=(fu)^!N.
   \qquad\text{(G10)}
   $$

   It is compatible with units, counits, composition, and further étale
   localization.
