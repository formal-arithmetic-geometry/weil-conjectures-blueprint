+++
id = "lem-rs-connectivity-pullback"
kind = "lemma"
title = "The pullback has connected semisimple geometric monodromy"
order = 2809
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-components", "def-wf-fundamental-representation", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-weil-group", "lem-rs-connectivity-reduction", "lem-wf-dense-identity-component", "lem-wf-finite-index-restriction-semisimple", "lem-wf-geometric-closure-semisimple"]
+++
Let $X_0$ be a normal,
separated finite-type
$k_0$-scheme with $X=X_0\times_{k_0}k$ connected, let
$\mathcal F$ be a lisse $\overline{\mathbf Q}_\ell$-Weil sheaf on
$X_0$ with
fundamental
representation $(V,\rho)$, where $\rho$ is
geometrically semisimple.
With $\Pi:=\pi_1(X,\bar x)$, the geometric subgroup of the
Weil group, $H:=H_{\mathrm{geom}}$ the
geometric monodromy
group (the Zariski closure of $\rho(\Pi)$ in
$\operatorname{GL}(V)$), and $H^\circ$ the identity component of
[def-wf-algebraic-components], put

$$
\Pi^\circ:=\{\gamma\in\Pi:\rho(\gamma)\in H^\circ\}
=\rho^{-1}\bigl(H^\circ\cap\rho(\Pi)\bigr).
$$

Let moreover $(X',\bar x')\to(X,\bar x)$ be a connected finite etale
cover with $\pi_1(X',\bar x')=\Pi^\circ$, and let $X'_0$ be a normal
finite-type $\mathbf F_{q^m}$-scheme with a finite etale morphism
$X'_0\to X_0^{(m)}=X_0\times_{k_0}\mathbf F_{q^m}$ for some $m\ge1$
with $X_0'\times_{\mathbf F_{q^m}}k=X'$. Then, for the pullback
$\mathcal F'$ of $\mathcal F$ to $X_0'$, the geometric part of its
fundamental representation is $(V,\rho|_{\Pi^\circ})$, its geometric
monodromy group is $H^\circ$ (connected), and $\rho|_{\Pi^\circ}$ is
geometrically semisimple.

## Proof

By [def-wf-fundamental-representation] (the equivalence of
lisse $\overline{\mathbf Q}_\ell$-sheaves on a connected scheme with
continuous representations of its etale fundamental group, natural
under base change, which replaces $\Pi$ by the subgroup
$\pi_1(X',\bar x')=\Pi^\circ$), the geometric restriction of the
fundamental representation of $\mathcal F'$ is
$(V,\rho|_{\Pi^\circ})$. Its geometric
monodromy group is the Zariski closure of $\rho(\Pi^\circ)$, which
equals $H^\circ$ by [lem-wf-dense-identity-component] applied to
the Zariski-dense subgroup $\rho(\Pi)\subseteq H$ (with
$\rho(\Pi)\cap H^\circ=\rho(\Pi^\circ)$). The representation
$\rho|_{\Pi^\circ}$ is geometrically semisimple by
[lem-wf-finite-index-restriction-semisimple], because
$\Pi^\circ\triangleleft\Pi$ has finite index by
[lem-rs-connectivity-reduction] and $V$ is
semisimple as a $\Pi$-module by geometric semisimplicity of
[def-wf-geometric-semisimplicity]; by
[lem-wf-geometric-closure-semisimple], $V$ is semisimple as a
module for the closure $H^\circ$ as well.
