+++
id = "proposition-lattices-representations-normal-scheme--1"
kind = "proposition"
title = "Monodromy from universal profinite étale covers"
name_showing = false
order = 1080001
aliases = ["bp-r332-1"]
lean = ["AlgebraicGeometry.ProEtale.exists_lisseMonodromy_of_isIntegrallyClosed_stalk", "AlgebraicGeometry.ProEtale.exists_lisseMonodromy"]
uses = ["definition-small-pro-etale-site", "definition-lisse-sheaves", "proposition-topos-functoriality"]
+++
Let $\ell$ be a prime, let $X$ be a nonempty connected, quasi-compact,
locally noetherian scheme, and suppose that every local ring of $X$ is
an integrally closed domain. Fix a field $\Omega$ and consider geometric
points $y:\operatorname{Spec}\overline\Omega\to X$. Here a lisse sheaf is a
$\Qbarl_X$-module which is pro-étale locally free of finite rank, as in
[definition-lisse-sheaves]; the coefficient sheaf has locally finite
continuous $\Qbarl$-valued functions as sections.

Write $F_y$ for the fibre functor on finite étale covers of $X$, and
$L_y=\Gamma(\operatorname{Spec}\overline\Omega,y^*L)$ for the stalk of a
lisse sheaf. There is a natural transport $L_y\simeq L_z$ along every
path $F_y\simeq F_z$. It respects identity paths and composition, the
canonical identifications obtained by reparametrising a geometric point,
and pullback along endomorphisms of $X$. Global sections are invariant
under transport, and transport preserves the evaluation pairings
$\mathcal{H}om(L,L')_y\times L_y\to L'_y$.

At every geometric point $t$, this transport makes the stalk functor an
equivalence between lisse $\Qbarl_X$-modules and finite-dimensional
continuous $\Qbarl$-representations of the ordinary profinite group
$\pi_1(X,t)=\operatorname{Aut}(F_t)$. Continuity means that
$g\mapsto\phi(\rho(g)v)$ is continuous for every vector $v$ and every
$\Qbarl$-linear functional $\phi$. Thus the stalk functor is faithful,
every equivariant linear map of stalks comes from a sheaf morphism, and
every such continuous representation is isomorphic to the stalk
representation of a lisse sheaf.

In particular, these conclusions hold when $X$ is nonempty, connected,
quasi-compact, locally noetherian and regular.
