+++
id = "lem-wft-kunneth-compatibilities"
kind = "lemma"
title = "Compact-support Künneth: Weil structures and traces"
order = 3938
uses = ["thm-sf-kunneth-relative", "fix-prop-projection-formula", "sk-prop-sf-cbc", "sk-def-sf-weil-complexes", "prop-pur-weil-equivariance-compatibilities", "sk-def-sp-trace", "sk-prop-sp-trace-composition", "sk-prop-sp-purity-bc"]
+++
Let $S$ be a separated finite-type $k$-scheme, $a:X\to S$ and $b:Y\to S$
separated of finite type, $u,v$ the projections of $X\times_SY$ and
$c=a\circ u=b\circ v$. Let $\Lambda$ be a field coefficient ring
($E$ or $\overline{\mathbf Q}_\ell$) and $K\in\Dbc(X,\Lambda)$,
$L\in\Dbc(Y,\Lambda)$, $K\boxtimes_SL=u^*K\otimes^Lv^*L$.

1. The composite

   $$
   \kappa_{K,L}:\ Rc_!(K\boxtimes_SL)\cong Ra_!Ru_!(u^*K\otimes v^*L)
   \cong Ra_!(K\otimes Ru_!v^*L)\cong Ra_!(K\otimes a^*Rb_!L)
   \cong Ra_!K\otimes Rb_!L
   $$

   of the composition isomorphism, the projection formula for $u$ (in
   the form of [fix-prop-projection-formula]), compact-support base change
   ([sk-prop-sf-cbc]) for the square $(u,v,a,b)$ and the projection formula
   for $a$ is an isomorphism, natural in $K,L$. It agrees with the
   relative Künneth isomorphism $\kappa^{\mathrm{rel}}_{K,L}$ of
   [thm-sf-kunneth-relative] for $B=S$, after the symmetry of $\otimes^L$.
2. If $S,X,Y,a,b$ come from $k_0$-schemes and $K,L$ carry Weil structures
   ([sk-def-sf-weil-complexes]), then $K\boxtimes_SL$ carries the product
   Weil structure and $\kappa_{K,L}$ is an isomorphism of Weil complexes.
3. If $a$ and $b$ are smooth of pure relative dimensions $d$ and $e$, then
   under $\kappa$ for $K=\Lambda_X(d)[2d]$, $L=\Lambda_Y(e)[2e]$ the smooth
   trace $\operatorname{Tr}_c$ of [sk-def-sp-trace] corresponds to
   $\operatorname{Tr}_a\otimes\operatorname{Tr}_b$.
