+++
kind = "proof"
of = "sk-p-product"
+++
A reductive Lie algebra is the sum of its center and
its derived algebra, and the derived algebra lies in the Lie algebra
of $H$ because commutators lie in $H$. We compare Lie algebras. Since
the stabilizer of a subspace is closed,
the $\rho(W(U_0))$-stable subspaces are precisely the $G$-stable subspaces.
Hence $V$ is
semisimple as a $G(\overline{\mathbf Q}_\ell)$-module and, by
Lemma [sk-i-restriction], also as a $G^\circ(\overline{\mathbf Q}_\ell)$-module.
By Lemma [sk-p-comparison], it is then a faithful semisimple
module for $\mathfrak g=\operatorname{Lie}(G^\circ)$, and
Proposition [sk-p-lie] shows that

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g].
$$

Put $T=Z(G^\circ)^\circ$ and
$\mathfrak h=\operatorname{Lie}(H^\circ)$. By the comparison between
groups and Lie algebras in Lemma [sk-p-comparison],
$\operatorname{Lie}(T)=Z(\mathfrak g)$. To see that
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h$, note that the
commutator morphism $G\times G\to G$ factors through the closed
subgroup $H$, because it does so on $\overline{\mathbf Q}_\ell$-points by the previous
lemma and $G\times G$ is reduced. For $X,Y\in\mathfrak g$, put
$R=\overline{\mathbf Q}_\ell[\varepsilon,\eta]/(\varepsilon^2,\eta^2)$. The commutator of
$1+\varepsilon X$ and $1+\eta Y$ in $G(R)$ is $1+\varepsilon\eta[X,Y]$, so
it lies in $H(R)$. The subring $\overline{\mathbf Q}_\ell[\varepsilon\eta]\subset R$ is a ring
of dual numbers, and the equations of $H$ vanish on
$1+\varepsilon\eta[X,Y]$ already over this subring. Hence
$[X,Y]\in\operatorname{Lie}(H)=\mathfrak h$.
Consequently

$$
\mathfrak g=\operatorname{Lie}(T)+\mathfrak h.
$$

The multiplication $T\times H^\circ\to G^\circ$ is a homomorphism
because $T$ is central. By Lemma [sk-p-geometry], its
image is a closed connected subgroup, and its Lie algebra contains
both summands on the right. Therefore the image has the same Lie
algebra as $G^\circ$, and it equals $G^\circ$, again by that lemma.
