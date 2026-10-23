+++
id = "sk-cor-sbc-applications"
kind = "corollary"
title = "Open direct images and smooth product families"
order = 2498
uses = ["sk-thm-sbc-coefficients"]
tags = ["sketch"]
+++
Let $\Lambda$ be an admissible coefficient ring.

1. **(1)** If $j:U\hookrightarrow Y$ is an open immersion and
   $g:Y'\to Y$ is smooth, with induced $j':U'\hookrightarrow Y'$
   and $u:U'\to U$, then for $K\in\Dctf(U,\Lambda)$ there is an
   isomorphism in $\Dctf(Y',\Lambda)$

   $$
   g^*Rj_*K\xrightarrow{\sim}Rj'_*u^*K.
   $$

2. **(2)** Let $S$ be smooth of finite type over $k$, let
   $a:X\to\operatorname{Spec}k$, and let $a_S:X\times_kS\to S$,
   $v:X\times_kS\to X$ and $b:S\to\operatorname{Spec}k$ be the
   projections. Then for $K\in\Dctf(X,\Lambda)$ there is an
   isomorphism in $\Dctf(S,\Lambda)$

   $$
   b^*Ra_*K\xrightarrow{\sim}Ra_{S,*}v^*K.
   $$

In (2), $Ra_*K$ is the cohomology of $X$ as an object on
$(\operatorname{Spec}k)_{\mathrm{pro\acute et}}$, with its coefficient and Galois
structures; so the constant family $X\times_kS\to S$ has the
pulled-back cohomology object even when $X$ is not proper.
