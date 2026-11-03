+++
id = "def-weil-global-geometric-frobenius"
kind = "definition"
title = "Global geometric Frobenius"
order = 3387
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-ordinary-compact-cohomology", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "def-weil-derived-direct-image", "def-compact-support-direct-image-detailed", "def-weil-compactifications-refinements", "prop-compactification-coherence-detailed", "lem-sfb-compactification-over-base", "def-weil-pbc-proetale-site"]
+++
Fix the finite-field datum [def-weil-finite-field-fiber] $p,a,q,k_0,k$, a
prime $\ell\neq p$. Write $\Ql=\mathbf Q_\ell$, choose an algebraic closure
$\Qlb$ of $\Ql$, and choose a finite extension $E/\Ql$ contained in $\Qlb$.
Let $Y_0$ be a separated finite-type
[def-weil-scheme-morphism-properties] $k_0$-scheme, put
$Y=Y_0\times_{k_0}k$, set $\gamma=\operatorname{Frob}_q$, the geometric
Frobenius [def-weil-frobenius-detailed], and
$g_Y=\operatorname{id}_{Y_0}\times\operatorname{Spec}(\gamma):Y\to Y$, and
let $\Lambda\in\{E,\Qlb\}$, regarded as a condensed ring, and choose a Weil
complex $K\in D^b_{c,\mathrm W}(Y,\Lambda)$ of [def-weil-weil-sheaf-complex],
with underlying object $\operatorname{For}(K)$ in the condensed category
$\Dbc(Y,\Lambda)$; for a pair $(K,\theta)$ with $K\in\Dbc(Y,\Lambda)$, read
$\operatorname{For}(K)=K$ and $\theta_K=\theta$ below. The Weil structure
$\theta_K$ of [def-weil-weil-sheaf-complex] is the isomorphism formed with the
derived pullback [def-weil-derived-pullback-tensor-hom]
$Lg_Y^*\operatorname{For}(K)\xrightarrow{\sim}\operatorname{For}(K)$, and the
ordinary cohomology [def-weil-ordinary-compact-cohomology] endomorphism is
induced by

$$
 \RGamma(Y,\operatorname{For}K)\xrightarrow{u_{g_Y,*}(\operatorname{For}K)}
 \RGamma(Y,Lg_Y^*\operatorname{For}K)
 \xrightarrow{\RGamma(\theta_K)}\RGamma(Y,\operatorname{For}K).
$$

The compactly supported endomorphism is the explicitly defined composite

$$
\RGammac(Y,\operatorname{For}K)\xrightarrow{u_{g_Y,!}(\operatorname{For}K)}
\RGammac(Y,Lg_Y^*\operatorname{For}K)
 \xrightarrow{\RGammac(\theta_K)}\RGammac(Y,\operatorname{For}K),
$$

where $s=\operatorname{Spec} k$, $a_Y:Y\to s$ is the structure morphism,
$\RGamma(Y,-)=\operatorname{Fib}_s(Ra_{Y*}(-))$ and
$\RGammac(Y,-)=\operatorname{Fib}_s(Ra_{Y!}(-))$. The first arrows are
defined as follows. Put $\gamma_s=\operatorname{Spec}(\gamma):s\to s$. The
automorphism $g_Y$ is semilinear over the base:

$$
a_Y\circ g_Y=\gamma_s\circ a_Y
$$

(not $a_Yg_Y=a_Y$). Since $\gamma_s$ is an isomorphism,
$R\gamma_{s!}=R\gamma_{s*}=\gamma_{s*}$, and

$$
\lambda_\gamma:\operatorname{Fib}_sR\gamma_{s!}\xrightarrow{\ \sim\ }\operatorname{Fib}_s
$$

