+++
id = "def-weil-residue-field"
kind = "definition"
title = "Residue field of a point of a scheme"
order = 415
lean = ["AlgebraicGeometry.Scheme.residueField"]
tags = ["mathlib"]
+++
Let $X$ be a scheme and $x\in X$ a point, with local ring $\mathcal O_{X,x}$ (the stalk of the structure sheaf at $x$) and maximal ideal $\mathfrak m_x$. The *residue field* of $X$ at $x$ is the field

$$
 \kappa(x)=\mathcal O_{X,x}/\mathfrak m_x .
$$

A morphism of schemes $f:X\to Y$ induces, for every $x\in X$, a homomorphism of fields $\kappa(f(x))\to\kappa(x)$, the map induced on residue fields by the local homomorphism $\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}$. For $Y=\operatorname{Spec}K$ with $K$ a field, $\kappa(f(x))=K$, so $\kappa(x)$ is a field extension of $K$ through $f$.
