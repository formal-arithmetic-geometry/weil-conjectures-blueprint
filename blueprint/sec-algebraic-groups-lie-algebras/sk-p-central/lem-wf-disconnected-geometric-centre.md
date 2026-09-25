+++
id = "lem-wf-disconnected-geometric-centre"
kind = "lemma"
title = "Finite centre of a disconnected geometric group"
order = 2725
uses = ["def-wf-algebraic-components", "def-wf-algebraic-radicals", "lem-wf-zero-dimensional-matrix-group-finite"]
+++
If $H_{\mathrm{geom}}^\circ$ is semisimple, then the centre
$Z(H_{\mathrm{geom}})$ is finite.

## Proof

The identity component of $Z(H_{\mathrm{geom}})$ is contained in
$Z(H_{\mathrm{geom}}^\circ)$. The latter is finite because
$H_{\mathrm{geom}}^\circ$ is semisimple in the sense of
[def-wf-algebraic-radicals]; its identity component is therefore
trivial. Applying
[lem-wf-zero-dimensional-matrix-group-finite] to the closed matrix
group $Z(H_{\mathrm{geom}})$ now shows that its set of points is
finite (and the centre is a finite group scheme).
