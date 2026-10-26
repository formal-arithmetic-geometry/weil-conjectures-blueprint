+++
id = "det-sf-cohsm-base-change"
kind = "lemma"
title = "Base change for the exceptional inverse image of a smooth morphism"
order = 2352
uses = ["thm-asd-smooth-tensor", "lem-pur-co-smooth-composition", "sk-prop-geo-p1-adjunction"]
+++
Let $\Lambda$ be a finite $\ell$-primary ring and $f:X\to S$ separated, smooth
of finite type and of pure relative dimension $d$, between schemes of finite
type over $k$. Let $g:S'\to S$ be a morphism of finite type,
$X'=X\times_SS'$, with projections $f':X'\to S'$ and $g':X'\to X$. For
$N\in D(S_{\mathrm{ét}},\Lambda)$ let

$$
\beta_N:g'^*f^!N\longrightarrow f'^!g^*N
$$

be the transpose under $Rf'_!\dashv f'^!$ of
$Rf'_!g'^*f^!N\xrightarrow{\sim}g^*Rf_!f^!N\xrightarrow{g^*\epsilon_N}g^*N$ (inverse
of compact-support base change, then the pulled-back counit). Then:

1. $\beta_N$ is an isomorphism for every $N$; in particular
$\beta_\Lambda:g'^*\omega_f\xrightarrow{\sim}\omega_{f'}$;
2. for every $N$ the square formed by $g'^*$ of the tensor map
$f^*N\otimes^{\mathbf L}\omega_f\to f^!N$, the tensor map for $f'$ at $g^*N$,
$\beta_N$ and $1\otimes\beta_\Lambda$ (via $g'^*f^*N=f'^*g^*N$) commutes.
