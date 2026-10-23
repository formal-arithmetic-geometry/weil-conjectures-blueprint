+++
kind  = "proof"
of    = "sk-p-dl-a1-perverse"
+++
We first prove that the geometric transform preserves
${}^pD^{\le0}$. Since ${}^pD^{\le0}$ is stable under extensions and
positive shifts, ordinary truncation reduces this to punctual sheaves
in degree zero and to objects $G[1]$ with $G$ constructible.
By the stalk formula of [sk-thm-inversion], the transform of a
geometric skyscraper is a lisse sheaf shifted by one, and so punctual
sheaves map into ${}^pD^{\le0}$.

For $G[1]$, the stalk formula and [sk-l-dl-a1-endpoints] show that
its transform lies in ordinary degrees $-2,-1,0$. Its degree-zero
stalk at a closed geometric point $y$ is

$$
 H_c^2(\mathbf A^1,G\otimes\mathcal L_{\psi(yx)}).
$$

On a dense open where $G$ is lisse with generic representation $V$,
this is $(V\otimes\chi_y)_{\pi_1}(-1)$, which is nonzero only if
$V$ has the rank-one quotient $\chi_y^{-1}$.
The characters $\chi_y$ are pairwise distinct. Indeed, the quotient
of two of them is the character of a nonzero linear function, whose
cohomology vanishes by [sk-lem-wft-character-integral], whereas a
trivial character has nonzero top compact-support cohomology; and a
character trivial on the dense open is trivial on the line, by the
surjectivity of fundamental groups. Since the map from $V$ onto a sum
of pairwise nonisomorphic simple characters is surjective, $V$ has at
most $\dim V$ such distinct quotients. Thus the degree-zero sheaf has
only finitely many nonzero closed geometric stalks. Being
constructible, it has finite support, and so the transform of $G[1]$
belongs to ${}^pD^{\le0}$.

The same argument applies to $\psi^{-1}$, and it is unchanged by a
Tate twist. By [sk-thm-inversion],
$\operatorname{FT}_{\psi^{-1}}(-)(1)$ is a quasi-inverse, and we have
shown that both geometric functors preserve ${}^pD^{\le0}$. Since
${}^pD^{\ge0}$ is the right orthogonal of ${}^pD^{\le-1}$
([sk-lem-wft-curve-heart]), the two mutually inverse equivalences also
preserve ${}^pD^{\ge0}$. Hence both functors are t-exact and induce
exact equivalences of the geometric hearts. With their canonical
Frobenius compatibilities and the equivariant inversion isomorphisms
of [sk-thm-inversion], they give quasi-inverse functors on the Weil
hearts, which are exact because the forgetful functors are exact and
reflect exactness ([sk-lem-wft-curve-heart]).
