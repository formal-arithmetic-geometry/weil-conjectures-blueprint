+++
id = "prop-wf-geometric-monodromy-semisimple"
kind = "theorem"
title = "Semisimplicity of geometric monodromy"
order = 2806
tags = ["latex:proposition"]
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-components", "def-wf-algebraic-radicals", "def-wf-geometric-semisimplicity", "def-wf-monodromy-data", "lem-wf-algebraic-component-cosets", "lem-wf-dense-identity-component", "lem-wf-faithful-semisimple-reductive", "lem-wf-finite-index-restriction-semisimple", "lem-wf-geometric-closure-semisimple", "lem-wf-no-central-torus", "lem-wf-zero-dimensional-matrix-group-finite"]
+++
Let $X_0$ be a
normal, geometrically connected
separated finite-type scheme
of pure dimension one over a finite field, let
$\mathcal F$ be a geometrically semisimple lisse Weil sheaf on $X_0$, and
let $H_{\mathrm{geom}}$ be its geometric monodromy group. After the
finite etale cover corresponding to the inverse image of
$H_{\mathrm{geom}}^\circ$ in $\Pi$, the geometric monodromy group is
connected and semisimple.

## Proof

Use the notation of the monodromy data in
[def-wf-monodromy-data]; its geometric representation is
semisimple in the sense of [def-wf-geometric-semisimplicity].
The quotient $H_{\mathrm{geom}}/H_{\mathrm{geom}}^\circ$ is finite by
[lem-wf-algebraic-component-cosets] and the component-group definition [def-wf-algebraic-components]. Its inverse image in $\Pi$ is
an open normal subgroup $\Pi^\circ$ of finite index. Normality of
$H_{\mathrm{geom}}^\circ$ and its invariance under the arithmetic
conjugation show that $\Pi^\circ$ is stable under the Weil descent
operator; it therefore defines the indicated finite etale cover (after
an inessential finite constant-field extension if necessary). By
[lem-wf-finite-index-restriction-semisimple], the restriction of
the geometric representation to $\Pi^\circ$ is semisimple. By
[lem-wf-dense-identity-component], the Zariski closure of
$\rho(\Pi^\circ)$ is exactly $H_{\mathrm{geom}}^\circ$. On this cover,
[lem-wf-geometric-closure-semisimple] gives a semisimple faithful
module, so [lem-wf-faithful-semisimple-reductive] makes the group
reductive. Its connected centre is trivial by
[lem-wf-no-central-torus]; the closed subgroup $Z(H)$ has
trivial identity component, so it is finite by
[lem-wf-zero-dimensional-matrix-group-finite]. Hence it is
semisimple by
[def-wf-algebraic-radicals].
