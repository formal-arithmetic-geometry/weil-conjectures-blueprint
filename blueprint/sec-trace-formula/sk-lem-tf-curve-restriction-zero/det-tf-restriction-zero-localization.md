+++
id = "det-tf-restriction-zero-localization"
kind = "lemma"
title = "Reduction to a punctured restriction"
order = 3497
uses = ["det-tf-supported-restriction"]
+++
In the situation of [det-tf-supported-restriction], work on the classical étale models:
let $X,Y$ be two copies of the strict localization of the curve at $y$, $T$ the strict
localization of $X\times Y$ at $(y,y)$, and

$$
 H=X\times\{y\},\quad V=\{y\}\times Y,\quad G=\Gamma_{(\Phi_X^m,\mathrm{id})},\quad B=\Delta,
$$

with $j_X:X-y\hookrightarrow X$, $j_Y:Y-y\hookrightarrow Y$,
$f:T-V\hookrightarrow T$ and $g:T-(H\cup V)\hookrightarrow T-V$. Put
$N=(\mathbb D_XK)|_{X-y}$ and $Q=K|_{Y-y}$. Suppose $K_{\bar y}=0$. Then:

1. **(i)** $\mathbb D_XK=Rj_{X*}N$ and $K=j_{Y!}Q$, and
   $P=(\mathbb D_XK\boxtimes K)|_T\simeq Rf_*g_!(N\boxtimes Q)$;
2. **(ii)** $R\Gamma(T,P)=0$ and $R\Gamma(B,b^*P)=0$;
3. **(iii)** under the localization triangles and the identification (i), the supported
   restriction $\rho_{a,b}:R\Gamma_G(T,P)\to R\Gamma_y(B,b^*P)$, shifted by one, is
   identified with the ordinary restriction
   $$
    R\Gamma\bigl(T-(V\cup G),g_!(N\boxtimes Q)\bigr)\longrightarrow
    R\Gamma\bigl(B-y,(N\boxtimes Q)|_{B-y}\bigr).
   $$
   In particular $\rho_{a,b}=0$ in $D(A)$ if and only if this restriction is zero.
