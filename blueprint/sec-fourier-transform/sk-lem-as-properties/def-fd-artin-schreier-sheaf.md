+++
id = "def-fd-artin-schreier-sheaf"
kind = "definition"
title = "The Artin–Schreier sheaf"
order = 3934
lean = ["AlgebraicGeometry.Etale.artinSchreierSheaf"]
uses = ["def-fd-additive-character", "def-weil-pbc-etale-site", "def-weil-pbc-finite-torsors", "def-weil-pbc-scheme-conventions", "def-sf-setting", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-module-pushforward-pullback", "sk-def-sfb-constructible", "sk-prop-ctf-finite-comparison"]
+++
Let $k$ be a finite field with $q$ elements, let $\Lambda$ be a
commutative ring in which $q$ is invertible, and let
$\Psi:(k,+)\to\Lambda^\times$ be an additive character. The
*Artin–Schreier map* is

$$
\mathrm{AS}_q:\mathbf A^1_k\to\mathbf A^1_k,\qquad x\longmapsto x^q-x .
$$

For $a\in k$ the translation $\sigma_a:x\mapsto x+a$ of $\mathbf A^1_k$
satisfies $\mathrm{AS}_q\circ\sigma_a=\mathrm{AS}_q$, so it acts on the
pushforward $(\mathrm{AS}_q)_*\Lambda$ of the constant étale sheaf of
$\Lambda$-modules (in the sense of [def-weil-pbc-etale-site]) by pullback
of sections, and $a\mapsto\sigma_a$ is an action of $(k,+)$. The
*Artin–Schreier sheaf* $\mathcal L_\Psi$ on $\mathbf A^1_k$ is the image
of the idempotent

$$
e_\Psi=\frac1q\sum_{a\in k}\Psi(-a)\,\sigma_a
$$

acting on $(\mathrm{AS}_q)_*\Lambda$, i.e. the $\Psi$-isotypic component,
on which each $\sigma_a$ acts by $\Psi(a)$. For a $k$-scheme $X$ (conventions
of [def-weil-pbc-scheme-conventions]) and a global function
$f\in\Gamma(X,\mathcal O_X)$, viewed as a morphism $f:X\to\mathbf A^1_k$,
the *Artin–Schreier sheaf of $f$* is

$$
\mathcal L_{\Psi,f}:=f^*\mathcal L_\Psi .
$$

Notation: for $k=k_0$ and the additive character $\psi$ of
[def-fd-additive-character] one writes $\mathcal L_{\psi,f}$ and
$\mathcal L_{\psi^{-1},f}$; for $a\in k_0$ put
$\mathcal L_{\psi(af)}:=\mathcal L_{\psi,af}$ (similarly
$\mathcal L_{\psi^{-1}(af)}:=\mathcal L_{\psi^{-1},af}$); on
$\mathbf A^1_{k_0}=\operatorname{Spec}k_0[x]$ one writes
$\mathcal L_\psi:=\mathcal L_{\psi,x}$ (the *Artin–Schreier*, or
*exponential*, sheaf) and $\mathcal L_{\psi(ax)}:=\mathcal L_{\psi,ax}$.

*Condensed coefficients.* For the $\ell$-adic coefficient rings the
construction is made on the pro-étale site. Let $\Lambda$ be an admissible
coefficient ring of [def-sf-setting] ($A$ finite, $\mathcal O_E$, $E$ or
$\Qlb$), regarded as a condensed ring, and let
$\Psi:(k,+)\to\Lambda(*)^\times$ be an additive character (for
$\Lambda=\mathcal O_E,E$ this requires $\mu_p\subset E$). The translations
$\sigma_a$ act by pullback on the pushforward
$(\mathrm{AS}_q)_*\Lambda_{\mathbf A^1_k}$ of the coefficient sheaf
$\Lambda_{\mathbf A^1_k}=p_{\mathbf A^1_k}^*\Lambda$
([det-def-sfb-pulled-back-coefficients], [det-def-sfb-module-pushforward-pullback]),
and $\mathcal L_\Psi\in\Mod(\mathbf A^1_{k,\mathrm{proét}},\Lambda)$ is the
image of the same idempotent $e_\Psi$; for $f:X\to\mathbf A^1_k$ put
$\mathcal L_{\Psi,f}=f^*\mathcal L_\Psi$, the pullback of $\Lambda$-modules.
Since $\mathrm{AS}_q$ is finite étale and its base change along itself is the
trivial $k$-torsor, $(\mathrm{AS}_q)_*\Lambda_{\mathbf A^1_k}$ becomes
isomorphic to $\Lambda^{k}$ after pullback along the cover $\mathrm{AS}_q$,
with $\sigma_a$ permuting the factors; hence $\mathcal L_\Psi$ has a finite
constant local model of rank one in the sense of [sk-def-sfb-constructible].
For non-torsion $\Lambda$ this $\Lambda_{\mathbf A^1_k}$-module is *the*
Artin–Schreier sheaf; the étale description above is used only for finite
$\Lambda$, where $\nu^*$ carries the étale sheaf to the pro-étale one, because
$\nu^*$ commutes with pushforward ([sk-prop-ctf-finite-comparison]) and with
images of idempotents. Extension of scalars along a coefficient map
$\Lambda\to\Lambda'$ carries $\mathcal L_\Psi$ to the Artin–Schreier sheaf of
the composite character, since it commutes with finite étale pushforward and
with images of idempotents.
