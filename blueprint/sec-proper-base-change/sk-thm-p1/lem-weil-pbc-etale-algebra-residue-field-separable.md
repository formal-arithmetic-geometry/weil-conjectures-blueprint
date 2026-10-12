+++
id = "lem-weil-pbc-etale-algebra-residue-field-separable"
kind = "lemma"
title = "Residue field extensions of an etale algebra are finite separable"
uses = ["def-weil-etale-morphism"]
lean = ["Algebra.IsUnramifiedAt instances IsSeparable / Module.Finite (p.ResidueField) (q.ResidueField); Algebra.formallyUnramified_iff_forall; AlgebraicGeometry.HasRingHomProperty.Spec_iff"]
tags = ["sheaf-dag", "mathlib", "stacks-00U3"]
+++
Let $A\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}A$ is etale [def-weil-etale-morphism], let $\mathfrak q\subset B$ be a prime ideal and $\mathfrak p=\mathfrak q\cap A$ (the preimage of $\mathfrak q$ in $A$). Then the residue field $\kappa(\mathfrak q)$ (the fraction field of $B/\mathfrak q$) is a finite separable extension of $\kappa(\mathfrak p)$ via the induced map $\kappa(\mathfrak p)\to\kappa(\mathfrak q)$; in particular every element of $\kappa(\mathfrak q)$ is a root of a separable polynomial with coefficients in $\kappa(\mathfrak p)$.
