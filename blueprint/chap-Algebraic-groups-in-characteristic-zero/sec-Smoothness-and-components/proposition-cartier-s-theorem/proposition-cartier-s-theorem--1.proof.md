+++
kind = "proof"
of = "proposition-cartier-s-theorem--1"
order = 1717001
uses = []
+++
First suppose that $k$ is algebraically closed. On an affine open
$\Spec A\subseteq G$, every maximal ideal is the kernel of a point
$e:A\to k$. Every tangent vector at $e$ extends to a derivation of $A$.
Indeed, if $x$ is this point of $G$ and $v$ is the corresponding
dual-number point, the morphism $(g,t)\mapsto gx^{-1}v(t)$ from
$\Spec(A[\varepsilon]/(\varepsilon^2))$ to $G$ restricts to the inclusion
of $\Spec A$. The thickening has the same underlying points, so this
morphism factors through $\Spec A$. On functions it is a section
$a\mapsto a+\varepsilon D(a)$, and evaluating $D$ at $e$ recovers the
given tangent vector. This is
`AlgebraicGeometry.GrpObj.exists_derivation_of_isOpenImmersion`.

Write $\mathfrak m=\ker e$. The invariant-derivation form of Cartier's
lemma shows that $\bigcap_{r\geq0}\mathfrak m^r$ is prime. A nilpotent
$b\in A$ therefore belongs to this intersection. Krull's intersection
theorem gives an $s\in A$ with $e(s)=1$ and $sb=0$
(`AlgHom.exists_apply_eq_one_mul_eq_zero_of_forall_exists_derivation`).
Thus the annihilator of $b$ is contained in no maximal ideal, so it is
the unit ideal and $b=0$. The affine opens cover $G$, proving reducedness
in `AlgebraicGeometry.isReduced_of_grpObj_of_isAlgClosed`.

For an arbitrary $k$ of characteristic zero, apply this argument after
base change to an algebraic closure. Reducedness descends along the
faithfully flat projection, as in `AlgebraicGeometry.isReduced_of_grpObj`.
Finally, a reduced scheme locally of finite type over a perfect field
is geometrically reduced. The smoothness theorem for geometrically
reduced group schemes then applies; this is
`AlgebraicGeometry.smooth_of_grpObj_of_isReduced`.
