+++
kind = "proof"
of = "proposition-six-operations-change-coefficients--19"
order = 646039
+++
Apply the following adjunction calculation to the pair displayed in this clause. Here $(\cdot)'$ denotes the stated scalar extension, not a geometric base change.

For the units and counits, consider one of the three adjunctions
$F\dashv G$ over $\Lambda$. Write $F'\dashv G'$ for the same adjunction over
$\Lambda'$, with unit $\eta'$ and counit $\varepsilon'$, and write $M'$ for
$M_{\Lambda'}$. The comparison for the left adjoint is an isomorphism
$c_F:F'(M')\simeq(FM)'$. In each case the comparison
$c_G:(GN)'\to G'(N')$ for the right adjoint was defined as the transpose of
$(\varepsilon_N)'\circ c_F$. In other words
$\varepsilon'_{N'}\circ F'(c_G)=(\varepsilon_N)'\circ c_F$, which is the
statement for the counit. For the unit we must show
$c_G\circ(\eta_M)'=G'(c_F)\circ\eta'_{M'}$ as maps $M'\to G'((FM)')$. We
compare transposes. The transpose of the right side is $c_F$. The transpose
of the left side is
$(\varepsilon_{FM})'\circ c_F\circ F'((\eta_M)')$. By naturality of $c_F$
this equals $(\varepsilon_{FM}\circ F\eta_M)'\circ c_F$, which is $c_F$ by a
triangle identity.

*Source:* the proof of Proposition [proposition-six-operations-change-coefficients].
