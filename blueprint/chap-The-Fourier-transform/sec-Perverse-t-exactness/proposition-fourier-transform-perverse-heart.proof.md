+++
kind = "proof"
of = "proposition-fourier-transform-perverse-heart"
order = 1255
uses = ["lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "lemma-integral-linear-character", "proposition-fourier-inversion", "lemma-perverse-weil-sheaves"]
+++
We show that the geometric transform and its inverse preserve
${}^pD^{\le0}$. Being mutually inverse, they then preserve
${}^pD^{\ge0}$ by orthogonality. The Weil statement follows by
Lemma [lemma-perverse-weil-sheaves], since the forgetful functor on
perverse Weil sheaves is exact and reflects exactness. The key point is
that the stalks of the transform are compactly supported cohomology
groups on the affine line, in degrees $0,1,2$. The group in degree two is
nonzero only at the finitely many points $y$ for which the twisted sheaf
has a geometrically constant quotient.

*Right exactness.* Since the transform is triangulated and
${}^pD^{\le0}$ is stable under extensions and
positive shifts, ordinary truncation reduces this to punctual sheaves
in degree zero and to objects $G[1]$ with $G$ constructible. Indeed, an
object of ${}^pD^{\le0}$ is an iterated extension of its shifted
ordinary cohomology sheaves $\mathcal H^a(K)[-a]$ with $a\le0$; the one
with $a=0$ is punctual, and the others are of the form $G[1]$ shifted
by a nonnegative amount.
Punctual sheaves map into ${}^pD^{\le0}$, since by the stalk formula
the transform of a geometric skyscraper is a lisse sheaf shifted by one.

For $G[1]$ we show that the transform lies in ordinary degrees
$-2,-1,0$ and that its degree-zero sheaf has finite support. The first
assertion follows from the stalk formula and
Lemma [lemma-cohomological-range-curve]. The degree-zero stalk at a closed
geometric point $y$ is

$$
H_c^2(\mathbf A^1,G\otimes\mathcal L_{\psi(yx)}).
$$

On a dense open where $G$ is lisse with generic representation $V$,
write $\chi_y$ for the character of $\pi_1$ given by the restriction of
$\mathcal L_{\psi(yx)}$. By localization we may discard the finitely many
remaining points, which contribute only in degree zero, and
Lemma [lemma-extreme-degrees-affine-curve] (whose proof of the
formula for $H^2_c$ uses only the geometric curve) shows that this stalk is
$(V\otimes\chi_y)_{\pi_1}(-1)$. It is nonzero only if
$V$ has the rank-one quotient $\chi_y^{-1}$.
The characters $\chi_y$ are pairwise distinct. Indeed, if
$\chi_y=\chi_{y'}$ with $y\ne y'$, then $\mathcal L_{\psi((y-y')x)}$ is
trivial on the dense open, hence on the line by the surjectivity of
fundamental groups. This is impossible, because its compactly
supported cohomology vanishes by Lemma [lemma-integral-linear-character],
whereas the constant sheaf has nonzero top cohomology with compact
support. If $V$ has pairwise nonisomorphic rank-one quotients
$\chi_1,\dots,\chi_n$, then the induced map
$V\to\chi_1\oplus\dots\oplus\chi_n$ is surjective. To see this, note
that its image is a subrepresentation of a sum of pairwise nonisomorphic simple
representations, hence the sum of some of the $\chi_i$, and it maps
onto each $\chi_i$. So $n\le\dim V$,
and $\chi_y^{-1}$ is a quotient of $V$ for at most $\dim V$ points $y$.
The degree-zero sheaf therefore has only finitely many nonzero closed
geometric stalks. Being constructible, it has finite support, and the
transform of $G[1]$ belongs to ${}^pD^{\le0}$.

*Exactness.* The argument for $\operatorname{FT}_\psi$ applies
equally to $\psi^{-1}$, and a Tate twist does not affect supports or
degrees. Both $\operatorname{FT}_\psi$ and its quasi-inverse
$\operatorname{FT}_{\psi^{-1}}(-)(1)$ of
Proposition [proposition-fourier-inversion] therefore preserve
${}^pD^{\le0}$. Since
${}^pD^{\ge0}$ is the right orthogonal of ${}^pD^{\le-1}$, the two
mutually inverse equivalences also preserve ${}^pD^{\ge0}$. Both
functors are therefore t-exact, and they induce exact equivalences of
the geometric hearts. With their canonical Frobenius compatibilities and
the equivariant inversion isomorphisms of
Proposition [proposition-fourier-inversion], they give quasi-inverse
functors on perverse Weil sheaves. These are exact because the forgetful
functors are exact and reflect exactness.
