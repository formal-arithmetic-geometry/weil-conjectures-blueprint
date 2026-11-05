+++
id = "prose-05-10"
kind = "hidden"
title = "Ind-constructible sheaves (1)"
order = 451
+++
The targets in the compactness statement are direct sums of objects of
$\Loc(\Dbc(X,\Lambda))$, and their cohomology sheaves need not be
constructible. Already the sheaf $\bigoplus_{n\in\mathbf N}\Lambda_X$ is
not constructible, since its stalks are not finitely generated. Such
sheaves are, however, filtered colimits of constructible sheaves, and both
continuity and the uniform bound for Ext groups extend to these colimits.

Recall that the ind-category
$\operatorname{Ind}(\mathcal C)$ of a small category $\mathcal C$ has as
objects the filtered diagrams in $\mathcal C$ (“formal filtered colimits”), with
$\Hom(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom(C_\alpha,D_\beta)$.
Proposition [proposition-ind-constructible-sheaves] below says that for
constructible sheaves the formal and the actual colimits agree.

The dévissage arguments need a class of sheaves that is abelian and
closed under extensions and direct sums, and on which $\Ext^q(C,-)$
behaves as on constructible sheaves. By
Proposition [proposition-ind-constructible-sheaves], the category
$\IndCons(X,\Lambda)$ has the first three properties, and
Corollary [corollary-ind-heart-b] gives the last.
