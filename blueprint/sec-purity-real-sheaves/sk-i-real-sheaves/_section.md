+++
id = "sk-i-real-sheaves"
kind = "section"
title = "The lisse sheaf–representation equivalence"
order = 2792
uses = ["sk-d-real-setup", "sk-d-real-weil", "sk-i-real-galois"]
+++
*Proposition (sketch).*

Throughout, $C_0$ is the curve and $C$ its base
change to $k$; $P=\pi_1(C)$ is the geometric fundamental group, $W(C_0)$ the
Weil group with degree map and chosen degree-one lift $\gamma$, and
$E\subset\Qlb$ a finite coefficient field with valuation ring
$\mathcal O_E$ and maximal ideal $\mathfrak m_E$, all as in
[sk-d-real-weil]. A lisse Weil sheaf $\mathcal F$ on $C_0$ has geometric
generic stalk $\mathcal F_{\bar\eta}$.

The functor $\mathcal F\mapsto(V,\rho)=(\mathcal F_{\bar\eta}, \rho_{\mathcal F})$ is an exact tensor equivalence between lisse Weil sheaves
on $C_0$ and the representations of [sk-d-real-weil]: a short exact
sequence $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ corresponds to
$0\to V'\to V\to V''\to0$. Subobjects, quotients and subquotients therefore
match on the two sides, in both directions.

## Proof

*Finite level.* Each $\mathcal O_E/\mathfrak m_E^n$ is a finite ring, so
[sk-i-real-galois] identifies locally constant sheaves of finite free
$\mathcal O_E/\mathfrak m_E^n$-modules on $C$ with finite free modules over
that ring carrying a continuous $P$-action. Rank is a property of the stalk
and is constant because $C$ is connected.

*Integral and rational levels.* A lisse adic model has surjective
transition maps, so the stalks $M_n$ form a surjective system whose limit is
finite free over $\mathcal O_E$, with continuous action because the
$\mathfrak m_E$-adic topology is the limit of the discrete quotient
topologies; levelwise reduction inverts the construction. Morphism groups
are the limits of their finite-level counterparts, with surjective transitions
and hence no $\varprojlim^1$ term, so the functor is fully faithful.
Inverting the uniformizer on morphisms and passing to the filtered colimit
over the finite $E\subset\Qlb$ are each given by a universal property and are
performed the same way on both sides, so the equivalence descends to the
coefficients of [sk-d-real-setup].

*Frobenius descent.* Geometric Frobenius is an automorphism of the
scheme $C$, so $\Frob^*$ is an autoequivalence of lisse sheaves on $C$;
comparing the stalks at $\bar\eta$ and $\Frob(\bar\eta)$ along a degree-one
lift $\gamma$ turns it into $\rho\mapsto\rho\circ c_\gamma$, conjugation by
$\gamma$ on $P$. A Weil structure $\varphi:\Frob^*\mathcal F\to\mathcal F$ is
therefore an automorphism $\Phi$ of $V$ with
$\Phi\,\rho(\gamma g\gamma^{-1})\,\Phi^{-1}=\rho(g)$ for $g\in P$, and since
every element of $W(C_0)$ is uniquely $g\gamma^{n}$ by [sk-d-real-weil],
setting $\rho(\gamma)=\Phi$ extends $\rho$ to $W(C_0)$. Another lift changes
$\Phi$ by an element of $\rho(P)$ and gives an isomorphic representation. The
morphism condition $u\varphi=\psi\,\Frob^{*}u$ says on stalks that $u$
intertwines the two operators $\Phi$, which with $P$-equivariance is exactly
$W(C_0)$-equivariance; hence full faithfulness.

*Exactness.* Exactness and tensor products are levelwise for adic
systems and survive the localization and the filtered colimit, and Weil
kernels and cokernels are computed on the underlying sheaves. The matching
of subobjects, quotients and subquotients follows.

Uses: [sk-d-real-setup], [sk-d-real-weil], [sk-i-real-galois]
