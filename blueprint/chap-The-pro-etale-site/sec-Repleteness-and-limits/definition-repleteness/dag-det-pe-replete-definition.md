+++
id = "dag-det-pe-replete-definition"
kind = "dag-definition"
title = "Replete topos of sheaves on a site"
name_showing = false
order = 84501
tags = ["sheaf-dag"]
split_from = "definition-repleteness--1"
dag_id = "det-pe-replete-definition"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.GrothendieckTopology.IsReplete"]
+++
Let $\mathcal C$ be a site and $\mathcal T=\Sh(\mathcal C)$. An *inverse sequence* in
$\mathcal T$ is a functor $\mathbf N^{\mathrm{op}}\to\mathcal T$, i.e. sheaves $F_n$
($n\ge0$) with transition maps $t_n\colon F_{n+1}\to F_n$. Its limit is the sheaf

$$
\Bigl(\varprojlim_nF_n\Bigr)(V)=\Bigl\{(x_n)\in\prod_nF_n(V):t_n(x_{n+1})=x_n\ \text{for all }n\Bigr\},
$$

with projections $p_m\colon\varprojlim_nF_n\to F_m$, $(x_n)\mapsto x_m$. A morphism of
sheaves $\varphi\colon F\to G$ is an *epimorphism* if it is locally surjective: for every
$V$ and $y\in G(V)$ there is a covering $\{V_k\to V\}$ and $x_k\in F(V_k)$ with
$\varphi(x_k)=y|_{V_k}$. The topos $\mathcal T$ is *replete* if, whenever all $t_n$ are
epimorphisms, every $p_m$ is an epimorphism.

(SHEAF DAG node `det-pe-replete-definition`; machine-alignment layer.) Split from [definition-repleteness--1]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`, `lem-weil-pbc-site-sheaf-sets-limits-sectionwise`.
