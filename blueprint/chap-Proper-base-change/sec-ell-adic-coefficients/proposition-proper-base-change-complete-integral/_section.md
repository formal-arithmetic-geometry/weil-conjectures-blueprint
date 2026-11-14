+++
id = "proposition-proper-base-change-complete-integral"
kind = "proposition"
title = "Proper base change for complete complexes"
order = 417
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness"]
+++
Let $p:X\to Y$ be proper, let $g:Y'\to Y$ be any morphism, and let
$p':X'\to Y'$ and $g':X'\to X$ be the projections from $X'=X\times_YY'$.
Fix a finite extension $E/\mathbf Q_\ell$. Suppose that
$K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ is derived $\pi_E$-complete and that
each reduction

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}
(\mathcal O_E/\pi_E^n)_X
$$

belongs to $D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$. Then
$Rp_*K$ is derived $\pi_E$-complete, and there are canonical isomorphisms

$$
\hat g^*Rp_*K\simeq R\varprojlim_n g^*Rp_*K_n,
\qquad
Rp'_*\hat g'^*K\simeq R\varprojlim_n Rp'_*g'^*K_n,
$$

and under them the derived limit of the base change maps
$g^*Rp_*K_n\to Rp'_*g'^*K_n$ is an isomorphism
$\hat g^*Rp_*K\xrightarrow{\ \sim\ }Rp'_*\hat g'^*K$.
