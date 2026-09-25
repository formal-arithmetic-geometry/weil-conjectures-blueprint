+++
id = "lem-fd-as-trace"
kind = "lemma"
title = "Trace function of the Artin–Schreier sheaf"
order = 2883
uses = ["def-fd-additive-character", "def-fd-artin-schreier-sheaf", "def-weil-local-frobenius-trace", "lem-fd-as-cover-affine-line"]
+++
Let $k_0=\mathbf F_q$, fix the nondegenerate additive character
$\psi=\Psi\circ\operatorname{Tr}$ of [def-fd-additive-character],
let $a\in k_0^\times$, and let $\mathcal L_{\psi,ax}$ be the
Artin–Schreier sheaf on
$\mathbf A^1_{k_0}$ attached to the linear function $x\mapsto ax$.
Then the *trace function* of $\mathcal L_{\psi,ax}$ is

$$
t_{\mathcal L_{\psi,ax}}(u)=\psi\bigl(\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)\bigr),
$$

for every closed point $u$ (with the local Frobenius convention of
[def-weil-local-frobenius-trace]); in particular, on the
$\mathbf F_{q^n}$-points of the line,

$$
t_{\mathcal L_{\psi,ax}}(x)=\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(ax)\bigr).
$$

## Proof

Fix a closed point $u$ of $\mathbf A^1_{k_0}$ of degree $n$, with
$u\in\kappa(u)\subset \overline k$ its image and geometric point
$\bar u$, and let $F_u$ be the local Frobenius operator of
[def-weil-local-frobenius-trace] (the $n$-fold iterate of the
geometric Frobenius), so that $F_u(y)=y^{q^n}$ for
$y\in\overline k$. By the affine-line covering
[lem-fd-as-cover-affine-line], the fibre of
$\pi:Y\to\mathbf A^1_{k_0}$, $y\mapsto y^p-y$, over $\bar u$ is
the set

$$
Y_{\bar u}=\{y\in\overline k:\ y^p-y=au\},
$$

which is an $\mathbf F_p$-torsor (the difference of two roots is a
root of $X^p-X$, hence lies in $\mathbf F_p$; the polynomial
$T^p-T-au$ is separable). The stalk
$(\pi_*\overline{\mathbf Q}_\ell)_{\bar u}=\overline{\mathbf Q}_\ell[Y_{\bar u}]$
carries the $\mathbf F_p$-action $\sigma_a:y\mapsto y+a$, the
Frobenius $F_u$ permuting the fibre via $y\mapsto y^{q^n}$, and
$\mathcal L_{\psi,au}$ is the image of the idempotent $e_\psi$ of
[def-fd-artin-schreier-sheaf]. Hence

$$
\operatorname{Tr}\bigl(F_u\mid (\mathcal L_{\psi,au})_{\bar u}\bigr)
=\frac1p\sum_{a\in\mathbf F_p}\psi(a)\cdot\#\operatorname{Fix}\bigl(F_u\circ\sigma_a\bigr),
$$

where $\#\operatorname{Fix}(F_u\circ\sigma_a)$ is the number of
$y\in Y_{\bar u}$ with $(y+a)^{q^n}=y$. Since $au\in\kappa(u)$,
its $q^n$-th power is itself, and by induction on $j$,

$$
y^{p^j}=y+\sum_{0\leq i<j}(au)^{p^i},
\qquad\text{so}\qquad
y^{q^n}=y^{p^{an}}=y+\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au),
$$

(with $q=p^a$); the relation $(y+a)^{q^n}=y^{q^n}+a$ gives
$\#\operatorname{Fix}(F_u\circ\sigma_a)=p$ if
$a=-\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)$ and $0$
otherwise. With the idempotent $e_\psi=\frac1p\sum_a\psi(-a)\sigma_a$
of [def-fd-artin-schreier-sheaf] the trace is therefore

$$
\frac1p\cdot\psi\Bigl(\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)\Bigr)\cdot p
=\psi\bigl(\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)\bigr),
$$

which is the announced formula.
