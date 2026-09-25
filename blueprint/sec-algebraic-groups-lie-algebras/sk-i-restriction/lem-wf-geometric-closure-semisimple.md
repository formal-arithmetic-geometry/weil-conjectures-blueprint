+++
id = "lem-wf-geometric-closure-semisimple"
kind = "lemma"
title = "Semisimplicity passes to the geometric closure"
order = 2661
uses = ["def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-semisimple-module", "def-wf-simple-module", "lem-wf-stabilizer-density"]
+++
If $\rho$ is geometrically semisimple, then $V$ is a semisimple
$H_{\mathrm{geom}}$-module.

## Proof

By geometric semisimplicity in
[def-wf-geometric-semisimplicity], write
$V=\bigoplus_i V_i$ with each $V_i$ irreducible under $\Pi$.
Every $V_i$ is $\Pi$-stable, hence is
$H_{\mathrm{geom}}$-stable by [lem-wf-stabilizer-density]. If a
proper $H_{\mathrm{geom}}$-subspace occurred inside $V_i$, it would be
$\Pi$-stable, contradicting irreducibility. Thus the same direct sum is
semisimple for $H_{\mathrm{geom}}$ in the sense of
[def-wf-simple-module], [def-wf-semisimple-module].
