+++
kind  = "proof"
of    = "sk-p-dl-a1-perverse"
+++
The stalks of the transform are compactly supported
cohomology groups on the affine line, which live in degrees $0,1,2$,
and the group in degree two is nonzero only at the finitely many
points $y$ for which the twisted sheaf has a geometrically constant
quotient. A Weil complex lies in one of the classes exactly when its
underlying complex on the geometric line does, because the largest
punctual subsheaf is preserved by Weil transport, so we may compute
stalks after base change to $k$. The proof of
[sk-lem-wft-curve-heart] applies verbatim to Weil complexes, so
these classes form a t-structure on Weil complexes whose heart consists
of the perverse Weil sheaves, and ${}^pD^{\ge0}$ is the right orthogonal
of ${}^pD^{\le-1}$. We show that the transform and its inverse preserve
${}^pD^{\le0}$. Since they are mutually inverse, they then also
preserve ${}^pD^{\ge0}$ by orthogonality.

*Right exactness.* Since the transform is triangulated and
${}^pD^{\le0}$ is stable under extensions and
positive shifts, ordinary truncation reduces this to punctual sheaves
in degree zero and to objects $G[1]$ with $G$ constructible.
By the stalk formula, the transform of a geometric skyscraper is a
lisse sheaf shifted by one, and so punctual sheaves map into
${}^pD^{\le0}$.

For $G[1]$, the stalk formula and
[sk-l-dl-a1-endpoints] show that its transform lies in
ordinary degrees $-2,-1,0$. Its degree-zero stalk at a closed
geometric point $y$ is

$$
 H_c^2(\mathbf A^1,G\otimes\mathcal L_{\psi(yx)}).
$$

On a dense open where $G$ is lisse with generic representation $V$,
write $\chi_y$ for the character of $\pi_1$ given by the restriction of
$\mathcal L_{\psi(yx)}$. Localization discards the finitely many
remaining points, which contribute only in degree zero, and
[sk-l-dl-a1-endpoints] shows that this stalk is
$(V\otimes\chi_y)_{\pi_1}(-1)$. It is nonzero only if
$V$ has the rank-one quotient $\chi_y^{-1}$.
The characters $\chi_y$ are pairwise distinct. Indeed, if
$\chi_y=\chi_{y'}$ with $y\ne y'$, then $\mathcal L_{\psi((y-y')x)}$ is
trivial on the dense open, hence on the line by the surjectivity of
fundamental groups. This is impossible, because its compactly
supported cohomology vanishes by [sk-lem-wft-character-integral],
whereas the constant sheaf has nonzero top cohomology with compact
support. If $V$ has pairwise nonisomorphic rank-one quotients
$\chi_1,\dots,\chi_n$, then the induced map
$V\to\chi_1\oplus\dots\oplus\chi_n$ is surjective. To see this, note
that its image is a subrepresentation of a sum of pairwise nonisomorphic simple
representations, hence the sum of some of the $\chi_i$, and it maps
onto each $\chi_i$. Hence $n\le\dim V$,
and $\chi_y^{-1}$ is a quotient of $V$ for at most $\dim V$ points $y$. Thus the degree-zero sheaf has
only finitely many nonzero closed geometric stalks. Being
constructible, it has finite support, and so the transform of $G[1]$
belongs to ${}^pD^{\le0}$.

*Exactness.* The same argument applies to $\psi^{-1}$, and it is
unchanged by a Tate twist. By [sk-thm-inversion],
$\operatorname{FT}_{\psi^{-1}}(-)(1)$ is a quasi-inverse, and we have
shown that both functors preserve ${}^pD^{\le0}$. Since
${}^pD^{\ge0}$ is the right orthogonal of ${}^pD^{\le-1}$, the two
mutually inverse equivalences also preserve ${}^pD^{\ge0}$. Hence both
functors are t-exact and induce mutually quasi-inverse exact
equivalences of the hearts, that is, of the categories of perverse
Weil sheaves.
