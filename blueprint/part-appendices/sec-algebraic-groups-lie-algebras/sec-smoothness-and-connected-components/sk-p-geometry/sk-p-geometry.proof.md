+++
kind = "proof"
of = "sk-p-geometry"
+++
Since $G$ is Noetherian, it has finitely many irreducible components.
By Proposition [sk-i-cartier], the scheme $G$ is smooth, and
since a regular local ring is a domain, distinct irreducible components
of $G$ do not meet. Hence the irreducible components are open and
closed, and they are exactly the connected components. Let $G^\circ$ be
the component containing $1$. Since $\Omega$ is algebraically closed,
$G^\circ\times G^\circ$ is irreducible, and hence so is the image of the
morphism $G^\circ\times G^\circ\to G$, $(x,y)\mapsto xy^{-1}$. This
image contains $1$, so it lies in $G^\circ$, and $G^\circ$ is a
subgroup. For the same reason the image of $G^\circ$ under conjugation
by a point of $G$ is irreducible and contains $1$, so conjugation
preserves $G^\circ$. Translations identify the
other components with its cosets.

Let $f:G\to G'$ be a homomorphism. By continuity of
multiplication and inversion, the closure $J$ of its image is a
subgroup. Chevalley's theorem [Stacks, Tag 054K](https://stacks.math.columbia.edu/tag/054K) says that $f(G)$ is
constructible, and a dense constructible subset contains a nonempty
open subset of its closure. Since $\Omega$ is algebraically closed, the
subgroup $f(G(\Omega))$ of $J(\Omega)$ therefore contains the $\Omega$-points of a
nonempty open $U\subseteq J$. Translating $U$ by the
inverse of one of its points in the image, we obtain an open
neighbourhood of $1$ contained in the image, and translating further
by points of the image, we see that the image is open in $J$. Its
complement is a union of cosets of this open subgroup, hence open as
well. Therefore the image is closed, and since it is dense in $J$, it
is equal to $J$.

Finally, let $K$ be as in the last assertion. By Cartier's theorem,
$\dim K=\dim\operatorname{Lie}(K)=\dim G$. Since a proper closed subset
of the irreducible variety $G$ has smaller dimension, $K$ and $G$ have
the same underlying closed subset. Both are reduced by
Proposition [sk-i-cartier], and hence they are equal as
schemes.
