+++
id = "lem-fd-additive-orthogonality"
kind = "lemma"
title = "Additive orthogonality over $\\mathbf F_{q^n}$"
order = 3019
lean = ["AddChar.sum_mulShift"]
uses = ["def-fd-additive-character"]
+++
For the nondegenerate additive character $\psi_n(x)=\psi(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(x))=\Psi(\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(x))$ of $\mathbf F_{q^n}$,

$$
\sum_{y\in\mathbf F_{q^n}}\psi_n\bigl((x-x')y\bigr)
=\begin{cases}q^n,&x=x',\\0,&x\ne x'.\end{cases}
$$
