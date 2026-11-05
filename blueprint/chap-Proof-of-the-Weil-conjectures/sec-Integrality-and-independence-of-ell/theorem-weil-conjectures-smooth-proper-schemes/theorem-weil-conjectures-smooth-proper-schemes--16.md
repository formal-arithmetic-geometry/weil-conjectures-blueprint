+++
id = "theorem-weil-conjectures-smooth-proper-schemes--16"
kind = "theorem"
title = "Functional equation"
order = 1388017
aliases = ["bp-r429-16"]
lean = ["TraceDatum.weilFunctionalEquation_of_pairing"]
uses = []
+++
Let $q>1$ and let $D$ be a trace datum of length $2d$ over a characteristic-zero field $K$, with finite-dimensional spaces $V_i$, endomorphisms $F_i$ and determinant factors $D.P_i=\det(1-TF_i\mid V_i)$. Fix an embedding $\iota:K\hookrightarrow\mathbf C$. Suppose that there are perfect pairings
$$
p_i:V_i\times V_{2d-i}\longrightarrow K,\qquad
p_i(F_iv,F_{2d-i}w)=q^d p_i(v,w).
$$
If $P_i\in\mathbf Z[T]$ and $P_i=\iota(D.P_i)$ in $\mathbf C[T]$, then
$$
\operatorname{Roots}_{\mathbf C}(P_{2d-i})
=\bigl[\,(q^dz)^{-1}:z\in\operatorname{Roots}_{\mathbf C}(P_i)\,\bigr]
$$
as multisets. This is the functional equation used in the Lean assembly for the smooth proper cohomological family.
