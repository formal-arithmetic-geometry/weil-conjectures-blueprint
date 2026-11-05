+++
id = "proposition-inverting-ell--2"
kind = "proposition"
title = "Inverting $\\ell$ (2)"
name_showing = false
order = 303003
aliases = ["bp-r089-2"]
lean = ["AlgebraicGeometry.ProEtale.isLocalization_boundedConstructibleExtendScalars", "AlgebraicGeometry.ProEtale.rationalizationEquivalence", "AlgebraicGeometry.ProEtale.rationalizationQCompEquivalenceIso"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--7", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "example-locally-constant-functions-w-local--1", "theorem-existence-contractible-covers--1", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-pro-etale-site-separably-closed--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "proposition-six-operations-change-coefficients--1"]
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
