+++
id = "dag-lem-pe-kflat-roos-representative-invariance"
kind = "dag-lemma"
title = "K-flat representative invariance of augmented scalar-extension Roos cones"
name_showing = false
order = 208505
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "lem-pe-kflat-roos-representative-invariance"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.KFlatRoos.Modules", "SheafOfModules.KFlatRoos.algebraModule", "SheafOfModules.KFlatRoos.algebraModuleMap_existsUnique", "SheafOfModules.KFlatRoos.algebraModuleMap", "SheafOfModules.KFlatRoos.tensorUnit_existsUnique", "SheafOfModules.KFlatRoos.tensorUnit", "SheafOfModules.KFlatRoos.levelModule", "SheafOfModules.KFlatRoos.structure_compatible", "SheafOfModules.KFlatRoos.levelMap", "SheafOfModules.KFlatRoos.level", "SheafOfModules.KFlatRoos.transition", "SheafOfModules.KFlatRoos.product", "SheafOfModules.KFlatRoos.oneSubShift", "SheafOfModules.KFlatRoos.roosX", "SheafOfModules.KFlatRoos.roosD", "SheafOfModules.KFlatRoos.roosD_sq", "SheafOfModules.KFlatRoos.roos", "SheafOfModules.KFlatRoos.unitProduct", "SheafOfModules.KFlatRoos.augmentation_comm", "SheafOfModules.KFlatRoos.augmentation", "SheafOfModules.KFlatRoos.productMap", "SheafOfModules.KFlatRoos.roosMap_comm", "SheafOfModules.KFlatRoos.roosMap"]
+++
Let $C$ be a site small in the module universe and $R$ a sheaf of commutative rings, with module category $\mathcal A=\operatorname{Mod}(R)$ `def-weil-sheaf-of-modules-category`. Assume countable products in $\mathcal A$ are exact. Let $B_{n+1}\to B_n$ for $n\ge1$ be a tower of sheaves of commutative $R$-algebras whose structure maps $R\to B_n$ commute with the transitions `def-weil-inverse-system`. No flatness or surjectivity of these ring maps is assumed. Use the unbounded derived category $D(R)$ and localization $Q$ of `def-weil-abstract-derived-category`, K-flat complexes with flat terms [def-pc-kflat-complex, def-pc-flat-sheaf-modules], and sheaf tensor [dag-def-pur-sheaf-tensor-product]. For each such complex $P$, set $T_n(P)=P\otimes_RB_n$ with its strict transition maps, $V(P)=\prod_nT_n(P)$ termwise, and $s_P$ by $\operatorname{pr}_ns_P=t_n\operatorname{pr}_{n+1}$. Define the Roos complex by
$$L(P)^i=V(P)^i\oplus V(P)^{i-1},\qquad d(x,y)=(dx,(1-s_P)x-dy),$$
and the chain map $\eta_P:P\to L(P)$ by $p\mapsto((p\otimes1)_n,0)$.
For a quasi-isomorphism $a:P\to P'$ between K-flat complexes with flat terms, the strict map $L(a)$ obtained by applying $\prod_n(a\otimes_RB_n)$ to both coordinates is a quasi-isomorphism and satisfies $L(a)\eta_P=\eta_{P'}a$. More generally, for every isomorphism $e:Q(P)\xrightarrow{\sim}Q(P')$ in $D(R)$ there is an isomorphism $v:Q(L(P))\xrightarrow{\sim}Q(L(P'))$ satisfying $v\,Q(\eta_P)=Q(\eta_{P'})e$. Consequently the condition that $\eta_P$ be a quasi-isomorphism depends only on the derived isomorphism class of $P$.

(SHEAF DAG node `lem-pe-kflat-roos-representative-invariance`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: statement. Placed through `sk-def-pe-derived-completion` (ancestor-1). DAG status: split. Lean names not on master: `SheafOfModules.KFlatRoos.representativeInvariance`. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-inverse-system`, `def-weil-sheaf-of-modules-category`.
