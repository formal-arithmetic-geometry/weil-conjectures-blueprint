+++
id = "def-weil-geometric-point"
kind = "definition"
title = "Geometric point of a scheme"
uses = ["def-pc-scheme", "def-weil-affine-spectrum", "def-weil-algebraic-closure", "def-weil-residue-field"]
lean = ["AlgebraicGeometry.Scheme.SpecToEquivOfField, IsAlgClosed"]
tags = ["mathlib", "stacks-03PO"]
+++
Let $Y$ be a scheme [def-pc-scheme]. A *geometric point* of $Y$ is a morphism of schemes $\bar y:\operatorname{Spec}\Omega\to Y$ [def-weil-affine-spectrum] where $\Omega$ is an algebraically closed field [def-weil-algebraic-closure]. The image of the unique point of $\operatorname{Spec}\Omega$ is a point $y\in Y$, and $\bar y$ is said to *lie over* $y$. Such a morphism is the same as a point $y\in Y$ together with a field homomorphism $\kappa(y)\to\Omega$ from the residue field [def-weil-residue-field]; in particular $\Omega$ is a field extension of $\kappa(y)$.
