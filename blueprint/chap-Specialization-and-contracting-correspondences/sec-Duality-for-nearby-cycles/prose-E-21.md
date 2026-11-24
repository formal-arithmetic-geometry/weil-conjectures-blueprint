+++
id = "prose-E-21"
kind = "hidden"
title = "Duality for nearby cycles (4)"
order = 1683
+++
We fix the notation for the slice. Let $b:X\to\mathbf A^1_S$ be a
coordinate map and let $S'=(\mathbf A^1_S)_{(s')}$ be the trait at the
generic point of the special fibre used in
(E.2).  Set
$X'=X\times_{\mathbf A^1_S}S'$, $M'=M|_{X'_{\bar\eta'}}$, and write
$g_s,g_\eta$ for the two pullbacks to the geometric generic point of
the coordinate line.  Restriction to the geometric generic point of the
coordinate line is compatible with internal Hom, and
Lemma [lemma-restriction-geometric-generic-fibre] and
Lemma [lemma-double-dual-geometric-generic-fibre], applied on each
geometric fibre, give, locally on $X$, isomorphisms

$$
g_\eta^*\href{@definition-verdier-dual-evaluation}{\mathbb D_{X_{\bar\eta}}M}\simeq \href{@definition-verdier-dual-evaluation}{\mathbb D_{X'_{\bar\eta'}}M'}\otimes \href{@definition-tate-twists}{A(1)[2]},
\qquad
g_s^*\href{@definition-verdier-dual-evaluation}{\mathbb D_{X_s}L}\simeq \href{@definition-verdier-dual-evaluation}{\mathbb D_{X'_{s'}}}(g_s^*L)\otimes \href{@definition-tate-twists}{A(1)[2]}
\tag{E.16}
$$

for $L\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X_s,A)}$. The twist comes from the
[dualizing complexes](@definition-verdier-dual-evaluation). For a closed embedding over $\mathbf A^1$
into $\mathbf A^r_{\mathbf A^1}$, [smooth purity](@theorem-smooth-purity-all-admissible-coefficients) gives [$A(r+1)[2r+2]$](@definition-tate-twists)
before generic restriction and [$A(r)[2r]$](@definition-tate-twists) after it. Moreover, the comparison of the complexes with closed support for the embedding preserves
evaluation. Thus on $\mathbf A^r_{\mathbf A^1_S}$ the identifications of
the [dualizing complexes](@definition-verdier-dual-evaluation) before and after slicing differ by [$A(1)[2]$](@definition-tate-twists) on
both fibres. Finally, the group $P$ acts trivially on [$A(1)[2]$](@definition-tate-twists), because roots of
unity of order prime to the residue characteristic lift over a strictly
henselian trait. So the twist commutes with taking $P$-invariants.
