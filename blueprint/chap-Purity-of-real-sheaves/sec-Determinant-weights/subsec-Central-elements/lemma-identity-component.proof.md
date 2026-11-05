+++
kind = "proof"
of = "lemma-identity-component"
order = 1134
uses = ["lemma-restriction-normal-subgroup", "lemma-connected-components-images-homomorphisms", "proposition-lie-algebras-faithful-semisimple-representation", "lemma-stable-subspaces-center", "proposition-cartier-s-theorem", "lemma-normality-geometric-monodromy", "lemma-identity-component--1"]
+++
A connected algebraic group is determined by its Lie algebra among its
closed connected subgroups, so it suffices to show that the Lie algebras
of $Z(G^\circ)^\circ$ and $H^\circ$ together span that of $G^\circ$. We show
that this Lie algebra is reductive, hence the sum of its center and its
derived algebra, and that the derived algebra lies in the Lie algebra of
$H$ because commutators lie in $H$.

*Reductivity.* Write $\mathfrak g=\operatorname{Lie}(G^\circ)$. Then

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g],
$$

by Proposition [proposition-lie-algebras-faithful-semisimple-representation],
once we know that $V$ is a faithful semisimple $\mathfrak g$-module. The
$\rho(W(U_0))$-stable subspaces are precisely the $G$-stable subspaces,
because the stabilizer of a subspace is closed. Hence $V$ is semisimple as a
$G(\overline{\mathbf Q}_\ell)$-module, and by Lemma [lemma-restriction-normal-subgroup]
it is also semisimple as a $G^\circ(\overline{\mathbf Q}_\ell)$-module. Then
Lemma [lemma-stable-subspaces-center] makes it a faithful
semisimple $\mathfrak g$-module.

*The center and the derived algebra.* Put $T=Z(G^\circ)^\circ$ and
$\mathfrak h=\operatorname{Lie}(H^\circ)$. The comparison between
groups and Lie algebras in Lemma [lemma-stable-subspaces-center] gives
$\operatorname{Lie}(T)=Z(\mathfrak g)$. Moreover
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h$, because the
commutator morphism $G\times G\to G$ factors through the closed
subgroup $H$: it does so on $\overline{\mathbf Q}_\ell$-points by
Lemma [lemma-normality-geometric-monodromy], and $G\times G$ is
reduced. To deduce the inclusion, let $X,Y\in\mathfrak g$ and put
$R=\overline{\mathbf Q}_\ell[\varepsilon,\eta]/(\varepsilon^2,\eta^2)$. The commutator of
$1+\varepsilon X$ and $1+\eta Y$ in $G(R)$ is $1+\varepsilon\eta[X,Y]$, and
it lies in $H(R)$. Here the subring $\overline{\mathbf Q}_\ell[\varepsilon\eta]\subset R$
is a ring of dual numbers, and the equations of $H$ vanish on
$1+\varepsilon\eta[X,Y]$ already over this subring. Hence
$[X,Y]\in\operatorname{Lie}(H)=\mathfrak h$, and

$$
\mathfrak g=\operatorname{Lie}(T)+\mathfrak h.
$$

*Back to groups.* The multiplication $T\times H^\circ\to G^\circ$ is a
homomorphism, because $T$ is central. By
Lemma [lemma-connected-components-images-homomorphisms] its
image is a closed connected subgroup, whose Lie algebra contains
both summands on the right, hence equals that of $G^\circ$. By the
same lemma the image is therefore $G^\circ$.
