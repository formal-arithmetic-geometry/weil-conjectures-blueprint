+++
kind  = "proof"
of    = "lem-wf-affine-nullstellensatz-vanishing"
+++
(1) For a maximal ideal $\mathfrak m$, the field $A/\mathfrak m$ is a
finitely generated $k$-algebra, hence a finite extension of $k$ by
Zariski's lemma. As $k$ is algebraically closed, the structure map
$k\to A/\mathfrak m$ is an isomorphism, so evaluation at $x$ is a
surjection $A\to k$ with kernel $\mathfrak m_x$. Conversely, the kernel
of a $k$-algebra homomorphism $A\to k$ is a maximal ideal, and the two
constructions are mutually inverse.

(2) By (1), $f(x)=0$ means $f\in\mathfrak m_x$. So $f$ lies in every
maximal ideal of $A$. By the Nullstellensatz (in the form: a finitely
generated algebra over a field is a Jacobson ring, so every prime ideal
is an intersection of maximal ideals), the intersection of the maximal
ideals of $A$ equals the intersection of its prime ideals, which is the
nilradical $\sqrt0$. Since $A$ is reduced, $\sqrt0=0$, hence $f=0$.
Equivalently, for any ideal $I\subseteq A$ the functions vanishing on the
$k$-points of $V(I)$ form $\sqrt I$; this is the form
$I(V(I))=\sqrt I$ of the Nullstellensatz.

(3) Write $Z=V(J)$ with $J\subseteq k[Y]$ radical, so that
$k[Z]=k[Y]/J$. For $g\in J$ and a $k$-point $x$ of $X$, one has
$(\varphi^*g)(x)=g(\varphi(x))=0$ because $\varphi(x)\in Z$. The
coordinate algebra $k[X]$ is reduced, so $\varphi^*g=0$ by (2). Thus
$\varphi^*:k[Y]\to k[X]$ kills $J$ and factors through $k[Y]/J$; the
factorization is unique because $k[Y]\to k[Y]/J$ is surjective.
