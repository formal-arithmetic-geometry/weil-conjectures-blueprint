+++
id = "sk-def-nagata-admissible"
kind = "definition"
title = "Admissible blow-up"
order = 150
lean = ["AlgebraicGeometry.IsAdmissible", "AlgebraicGeometry.Scheme.IdealSheafData.blowup", "AlgebraicGeometry.Scheme.IdealSheafData.blowupMap"]
tags = ["sketch"]
+++
Let $T$ be a scheme and $U\subseteq T$ an open subscheme. For a
finite-type quasi-coherent ideal $\mathcal I\subseteq\mathcal O_T$ with
$\mathcal I|_U=\mathcal O_U$, the blow-up

$$
b:\operatorname{Bl}_{\mathcal I}(T)\longrightarrow T,\qquad
b^{-1}(V)=\operatorname{Proj}\Bigl(\bigoplus_{m\geq0}\mathcal I(V)^m\Bigr)
\quad(V\subseteq T\text{ affine}),
$$

glued from these affine pieces, is called *$U$-admissible*. Its center is
disjoint from $U$.
