+++
kind = "proof"
of = "lemma-fourier-transform-constant-sheaf"
order = 1235
uses = ["lemma-stability", "lemma-artin-schreier-character-sheaf", "lemma-integral-linear-character", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For $K=E$, the stalk formula (16.2) at $y$ is the
integral of the character sheaf $\mathcal L_{\psi(xy)}$ over the line,
shifted by one. By Lemma [lemma-integral-linear-character] it
vanishes for $y\ne0$ and equals $E(-1)[-2]$ at $y=0$. Hence
$\operatorname{FT}_\psi(E)$ is supported at the origin, and with the
shift $[1]$ it is $\delta_0(-1)[-1]$. For $K=\delta_0$, the
pullback by the first projection is supported on
$\{0\}\times\mathbf A^1$. Since the kernel is trivial there and the second
projection is an isomorphism, this gives $E[1]$. Moreover, the trace map and
the unit trivialization are defined over $k_0$, so both identifications
are Frobenius-equivariant.
