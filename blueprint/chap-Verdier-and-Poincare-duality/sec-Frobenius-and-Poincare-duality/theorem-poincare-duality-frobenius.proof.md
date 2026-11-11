+++
kind = "proof"
of = "theorem-poincare-duality-frobenius"
order = 886
uses = ["definition-perfect-pairing", "theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing"]
+++
The pairing $\beta_K$ is a composite of maps each of which commutes with
pullback along Frobenius, so it is equivariant. Over a
field the remaining statements then follow by linear algebra, because the
pairing is perfect.

Cup product with mixed supports and evaluation are natural for pullback
by Frobenius, and the isomorphism $\gamma_{a_X}$ and the trace map are equivariant
by Proposition [proposition-purity-trace-commute-frobenius]. Moreover, the contragredient Weil structure on $K^\vee$ is chosen so that evaluation
$K\otimes K^\vee\to\Lambda_X$ is a morphism of Weil complexes, with the
trivial structure on $\Lambda_X$. It follows that the composite $\beta_K$ is equivariant, which gives $\langle Fx,Fy\rangle=\langle
x,y\rangle$ for the first pairing. The second pairing is obtained by moving the
twist from the second factor to the values. Now geometric Frobenius acts on $\Lambda(d)$ by $q^{-d}$ and on
$\Lambda(-d)$ by $q^d$, so for $y$ in $H^{2d-i}(X,K^\vee)$ the
operator $F$ on $y\otimes\zeta$, with $\zeta$ a generator of
$\Lambda(d)$, is $q^{-d}(Fy)\otimes\zeta$. Removing the twist, we get the
displayed identity $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$.

For field coefficients, Corollary [corollary-degreewise-duality-over-fields] identifies
$H^{2d-i}(X,K^\vee)$, via the untwisted pairing, with the dual of
$H_c^i(X,K)$ tensored with $\Lambda(-d)$. Moreover, Frobenius on $H_c^i(X,K)$ is invertible, because $\phi_K$ is an isomorphism and pullback along the
automorphism $\operatorname{Fr}_X$ is invertible on cohomology.
In matrix terms, choose dual bases for the perfect pairing, let $F_i$ be the
matrix of $F$ on $H^i_c(X,K)$ and $F_{2d-i}$ that on $H^{2d-i}(X,K^\vee)$. Then the identity $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$ reads ${}^tF_iF_{2d-i}=q^d$. In other words, Frobenius on
$H^{2d-i}(X,K^\vee)$ is $q^d$ times the inverse transpose of Frobenius on
$H_c^i(X,K)$. Since a matrix and its transpose have the same characteristic polynomial, this proves the eigenvalue statement with algebraic multiplicities. Finally, taking determinants of
$F_{2d-i}=q^d\,{}^t(F_i)^{-1}$ on spaces of dimension $b$, we get
$\det F_{2d-i}=q^{db}(\det F_i)^{-1}$.
