+++
kind  = "proof"
of    = "lem-pc-cech-resolution"
+++
Fix a point of $X$ and a covering open $U_i$ containing it. (Exactness needs neither quasi-coherence nor affineness.)
Restrict the augmented complex to $U_i$. This restricted cover
contains the entire space $U_i$ as one member; insertion of that
index gives a contracting homotopy of the augmented Cech complex.
Thus the complex is locally exact, and hence exact as a complex
of sheaves. This argument does not identify a boundary stalk of
an open direct image with zero.

The intersections $U_y$ are affine: for two affine opens this follows
by pulling the closed diagonal of $X/S$ back to their affine
product over $S$, and the general case follows by induction.
Each $j_y$ is an affine morphism, since its inverse image in every
affine open of $X$ is again such an affine intersection.
By [lem-pc-affine-morphism-hi],
$R^qj_{y,*}(\mathcal F|_{U_y})=0$ for $q>0$.
For an affine open $V\subseteq S$, the inverse image
$U_y\times_S V$ is affine. The Leray spectral sequence for $j_y$
restricted over $V$, together with the preceding vanishing and
[pqf-lem-affine-vanishing], gives

$$
H^q(f^{-1}V,j_{y,*}(\mathcal F|_{U_y}))
=H^q(U_y\times_S V,\mathcal F)=0\quad(q>0).
$$

Affine opens form a basis on $S$, so all higher direct images under
$f$ of these Cech terms vanish. A resolution by $f_*$-acyclic
objects computes the right derived functors (apply $f_*$ to an
injective double resolution and use its two spectral sequences).
The terms $f_*\check{\mathcal C}^p$ are quasi-coherent on the affine scheme
$S$ (direct images of quasi-coherent modules along the affine maps
$U_y\to S$), $\Gamma(S,-)$ is exact on quasi-coherent modules, and
$\Gamma(S,f_*\check{\mathcal C}^p)=\check C^p(\mathcal U,\mathcal F)$; so taking
global sections gives the last claim.
