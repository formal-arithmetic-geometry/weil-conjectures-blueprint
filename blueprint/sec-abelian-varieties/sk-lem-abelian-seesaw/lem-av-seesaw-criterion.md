+++
id = "lem-av-seesaw-criterion"
kind = "lemma"
title = "Triviality on a fibre through $h^0$"
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_iso_unit_fiber_iff", "AlgebraicGeometry.Scheme.Modules.nonempty_iso_fiber_iff"]
order = 444
uses = ["def-sc-invertible-module"]
+++
Let $f:P\to T$ be a proper morphism with geometrically integral fibres, and for
$t\in T$ write $P_t$ for the fibre over $\kappa(t)$ and $\mathcal F_t$ for the
restriction of an $\mathcal O_P$-module $\mathcal F$ to $P_t$.

1. **(1)** Let $\mathcal A,\mathcal B$ be invertible $\mathcal O_P$-modules with
   $\mathcal A\otimes\mathcal B\simeq\mathcal O_P$. Then $\mathcal A_t\simeq\mathcal O_{P_t}$
   if and only if $H^0(P_t,\mathcal A_t)\ne0$ and $H^0(P_t,\mathcal B_t)\ne0$.
1. **(2)** Let $\mathcal M,\mathcal N$ be invertible $\mathcal O_P$-modules. Then
   $\mathcal M_t\simeq\mathcal N_t$ if and only if
   $H^0\bigl(P_t,(\mathcal M\otimes\mathcal N^{\vee})_t\bigr)\ne0$ and
   $H^0\bigl(P_t,(\mathcal N\otimes\mathcal M^{\vee})_t\bigr)\ne0$.
