+++
id = "sk-d-trace"
kind = "definition"
title = "Ordinary categorical trace"
order = 2613
uses = ["sk-d-setup"]
lean = ["CategoryTheory.MonoidalCategory.trace"]
tags = ["sketch"]
+++
Let $\mathcal C$ be a braided monoidal category with unit $\mathbf 1$, and let
$P\in\mathcal C$ have a right dual $P^\vee$, with coevaluation
$\mathrm{coev}:\mathbf 1\to P\otimes P^\vee$ and evaluation
$\mathrm{ev}:P^\vee\otimes P\to\mathbf 1$. For $v:P\to P$, define

$$
\tr(v\mid P)=
\bigl[\mathbf 1\xrightarrow{\mathrm{coev}}P\otimes P^\vee
\xrightarrow{v\otimes1}P\otimes P^\vee
\xrightarrow{\mathrm{sym}}P^\vee\otimes P
\xrightarrow{\mathrm{ev}}\mathbf 1\bigr]\in\operatorname{End}(\mathbf 1),
$$

where $\mathrm{sym}$ is the braiding. For $P\in\Perf(R)$, with
$P^\vee=R\operatorname{Hom}_R(P,R)$, evaluation and coevaluation give its
duality in the symmetric monoidal category $(\Perf(R),\otimes_R^{\mathrm L},R)$,
whose unit has endomorphism ring $R$; this gives $\tr_R(v\mid P)\in R$.
