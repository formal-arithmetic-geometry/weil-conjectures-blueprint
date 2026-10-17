+++
id = "det-tf-supported-restriction"
kind = "definition"
title = "Supported class and supported restriction"
uses = ["thm-trf-kunneth-verdier", "lem-trf-exceptional-internal-hom-exchange"]
+++
Let $X_0$ be a smooth curve over $k_0$, $X=X_0\times_{k_0}k$ with $k$-linear Frobenius $\Phi_X$,
$K\in\Dctf(X,A)$, $m\geq1$, and $y$ a fixed point of
$\Phi_X^m$. Let $a=(\Phi_X^m,\operatorname{id}_X)$ and $b=\Delta_X$ be the transposed
Frobenius graph and the diagonal, closed immersions $X\to X\times X$; their intersection is the finite fixed scheme of
$\Phi_X^m$, so on $T$ below it is the single point $y$. Let $T$ be the strict localization of $X\times X$
at $(y,y)$, and put $P=(\mathbb D_XK\boxtimes K)|_T$, where $\mathbb D_XK=\cHom_A(K,\omega_X)$.

1. **(Supported class.)** By the Künneth–Verdier isomorphism ([thm-trf-kunneth-verdier])
   and the exchange of exceptional pullback with internal Hom
   ([lem-trf-exceptional-internal-hom-exchange]),
   $$
    a^!(\mathbb D_XK\boxtimes K)\simeq R\mathcal Hom\bigl((\Phi_X^m)^*K,K\bigr).
   $$
   For $v:(\Phi_X^m)^*K\to K$, the *supported class* $[v]\in H^0R\Gamma_a(T,P)$ is the
   image of $v$ under
   $\operatorname{Hom}((\Phi_X^m)^*K,K)\simeq H^0R\Gamma(X,a^!(\mathbb D_XK\boxtimes K))
   =H^0R\Gamma_a(X\times X,\mathbb D_XK\boxtimes K)\to H^0R\Gamma_a(T,P)$.
2. **(Supported restriction.)** The *supported restriction*
   $$
    \rho_{a,b}:R\Gamma_a(T,P)\longrightarrow R\Gamma_y(b,b^*P)
   $$
   is $R\Gamma(T,-)$ of the composite $Ra_*a^!P\to P\to Rb_*b^*P$ of the counit of
   $Ra_*\dashv a^!$ and the unit of $b^*\dashv Rb_*$, followed by the factorization through
   local cohomology at $y$: after restriction to $b$, the source $b^*Ra_*a^!P$ is supported
   on $a\cap b=\{y\}$. Equivalently, $\rho_{a,b}$ is the ordinary pullback along $b$ of the
   support object, followed by the exchange morphism to local cohomology with support in
   the intersection.
