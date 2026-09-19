+++
id = "def-nagata-proj-closed-center-finite-degree"
kind = "definition"
title = "Finite-degree data attached to a closed center in Proj"
order = 299
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center"]
uses = ["def-nagata-relative-proj", "lemma-nagata-proj-closed-center-finite-degree-exists"]
+++
Let $\mathcal I$ be a finite type quasi-coherent ideal on a qcqs scheme
$X$, let $\mathcal A=\bigoplus_{n\geq0}\mathcal I^n$, let
$X'=\operatorname{Proj}_X(\mathcal A)$, and let
$Z'\hookrightarrow X'$ be of finite presentation. Select, by classical
choice from the nonempty witness type supplied by
[lemma-nagata-proj-closed-center-finite-degree-exists], a pair
$(d,\mathcal F)$. No property of the selected pair is built into this
definition. Denote it by
$\mathsf{FD}(Z')=(d(Z'),\mathcal F(Z'))$.
