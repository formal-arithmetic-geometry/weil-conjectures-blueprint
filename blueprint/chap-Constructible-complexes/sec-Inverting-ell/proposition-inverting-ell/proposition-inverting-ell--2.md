+++
id = "proposition-inverting-ell--2"
kind = "proposition"
title = "Inverting $\\ell$ (2)"
name_showing = false
order = 303003
aliases = ["bp-r089-2"]
lean = ["AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
+++
Let $\ell$ be prime, let $E\subset\overline{\mathbf Q}_\ell$ be a finite
extension of $\mathbf Q_\ell$, and assume that the underlying
topological space of $X$ is Noetherian.

Derived extension of scalars

$$
F=E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}-:
\Dbc(X,\mathcal O_E)\longrightarrow\Dbc(X,E)
$$

is a localization at the morphisms whose mapping cone is killed by
some power of $\ell$. Thus it induces an equivalence

$$
\Dbc(X,\mathcal O_E)[\ell^{-1}]\xrightarrow{\ \sim\ }\Dbc(X,E),
$$

where the source is the Verdier quotient by the complexes $K$ with
$\ell^n\operatorname{id}_K=0$ for some $n\geq0$; equivalently, it has
the objects of $\Dbc(X,\mathcal O_E)$ and Hom groups tensored with $E$. If $Q$ denotes the
quotient functor and $\Phi$ the displayed equivalence, there is a natural
isomorphism $\Phi\circ Q\simeq F$.
