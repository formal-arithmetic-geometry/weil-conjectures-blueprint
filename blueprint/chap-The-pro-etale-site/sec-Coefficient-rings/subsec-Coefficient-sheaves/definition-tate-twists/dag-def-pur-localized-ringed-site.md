+++
id = "dag-def-pur-localized-ringed-site"
kind = "dag-definition"
title = "Localization of a ringed site at an object and restriction of modules"
name_showing = false
order = 184503
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-localized-ringed-site"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
+++
Let $\mathcal C$ be a site and $U$ an object of $\mathcal C$. The *localization* $\mathcal C/U$ is the category of objects $V\to U$ over $U$, a family $\{V_j\to V\}$ of morphisms over $U$ being a covering of $\mathcal C/U$ if and only if it is a covering of $\mathcal C$ (equivalently: a sieve on $V/U$ covers if and only if its image under the forgetful functor $j_U:\mathcal C/U\to\mathcal C$ generates a covering sieve of $V$). For a sheaf $\mathcal F$ on $\mathcal C$ (with values in sets, abelian groups or rings) its *restriction* $\mathcal F|_U=j_U^{-1}\mathcal F$ is the sheaf on $\mathcal C/U$ given by $\mathcal F|_U(V/U)=\mathcal F(V)$. For a sheaf of rings $\mathcal O$ on $\mathcal C$ this gives the sheaf of rings $\mathcal O_U=\mathcal O|_U$ on $\mathcal C/U$, and for a sheaf of $\mathcal O$-modules $\mathcal F$ the sheaf of $\mathcal O_U$-modules $\mathcal F|_U$, $\mathcal F|_U(V/U)=\mathcal F(V)$ with its $\mathcal O(V)$-module structure; a morphism $\varphi:\mathcal F\to\mathcal G$ of $\mathcal O$-modules restricts to $\varphi|_U:\mathcal F|_U\to\mathcal G|_U$, $(\varphi|_U)_{V/U}=\varphi_V$. For a morphism $a:V\to U$ of $\mathcal C$ the functor $\mathcal C/V\to\mathcal C/U$, $(W\to V)\mapsto(W\to V\to U)$, identifies $\mathcal C/V$ with the localization $(\mathcal C/U)/(V/U)$ (relocalization), and restricting a sheaf of $\mathcal O_U$-modules on $\mathcal C/U$ along it gives a sheaf of $\mathcal O_V$-modules on $\mathcal C/V$; restricting $\mathcal F|_U$ in this way gives $\mathcal F|_V$, sectionwise the identity.

(SHEAF DAG node `def-pur-localized-ringed-site`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: mathlib. Lean names not on master: `CategoryTheory.GrothendieckTopology.over`, `CategoryTheory.Sheaf.over`, `SheafOfModules.overFunctor`, `SheafOfModules.over`, `SheafOfModules.Hom.over`, `SheafOfModules.overMap`, `SheafOfModules.overFunctorMap`. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
