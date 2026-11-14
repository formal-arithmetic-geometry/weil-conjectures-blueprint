+++
id = "dag-lem-pur-torsion-sheaf-constant-module"
kind = "dag-lemma"
title = "An abelian sheaf killed by N is a module over the constant sheaf Z/N"
name_showing = false
order = 184522
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-torsion-sheaf-constant-module"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.constantZModRingSheaf", "CategoryTheory.IsConstantZModSheafModuleStructure", "CategoryTheory.existsUnique_constantZModSheafModuleStructure", "CategoryTheory.torsionSheafModuleStructure", "CategoryTheory.torsionSheafModuleStructure_spec", "CategoryTheory.torsionSheafModule", "CategoryTheory.torsionSheaf_hom_linear", "CategoryTheory.constantZModModuleSheaf_nsmul"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let $\mathcal C$ be a site, $N\in\mathbf Z_{\geq1}$, and let $(\mathbf Z/N\mathbf Z)_{\mathcal C}$
be the constant sheaf of rings [dag-def-weil-pbc-constant-sheaf] with value
$\mathbf Z/N\mathbf Z$. Let $\mathcal F$ be a sheaf of abelian groups on $\mathcal C$ with
$N\cdot x=0$ for every object $U$ and every $x\in\mathcal F(U)$. Then:

1. $\mathcal F$ carries a unique structure of sheaf of
$(\mathbf Z/N\mathbf Z)_{\mathcal C}$-modules `def-weil-sheaf-of-modules-category` with
underlying sheaf of abelian groups $\mathcal F$ such that, for every $U$, a section of
$(\mathbf Z/N\mathbf Z)_{\mathcal C}(U)$ coming from the constant presheaf, i.e. the image of
a class $a\in\mathbf Z/N\mathbf Z$, acts on $\mathcal F(U)$ as multiplication by any
integer representative of $a$;
2. if $\mathcal F,\mathcal G$ are two such sheaves, every morphism of sheaves of abelian
groups $\mathcal F\to\mathcal G$ is $(\mathbf Z/N\mathbf Z)_{\mathcal C}$-linear, so the
sheaves of $(\mathbf Z/N\mathbf Z)_{\mathcal C}$-modules are exactly the sheaves of abelian
groups killed by $N$, with the same morphisms.

(SHEAF DAG node `lem-pur-torsion-sheaf-constant-module`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `sk-def-pbc-conventions`.
