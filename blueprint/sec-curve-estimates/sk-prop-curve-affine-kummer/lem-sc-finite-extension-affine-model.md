+++
id = "lem-sc-finite-extension-affine-model"
kind = "lemma"
title = "An affine curve model for a finite extension"
lean = ["AlgebraicGeometry.IsConnectedCurve.normalizationIn"]
order = 1420
uses = ["def-fin-normalization-extension", "def-sc-curves", "def-sc-function-field", "def-weil-pbc-scheme-conventions", "lem-fin-normalization-extension-finite", "lem-sc-normal-dim1-dvr"]
+++
Let $C/k$ be a smooth integral affine
connected curve over algebraically closed $k$,
and let $L/k(C)$ be finite, with function field as in
[def-sc-function-field].
The normalization
$h:C'\to C$ in $L$ is a
finite morphism
from a smooth integral affine connected curve with function field $L$.
