+++
id = "proposition-properties-trace--3"
kind = "proposition"
title = "Scalar extension"
order = 895004
aliases = ["bp-r270-3"]
lean = ["CategoryTheory.Functor.trace_eq_unitEndRingHom_trace"]
uses = ["definition-categorical-trace"]
+++
Let $F:\mathcal C\to\mathcal D$ be an additive braided strong monoidal
functor between preadditive braided monoidal categories. Its unit
isomorphism induces a ring map

$$
\rho_F:\End(\mathbf 1_{\mathcal C})\longrightarrow
\End(\mathbf 1_{\mathcal D}).
$$

Suppose $P$, $F(P)$ and $P'$ have right duals, and
$e:F(P)\xrightarrow{\sim}P'$ intertwines $F(v)$ and $v'$. Then

$$
\operatorname{tr}(v'\mid P')=\rho_F(\operatorname{tr}(v\mid P)).
$$

This is the functorial form of scalar extension: for
$F=-\otimes_A^{\mathbf L}B$, the map $\rho_F$ is the coefficient map
under the identifications of the endomorphism rings of the units with
$A$ and $B$.
