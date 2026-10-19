+++
id = "lem-wf-lisse-stalk-vanishing"
kind = "lemma"
title = "Lisse sheaves with vanishing geometric stalks"
lean = ["AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.isZero_of_forall_subsingleton_stalk", "AlgebraicGeometry.ProEtale.isZero_adicUpperStar_of_forall_subsingleton_stalk"]
order = 2928
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-module-pushforward-pullback", "sk-lem-coefficient-heart"]
+++
Let $X$ be a scheme and $\overline{\mathbf Q}_{\ell,X}=p_X^*\underline{\Qlb}$ the coefficient
sheaf on $X_{\mathrm{proét}}$ ([sk-def-sfb-pulled-back-coefficients],
[sk-def-sfb-qlbar-condensed]). For a $\overline{\mathbf Q}_{\ell,X}$-module $H$ and a geometric
point $s:\Spec K\to X$, with $K$ algebraically closed, write
$H_s=\Gamma(\Spec K,s^*H)$ for the stalk, $s^*$ being the pullback of module objects
([sk-def-sfb-module-pushforward-pullback]). Call $H$ *lisse* if it is locally free of finite
rank for the pro-étale topology ([sk-lem-coefficient-heart]).

1. If $H$ is lisse and over every point $x\in X$ there is a geometric point $s$ of $X$ with
   $H_s=0$, then $H=0$.
2. Let $g:Z\to X$ be a morphism of schemes such that $g^*H$ is lisse. If $H_s=0$ for every
   geometric point $s$ of $X$, then $g^*H=0$.
