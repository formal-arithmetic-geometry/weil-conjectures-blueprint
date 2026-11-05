+++
id = "lemma-verdier-duality-preserves-constructibility--1"
kind = "lemma"
title = "Verdier duality with finite coefficients and a Tor bound"
name_showing = false
order = 835001
aliases = ["bp-r250-1"]
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_and_torAmplitudeIn_verdierDual_of_perfectField"]
uses = ["definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
Let $k$ be a perfect field and $\Lambda$ a finite commutative ring whose
exponent is invertible in $k$. Let $a_X:X\to\operatorname{Spec}k$ be
separated of finite type and admit a compactification. Work on the small
étale site, and put $\omega_X=a_X^!\Lambda_k$ and
$\mathbb D_XK=\cHom_{\Lambda_X}(K,\omega_X)$.

Let $d\geq 0$ be an integer with $\dim X\leq d$, and let
$K\in\Dbc(X,\Lambda)$ have Tor amplitude in $[a,b]$. Then

$$
\mathbb D_XK\in\Dctf(X,\Lambda),\qquad
\operatorname{Tor\!\ amplitude}(\mathbb D_XK)\subseteq[-b-2d,-a].
$$

In particular, $\mathbb D_X$ preserves $\Dctf(X,\Lambda)$ for these
coefficients. This is the finite-coefficient form used in the Lean proof
of Verdier biduality.
