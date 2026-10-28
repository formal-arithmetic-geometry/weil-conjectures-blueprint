+++
id = "prose-10-01"
kind = "hidden"
title = "What smooth purity says and its coefficients"
order = 2875
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. Smooth purity
says that the right adjoint of $Rf_!$ is inverse image followed by the
Tate twist $(d)$ and the shift $[2d]$:
$f^!\simeq f^*(d)[2d]$ (Theorem [sk-thm-purity-transport]). This is the
$\ell$-adic analogue of the formula $f^!=f^*\otimes\Omega^d_{X/Y}[d]$ of
coherent duality, the twist $(d)$ and the shift $[2d]$ playing the role
of the relative canonical bundle. We need it for two reasons. For the
structure map of a smooth variety it identifies the dualizing complex
with $\Lambda(d)[2d]$, which is what turns Verdier duality into
Poincaré duality, and its counit is the trace map
$H^{2d}_c(X,\Lambda(d))\to\Lambda$ used in the trace formula.

Here $f^!$ is the right adjoint of $Rf_!$ constructed abstractly by Brown
representability (Theorem [sk-prop-sf-existence]), restricted to $\Dctf$
by Theorem [sk-thm-existence]. Smooth purity (Theorem [sk-thm-purity-transport])
describes it explicitly for smooth $f$.
The compatibility of smooth purity and of the trace map with Frobenius, which the trace formula and the
theory of weights need, is proved in Section “Frobenius and Weil complexes”.

Throughout this section $\Lambda$ is an admissible coefficient ring, that is,
a finite commutative ring killed by a power of $\ell$, $\mathcal O_E$,
$E$ or $\overline{\mathbf Q}_\ell$, and Tate twists are those of Definition [sk-def-sp-tate-twist].
For integral coefficients and for coefficients in a field, $\Dctf=\Dbc$, and we
write $\Dbc$ in calculations that only concern these cases.

The proof passes through finite rings $A$ with $\ell^rA=0$,
such as $\mathcal O_E/\ell^n$. For these, $\Dctf$ is the category of
Definition [sk-def-sfb-constructible], and on the pro-étale site
$\Dctf(T,A)$ is identified with the pullback
of its étale counterpart by Corollary [sk-cor-pe-finite-tor-comparison]. The Tor
condition ensures that derived
change of coefficients preserves boundedness, as the example after
Proposition [sk-prop-scalar-six] shows.
