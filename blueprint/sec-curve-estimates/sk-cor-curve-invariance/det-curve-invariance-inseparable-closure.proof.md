+++
kind = "proof"
of = "det-curve-invariance-inseparable-closure"
+++
Since $k$ is separably closed, $\bar k/k$ is purely inseparable: every
$a\in\bar k$ satisfies $a^{p^e}\in k$ for some $e$ (or $\bar k=k$ in
characteristic zero). Hence $\operatorname{Spec}\bar k\to\operatorname{Spec}k$
is integral, surjective and radicial: for every $k$-algebra $R$, each element
of $\bar k\otimes_kR$ has a $p^e$th power in the image of $R$, so
$\operatorname{Spec}(\bar k\otimes_kR)\to\operatorname{Spec}R$ is bijective
on points with purely inseparable residue field extensions; that is, a universal homeomorphism. Its
base change $u:C_{\bar k}\to C$ is again a universal homeomorphism
([lem-weil-pbc-universal-homeomorphism-base-change]). By
[thm-weil-pbc-universal-homeomorphism-invariance], $u^{-1}$ is an
equivalence of étale topoi compatible with cohomology, so the pullback maps
$H^q(C,F)\to H^q(C_{\bar k},u^{-1}F)$ are isomorphisms.

For the square: the two composites $C_{\bar k'}\to C$ are the same morphism,
because $\bar k\subseteq\bar k'$ extends $k\subseteq k'$, and pullback maps
on cohomology are functorial for composition of morphisms (the pullback map
of a composite is the composite of the pullback maps, via the canonical
isomorphism $(fg)^{-1}\cong g^{-1}f^{-1}$). Hence the square commutes.
