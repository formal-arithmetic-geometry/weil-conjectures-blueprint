+++
id = "prop-trf-rational-frobenius-integral-model"
kind = "theorem"
title = "Integral models of rational Frobenius operators"
order = 2301
tags = ["latex:proposition"]
uses = ["def-trf-coefficient-conventions", "def-trf-frobenius-coefficient-morphism", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-scheme-frobenius", "def-weil-derived-complete-integral-detailed", "def-weil-derived-pullback-tensor-hom", "def-weil-global-geometric-frobenius", "def-weil-integral-rational-qbar-compact-support", "def-weil-pbc-adic-coefficient-datum", "def-weil-rationalization-karoubi", "def-weil-weil-sheaf-complex", "lem-trf-absolute-frobenius-site", "lem-trf-frobenius-operator-compact-description", "prop-trf-graph-frobenius-operator", "prop-trf-scheme-galois-comparison", "prop-weil-pbc-rational-transport", "thm-trf-frobenius-fixed-points"]
+++
Fix the global finite-field datum $p,a,q,k_0,k$ and the coefficient
conventions of [def-trf-coefficient-conventions], with $E$, $\mathcal O_E$,
a uniformizer $\varpi=\varpi_E$ and $A_n=A_{E,n}=\mathcal O_E/\varpi^n$.
Let $X_0$ be a separated finite-type $k_0$-scheme, $X=X_0\times_{k_0}k$,
$g_\gamma$ the geometric-Frobenius automorphism and $\Phi$ the $q$-power
scheme Frobenius of [def-trf-scheme-frobenius], and $\kappa^{(m)}$ the
comparison isomorphisms of [prop-trf-scheme-galois-comparison].

Let $K_{\mathcal O}\in D^b_c(X,\mathcal O_E)$ be an integral object
([def-weil-derived-complete-integral-detailed]) whose reductions
$K_n=K_{\mathcal O}\otimes^L_{\mathcal O_E}A_n$ lie in $D^b_{ctf}(X,A_n)$,
and let $K_E$ be the same object of the rationalized category
$D^b_c(X,E)=D^b_c(X,\mathcal O_E)[1/\varpi]$ of
[def-weil-rationalization-karoubi] (so $K_{\mathcal O}$ is a lattice of
$K_E$). Let

$$
\varphi_E:Lg_\gamma^*K_E\longrightarrow K_E
$$

be an arbitrary morphism of $D^b_c(X,E)$ (for instance the Weil
structure of an $E$-Weil complex, [def-weil-weil-sheaf-complex]); no
invertibility, and no invertibility on any lattice, is assumed.

*$E$-stage operators.* All functors below at the stage $E$ are the
rationalizations, by [prop-weil-pbc-rational-transport], of the
integral ones: the pullbacks $Lg_\gamma^{i*}$ with their composition
isomorphisms, $R\Gamma_c(X,-)$ of
[def-weil-integral-rational-qbar-compact-support], the compact-support
base-change isomorphisms $g_{\gamma,c}^{m,*}$ along the automorphisms
$g_\gamma^m$, and the stalk functors with the stalk transports
$\tau_{y,m}$ of [def-trf-frobenius-operators]. Put
$\varphi_E^{[m]}=\varphi_E\circ Lg_\gamma^*\varphi_E\circ\cdots\circ
L(g_\gamma^{m-1})^*\varphi_E:Lg_\gamma^{m*}K_E\to K_E$, as in
[def-trf-iterated-weil-map], and define, by the formulas of
[def-trf-frobenius-operators] in the form of
[lem-trf-frobenius-operator-compact-description],

$$
F_{c,K_E}^{\,m}=R\Gamma_c(X,\varphi_E^{[m]})\circ g_{\gamma,c}^{m,*},
\qquad
F_{y,m}=\varphi^{[m]}_{E,\bar y}\circ\tau_{y,m}
$$

on $R\Gamma_c(X,K_E)$ and on $K_{E,\bar y}$, for $m\geq1$ and
$y\in X_0(\mathbf F_{q^m})$ with geometric point $\bar y$. For $m=1$ and
invertible $\varphi_E$ the first is the compactly supported operator of
[def-weil-global-geometric-frobenius].

*Stalk normalization.* For $y\in X_0(\mathbf F_{q^m})$ one has
$\Phi^m\circ\bar y=\bar y$ ([thm-trf-frobenius-fixed-points]), whence a
natural identification $\iota_M:M_{\bar y}\cong(L\Phi^{m*}M)_{\bar y}$
for every $M$; as throughout, the stalk transport of
[def-trf-frobenius-operators] is taken in the form
$\tau_{y,m}=(\kappa^{(m)}_M)_{\bar y}\circ\iota_M$, natural in $M$ and
defined with no Weil structure on $M$, at every finite level $A_n$ (this
is the normalization under which the stalk map of the scheme-Frobenius
map $u_m$ of [def-trf-iterated-weil-map] is $F_{y,m}$). On integral
objects $\tau_{y,m}$ is the derived limit of these levelwise isomorphisms
on the reduction tower, and at the stage $E$ its rationalization. For a
Frobenius coefficient morphism $\psi$ on $K_n$ with iterates $\psi_m$,
the stalk endomorphism of $K_{n,\bar y}$ is
$\psi_{m,\bar y}=(\psi_m)_{\bar y}\circ\iota_{K_n}$, as in the
coefficient-morphism trace formula of the trace-formula chapter.

Then:

1. *Clearing denominators.* There are an integer $N\geq0$ and a morphism
$u:Lg_\gamma^*K_{\mathcal O}\to K_{\mathcal O}$ of
$D^b_c(X,\mathcal O_E)$ with $\varphi_E=\varpi^{-N}u$ in
$D^b_c(X,E)$; that is, $\varpi^N\varphi_E$ maps the lattice into itself.
1. *Integral Frobenius coefficient morphisms.* For such $(N,u)$ let
$u_n:Lg_\gamma^*K_n\to K_n$ be the reduction of $u$ modulo $\varpi^n$
and put
$$
\psi_n=u_n\circ\kappa_{K_n}:L\Phi^*K_n\longrightarrow K_n .
$$
Each $\psi_n$ is a Frobenius coefficient morphism on $K_n$ in the sense
of [def-trf-frobenius-coefficient-morphism] (in general not
invertible), the $\psi_n$ are compatible with the transitions
$K_{n+1}\otimes^L_{A_{n+1}}A_n\cong K_n$, and the iterates are
$$
\psi_{n,m}=u_n^{[m]}\circ\kappa^{(m)}_{K_n},\qquad
u_n^{[m]}=u_n\circ Lg_\gamma^*u_n\circ\cdots\circ L(g_\gamma^{m-1})^*u_n .
$$
1. *Global operator.* For every $n,m\geq1$,
$$
F_{c,m}(\psi_n)=T_{c_m}(\psi_{n,m})
=R\Gamma_c(X,u_n^{[m]})\circ g_{\gamma,c}^{m,*}
\quad\text{on }R\Gamma_c(X,K_n).
$$
Let $U_m=R\Gamma_c(X,u^{[m]})\circ g_{\gamma,c}^{m,*}$ be the integral
endomorphism of $R\Gamma_c(X,K_{\mathcal O})=R\varprojlim_nR\Gamma_c(X,K_n)$;
it is the derived limit of the levelwise operators $F_{c,m}(\psi_n)$
(the realization of the graph operators $T_{c_m}(\psi_{n,m})$), and
$$
\boxed{\,F_{c,K_E}^{\,m}=\varpi^{-Nm}\,\bigl(U_m\otimes_{\mathcal O_E}E\bigr)
\quad\text{on }R\Gamma_c(X,K_E)=R\Gamma_c(X,K_{\mathcal O})\otimes_{\mathcal O_E}E.\,}
$$
1. *Local operators.* For $y\in X_0(\mathbf F_{q^m})$ the stalk
endomorphism of $\psi_{n,m}$ is $\psi_{n,m,\bar y}=u^{[m]}_{n,\bar y}\circ\tau_{y,m}$
on $K_{n,\bar y}$; the integral endomorphism
$U_{y,m}=u^{[m]}_{\bar y}\circ\tau_{y,m}$ of $K_{\mathcal O,\bar y}$
reduces modulo $\varpi^n$ to $\psi_{n,m,\bar y}$, and
$$
\boxed{\,F_{y,m}=\varpi^{-Nm}\,\bigl(U_{y,m}\otimes_{\mathcal O_E}E\bigr)
\quad\text{on }K_{E,\bar y}=K_{\mathcal O,\bar y}\otimes_{\mathcal O_E}E.\,}
$$

Replacing $(N,u)$ by $(N+1,\varpi u)$ multiplies $U_m,U_{y,m}$ by
$\varpi^m$ and leaves the right-hand sides unchanged. *Example:* for
$X_0=\Spec\mathbf F_q$, $K_E=E^2$ and $\varphi_E=\operatorname{diag}(1,\ell)$,
one may take $N=0$ and $u=\operatorname{diag}(1,\ell)$ on
$\mathcal O_E^2$; no rescaling $c\,\varphi_E$ ($c\in E^\times$) is invertible
on any lattice, since its eigenvalues $c,c\ell$ are not both units, but
$\psi_n=u\bmod\varpi^n$ is a (non-invertible) Frobenius coefficient
morphism.
