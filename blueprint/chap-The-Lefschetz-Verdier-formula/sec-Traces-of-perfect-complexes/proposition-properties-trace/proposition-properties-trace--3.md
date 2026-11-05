+++
id = "proposition-properties-trace--3"
kind = "proposition"
title = "Scalar extension"
order = 896006
aliases = ["bp-r270-3"]
lean = ["CategoryTheory.Functor.trace_eq_unitEndRingHom_trace"]
uses = ["definition-categorical-trace--2"]
+++
Let $F:\mathcal C\to\mathcal D$ be an additive braided strong monoidal
functor between preadditive braided monoidal categories, with unit
isomorphism $\phi_0:\mathbf 1_{\mathcal D}\xrightarrow{\sim}F(\mathbf 1_{\mathcal C})$.
Then

$$
\rho_F:\operatorname{End}(\mathbf 1_{\mathcal C})\longrightarrow
\operatorname{End}(\mathbf 1_{\mathcal D}),\qquad
a\longmapsto\phi_0^{-1}\circ F(a)\circ\phi_0,
$$

is a ring map. Suppose that $P$, $F(P)$ and $P'$ have right duals, and that
an isomorphism $e:F(P)\xrightarrow{\sim}P'$ satisfies $e\circ F(v)=v'\circ e$
for endomorphisms $v$ of $P$ and $v'$ of $P'$. Then

$$
\operatorname{tr}(v'\mid P')=\rho_F(\operatorname{tr}(v\mid P)).
$$

In particular, for every ring map $A\to B$, the image of
$\operatorname{tr}_A(v\mid P)$ in $B$ is
$\operatorname{tr}_B(v\otimes_A^{\mathbf L}B\mid P\otimes_A^{\mathbf L}B)$.
