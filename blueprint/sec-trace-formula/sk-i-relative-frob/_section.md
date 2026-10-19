+++
id = "sk-i-relative-frob"
kind = "lemma"
title = "Relative Frobenius comparison"
order = 2631
uses = ["sk-d-relative-frob", "sk-d-setup", "sk-d-weil"]
lean = ["AlgebraicGeometry.ProEtale.isFinite_relativeFrobenius", "AlgebraicGeometry.ProEtale.isUniversalHomeomorphism_relativeFrobenius"]
tags = ["sketch"]
+++
Here $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$, $A$ is a finite
commutative $\ell$-primary ring, and $\Phi_X$ denotes the scheme Frobenius of
$X=X_0\times_{k_0}k$, as in Definition [sk-d-weil].

Let $f_0:X_0\to Y_0$ be a morphism of separated schemes of finite
type over $k_0$, write $f:X\to Y$ for its geometric base change, and
let $m\geq1$. Put

$$
 X'_m=Y\times_{\Phi_Y^m,Y,f}X,
 \quad p_m:X'_m\to X,\quad f'_m:X'_m\to Y,
 \quad r_m=(f,\Phi_X^m):X\to X'_m,
$$

where $p_m$ and $f'_m$ are the two projections.

1. **(1)** The relative Frobenius $r_m$ is a finite universal homeomorphism,
$p_mr_m=\Phi_X^m$ and $f'_mr_m=f$, and there are natural isomorphisms
of functors $\Dctf(X,A)\to\Dctf(Y,A)$

$$
\begin{aligned}
 \theta_{f,m}:(\Phi_Y^m)^*Rf_!K
 &\simeq Rf'_{m!}p_m^*K
 \xrightarrow{Rf'_{m!}\eta_{r_m}}
 Rf'_{m!}Rr_{m*}r_m^*p_m^*K\\
 &\simeq Rf_!(\Phi_X^m)^*K,
\end{aligned}
$$

compatible with iteration in $m$.

1. **(2)** For a Frobenius correspondence $\psi:\Phi_X^*K\to K$ on
$K\in\Dctf(X,A)$, the object $L=Rf_!K$ of $\Dctf(Y,A)$ carries the
Frobenius correspondence $\psi'=Rf_!\psi\circ\theta_{f,1}:\Phi_Y^*L\to L$,
and its iterates are

$$
 \psi'_m=Rf_!\psi_m\circ\theta_{f,m}.
$$

1. **(3)** The composition isomorphism
$R\Gamma_c(Y,L)\simeq R\Gamma_c(X,K)$ in $D^b(A)$ intertwines the
global operators $T_{c_m}(\psi'_m)$ on $Y$ and $T_{c_m}(\psi_m)$ on
$X$ of Definition [sk-d-weil].

1. **(4)** At $y\in Y_0(\mathbf F_{q^m})$, compact-support base change
identifies $(L_{\bar y},\psi'_{m,\bar y})$ with

$$
 \left(R\Gamma_c(X_{\bar y},K|_{X_{\bar y}}),
 T_{c_1}(\psi_m|_{X_{\bar y}})\right),
$$

where the fibre is regarded as a scheme over $\mathbf F_{q^m}$, with
the $q^m$-power Frobenius as its scheme Frobenius.
