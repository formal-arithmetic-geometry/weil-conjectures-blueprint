+++
kind = "proof"
of = "proposition-six-operations-change-coefficients"
order = 647
+++
The first assertion is
Lemma [lemma-extension-scalars-preserves-dctf]. Next, the maps for $f^*$ and $\otimes^{\mathbf L}$ are isomorphisms by definition, and those for $Rf_*$,
$Rf_!$, $f^!$ and $\cHom$ by
Lemmas [lemma-change-coefficients-direct-image],
[lemma-change-coefficients-compact-support],
[lemma-change-coefficients-exceptional-inverse-image]
and [lemma-change-coefficients-internal-hom]. As for the compatibilities, the one with composites of coefficient maps was explained before
Lemma [lemma-extension-scalars-preserves-dctf], and for $f^!$ after
(7.1). The compatibility with composition of morphisms, on the other hand, holds for $f^*$ by the coherence of the
associativity isomorphisms for pullbacks. It holds for $Rf_*$ because
adjoint transposes of composites are composites. For $Rf_!$ the composition isomorphism is built from $R(qr)_*\simeq Rq_*Rr_*$ and the
interchange of an open and a proper direct image. Since the interchange is a map out of an extension by zero, the claim follows from the case of $Rf_*$ and restriction to the open subscheme. Finally, for $f^!$ it was shown after
(7.1).

For the units and counits, consider one of the three adjunctions
$F\dashv G$ over $\Lambda$. We write $F'\dashv G'$ for the same adjunction over
$\Lambda'$, with unit $\eta'$ and counit $\varepsilon'$, and write $M'$ for
$M_{\Lambda'}$. Then the comparison for the left adjoint is an isomorphism $c_F:F'(M')\simeq(FM)'$. In each case the comparison
$c_G:(GN)'\to G'(N')$ for the right adjoint was defined as the transpose of
$(\varepsilon_N)'\circ c_F$. In other words
$\varepsilon'_{N'}\circ F'(c_G)=(\varepsilon_N)'\circ c_F$, which is the
statement for the counit. For the unit we must show
$c_G\circ(\eta_M)'=G'(c_F)\circ\eta'_{M'}$ as maps $M'\to G'((FM)')$. We
compare transposes. The transpose of the right side is $c_F$, whereas the transpose of the left side is
$(\varepsilon_{FM})'\circ c_F\circ F'((\eta_M)')$. By naturality of $c_F$
this equals $(\varepsilon_{FM}\circ F\eta_M)'\circ c_F$, which is $c_F$ by a
triangle identity.
