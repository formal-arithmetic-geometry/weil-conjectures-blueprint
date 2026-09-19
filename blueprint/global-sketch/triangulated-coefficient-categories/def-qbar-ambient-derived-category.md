+++
id = "def-qbar-ambient-derived-category"
kind = "definition"
title = "Ambient algebraically closed coefficient category"
order = 21
uses = ["def-filtered-two-colimit", "def-qbar-ambient-finext-diagram", "def-qbar-pair-triangulation"]
+++
For a scheme $Y$, fix a prime $\ell\neq p$ and an algebraic closure
$\Qlb/\Ql$. Apply Definitions [def-filtered-two-colimit] and
[def-qbar-pair-triangulation] to the ambient diagram of
Definition [def-qbar-ambient-finext-diagram], and define

$$
D(Y,\Qlb)=
\underset{E\in\mathcal E_\ell}{\operatorname{2-colim}^{\mathrm{pair}}}
D(Y_{\mathrm{proet}},E_Y).
$$

Thus an object, morphism, shift, or distinguished triangle in
$D(Y,\Qlb)$ is represented at one finite coefficient field, modulo the
explicit common-stage relation.
