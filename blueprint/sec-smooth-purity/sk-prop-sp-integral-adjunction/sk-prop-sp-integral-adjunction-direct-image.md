+++
id = "det-sp-integral-direct-image-tower"
kind = "lemma"
title = "Tower description of the integral compactly supported direct image"
uses = ["det-sp-normalized-equivalence", "det-sp-tower-shriek-levels", "det-sp-tower-bound-uniform", "det-sp-reduction-direct-image"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, with a
compactification $f=\bar f\circ j$, and $M\in\Dbc(X,\mathcal O_E)$.

1. The tower $Rf_{!,\bullet}\operatorname{red}_XM$ is normalized constructible, with
   the Tor bounds of $M$ widened by $2d$.
2. There is a canonical isomorphism in $\Dbc(Y,\mathcal O_E)$
   $$
   Rf_{!,\mathcal O_E}M\simeq R\varprojlim_nRf_{!,\mathcal O_E/\ell^n}(M/\ell^n),
   $$
   where $Rf_{!,\mathcal O_E}=R\bar f_*j_!$, independent of the
   compactification; consequently
   $(Rf_{!,\mathcal O_E}M)\otimes^{\mathbf L}_{\mathcal O_{E,Y}}\mathcal O_{E,Y}/\ell^n\simeq
   Rf_{!,\mathcal O_E/\ell^n}(M/\ell^n)$ and
   $\operatorname{red}_YRf_{!,\mathcal O_E}M\simeq Rf_{!,\bullet}\operatorname{red}_XM$.
3. $f^*_{\mathcal O_E}K$ has reductions $f^*_{\mathcal O_E/\ell^n}(K/\ell^n)$, and for
   $K\in\Dbc(Y,\mathcal O_E)$ the projection formula
   $Rf_{!,\mathcal O_E}(M\otimes^{\mathbf L}f^*_{\mathcal O_E}K)\simeq Rf_{!,\mathcal O_E}M\otimes^{\mathbf L}K$
   holds in $\Dbc(Y,\mathcal O_E)$.
