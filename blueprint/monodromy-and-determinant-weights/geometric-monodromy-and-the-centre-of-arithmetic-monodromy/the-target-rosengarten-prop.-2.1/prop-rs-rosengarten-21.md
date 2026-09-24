+++
id = "prop-rs-rosengarten-21"
kind = "theorem"
title = "Curve form of Rosengarten Prop. 2.1: semisimplicity of geometric monodromy"
order = 4133
tags = ["latex:proposition"]
uses = ["def-sbc-normal-dominant-galois", "def-weil-finite-field-fiber", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-components", "def-wf-algebraic-radicals", "def-wf-fundamental-representation", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-reductive-group", "def-wf-unipotent-radical", "def-wf-weil-group", "lem-rs-connectivity-cover", "lem-rs-connectivity-pullback", "lem-wf-faithful-semisimple-reductive", "lem-wf-geometric-closure-semisimple", "lem-wf-no-central-torus", "lem-wf-unipotent-fixed-vector", "lem-wf-zero-dimensional-matrix-group-finite"]
+++
Fix the global finite-field
datum $(p,a,q,k_0,k)$, let $X_0$ be a
normal,
separated finite-type
$k_0$-scheme of pure dimension one with
$X=X_0\times_{k_0}k$ connected, and let
$\mathcal F$ be a lisse $\overline{\mathbf Q}_\ell$-Weil sheaf on
$X_0$ with
fundamental
representation $(V,\rho)$ of the Weil
group $W(X_0)$, assumed
geometrically semisimple.
Let $H_{\mathrm{geom}}\subseteq\operatorname{GL}(V)$ be the
geometric monodromy
group – the Zariski closure of
$\rho(\pi_1(X,\bar x))$ – and let
$H_{\mathrm{geom}}^\circ\subseteq H_{\mathrm{geom}}$ be its
identity component. Then the
identity component $H_{\mathrm{geom}}^\circ$ is a
semisimple algebraic group (in
the sense of [def-wf-reductive-group] and
[def-wf-unipotent-radical]: connected, reductive, with finite
centre); equivalently, after the connected finite etale cover
attached to the inverse image of $H_{\mathrm{geom}}^\circ$ in
$\pi_1(X,\bar x)$ (the reduction of the proof), the geometric
monodromy group is connected and semisimple. This is the precise
formulation under the connected definition of *semisimple
algebraic group* in [def-wf-algebraic-radicals]. The source
writes $G_{\mathrm{geom}}$ itself as semisimple after first
replacing the base by the connected finite etale cover; without that
replacement a finite disconnected monodromy group shows that the
literal connected wording would be false.

## Proof

Apply [lem-rs-connectivity-cover] to
$(X_0,\mathcal F,\rho)$, and for the resulting cover and its normal
model apply [lem-rs-connectivity-pullback]; rename the resulting
datum (the finite
etale cover $X_0'\to X_0^{(m)}$, normal finite type with geometric
monodromy group $H^\circ$, connected, and fundamental representation
$(V,\rho|_{\Pi^\circ})$, still geometrically semisimple, with $V$
semisimple as a module for the closure $H^\circ$ by
[lem-wf-geometric-closure-semisimple]) to $(X_0,\mathcal F,\rho)$,
so that $H:=H_{\mathrm{geom}}$ is connected. By
[lem-wf-faithful-semisimple-reductive] the connected group $H$
is reductive: that lemma applies the connected-unipotent fixed-vector
lemma [lem-wf-unipotent-fixed-vector] to every connected normal
unipotent subgroup and uses faithfulness to make each such subgroup
trivial. By [lem-wf-no-central-torus],
$Z(H)^\circ=1$. The identity component of the closed subgroup
$Z(H)\subseteq H$ of the finite-type affine group $H$ is therefore
trivial, and $Z(H)$ has finitely many points by
[lem-wf-zero-dimensional-matrix-group-finite]: $Z(H)$ is
finite. Connected,
reductive, with finite centre, is semisimplicity by
[def-wf-algebraic-radicals]. This proves the identity-component
assertion; the equivalent formulation is the cover of
[lem-rs-connectivity-cover], over which the geometric monodromy
group is connected and equal to the semisimple group $H^\circ$ by
[lem-rs-connectivity-pullback].
