+++
kind = "proof"
of = "lemma-connected-components-images-homomorphisms"
order = 1715
uses = ["proposition-cartier-s-theorem"]
+++
For (1) we use smoothness to see that irreducible and connected components
coincide; for (2), Chevalley's theorem gives an open subset of the closure
inside the image, and translations spread it over the closure; (3) is a
dimension count.

*Components.* The irreducible components of $G$ are finite in number,
as $G$ is Noetherian, and they are exactly the connected components. Indeed,
$G$ is smooth by Proposition [proposition-cartier-s-theorem], and a
regular local ring is a domain. So distinct irreducible components of
$G$ do not meet, and they are open and closed. Let $G^\circ$ be the
component containing $1$. It is a subgroup. To see this, note that
$G^\circ\times G^\circ$ is irreducible, $\Omega$ being algebraically
closed. Hence the image of the morphism $G^\circ\times G^\circ\to G$,
$(x,y)\mapsto xy^{-1}$, is irreducible. It contains $1$, so it lies in
$G^\circ$. For the same reason the image of $G^\circ$ under conjugation
by a point of $G$ is irreducible and contains $1$, so $G^\circ$ is
normal. Translating $G^\circ$ by points of
$G$, we see that the other components are its cosets.

For example, the homomorphism $\mathbf G_m\to\mathbf G_m$, $x\mapsto x^2$, has image all
of $\mathbf G_m$ and kernel $\mu_2$, a closed subgroup with two
components.

*Images.* Let $f:G\to G'$ be a homomorphism. We show that its image
equals the closure $J$ of the image, which is a subgroup by continuity of
multiplication and inversion. First, the subgroup $f(G(\Omega))$ of
$J(\Omega)$ contains the $\Omega$-points of a nonempty open
$U\subseteq J$. Indeed, $f(G)$ is constructible by Chevalley's theorem
[Stacks, [054K](https://stacks.math.columbia.edu/tag/054K)], a dense constructible subset contains a nonempty open
subset of its closure, and $\Omega$ is algebraically closed. Translating
$U$ by the inverse of one of its points in the image, we obtain an open
neighbourhood of $1$ contained in the image. Translating further by
points of the image, we see that the image is open in $J$. It is then
also closed, since its complement is a union of cosets of this open
subgroup. As it is dense in $J$, it is equal to $J$.

*Lie algebras.* Let $K$ be as in (3). Cartier's theorem gives
$\dim K=\dim\operatorname{Lie}(K)=\dim G$, so $K$ and $G$ have the same
underlying closed subset, as a proper closed subset of the irreducible
variety $G$ has smaller dimension. They are equal as schemes, since both
are reduced by Proposition [proposition-cartier-s-theorem].
