+++
id = "lem-wf-semisimple-group-lie-algebra"
kind = "lemma"
title = "The Lie algebra of a semisimple matrix group"
order = 2687
uses = ["def-wf-algebraic-representations", "def-wf-lie-radical-centre", "def-wf-semisimple-lie-algebra", "def-wf-semisimple-module", "def-wf-simple-module", "lem-ag-connected-group-central-radical", "lem-ag-lie-centre", "lem-wf-zero-dimensional-matrix-group-finite"]
+++
If $H\subseteq\operatorname{GL}(V)$ is connected, $Z(H)$ is finite,
and $V$ is a faithful
semisimple $H$-module over
$\overline{\mathbf Q}_\ell$, then $\operatorname{Lie}(H)$ is a
semisimple Lie algebra.

## Proof

Put $\mathfrak h=\operatorname{Lie}(H)$ and
$\mathfrak r=\operatorname{rad}(\mathfrak h)$, as in
[def-wf-lie-radical-centre]. By
[lem-ag-connected-group-central-radical],
$\mathfrak r=\mathfrak z(\mathfrak h)$. By [lem-ag-lie-centre],
$\mathfrak z(\mathfrak h)=\operatorname{Lie}Z(H)$. The finite group
$Z(H)$ is a reduced zero-dimensional closed matrix group
([lem-wf-zero-dimensional-matrix-group-finite]), so
its Lie algebra is zero. Hence $\mathfrak z(\mathfrak h)=0$, and
therefore $\mathfrak r=0$. By
[def-wf-semisimple-lie-algebra], this says precisely that
$\mathfrak h$ is semisimple.
