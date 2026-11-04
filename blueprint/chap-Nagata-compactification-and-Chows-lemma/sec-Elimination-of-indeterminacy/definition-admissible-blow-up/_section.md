+++
id = "definition-admissible-blow-up"
kind = "definition"
title = "Admissible blow-up"
order = 1416
lean = ["AlgebraicGeometry.IsAdmissible", "AlgebraicGeometry.Scheme.IdealSheafData.blowup", "AlgebraicGeometry.Scheme.IdealSheafData.blowupMap"]
+++
Let $T$ be quasi-compact and quasi-separated, and let $U\subseteq T$ be a
quasi-compact open. For a quasi-coherent ideal of finite type
$\mathcal I\subseteq\mathcal O_T$ with
$\mathcal I|_U=\mathcal O_U$, the blow-up

$$
b:\operatorname{Bl}_{\mathcal I}(T)=
\operatorname{Proj}_T\Bigl(\bigoplus_{m\geq0}\mathcal I^m\Bigr)
\longrightarrow T
$$

is called $U$-admissible. Its center is disjoint from $U$.
