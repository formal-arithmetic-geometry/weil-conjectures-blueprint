+++
id = "sk-thm-acyclicity"
kind = "theorem"
title = "Acyclicity criterion"
order = 1097
lean = ["CategoryTheory.Functor.nonempty_rightDerivedObjIso_homology_of_acyclic"]
tags = ["sketch"]
+++
Let $v$ be a left exact functor between abelian categories with
enough injectives. If $F\to I^\bullet$ is a resolution by
$v$-acyclic objects (i.e. $R^qvI^m=0$ for $q>0$), then

$$
\mathcal H^q(vI^\bullet)\xrightarrow{\ \sim\ }R^qvF :
$$

the cohomology of a termwise-acyclic complex computes the derived
functor.
