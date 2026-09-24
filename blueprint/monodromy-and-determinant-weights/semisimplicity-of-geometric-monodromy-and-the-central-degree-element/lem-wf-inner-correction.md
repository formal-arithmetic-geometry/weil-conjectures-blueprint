+++
id = "lem-wf-inner-correction"
kind = "lemma"
title = "Inner correction to a degree element"
order = 4109
uses = ["def-wf-algebraic-radicals", "def-wf-arithmetic-monodromy-extension", "def-wf-geometric-semisimplicity", "lem-wf-dense-identity-component", "lem-wf-finite-index-restriction-semisimple", "lem-wf-finite-outer-power", "lem-wf-geometric-closure-semisimple"]
+++
Assume $\rho$ is geometrically semisimple and
$H=H_{\mathrm{geom}}^\circ$ is semisimple. There are $n>0$
and $z_0\in G^{[n]}$ which centralizes $H$.

## Proof

Let $\Pi=\pi_1(X,\bar x)$ and
$\Pi^\circ=\Pi\cap\rho^{-1}(H)$. Its index in $\Pi$ is finite, and
the geometric module is semisimple by
[def-wf-geometric-semisimplicity]; hence
[lem-wf-finite-index-restriction-semisimple] makes
$V|_{\Pi^\circ}$ semisimple. By
[lem-wf-dense-identity-component], the closure of
$\rho(\Pi^\circ)$ is $H$; hence
[lem-wf-geometric-closure-semisimple] makes $V$ a semisimple
faithful $H$-module. The matrix $a=\rho(s)$ normalizes $H$, so
[lem-wf-finite-outer-power] applies. If
$\alpha^n=\operatorname{Int}(h)$, set

$$
z_0=(h^{-1},n)\in G^{[n]}.
$$

For $x\in H$, the multiplication rule of
[def-wf-arithmetic-monodromy-extension] gives
$z_0xz_0^{-1}=h^{-1}\alpha^n(x)h=x$. Thus $z_0$ centralizes $H$,
which is semisimple in the sense of
[def-wf-algebraic-radicals], and has positive degree $n$.
