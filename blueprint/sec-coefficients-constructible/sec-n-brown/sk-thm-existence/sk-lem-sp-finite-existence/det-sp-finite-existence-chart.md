+++
id = "det-sp-finite-existence-chart"
kind = "lemma"
title = "The finite Brown adjoint on a coordinate chart"
order = 2913
uses = ["cor-pur-affine-space-purity", "lem-pur-co-smooth-etale-locality", "lem-amb-etale-adjoint-locality", "cor-amb-affine-space-adjunction", "det-sf-mate-open-restriction"]
+++
Let $\Lambda_n=\mathbf Z/\ell^n\mathbf Z$, let $f:X\to Y$ be smooth of pure relative
dimension $d$, and let $j:U\hookrightarrow X$ be open with $f j=p_d\circ e$,
$e:U\to\mathbf A^d_Y$ étale (separated, of finite type). For
$K\in\Dctf(Y,\Lambda_n)$:

1. $e_!\dashv e^*$, so $e^!\simeq e^*$ with counit
$\sigma:e_!e^*\to\mathrm{id}$, which on geometric stalks is the sum over the
points of the fibre of $e$;
2. $Rp_{d!}\dashv p_d^*(-)(d)[2d]$, with counit
$\tau_K:Rp_{d!}p_d^*K(d)[2d]\simeq K\otimes^{\mathbf L}Rp_{d!}\Lambda_n(d)[2d]
\xrightarrow{1\otimes\operatorname{Tr}_{p_d}}K$;
3. there is a unique isomorphism
$j^*f^!K\simeq e^*p_d^*K(d)[2d]$ under which the counit of
$R(fj)_!\dashv(fj)^!$ (transported via $j^*f^!\simeq(fj)^!$) becomes
$\tau_K\circ Rp_{d!}(\sigma_{p_d^*K(d)[2d]})$.
