+++
id = "det-pbc-complete-exchange-map"
kind = "definition"
title = "The completed exchange map"
order = 1401
uses = ["det-pbc-complete-towers", "det-pbc-complete-tower-calculus", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits", "sk-def-sfb-base-change-morphism", "sk-prop-sfb-module-pullback-exact"]
+++
Consider a cartesian square of schemes

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

and fix $E/\Ql$ finite.

1. *Base change morphism over $\mathcal O_E$.* For
   $M\in D(X_{\mathrm{proét}},\mathcal O_E)$, the base change morphism
   $\operatorname{Ex}_M\colon g^*Rp_*M\to Rp'_*g'^*M$ is the composite of the unit
   of $p'^*\dashv Rp'_*$, the pullback comparison $p'^*g^*\simeq g'^*p^*$ of the
   square and the counit of $p^*\dashv Rp_*$, exactly as in
   [sk-def-sfb-base-change-morphism] but on the full derived categories of
   $\mathcal O_E$-modules (the module pullbacks are exact,
   [sk-prop-sfb-module-pullback-exact]). The same formula with the levelwise
   functors of [det-pbc-complete-towers] (2) defines
   $\operatorname{Ex}^{\operatorname{Tow}}\colon g^*_{\operatorname{Tow}}Rp^{\operatorname{Tow}}_*
   \to Rp'^{\operatorname{Tow}}_*g'^*_{\operatorname{Tow}}$, and
   $\operatorname{ev}_n\operatorname{Ex}^{\operatorname{Tow}}_{M_\bullet}=
   \operatorname{Ex}_{\operatorname{ev}_nM_\bullet}$ by
   [det-pbc-complete-tower-calculus] (3).
2. *Completed exchange map.* For $K\in D(X_{\mathrm{proét}},\mathcal O_E)$ with
   reductions $K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$,
   the *completed exchange map*
   $$
   \operatorname{Ex}^{\mathrm{comp}}_K\colon g^*_{\mathrm{comp}}Rp_*K\longrightarrow
   Rp'_*g'^*_{\mathrm{comp}}K
   $$
   between the completed inverse images of
   [lemma-weil-pbc-completed-pullback-reduction] is the composite
   $$
   \begin{aligned}
   g^*_{\mathrm{comp}}Rp_*K
   &=R\varprojlim g^*_{\operatorname{Tow}}\operatorname{red}(Rp_*K)
   \xrightarrow{\ \sim\ }R\varprojlim g^*_{\operatorname{Tow}}Rp^{\operatorname{Tow}}_*\operatorname{red}(K)\\
   &\xrightarrow{\ R\varprojlim\operatorname{Ex}^{\operatorname{Tow}}_{\operatorname{red}(K)}\ }
   R\varprojlim Rp'^{\operatorname{Tow}}_*g'^*_{\operatorname{Tow}}\operatorname{red}(K)
   \xrightarrow{\ \sim\ }Rp'_*R\varprojlim g'^*_{\operatorname{Tow}}\operatorname{red}(K)
   =Rp'_*g'^*_{\mathrm{comp}}K,
   \end{aligned}
   $$
   where the first isomorphism is [prop-weil-pbc-direct-image-limits] (2) for $p$
   and the last is the inverse of [prop-weil-pbc-direct-image-limits] (1) for
   $p'$. Its level-$n$ ingredient is the exchange map
   $\operatorname{Ex}_{K_n}\colon g^*Rp_*K_n\to Rp'_*g'^*K_n$, conjugated by
   the projection-formula isomorphism $(Rp_*K)_n\simeq Rp_*K_n$; the
   $\operatorname{Ex}_{K_n}$ are compatible with the transitions $K_{n+1}\to K_n$
   because they are the levels of one morphism of towers.

The completed exchange map is natural in $K$, being built from natural
transformations. It is defined for every $K$. When $K$ is derived complete,
$K\simeq R\varprojlim_nK_n$ and, by
[lemma-weil-pbc-completed-pullback-reduction], $g'^*_{\mathrm{comp}}K$ is the
derived completion of $g'^*K$.
