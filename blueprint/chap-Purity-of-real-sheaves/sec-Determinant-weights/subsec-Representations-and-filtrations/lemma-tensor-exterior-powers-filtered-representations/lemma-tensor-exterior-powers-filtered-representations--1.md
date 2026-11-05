+++
id = "lemma-tensor-exterior-powers-filtered-representations--1"
kind = "lemma"
title = "Simple subquotients of a tensor product"
name_showing = false
order = 1124001
aliases = ["bp-r345-1"]
lean = ["Subrepresentation.exists_subquotient_tprod_equiv"]
uses = []
+++
The tensor filtration is bypassed by Lean, which uses the following
consequence about simple subquotients.

Let $W$ be a group, let $k$ be a field, and let $V$ and $V'$ be
finite-dimensional $k$-representations of $W$. If $Q$ is a simple
subquotient of $V\otimes_k V'$, then there are stable subspaces
$U_V\subsetneq S_V\subseteq V$ and $U_{V'}\subsetneq S_{V'}\subseteq V'$
such that $A=S_V/U_V$ and $B=S_{V'}/U_{V'}$ are simple and $Q$ is
isomorphic, as a $W$-representation, to a subquotient of $A\otimes_k B$.
