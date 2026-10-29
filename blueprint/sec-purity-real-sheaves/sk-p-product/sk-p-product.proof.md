+++
kind  = "proof"
of    = "sk-p-product"
+++
A reductive Lie algebra is the sum of its center and its derived algebra,
and the derived algebra lies in the Lie algebra of $H$ because commutators
lie in $H$. We compare Lie algebras. Since the stabilizer of a subspace is
closed, the $\rho(W(U_0))$-stable subspaces are precisely the $G$-stable
subspaces. Hence $V$ is semisimple as a
$G(\overline{\mathbf Q}_\ell)$-module and, by [sk-i-restriction], also as a
$G^\circ(\overline{\mathbf Q}_\ell)$-module. By [sk-p-comparison], it is
then a faithful semisimple module for $\mathfrak g=\Lie(G^\circ)$, and
[sk-p-lie] shows that

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g].
$$

Put $T=Z(G^\circ)^\circ$ and $\mathfrak h=\Lie(H^\circ)$. By the
comparison between groups and Lie algebras in [sk-p-comparison],
$\Lie(T)=Z(\mathfrak g)$. To see that
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h$, note that the commutator
morphism $G\times G\to G$ factors through the closed subgroup $H$, because
it does so on $\overline{\mathbf Q}_\ell$-points by
[sk-lem-walg-normal-commutator] and $G\times G$ is reduced. For
$X,Y\in\mathfrak g$, put
$R=\overline{\mathbf Q}_\ell[\varepsilon,\eta]/(\varepsilon^2,\eta^2)$. The
commutator of $1+\varepsilon X$ and $1+\eta Y$ in $G(R)$ is
$1+\varepsilon\eta[X,Y]$, so it lies in $H(R)$. The subring
$\overline{\mathbf Q}_\ell[\varepsilon\eta]\subset R$ is a ring of dual
numbers, and the equations of $H$ vanish on $1+\varepsilon\eta[X,Y]$
already over this subring. Hence $[X,Y]\in\Lie(H)=\mathfrak h$.
Consequently

$$
\mathfrak g=\Lie(T)+\mathfrak h.
$$

The multiplication $T\times H^\circ\to G^\circ$ is a homomorphism because
$T$ is central. By [sk-p-geometry], its image is a closed connected
subgroup, and its Lie algebra contains both summands on the right.
Therefore the image has the same Lie algebra as $G^\circ$, and it equals
$G^\circ$, again by that lemma.

For the complement:

*The Lie inclusion.* Let $H\subseteq G$ be as in the complement of
[sk-lem-walg-normal-commutator], over any field $k$, and
$X,Y\in\Lie(G)$. Take $R=k[\varepsilon,\delta]/(\varepsilon^2,\delta^2)$;
then $1+\varepsilon X$ and $1+\delta Y$ lie in $G(R)$ by
[def-wf-lie-algebra-derivation], and direct matrix multiplication gives

$$
(1+\varepsilon X)(1+\delta Y)(1-\varepsilon X)(1-\delta Y)
=1+\varepsilon\delta(XY-YX),
$$

an $R$-point of $H$ by hypothesis. The $k$-algebra map
$k[\eta]/\eta^2\to R$, $\eta\mapsto\varepsilon\delta$, is injective and
carries $1+\eta[X,Y]$ to this point; so for each defining equation $f$ of
$H$, $f(1+\eta[X,Y])$ maps to $0$ and hence vanishes, i.e.
$1+\eta[X,Y]\in H(k[\eta]/\eta^2)$ and $[X,Y]\in\Lie(H)$ by
[def-wf-lie-algebra-derivation]. No reducedness is used. If $k$ is
algebraically closed of characteristic zero, [sk-i-cartier] gives
$\Lie(G^\circ)=\Lie(G)$ and $\Lie(H^\circ)=\Lie(H)$ through the
inclusions, so $[\Lie(G^\circ),\Lie(G^\circ)]\subseteq\Lie(H^\circ)$.

*Semisimplicity for $G^\circ(k)$.* Let $\rho$ be semisimple and $k$
algebraically closed. By the density paragraph of the proof of
[sk-lem-walg-normal-commutator], the $W$-stable subspaces of $k^n$ are
exactly the $G(k)$-stable ones, so a decomposition of $k^n$ into simple
$W$-modules is a decomposition into simple $G(k)$-modules. Conjugation by
$g\in G(k)$ is an automorphism of $G$ fixing $1$, so it preserves the
connected component of $1$; thus $G^\circ(k)$ is normal in $G(k)$, and
[sk-i-restriction] shows that $k^n$ is a semisimple $G^\circ(k)$-module.

*The general product.* The general version is the same argument, the two
hypotheses replacing the commutator and semisimplicity statements above;
surjectivity on underlying spaces follows because the closed image
contains all closed points.