is the canonical coefficient-section identification for the base
automorphism, induced by $\Gamma(s,\gamma_{s*}M)=\Gamma(\gamma_s^{-1}s,M)=\Gamma(s,M)$
on the small pro-étale site [def-weil-pbc-proetale-site] of $s$. It is
coherent: $\lambda_{\mathrm{id}}=\mathrm{id}$, and for automorphisms
$\gamma,\gamma'$ of $k$ one has
$\lambda_{\gamma'\gamma}=\lambda_\gamma\circ(\lambda_{\gamma'})_{R\gamma_{s*}}\circ\operatorname{Fib}_s(c)$,
where $c:R(\gamma'_s\gamma_s)_*\cong R\gamma'_{s*}R\gamma_{s*}$ is the
compositor. For $L\in\Dbc(Y,\Lambda)$, with $\eta_{g_Y}$ the unit of
$Lg_Y^*\dashv Rg_{Y*}$ [def-weil-derived-direct-image], define
$u_{g_Y,!}(L)$ as the composite

$$
\begin{aligned}
\operatorname{Fib}_sRa_{Y!}L
&\xrightarrow{\operatorname{Fib}_sRa_{Y!}(\eta_{g_Y,L})}
\operatorname{Fib}_sRa_{Y!}Rg_{Y*}Lg_Y^*L
\simeq
\operatorname{Fib}_sR\gamma_{s!}Ra_{Y!}Lg_Y^*L
\xrightarrow{\lambda_\gamma}
\operatorname{Fib}_sRa_{Y!}Lg_Y^*L .
\end{aligned}
$$

The middle identification is $Rg_{Y*}\cong Rg_{Y!}$ followed by the
composition law, using $a_Yg_Y=\gamma_sa_Y$:
$Ra_{Y!}Rg_{Y!}\cong R(a_Yg_Y)_!=R(\gamma_sa_Y)_!\cong R\gamma_{s!}Ra_{Y!}$.
Explicitly, as $g_Y$ is not a $k$-morphism, it is computed on a compactification
descended from $Y_0$: choose a compactification $Y_0\hookrightarrow\bar Y_0$
over $k_0$ ([lem-sfb-compactification-over-base]) and base change it to
$Y\xrightarrow{j}\bar Y\xrightarrow{\bar a}s$
([def-weil-compactifications-refinements],
[def-compact-support-direct-image-detailed]). Then
$\bar g=\operatorname{id}_{\bar Y_0}\times\gamma_s$ is an automorphism of
$\bar Y$ with $\bar gj=jg_Y$ and $\bar a\bar g=\gamma_s\bar a$, and the
middle identification is

$$
R\bar a_*j_!Rg_{Y*}\cong R\bar a_*R\bar g_*j_!\cong R(\bar a\bar g)_*j_!
=R(\gamma_s\bar a)_*j_!\cong R\gamma_{s*}R\bar a_*j_!,
$$

whose first arrow is transport of structure of $j_!$ along the isomorphisms
$(g_Y,\bar g)$ and whose other arrows are composition isomorphisms of derived
direct images. It is independent of $\bar Y_0$: two descended
compactifications are dominated by a third, and refinement morphisms, being
characterized by restricting to the identity on $Y$, commute with it
([prop-compactification-coherence-detailed]). The ordinary version
$u_{g_Y,*}(L)$ is the same composite with $Ra_{Y*}$ in place of $Ra_{Y!}$,
$\operatorname{Fib}_sRa_{Y*}(\eta_{g_Y,L})$ as first arrow, the composition
identification $Ra_{Y*}Rg_{Y*}\cong R(\gamma_sa_Y)_*\cong R\gamma_{s*}Ra_{Y*}$,
and $\lambda_\gamma:\operatorname{Fib}_sR\gamma_{s*}\cong\operatorname{Fib}_s$. Thus
for the Weil pair $(\operatorname{For}K,\theta_K)$

$$
F_K=\RGamma(\theta_K)\circ u_{g_Y,*}(\operatorname{For}K),\qquad
F_{c,K}=\RGammac(\theta_K)\circ u_{g_Y,!}(\operatorname{For}K).
$$

Replacing $(\gamma,g_Y,\gamma_s)$ by $(\gamma^m,g_Y^m,\gamma_s^m)$ defines
$u_{g_Y^m,*}$ and $u_{g_Y^m,!}$. The same formulas, read in $\Dbc(-,\Lambda)$
for $\Lambda\in\{A_{E,n},\mathcal O_E\}$ of
[def-weil-ordinary-compact-cohomology], define these arrows and $F$
uniformly for finite, integral and rational coefficients. Both operators,
and their actions on cohomology [def-weil-ordinary-compact-cohomology], are
denoted $F$.
