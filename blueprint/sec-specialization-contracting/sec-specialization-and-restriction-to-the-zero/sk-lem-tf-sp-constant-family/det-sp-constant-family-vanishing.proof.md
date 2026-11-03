+++
kind = "proof"
of = "det-sp-constant-family-vanishing"
uses = ["det-sp-nearby-cycles-exchanges", "det-sp-constant-family-conservative", "sbc-thm-bounded-derived-smooth-base-change"]
+++
*Exchanges.* For $f\colon Y'\to Y$, the morphism $f\times\mathrm{id}_S$ of constant families has
fibres $f$. The specialization units are adjunction units of $\bar j$, and the exchanges of
[det-sp-nearby-cycles-exchanges] are their mates; since these exchanges commute with composition
and with the units, the squares relating $\sigma_Y$ and $\sigma_{Y'}$ through the proper exchange
(for proper $f$) or the pullback exchange (for smooth $f$) commute. Both exchanges are invertible
in these cases, so taking cofibres gives the two displayed isomorphisms. In particular $B$ is an
exact functor with bounded constructible values, and smooth exchange for étale maps makes the
vanishing of $B_Y(L)$ local on $Y$. A closed immersion $Y\hookrightarrow\mathbf A^n$ and the
faithfulness of its direct image reduce it to all affine spaces.

*Generic vanishing on affine space.* For $Y=\mathbf A^n$, the complex $B_Y(L)$ vanishes on a dense
open subset. Use the truncation triangles to reduce to a sheaf, shrink until it is locally
constant, and pass to a finite étale cover that makes it constant. Smooth base change
[sbc-thm-bounded-derived-smooth-base-change] for the smooth structure map to $\operatorname{Spec}k$
reduces the assertion there to $R\Psi_S(M_\eta)=M$ for a finite $A$-module $M$, which is the
calculation at a geometric generic point of a strictly henselian trait. Surjective étale pullback
detects vanishing.

*Induction.* Induct on $n$, with the point calculation as base. Let $T$ be the closure of the
support of $B_{\mathbf A^n}(L)$, a proper closed subset by the preceding step. By the linear form
of Noether normalization there is a linear projection $q\colon\mathbf A^n\to\mathbf A^{n-1}$ finite
on $T$: choose its kernel line to avoid the intersection of the projective closure of $T$ with the
hyperplane at infinity. Compactify that line to obtain
$\bar q\colon\bar Y=\mathbf P^1\times\mathbf A^{n-1}\to\mathbf A^{n-1}$, the open immersion
$v\colon\mathbf A^n\hookrightarrow\bar Y$, and $\bar L=v_!L$. By locality, $B_{\bar Y}(\bar L)$ is
supported on $T\cup(\bar Y\setminus\mathbf A^n)$, which is closed in $\bar Y$ and finite over
$\mathbf A^{n-1}$: $T$ is finite, hence proper over the base and closed in $\bar Y$, and the
boundary is one section. The proper exchange and the induction hypothesis give

$$
R\bar q_*B_{\bar Y}(\bar L)\simeq B_{\mathbf A^{n-1}}(R\bar q_*\bar L)=0.
$$

By [det-sp-constant-family-conservative], $B_{\bar Y}(\bar L)=0$; restricting to $\mathbf A^n$
gives $B_{\mathbf A^n}(L)=0$.
