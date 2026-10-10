+++
id = "prop-cohomological-finiteness"
kind = "theorem"
title = "Compact-support finiteness and Frobenius"
order = 2431
tags = ["latex:proposition"]
uses = ["cor-galois-lisse-representations", "cor-weil-pbc-geometric-fiber-finite", "def-weil-derived-complete-integral-detailed", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "fin4-lem-fibrewise-cohomological-dimension", "prop-finite-compact-support-constructibility", "sbc-thm-finiteness-finite-type", "thm-galois-fundamental"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, choose a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
choose a finite extension $E/\Ql$ contained in $\Qlb$. Let $Y_0$ be a
separated finite-type
$k_0$-scheme, put $Y=Y_0\times_{k_0}k$, and choose
$K\in D^b_{c,\mathrm W}(Y,E)$, a
Weil complex. Write $E_Y$ for the constant
Weil sheaf. Then the
$E$-coefficient abbreviations mean
$H^i(Y,E)=H^i(Y,E_Y)$ and $H_c^i(Y,E)=H_c^i(Y,E_Y)$. The
ordinary and compact-support
cohomology groups, in particular $H_c^i(Y,K)$ meaning
$H_c^i(Y,\operatorname{For}K)$, are finite-dimensional, vanish outside a
finite interval, and carry the
geometric Frobenius
automorphism. If $Y_0$ is
proper, the
canonical isomorphism

$$
H_c^i(Y,K)\xrightarrow{\sim}H^i(Y,K)
$$

is Frobenius-equivariant.
If $Y$ has dimension $e\in\mathbf Z_{\geq0}$ and $K=E_Y$ is the
constant Weil sheaf, then

$$
H_c^i(Y,E)=0\qquad\text{for }i<0\text{ or }i>2e.
$$

For proper $Y$, the
ordinary cohomology also
satisfies $H^i(Y,E)=0$ for $i<0$ or $i>2e$. In
particular, if $X_0/\Fq$ is smooth,
proper, geometrically connected of pure dimension
$d\in\mathbf Z_{\geq0}$, and $X=X_0\times_{\Fq}k$, then

$$
H^i(X,\Ql)=0\qquad\text{for }i\notin[0,2d].
$$

Moreover, if $Y_0$ is geometrically connected (neither properness nor
smoothness is needed), then $H^0(Y,E)\cong E$, and the
geometric Frobenius acts as the
identity on this group; in particular $H^0(X,\Ql)\cong\Ql$ with
$F=\mathrm{id}$ for every smooth, separated finite-type, geometrically
connected $X_0$.
