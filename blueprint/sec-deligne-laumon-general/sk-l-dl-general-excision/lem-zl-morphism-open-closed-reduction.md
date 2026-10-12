+++
id = "lem-zl-morphism-open-closed-reduction"
kind = "lemma"
title = "Open–closed reduction for the direct-image assertion"
order = 3120
uses = ["def-weil-complex-weights", "def-weil-open-closed-recollement", "def-weil-punctual-weights", "lem-a1-mixed-direct-summand", "lem-sp-long-exact-of-triangle", "lem-weil-heart-short-exact-triangles", "lem-zl-complex-extension", "lem-zl-finite-pushforward", "lem-zl-open-closed-weight", "prop-functor-package", "prop-sf-open-closed-triangle-all-stages"]
+++
For a separated finite-type morphism $f_0:X_0\to Y_0$ of separated
finite-type $k_0$-schemes, say that $f_0$ satisfies the
*direct-image assertion* if, for every $w\in\mathbf R$ and every
constructible Weil sheaf $\mathcal F$ on $X_0$ which is $\iota$-mixed of
weights at most $w$ ([def-weil-punctual-weights]), the sheaf
$R^rf_{0!}\mathcal F$ is $\iota$-mixed of weights at most $w+r$ for
every $r$; say that $f_0$ satisfies the *complex form* of the assertion
if $Rf_{0!}$ carries $D_{\le w}(X_0)$ into $D_{\le w}(Y_0)$ for every
$w$ ([def-weil-complex-weights]).

1. *(Source.)* Let $j_0:U_0\hookrightarrow X_0$ be open with closed
   complement $i_0:Z_0\hookrightarrow X_0$. If the direct-image
   assertion (resp. its complex form) holds for $f_0j_0$ and $f_0i_0$,
   it holds for $f_0$.
1. *(Target.)* Let $j'_0:V_0\hookrightarrow Y_0$ be open with closed
   complement $i'_0:T_0\hookrightarrow Y_0$, and let
   $f_{V}:f_0^{-1}(V_0)\to V_0$, $f_T:f_0^{-1}(T_0)\to T_0$ be the
   restrictions of $f_0$. If the direct-image assertion (resp. its
   complex form) holds for $f_V$ and $f_T$, it holds for $f_0$.
   By induction, the same holds for any finite stratification of $Y_0$
   by locally closed pieces built from successive open–closed
   decompositions.
1. *(Coefficients.)* Fix $f_0$ and $w$, and let
   $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ be an exact
   sequence of constructible Weil sheaves on $X_0$. If
   $R^rf_{0!}\mathcal F'$ and $R^rf_{0!}\mathcal F''$ are $\iota$-mixed
   of weights at most $w+r$ for every $r$, so is $R^rf_{0!}\mathcal F$.
   By induction on the length, the same holds for a finite filtration of
   $\mathcal F$ by Weil subsheaves.
