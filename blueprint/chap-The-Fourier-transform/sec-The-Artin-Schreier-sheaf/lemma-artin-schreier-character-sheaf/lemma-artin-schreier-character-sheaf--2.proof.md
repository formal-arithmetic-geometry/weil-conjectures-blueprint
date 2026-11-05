+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf--2"
order = 1217010
uses = ["lemma-artin-schreier-character-sheaf--1", "proposition-topos-functoriality"]
+++
Take the simultaneous Artin–Schreier cover
$u^q-u=f$, $v^q-v=g$, a $k_0^2$-torsor over $X$. The sheaves associated
to $f$, $g$, $-f$, and $f+g$ are isotypic components for the characters
$\psi(c_1)$, $\psi(c_2)$, $\psi(-c_1)$, and $\psi(c_1+c_2)$.
The internal-hom calculation for isotypic components gives

$$
\mathcal L_{\psi,-f}\simeq
\mathcal H om(\mathcal L_{\psi,f},\Qbarl),\qquad
\mathcal L_{\psi,f+g}\simeq
\mathcal H om(\mathcal L_{\psi,-f},\mathcal L_{\psi,g}).
$$

These are applications of
`AlgebraicGeometry.nonempty_iso_ihom_adicConstant_artinSchreierPlane` and
`AlgebraicGeometry.nonempty_iso_ihom_artinSchreierPlane`.
Lean expresses tensoring with a lisse sheaf as the internal hom out of
its dual. Substituting the first isomorphism into the second gives the
claimed tensor isomorphism.
