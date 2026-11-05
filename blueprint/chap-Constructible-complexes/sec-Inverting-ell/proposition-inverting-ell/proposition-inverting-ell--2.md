+++
id = "proposition-inverting-ell--2"
kind = "proposition"
title = "Inverting $\\ell$ (2)"
name_showing = false
order = 303002
aliases = ["bp-r089-2"]
lean = ["AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves"]
+++
Let $\ell$ be prime, let $E\subset\overline{\mathbf Q}_\ell$ be a finite
extension of $\mathbf Q_\ell$ with the restricted norm, and assume that
the underlying topological space of $X$ is Noetherian. In this detail,
$\Dbc$ denotes bounded complexes whose cohomology sheaves are pro-étale
locally finitely presented over the coefficient sheaf on the strata of
a finite constructible locally closed stratification.

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

Here the source is the Verdier quotient by the complexes $K$ with
$\ell^n\operatorname{id}_K=0$ for some $n\geq0$. If $Q$ denotes the
quotient functor and $\Phi$ the displayed equivalence, there is a natural
isomorphism $\Phi\circ Q\simeq F$.
