+++
id = "def-sbc-normal-dominant-galois"
kind = "definition"
title = "Integral, normal, dominant, Galois covers, and geometrical connectedness"
lean = ["AlgebraicGeometry.IsIntegral", "AlgebraicGeometry.IsNormalScheme", "AlgebraicGeometry.IsDominant", "AlgebraicGeometry.Scheme.GaloisCoverAction", "AlgebraicGeometry.Scheme.GaloisCover", "AlgebraicGeometry.Scheme.Hom.deckGroup", "AlgebraicGeometry.GeometricallyConnected", "AlgebraicGeometry.GeometricallyReduced"]
order = 1568
uses = ["def-weil-pbc-scheme-conventions"]
+++
A scheme $S$ is *integral* if it is nonempty and $\mathcal O_S(U)$ is an integral domain for every nonempty open
$U\subseteq S$; it is *normal* if it is integral and the local ring at every point is a normal domain (a domain
integrally closed in its fraction field). A morphism $f:X\to Y$ is *dominant* if $f(X)$ is dense in $Y$.

Let $G$ be a group. A *Galois cover with group $G$* of a scheme $C$ is a finite étale surjective morphism
$\pi:Z\to C$ together with a left action of $G$ on $Z$ by morphisms over $C$ such that
- **(a)** the action is simply transitive on every geometric fibre: for every algebraically closed field $\Omega$ and
  all $x,y:\operatorname{Spec}\Omega\to Z$ with $\pi x=\pi y$ there is a unique $g\in G$ with $g\circ x=y$;
- **(b)** $\pi$ is the quotient of $Z$ by $G$: every morphism $Z\to W$ invariant under $G$ factors uniquely through
  $\pi$.

For a finite group $G$ one also uses the variant in which (a) and (b) are replaced by the condition that $Z$ is a
$G$-torsor over $C$: the morphism $\coprod_{g\in G}Z\to Z\times_CZ$ with $g$-th component $(g,\mathrm{id})$ is an isomorphism.
The total space is not required to be connected. The *deck group* of a morphism $\pi:Z\to C$ is the group of its
automorphisms over $C$.

A morphism $f:X\to S$ is *geometrically connected* (resp. *geometrically reduced*) if for every field $K$ and every
morphism $\operatorname{Spec}K\to S$ the scheme $X\times_S\operatorname{Spec}K$ is connected (resp. reduced).
Equivalently, every fibre $X_s$ is geometrically connected (resp. geometrically reduced) over $\kappa(s)$.
