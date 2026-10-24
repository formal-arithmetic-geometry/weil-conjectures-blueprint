+++
id = "thm-sc-serre-duality-curve"
kind = "theorem"
title = "Serre duality for smooth proper curves"
order = 713
uses = ["def-sc-curves", "def-sc-function-field", "def-sc-kahler-differentials", "lem-sc-canonical-sheaf", "lem-sc-deg-principal-zero", "lem-sc-finite-duality", "lem-pc-tensor-dual-invertible", "lem-sc-morphism-from-function", "lem-sc-p1-hi-vanishing", "lem-sc-smooth-regular", "lem-weil-pbc-finite-proper", "pqf-def-coherent", "pqf-lem-affine-vanishing", "pqf-lem-fff-vanishing", "pqf-lem-finite-qf", "pqf-lem-leray", "pqf-lem-leray-lowdegree", "pqf-lem-qf-finitefibres", "pqf-lem-sheaf-zero-stalks", "thm-pqf-finite-iff-proper-finite-fibres", "thm-sc-p1-duality"]
lean = ["AlgebraicGeometry.Scheme.serreDuality"]
+++
Let $k$ be a field, $C$ a scheme over $k$ which is smooth of
relative dimension $1$ and proper over $k$, and let
$\omega_C:=\Omega^1_{C/k}$ be the sheaf of Kähler differentials of $C$
over $k$ ([def-sc-kahler-differentials]). For a finite locally free
$\mathcal O_C$-module $\mathcal M$ (a
quasi-coherent module Zariski-locally isomorphic to
$\mathcal O_C^{\oplus r}$ for some $r\ge0$) write
$\mathcal M^{\vee}:=\mathcal H om_{\mathcal O_C}(\mathcal M,\mathcal O_C)$.
Then for $p,q\ge0$ with $p+q=1$ there are $k$-linear isomorphisms

$$
e_{\mathcal M}:H^q(C,\mathcal M)^{\vee}\;\xrightarrow{\ \sim\ }\;
H^{p}\bigl(C,\;\mathcal M^{\vee}\otimes\omega_C\bigr),
$$

natural in $\mathcal M$: for every morphism
$\varphi:\mathcal M\to\mathcal N$ of finite locally free modules,
$e_{\mathcal M}\circ H^q(\varphi)^{\vee}
=H^p(\varphi^{\vee}\otimes1)\circ e_{\mathcal N}$. In particular, for
an invertible $\mathcal M$ ([def-sc-invertible-module],
so $\mathcal M^{\vee}\cong\mathcal M^{-1}$ by
[lem-pc-tensor-dual-invertible]):

$$
H^1(C,\mathcal M)^{\vee}\;\cong\;
H^0\bigl(C,\;\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr),
\qquad
H^0(C,\mathcal M)^{\vee}\;\cong\;
H^1\bigl(C,\;\Omega^1_{C/k}\otimes\mathcal M^{-1}\bigr).
$$

For a coherent
$\mathcal F$ which is not locally free the right hand side must be
replaced by $\operatorname{Ext}^{p}(\mathcal F,\omega_C)$, as in
[thm-sc-p1-duality]: e.g. for the skyscraper
$\mathcal F=\kappa(x)$ at a $k$-rational point $x$ of $C$,
$H^0(C,\mathcal F)^{\vee}=k$ but $\mathcal F^{\vee}=0$.
