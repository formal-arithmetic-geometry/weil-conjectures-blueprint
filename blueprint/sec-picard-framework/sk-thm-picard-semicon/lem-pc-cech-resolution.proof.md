+++
kind  = "proof"
of    = "lem-pc-cech-resolution"
+++
Fix a point of $X$ and a covering open $U_i$ containing it.
Restrict the augmented complex to $U_i$. This restricted cover
contains the entire space $U_i$ as one member; insertion of that
index gives a contracting homotopy of the augmented Cech complex.
Thus the complex is locally exact, and hence exact as a complex
of sheaves. This argument does not identify a boundary stalk of
an open direct image with zero.

The intersections $U_J$ are affine: for two affine opens this follows
by pulling the closed diagonal of $X/S$ back to their affine
product over $S$, and the general case follows by induction.
Each $j_J$ is an affine morphism, since its inverse image in every
affine open of $X$ is again such an affine intersection.
By [lem-pc-affine-morphism-hi],
$R^qj_{J,*}(\mathcal F|_{U_J})=0$ for $q>0$.
For an affine open $V\subseteq S$, the inverse image
$U_J\times_S V$ is affine. The Leray spectral sequence for $j_J$
restricted over $V$, together with the preceding vanishing and
[lem-pc-affine-vanishing], gives

$$
H^q(f^{-1}V,j_{J,*}(\mathcal F|_{U_J}))
=H^q(U_J\times_S V,\mathcal F)=0\quad(q>0).
$$

Affine opens form a basis on $S$, so all higher direct images under
$f$ of these Cech terms vanish. A finite resolution by acyclic
objects computes the right derived functor (apply $f_*$ to an
injective double resolution and use its two spectral sequences).
This proves the assertion.
