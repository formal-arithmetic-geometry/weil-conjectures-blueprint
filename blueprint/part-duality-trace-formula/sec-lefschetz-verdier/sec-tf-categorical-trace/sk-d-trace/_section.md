+++
id = "sk-d-trace"
kind = "definition"
title = "Categorical trace"
order = 542
lean = ["CategoryTheory.MonoidalCategory.trace"]
uses = ["sk-d-setup"]
tags = ["sketch"]
+++
For $P\in\operatorname{Perf}(A)$ put
$P^\vee=R\!\operatorname{Hom}_A(P,A)$. If $v:P\to P$ is a morphism in $D(A)$, its trace is the scalar

$$
\operatorname{tr}_A(v\mid P)=
\left[A\xrightarrow{\operatorname{coev}}P\otimes^{\mathbf L} P^\vee
\xrightarrow{v\otimes^{\mathbf L}1}P\otimes^{\mathbf L} P^\vee
\xrightarrow{\sim}P^\vee\otimes^{\mathbf L} P
\xrightarrow{\operatorname{ev}}A\right]\in A.
$$

Here $\operatorname{coev}$ and $\operatorname{ev}$ are the coevaluation
and evaluation of the dual pair $(P,P^\vee)$ in $D(A)$, and the unlabelled
arrow is the symmetry isomorphism, which includes the Koszul sign.

*General form.* The same composite defines the trace in any braided monoidal
category $\mathcal C$ with unit $\mathbf 1$. If $P\in\mathcal C$ has a right
dual $P^\vee$, with coevaluation $\mathrm{coev}:\mathbf 1\to P\otimes P^\vee$ and
evaluation $\mathrm{ev}:P^\vee\otimes P\to\mathbf 1$, then for $v:P\to P$

$$
\tr(v\mid P)=
\bigl[\mathbf 1\xrightarrow{\mathrm{coev}}P\otimes P^\vee
\xrightarrow{v\otimes1}P\otimes P^\vee
\xrightarrow{\mathrm{sym}}P^\vee\otimes P
\xrightarrow{\mathrm{ev}}\mathbf 1\bigr]\in\operatorname{End}(\mathbf 1),
$$

where $\mathrm{sym}$ is the braiding. For a commutative ring $R$ and
$P\in\Perf(R)$, with $P^\vee=R\operatorname{Hom}_R(P,R)$, evaluation and
coevaluation give its duality in the symmetric monoidal category
$(\Perf(R),\otimes_R^{\mathrm L},R)$, whose unit has endomorphism ring $R$; this
gives $\tr_R(v\mid P)\in R$, and for $R=A$ it is the trace defined above.
